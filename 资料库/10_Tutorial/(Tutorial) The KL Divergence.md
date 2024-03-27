#Tag_Tutorial 

![[Pasted image 20240327170828.png]]

而VAE中，Loss计算公式为：
$E_{z|x}[logP(x|z)]-KL(q(z|x)||p(z))-KL(q(z|x)||p(z|x))$

最后一项省略，
![[Pasted image 20240327171252.png]]
参考：[Variational autoencoders. (jeremyjordan.me)](https://www.jeremyjordan.me/variational-autoencoders/)