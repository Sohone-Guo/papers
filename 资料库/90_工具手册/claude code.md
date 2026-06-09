[Anthropic API | DeepSeek API Docs](https://api-docs.deepseek.com/zh-cn/guides/anthropic_api)

### 安装方式
##### Ubuntu 系统
```bash
# 安装 Claude Code
sudo npm install -g @anthropic-ai/claude-code@latest --registry=https://registry.npmmirror.com

# 配置模型
# 创建配置目录（如果不存在）
mkdir -p ~/.claude
# 创建并编辑配置文件（使用 nano 编辑器）
nano ~/.claude/settings.json
```

settings.json
```settings.json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-...",
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro",
    "ANTHROPIC_MODEL": "deepseek-v4-pro"
  }
}
```

更新系统
```bash
claude update
```

##### Windows 系统
配置文件基于CC Switch