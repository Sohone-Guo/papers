```bash
# Windows Powershell 启动高速版 Claude 模型
$env:ANTHROPIC_BASE_URL="https://api.apiyi.com";
$env:ANTHROPIC_AUTH_TOKEN="sk-"
$env:ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL="claude-sonnet-4-5-20250929"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL="claude-sonnet-4-5-20250929"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL="claude-sonnet-4-5-20250929"
$env:CLAUDE_CODE_SUBAGENT_MODEL="claude-sonnet-4-5-20250929"
claude

export ANTHROPIC_BASE_URL=https://api.apiyi.com
export ANTHROPIC_AUTH_TOKEN=sk-
export ANTHROPIC_MODEL=claude-sonnet-4-5-20250929
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-sonnet-4-5-20250929
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5-20250929
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-sonnet-4-5-20250929
export CLAUDE_CODE_SUBAGENT_MODEL=claude-sonnet-4-5-20250929
```