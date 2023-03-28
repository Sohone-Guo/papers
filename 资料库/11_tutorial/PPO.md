前后两个策略之间的 KL散度小于某一阈值

传统的 Policy Gradient Method 仅仅能够利用采样得到的 samples 进行一次更新，就要将这些samples扔掉，重新采样，再实现更新。而本文所提出的方法可以进行 

multiple epochs of minibatch updates

[Proximal Policy Optimization Algorithms - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/82494810)

https://arxiv.org/pdf/1707.06347.pdf