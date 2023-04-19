# Information
---
- VQ-VAE #VAE

# Mainly Idea
---
![[Pasted image 20230414141202.png]]

- Copy gradients from decoder input $z_q(x)$ to encoder output $z_e(x)$ .
	- $z_q(x)=z_e(x)+(z_q(x)-z_e(x)).detach()$ 
- Total training objective:
	- $L=logp(x|z_q(x))+||sg[z_e(x)]-e||^2_2+\beta||z_e(x)-sg[e]||^2_2$ 
		- decoder optimises is the first loss term
		- encoder optimises is the first and last loss term
		- the embeddings optimises is the middle loss term

# Reference
---


# Attachment
---
![[1711.00937v2.pdf]]