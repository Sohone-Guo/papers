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

```bash
npm install -g @anthropic-ai/claude-code
```


#### CC Switch API易剩余金额获取
```json
({
  request: {
    url: "https://api.apiyi.com/api/token/?p=0&pageSize=100",
    method: "GET",
    headers: {
      "Accept": "application/json",
      "Authorization": "...",
      "Content-Type": "application/json"
    }
  },
  extractor: function(response) {
    let remaining = 0;
    for (let i = 0; i < response.data.length; i++) {
      if (response.data[i].name === "...") {
        remaining = response.data[i].remain_quota / 500000;
        break;
      }
    }
    return {
      remaining: remaining,
      unit: "USD"
    };
  }
})
```

bash
```bash
curl --compressed -s 'https://api.apiyi.com/api/token/?p=0&pageSize=100' \
  -H 'Accept: application/json' \
  -H 'Authorization: ...' \
  -H 'Content-Type: application/json' | jq '.data[] | select(.name=="...") | .remain_quota / 500000'
```