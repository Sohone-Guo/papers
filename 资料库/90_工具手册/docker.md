### 共享内存不够
```
$ docker run --shm-size=256m
```

### 指定GPU

```
$ docker --gpus '"device=6,7"'
```

### Docker清理
```
$ docker system prune
```

### 本地仓库
搭建本地仓库
```bash
# 下载本地仓库的容器
$ docker pull registry:latest
# 启动容器
$ docker run -d -p 5000:5000 --restart=always --name registry registry:latest
```

使用本地仓库
```bash
# 上传image to 本地仓库
# 1、打标签
$ docker tag myimage 192.168.2.204:5000/myimage
# 2、推送至本地仓库
$ docker push 192.168.2.204:5000/myimage
```