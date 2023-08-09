```python
source_input_hiddens.permute(1, 0, 2)
```

```python
copy_probabilities = self._scatter(
	encoder_input, output_len,
	torch.zeros_like(output_probabilities),
	attn_weights)

output_probabilities.scatter_add_(2, text_n_gram_index.unsqueeze(1),
								  text_n_gram_value.unsqueeze(1))
```

#### LSTM with padding
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

# 构建数据集
data = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

# 将数据长度从长到短排序
data.sort(key=lambda x: len(x), reverse=True)

# 创建padding和转换为Tensor
padded_data = nn.utils.rnn.pad_sequence([torch.tensor(d) for d in data], batch_first=True)

# 创建数据长度Tensor
lengths = torch.tensor([len(d) for d in data])

# 定义模型
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        
    def forward(self, x, lengths):
        packed_input = pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
        packed_output, (h_n, c_n) = self.lstm(packed_input)
        output, _ = pad_packed_sequence(packed_output, batch_first=True)
        output = self.fc(output)
        return output

# 初始化模型和损失函数
input_size = 1
hidden_size = 10
num_layers = 1
output_size = 1
model = LSTMModel(input_size, hidden_size, num_layers, output_size)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 训练模型
num_epochs = 100
for epoch in range(num_epochs):
    optimizer.zero_grad()
    outputs = model(padded_data.unsqueeze(-1).float(), lengths)  # 添加一个维度来匹配LSTM的输入
    loss = criterion(outputs, padded_data.float())
    loss.backward()
    optimizer.step()
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

```