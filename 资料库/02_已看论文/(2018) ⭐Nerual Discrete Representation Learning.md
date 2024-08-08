#Tag_计算机视觉 
# Information
---
- VQ-VAE

# Mainly Idea
---
![[Pasted image 20230414141202.png]]

### Training
- Copy gradients from decoder input $z_q(x)$ to encoder output $z_e(x)$ .
	- $z_q(x)=z_e(x)+(z_q(x)-z_e(x)).detach()$ 
- Total training objective:
	- $L=logp(x|z_q(x))+||sg[z_e(x)]-e||^2_2+\beta||z_e(x)-sg[e]||^2_2$ 
		- decoder optimises is the first loss term
		- encoder optimises is the first and last loss term
		- the embeddings optimises is the middle loss term

### Generation
训练另一个autoregressive distribution模型
例如：
- 获取所有图片的Discrete hidden.
- 训练一个PixelCNN or RNN 等，给部分discrete hidden预测下一个discrete hidden
- 完成整体discrete hidden后，通过decode进行照片生成
# Reference
---
- VQ-VAE dictioniary updates with Exponential Moving Averages
	- A set of ${z_{i,1}, z_{i,2}, z_{i,n_i}}$ be outputs from the encoder that are closest to dictionary item $e_i$.
		- $n_i$ 是与$e_i$ 相似的个数
	- ![[Pasted image 20230419164243.png]]
- 为什么codebook不会塌陷成一个vector?
	- 因为初始状态encoder和codebook的空间一致
# Attachment
---
![[1711.00937v2.pdf]]