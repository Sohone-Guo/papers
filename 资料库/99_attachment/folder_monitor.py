#!/usr/bin/env python3
"""
飞书文件夹监控机器人
功能：监控指定文件夹，每小时检查一次文件变动，并通过飞书机器人发送通知
作者：DeepSeek助手
"""

import os
import time
import json
import hashlib
import requests
from datetime import datetime
from pathlib import Path
import sys

class FolderMonitor:
    def __init__(self, folder_path, app_id, app_secret, feishu_group_id):
        """
        初始化监控器
        
        Args:
            folder_path: 要监控的文件夹路径
            app_id: 飞书应用的app_id
            app_secret: 飞书应用的app_secret
            feishu_group_id: 飞书群聊ID
        """
        self.folder_path = Path(folder_path).resolve()
        self.app_id = app_id
        self.app_secret = app_secret
        self.feishu_group_id = feishu_group_id
        
        # 确保文件夹存在
        if not self.folder_path.exists():
            print(f"错误：文件夹不存在 - {self.folder_path}")
            sys.exit(1)
        
        # 状态文件路径（用于存储上次检查的状态）
        self.state_file = self.folder_path / ".folder_monitor_state.json"
        
        # 飞书API配置
        self.token_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        self.message_url = "https://open.feishu.cn/open-apis/im/v1/messages"
        
        # 缓存token
        self.cached_token = None
        self.token_expire_time = 0
        
        # 文件状态记录
        self.last_state = {}
        
        print(f"初始化完成，监控文件夹: {self.folder_path}")
        print(f"飞书群ID: {self.feishu_group_id}")
    
    def get_file_hash(self, file_path):
        """计算文件的MD5哈希值"""
        hash_md5 = hashlib.md5()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            print(f"计算文件哈希出错 {file_path}: {e}")
            return None
    
    def scan_folder(self):
        """扫描文件夹，返回文件状态字典"""
        file_state = {}
        
        # 遍历文件夹中的所有文件（不包括子目录）
        for item in self.folder_path.iterdir():
            if item.is_file():
                # 获取文件信息
                stat = item.stat()
                file_hash = self.get_file_hash(item)
                
                if file_hash:  # 只有能成功读取的文件才记录
                    file_state[str(item.name)] = {
                        "size": stat.st_size,
                        "mtime": stat.st_mtime,
                        "hash": file_hash,
                        "path": str(item)
                    }
        
        return file_state
    
    def get_feishu_token(self):
        """获取飞书tenant_access_token"""
        # 如果token未过期，直接返回缓存的token
        if self.cached_token and time.time() < self.token_expire_time:
            return self.cached_token
        
        # 获取新token
        payload = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        
        try:
            response = requests.post(self.token_url, json=payload, timeout=10)
            data = response.json()
            
            if data.get("code") == 0:
                self.cached_token = data["tenant_access_token"]
                # 设置过期时间（提前60秒）
                self.token_expire_time = time.time() + data["expire"] - 60
                print(f"飞书Token获取成功，有效期至: {datetime.fromtimestamp(self.token_expire_time).strftime('%Y-%m-%d %H:%M:%S')}")
                return self.cached_token
            else:
                print(f"获取Token失败: {data}")
                return None
        except Exception as e:
            print(f"获取Token异常: {e}")
            return None
    
    def send_feishu_message(self, title, content):
        """发送消息到飞书群"""
        token = self.get_feishu_token()
        if not token:
            print("无法获取飞书Token，消息发送失败")
            return False
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        # 构建消息内容
        message_content = {
            "zh_cn": {
                "title": title,
                "content": [
                    [{
                        "tag": "text",
                        "text": content
                    }]
                ]
            }
        }
        
        payload = {
            "receive_id": self.feishu_group_id,
            "msg_type": "post",
            "content": json.dumps(message_content)
        }
        
        try:
            # 发送到群聊
            response = requests.post(
                f"{self.message_url}?receive_id_type=chat_id",
                headers=headers,
                json=payload,
                timeout=10
            )
            
            result = response.json()
            if result.get("code") == 0:
                print(f"消息发送成功: {title}")
                return True
            else:
                print(f"消息发送失败: {result}")
                return False
        except Exception as e:
            print(f"发送消息异常: {e}")
            return False
    
    def detect_changes(self):
        """检测文件变化"""
        current_state = self.scan_folder()
        
        if not self.last_state:  # 第一次运行，没有比较基准
            self.last_state = current_state
            return None, None, None
        
        # 找出新增的文件
        added = [name for name in current_state if name not in self.last_state]
        
        # 找出删除的文件
        removed = [name for name in self.last_state if name not in current_state]
        
        # 找出修改的文件
        modified = []
        for name in current_state:
            if name in self.last_state:
                old_file = self.last_state[name]
                new_file = current_state[name]
                
                # 比较文件大小、修改时间或哈希值
                if (old_file["size"] != new_file["size"] or 
                    old_file["mtime"] != new_file["mtime"] or 
                    old_file["hash"] != new_file["hash"]):
                    modified.append(name)
        
        # 更新状态
        self.last_state = current_state
        
        return added, removed, modified
    
    def run(self):
        """主运行循环"""
        print("=" * 50)
        print(f"文件夹监控程序启动 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)
        
        # 第一次启动时发送测试消息
        print("\n发送启动测试消息...")
        self.send_feishu_message(
            "📁 文件夹监控机器人已启动",
            f"监控文件夹: {self.folder_path}\n启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        
        # 第一次扫描，建立基准状态
        print("\n进行首次文件夹扫描...")
        self.last_state = self.scan_folder()
        file_count = len(self.last_state)
        print(f"发现 {file_count} 个文件，已建立监控基准")
        
        # 主循环
        print("\n开始监控循环（每小时检查一次）...")
        print("按 Ctrl+C 停止程序\n")
        
        check_count = 0
        try:
            while True:
                check_count += 1
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"\n[{current_time}] 第{check_count}次检查...")
                
                # 检测变化
                added, removed, modified = self.detect_changes()
                
                # 如果有变化，发送通知
                if added or removed or modified:
                    print("检测到文件变化！")
                    
                    # 构建消息内容
                    title = "📁 文件夹内容发生变化"
                    content = f"监控文件夹: {self.folder_path}\n"
                    content += f"检查时间: {current_time}\n"
                    
                    if added:
                        content += f"\n📤 新增文件 ({len(added)}个):\n"
                        for file in added[:10]:  # 最多显示10个
                            content += f"  • {file}\n"
                        if len(added) > 10:
                            content += f"  ... 等{len(added)}个文件\n"
                    
                    if removed:
                        content += f"\n🗑️ 删除文件 ({len(removed)}个):\n"
                        for file in removed[:10]:
                            content += f"  • {file}\n"
                        if len(removed) > 10:
                            content += f"  ... 等{len(removed)}个文件\n"
                    
                    if modified:
                        content += f"\n✏️ 修改文件 ({len(modified)}个):\n"
                        for file in modified[:10]:
                            content += f"  • {file}\n"
                        if len(modified) > 10:
                            content += f"  ... 等{len(modified)}个文件\n"
                    
                    # 发送消息
                    self.send_feishu_message(title, content)
                else:
                    print("未发现文件变化")
                
                # 等待1小时
                print(f"下次检查将在1小时后 ({datetime.fromtimestamp(time.time() + 3600).strftime('%H:%M:%S')})")
                time.sleep(3600)  # 3600秒 = 1小时
                
        except KeyboardInterrupt:
            print("\n\n程序被用户中断")
            # 发送关闭通知
            self.send_feishu_message(
                "🛑 文件夹监控机器人已停止",
                f"监控文件夹: {self.folder_path}\n停止时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n总检查次数: {check_count}"
            )
            print("程序已退出")

def main():
    """主函数"""
    print("飞书文件夹监控机器人 v1.0")
    print("-" * 50)
    
    # 配置信息 - 请根据实际情况修改！
    CONFIG = {
        # 要监控的文件夹路径（默认监控程序所在文件夹）
        "FOLDER_PATH": ".",  # 当前目录，可以修改为其他路径如 "/path/to/your/folder"
        
        # 飞书应用信息 - 需要替换为你的实际信息！
        "APP_ID": ".",  # 替换为你的app_id
        "APP_SECRET": ".",  # 替换为你的app_secret
        
        # 飞书群ID - 已经提供了你的群ID
        "FEISHU_GROUP_ID": "oc_8519d60c1465a88c7c376e899718a212"
    }
    
    # 显示配置信息
    print("当前配置:")
    print(f"  监控文件夹: {os.path.abspath(CONFIG['FOLDER_PATH'])}")
    print(f"  飞书群ID: {CONFIG['FEISHU_GROUP_ID']}")
    print(f"  APP_ID: {CONFIG['APP_ID'][:10]}...")  # 只显示前10位
    print(f"  APP_SECRET: {CONFIG['APP_SECRET'][:10]}...")  # 只显示前10位
    print("-" * 50)
    
    # 检查配置
    if CONFIG["APP_ID"] == "your_app_id_here" or CONFIG["APP_SECRET"] == "your_app_secret_here":
        print("\n❌ 错误：请先修改配置文件中的APP_ID和APP_SECRET！")
        print("获取方法:")
        print("1. 访问 https://open.feishu.cn/app")
        print("2. 创建应用或选择已有应用")
        print("3. 在'凭证与基础信息'中获取App ID和App Secret")
        return
    
    # 创建并启动监控器
    try:
        monitor = FolderMonitor(
            folder_path=CONFIG["FOLDER_PATH"],
            app_id=CONFIG["APP_ID"],
            app_secret=CONFIG["APP_SECRET"],
            feishu_group_id=CONFIG["FEISHU_GROUP_ID"]
        )
        monitor.run()
    except Exception as e:
        print(f"程序运行出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()