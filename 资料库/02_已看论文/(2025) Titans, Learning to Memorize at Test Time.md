Tags: #Tag_基础理论 
# Information
---


# Mainly Idea
---
问题：Transformer 的核心瓶颈长上下文太贵， 线性 Transformer / 现代线性循环模型省了算力，但“记不住”。

在测试的时候，如果一个很长的内容，使用网络模型去记忆历史。
测试过程需要Loss参与训练网络记忆模型。在Transformer中，qkv, 就是中间的检索内容，那么如果训练这个记忆网络，就是输入q, 网络需要反馈v， 通过这样的方式记忆网络。

# Question
---


# Reference
---


# Attachment
---
![[2501.00663v1.pdf]]