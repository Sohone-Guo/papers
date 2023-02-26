### 共享内存不够
```
$ docker run --shm-size=256m
```

### 指定GPU

```
$ docker --gpus '"device=6,7"'
```