#Tag_基础理论 
# Information
---
- VQ-VAE
- Sequence Models
- [[Discrete Variable]]
- Neural Machine Translation
# Mainly Idea
---
![[Pasted image 20230419174552.png]]
- $X$ → Encoder(Self-attention-layer)
- $Y$ → Encoder(CNN) (减少长度hidden)
- $l=z_q(y)$ 是VQ后的结果
- Decoder, 将$z_q(y)$ 通过CNN 增加长度，后Transformer到$y$

为了预测是时候获得的$l$， 训练另一个模型(transformer-regressively), 获得$l=lp(x)$.


# Reference
---
- [[(2018) ⭐Theory and Experiments on Vector Quantized Antoencoders]]

# Attachment
---
![[Fast Decoding in Sequence Ｍodels Using Discrete Latent Variables (2018).pdf]]