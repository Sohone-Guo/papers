[Anthropic API | DeepSeek API Docs](https://api-docs.deepseek.com/zh-cn/guides/anthropic_api)
```bash
Get-ChildItem Env: | Where-Object Name -like 'ANTHROPIC_*'

[Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://api.deepseek.com/anthropic", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_AUTH_TOKEN", "sk-98e3d1519ba74f4b993ad834352bf439", "User")
[Environment]::SetEnvironmentVariable("API_TIMEOUT_MS", "600000", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_MODEL", "deepseek-chat", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_SMALL_FAST_MODEL", "deepseek-chat", "User")
[Environment]::SetEnvironmentVariable("CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC", "1", "User")
```