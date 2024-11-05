Tags: #Tag_计算机视觉 
# Information
---


# Mainly Idea
---
ChatGPT给的样例
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchdiffeq import odeint

# 定义简单的流网络（例如MLP）
class FlowNet(nn.Module):
    def __init__(self, dim):
        super(FlowNet, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(dim + 1, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, dim)
        )

    def forward(self, x, t):
        # 将时间t与输入拼接，以便每一步使用不同时间点的动态
        t_expanded = t.expand(x.size(0), 1)  # 扩展时间维度
        x_and_t = torch.cat([x, t_expanded], dim=1)
        return self.net(x_and_t)


# 生成数据分布（目标分布，比如一个二维高斯分布）
def sample_data(num_samples=1000):
    mean = torch.tensor([2.0, 2.0])
    cov = torch.tensor([[0.5, 0.1], [0.1, 0.5]])
    return torch.distributions.MultivariateNormal(mean, cov).sample((num_samples,))


# 定义Flow Matching损失函数
def flow_matching_loss(flow_net, x, target_distribution):
    t = torch.rand(x.size(0), 1)  # 随机时间
    noise = torch.randn_like(x)   # 添加随机噪声

    # 计算流模型的速度场
    dx_dt = flow_net(x, t)
    
    # 对ODE的目标做插值
    interpolated = (1 - t) * noise + t * target_distribution
    
    # Flow Matching损失：MSE形式
    loss = torch.mean((dx_dt - (target_distribution - x)) ** 2)
    return loss


# 初始化模型和优化器
dim = 2  # 数据的维度
flow_net = FlowNet(dim)
optimizer = optim.Adam(flow_net.parameters(), lr=1e-3)

# 训练Flow Matching模型
num_epochs = 1000
for epoch in range(num_epochs):
    x = torch.randn(128, dim)  # 从初始噪声分布中采样
    target_distribution = sample_data(num_samples=128)  # 从目标分布中采样

    # 计算损失并进行反向传播
    loss = flow_matching_loss(flow_net, x, target_distribution)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

# 测试模型
test_noise = torch.randn(1000, dim)
time_points = torch.linspace(0, 1, 10)
flow_samples = odeint(flow_net, test_noise, time_points).detach()

print("Flow Matching模型训练完成。")

```

参考：[18_flow_matching](https://jmtomczak.github.io/blog/18/18_fm.html)
```python
class FlowMatching(nn.Module):
    def __init__(self, vnet, sigma, D, T, stochastic_euler=False, prob_path="icfm"):
        super(FlowMatching, self).__init__()

        print('Flow Matching by JT.')

        self.vnet = vnet

        self.time_embedding = nn.Sequential(nn.Linear(1, D), nn.Tanh())
        
        # other params
        self.D = D
        
        self.T = T

        self.sigma = sigma
        
        self.stochastic_euler = stochastic_euler
        
        assert prob_path in ["icfm", "fm"], f"Error: The probability path could be either Independent CFM (icfm) or Lipman's Flow Matching (fm) but {prob_path} was provided."
        self.prob_path = prob_path
        
        self.PI = torch.from_numpy(np.asarray(np.pi))
    
    def log_p_base(self, x, reduction='sum', dim=1):
        log_p = -0.5 * torch.log(2. * self.PI) - 0.5 * x**2.
        if reduction == 'mean':
            return torch.mean(log_p, dim)
        elif reduction == 'sum':
            return torch.sum(log_p, dim)
        else:
            return log_p
    
    def sample_base(self, x_1):
        # Gaussian base distribution
        if self.prob_path == "icfm":
            return torch.randn_like(x_1)
        elif self.prob_path == "fm":
            return torch.randn_like(x_1)
        else:
            return None
    
    def sample_p_t(self, x_0, x_1, t):
        if self.prob_path == "icfm":
            mu_t = (1. - t) * x_0 + t * x_1
            sigma_t = self.sigma
        elif self.prob_path == "fm":
            mu_t = t * x_1
            sigma_t = t * self.sigma - t + 1.
        
        x = mu_t + sigma_t * torch.randn_like(x_1)
        
        return x
    
    def conditional_vector_field(self, x, x_0, x_1, t):
        if self.prob_path == "icfm":
            u_t = x_1 - x_0
        elif self.prob_path == "fm":
            u_t = (x_1 - (1. - self.sigma) * x) / (1. - (1. - self.sigma) * t)
        
        return u_t

    def forward(self, x_1, reduction='mean'):
        # =====Flow Matching
        # =====
        # z ~ q(z), e.g., q(z) = q(x_0) q(x_1), q(x_0) = base, q(x_1) = empirical
        # t ~ Uniform(0, 1)
        x_0 = self.sample_base(x_1)  # sample from the base distribution (e.g., Normal(0,I))
        t = torch.rand(size=(x_1.shape[0], 1))
        
        # =====
        # sample from p(x|z)
        x = self.sample_p_t(x_0, x_1, t)  # sample independent rv 

        # =====
        # invert interpolation, i.e., calculate vector field v(x,t)
        t_embd = self.time_embedding(t)
        v = self.vnet(x + t_embd)
        
        # =====
        # conditional vector field
        u_t = self.conditional_vector_field(x, x_0, x_1, t)

        # =====LOSS: Flow Matching
        FM_loss = torch.pow(v - u_t, 2).mean(-1)
        
        # Final LOSS
        if reduction == 'sum':
            loss = FM_loss.sum()
        else:
            loss = FM_loss.mean()

        return loss

    def sample(self,  batch_size=64):
        # Euler method
        # sample x_0 first
        x_t = self.sample_base(torch.empty(batch_size, self.D))
        
        # then go step-by-step to x_1 (data)        
        ts = torch.linspace(0., 1., self.T)
        delta_t = ts[1] - ts[0]
        
        for t in ts[1:]:
            t_embedding = self.time_embedding(torch.Tensor([t]))
            x_t = x_t + self.vnet(x_t + t_embedding) * delta_t
            # Stochastic Euler method
            if self.stochastic_euler:
                x_t = x_t + torch.randn_like(x_t) * delta_t
        
        x_final = torch.tanh(x_t)
        return x_final
    
    def log_prob(self, x_1, reduction='mean'):
        # backward Euler (see Appendix C in Lipman's paper)
        ts = torch.linspace(1., 0., self.T)
        delta_t = ts[1] - ts[0]
        
        for t in ts:
            if t == 1.:
                x_t = x_1 * 1.
                f_t = 0.
            else:
                # Calculate phi_t
                t_embedding = self.time_embedding(torch.Tensor([t]))
                x_t =x_t - self.vnet(x_t + t_embedding) * delta_t
                
                # Calculate f_t
                # approximate the divergence using the Hutchinson trace estimator and the autograd
                self.vnet.eval()  # set the vector field net to evaluation
                
                x = torch.FloatTensor(x_t.data)  # copy the original data (it doesn't require grads!)
                x.requires_grad = True 
                
                e = torch.randn_like(x)  # epsilon ~ Normal(0, I) 
                
                e_grad = torch.autograd.grad(self.vnet(x).sum(), x, create_graph=True)[0]
                e_grad_e = e_grad * e
                f_t = e_grad_e.view(x.shape[0], -1).sum(dim=1)

                self.vnet.eval()  # set the vector field net to train again
        
        log_p_1 = self.log_p_base(x_t, reduction='sum') - f_t
        
        if reduction == "mean":
            return log_p_1.mean()
        elif reduction == "sum":
            return log_p_1.sum()

```

# Question
---


# Reference
---


# Attachment
---
![[FLOW MATCHING FOR GENERATIVE MODELING 1.pdf]]