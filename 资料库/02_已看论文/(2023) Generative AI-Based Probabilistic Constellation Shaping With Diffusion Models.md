Tags: #Tag_物理层 
# Information
---


# Mainly Idea
---
It designs the probability of occurrence of constellation symbols within the correspoinding geometry.

只有训练了一个DDPM，即做Probabilistic shaping又做Symbol reconstruction。
训练方式：
- 获取$x_0$ (randomly probabilistic shaping), 可以随机多次采样，选择不同symbols
- $x_0$ 添加不同时间长度的noise, 模拟不同SNR效果。
- 训练模型。
使用方式①：Probabilistic shaping
- 平均才1000个symbols点，计算SNR对应的噪音进行加噪。
- Diffusion模型去噪获得结果，
- 计算结果的概率（通过个数）
使用方式②：接收端去噪。
- 接收到的symbols
- 通过diffusion去噪


DDPM is learning the diffusion process for generating constellation symbos.
![[Pasted image 20240817140343.png]]
==bits to symbols会改变，由SNR决定。==

(#) $x$和$s$是一一对应的，可以直接将x理解成s也可以（原文公式15下面所提）
![[Pasted image 20240817151205.png]]
训练的时候如上。

测试的时候，将SNR计算的Noise加入到symbol中，通过diffusion获得概率图进行操作。并且还能去噪。
# Question
---
**Probabilistic Constellation Shaping 的基本概念如下：**
1. **非均匀概率分布**：==与传统方法不同，PCS 通过分配不同的概率给星座图中的不同符号点，使得某些符号（通常是那些靠近原点、功率较低的符号）比其他符号更频繁地被选择。这种方法可以降低平均传输功率并减少误码率==。
2. **信道优化**：通过调整符号选择的概率分布，PCS 可以更好地匹配信道条件，最大化信道容量。它尤其适用于高噪声或信道不理想的情况，使得通信系统在更广泛的条件下保持高效。
3. **提升传输效率**：PCS 可以在不增加带宽的情况下提升信息传输速率，因为它有效地利用了星座图中所有符号的潜在信息容量。
4. **减少误码率**：通过减少高功率符号的使用频率，PCS 可以降低信号在传输过程中被噪声破坏的风险，从而减少误码率。
Modulation Order(调制阶数)
	![[Pasted image 20240817140841.png]]

# Reference
---


# Attachment
---
![[2023.Generative AI-Based Probabilistic Constellation Shaping With Diffusion Models.pdf]]