Tags: #Tag_自然语言处理 
# Information
---


# Mainly Idea
---
![[Pasted image 20240522130951.png]]

实现的方法是通过ChatGPT4来实现的（论文没有给代码）
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import grad

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Gradient Supervision Loss
def gradient_supervision_loss(model, x_i, x_j, y_i, y_j):
    # Forward pass
    y_hat_i = model(x_i)
    y_hat_j = model(x_j)

    # Compute gradients
    grad_outputs_i = torch.ones_like(y_hat_i)
    grad_outputs_j = torch.ones_like(y_hat_j)

    grads_i = grad(outputs=y_hat_i, inputs=x_i, grad_outputs=grad_outputs_i, create_graph=True)[0]
    grads_j = grad(outputs=y_hat_j, inputs=x_j, grad_outputs=grad_outputs_j, create_graph=True)[0]

    # Ground truth gradient
    gt_grad = x_j - x_i

    # Normalize gradients
    gt_grad = gt_grad / (gt_grad.norm() + 1e-8)
    predicted_grad = (grads_j - grads_i) / ((grads_j - grads_i).norm() + 1e-8)

    # Cosine similarity loss
    gs_loss = 1 - (gt_grad * predicted_grad).sum()
    return gs_loss

# Initialize model, optimizer, and example data
model = SimpleModel()
optimizer = optim.Adam(model.parameters(), lr=0.001)
x_i = torch.randn(10, 10, requires_grad=True)
x_j = torch.randn(10, 10, requires_grad=True)
y_i = model(x_i)
y_j = model(x_j)

# Training loop
epochs = 10
for epoch in range(epochs):
    optimizer.zero_grad()
    loss = gradient_supervision_loss(model, x_i, x_j, y_i, y_j)
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch+1}, Loss: {loss.item()}')

```
# Question
---
- Leveraging an overlooked supervisory signal found in existing datasets.
- We complement the traditional "curve fitting" to individual training points of standard supervised learning, with "aligning the curve" with pairs of counterfactual training points.
- ==A novel training objective (gradient supervision)?==
	- Gradient本身也被监督（被限制）

# Reference
---


# Attachment
---
![[2004.09034v1.pdf]]