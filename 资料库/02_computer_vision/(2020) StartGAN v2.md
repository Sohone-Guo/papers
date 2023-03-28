# Information
---
- 2020
- NAVER Corp

# Mainly Idea
---
- 公式定义
	- $x$ 是输入图片，$y$ 是$x$ 对应的领域标签
	- $s$ 是Style code, 来自，$s=F(z), z是高斯$ ，或者$s=E(x), x是图片$
	- $D$ 是判别器，$G$ 是生成器
	
- 相应的LOSS公式
	- $L_{adv}=E_{x,y}[logD_y(x)]+E_{x,y,z}[log(1-D_y(G(x, s)))]$
	- $L_{sty}=E_{x,y,z}[|s-E_y(G(x,s))|]$
	- $L_{ds}=E_{x,y,z_1,z_2}[|G(x,s_1)-G(x, s_2)|]$
	- $L_{cyc}=E_{x,y,y,z}[|x-G(G(x, s), s)|]$
	 

# Reference
---


# Attachment
---
![[StartGAN v2, Diverse Image Synthesis for Multiple Domains (2020).pdf]]