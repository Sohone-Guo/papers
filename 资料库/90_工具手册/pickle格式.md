保存成cpickle格式，大量的矩阵等数据读取速度会很快

```python
# import scipy.io
# import numpy as np
import hdf5storage
import pickle
# # 读取文件
# ch_matrix = hdf5storage.loadmat("datasets/AI_codebook_compress_data/ChanneleTypeIIRank1Part1.mat")["channel"]

# Step 1: 读取 .mat 文件
mat_data = hdf5storage.loadmat("datasets/AI_codebook_compress_data/ChanneleTypeIIRank1Part1.mat")

# Step 2: 提取 'channel' 数据
channel_data = mat_data["channel"]

# Step 3: 保存为 .pkl 文件（使用最高协议以获得更快速度和更小体积）
with open("datasets/AI_codebook_compress_data_cpickle/ChanneleTypeIIRank1Part1.pkl", "wb") as f:
    pickle.dump(channel_data, f, protocol=pickle.HIGHEST_PROTOCOL)

print("转换完成 ✅，文件已保存为 'channel_data.pkl'") 
```