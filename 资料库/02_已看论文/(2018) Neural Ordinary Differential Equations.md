#Tag_基础理论 
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
	- [Chapter 3: Neural Ordinary Differential Equations (implicit-layers-tutorial.org)](http://implicit-layers-tutorial.org/neural_odes/)
	- [ordinary differential equations - Neural ODEs - Adjoint Sensitivity Method for multiple time points - Mathematics Stack Exchange](https://math.stackexchange.com/questions/4176064/neural-odes-adjoint-sensitivity-method-for-multiple-time-points)
- 其他资料
	- 公式离散化
		- ![[Pasted image 20230522134317.png]]
	- what is the adjoint sensitivity method?
		- ?
	- Reverse-mode differentiation of an ODE solution
		- ![[Pasted image 20230522134243.png]]
	- Jacobi's formula
		- ![[Pasted image 20230524000014.png]]
		- [Jacobi's formula - Wikipedia](https://en.wikipedia.org/wiki/Jacobi%27s_formula)
# Attachment
---
- PPT
	- ![[Volokhova_CNF.pdf]]
	- ![[20200710_Mila_Neural_ODEs_tutorial_Vikram_Voleti 1.pdf]]
- paper: ![[Neural Ordinary Differential Equation.pdf]]