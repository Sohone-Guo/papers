# Information
---


# Mainly Idea
---
Models sucb as residual networks, recurrent neural netowrk decoders, and normalizing flows:
$h_{t+1}=h_{t}+f(h_t,\theta)$  → $\frac{dh(t)}{dt}=f(h(t),t,\theta)$

The model can be trained directly, but incurs a high memory cost.

- ODE Solve
	- ![[Pasted image 20230522145022.png]]
	- Euler's Method: ![[Pasted image 20230522144921.png]]
	- Runge-Kutta Method:![[Pasted image 20230522144950.png]]
- Adjoint Sensitivity Method
	- ![[Pasted image 20230522145213.png]]
# Reference
---
- 相关资料
	- https://www.youtube.com/watch?v=sIFnARdTVvE
- 其他资料
	- 公式离散化
		- ![[Pasted image 20230522134317.png]]
	- what is the adjoint sensitivity method?
		- ?
	- Reverse-mode differentiation of an ODE solution
		- ![[Pasted image 20230522134243.png]]
# Attachment
---
- PPT
	- ![[Volokhova_CNF.pdf]]
- paper: ![[Neural Ordinary Differential Equation.pdf]]