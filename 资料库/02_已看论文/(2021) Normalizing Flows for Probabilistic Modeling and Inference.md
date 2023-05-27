#Tag_基础理论 
# Information
---
- [[DeepMind]]

# Mainly Idea
---
Normalizing flow improve their expressive power.

#### 2 Normalizing Flow
2.3 Using Flows for Modling and Inference
2.3.1 Forward KL Divergence and Maximum likelihood estimation
![[Pasted image 20230515135701.png]]
2.3.2 <font color="#c00000">Reverse KL Divergence: often used for *variational inference*</font> <font color="#c00000">(没懂)</font>
![[Pasted image 20230515135726.png]]
#### 3 Constructing Flows Part Ⅰ: Finite Compositions
![[Pasted image 20230515140114.png]]
- Autoregressive Flows
	- 定义
		- $z'_i = T(z_i;h_i)$, $h_i=c_i(z_{<i})$    
			- $T$ is transformer
			- $C$ is conditioner
		- 相关图片![[Pasted image 20230515140720.png]]
	- 公式
		- Transformer type
			- Affine transformers: ![[Pasted image 20230515141015.png]]
			- Combination-based transformers: 有很多小的transformers组成 ![[Pasted image 20230515141329.png]]
			- Intergration-based transformers. <font color="#c00000">(没懂)</font>
			- Spline-based transformers: the transformer $T(z_i, h_i)$将 $z_{i0}...z_{ik}$ 用于each interval $[z_{i(k-1)}, z_{ik}]$
		- Conditioner type
			- Recurrent conditioners: ![[Pasted image 20230515142457.png]]
			- Masked conditioners
			- Coupling layers: ![[Pasted image 20230515143204.png]]
- Linear Flows
- Residual Flows
- 
# Reference
---


# Attachment
---
![[Normalizing Flows for Probabilistic Modeling and Inference.pdf]]