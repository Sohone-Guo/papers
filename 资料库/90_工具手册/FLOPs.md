[深度学习中的FLOPs介绍及计算(注意区分FLOPS)___Jupiter__的博客-CSDN博客](https://blog.csdn.net/qq_41834400/article/details/120283103)
```python
import torch
from thop import profile

# 创建一个示例模型
model = YourModel()

# 准备一个示例输入张量
input_data = torch.randn(1, 3, 224, 224)  # 这里的输入大小应与你的模型兼容

# 使用thop计算FLOPs
flops, params = profile(model, inputs=(input_data,))
print(f"FLOPs: {flops / 1e9} G FLOPs")  # 打印FLOPs，以十亿次浮点操作为单位

```

```python
import torch
import torchsummary
from your_model_module import YourModel  # 导入你的模型

# 创建模型实例
model = YourModel()

# 将模型移到设备（GPU或CPU）上
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 打印模型摘要，包括FLOPs
summary = torchsummary.summary(model, (3, 224, 224))  # 输入尺寸根据你的数据进行调整
print(summary)

```

```python
import numpy as np

# 定义矩阵的维度
matrix_size = 1000

# 创建两个随机矩阵
matrix_A = np.random.rand(matrix_size, matrix_size)
matrix_B = np.random.rand(matrix_size, matrix_size)

# 执行矩阵乘法并计时
import time
start_time = time.time()
result_matrix = np.dot(matrix_A, matrix_B)
end_time = time.time()

# 计算FLOPs
total_flops = 2 * matrix_size**3  # 矩阵乘法需要2n^3次浮点运算

# 计算运行时间
elapsed_time = end_time - start_time

# 计算FLOPs/s
flops_per_second = total_flops / elapsed_time

print(f"矩阵乘法的FLOPs：{total_flops}")
print(f"运行时间：{elapsed_time} 秒")
print(f"FLOPs/s：{flops_per_second}")

```