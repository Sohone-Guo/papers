
Could not initialize OptiX!
```bash
docker run -it --name test-sionna --gpus 'all,"capabilities=compute,graphics,utility"' --shm-size "4g" tensorflow/tensorflow:2.11.1-gpu /bin/bash
```