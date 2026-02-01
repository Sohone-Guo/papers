
[手把手教学：用n8n+RSS+飞书实现多平台热点自动抓取（含RSS源分享）-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2574814)
### 安装 n8n
[Docker | n8n Docs](https://docs.n8n.io/hosting/installation/docker/)

1）建一个网络
```bash
docker volume create n8n_data
docker network create n8n-net
```

2）启动 n8n（外部模式 + 后台自启）
```bash
docker run -d \
  --name n8n \
  --restart unless-stopped \
  --network n8n-net \
  -p 5678:5678 \
  -e GENERIC_TIMEZONE="CST" \
  -e TZ="CST" \
  -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
  -e N8N_RUNNERS_ENABLED=true \
  -e N8N_RUNNERS_MODE=external \
  -e N8N_RUNNERS_BROKER_LISTEN_ADDRESS=0.0.0.0 \
  -e N8N_RUNNERS_AUTH_TOKEN="CHANGE_ME_TO_A_RANDOM_SECRET" \
  -e N8N_NATIVE_PYTHON_RUNNER=true \
  -e N8N_SECURE_COOKIE=false \
  -v n8n_data:/home/node/.n8n \
  docker.1ms.run/n8nio/n8n:2.4.8
```

3）启动 runners sidecar（同版本 + 后台自启）
```bash
docker run -d \
  --name n8n-runners \
  --restart unless-stopped \
  --network n8n-net \
  -e N8N_RUNNERS_TASK_BROKER_URI="http://n8n:5679" \
  -e N8N_RUNNERS_AUTH_TOKEN="CHANGE_ME_TO_A_RANDOM_SECRET" \
  docker.1ms.run/n8nio/runners:2.4.8
```


### 安装飞书节点
[n8n-nodes-feishu-lite - npm](https://www.npmjs.com/package/n8n-nodes-feishu-lite)

