#Tag_基础理论 
# Information
---


# Mainly Idea
---
重要的出发点：
It is based on the idea that a good representation is one in which the data has a distribution that is easy to model.

设计一个逆函数，但是逆函数不能太复杂，并通过Chane of variables的方式减少逆函数所需要的复杂度
- Change of Variables的Loss公式：
	- ![[Pasted image 20230506162948.png]]
- 其中Det的计算方法：
	- ![[Pasted image 20230506163130.png]]

# Reference
---
- 为什么需要Det, 不能直接逆函数吗？
	- 逆函数比较简单，通过change of variables的方法可以减轻逆函数所需要的复杂度。
- https://github.com/VincentStimper/normalizing-flows/
- invertible好处![[Pasted image 20230524125744.png]]
# Attachment
---
![[1410.8516.pdf]]
![[normalizing-flows-master.zip]]