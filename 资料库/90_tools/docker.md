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

### 启动和关闭
```
$ systemctl start docker
```