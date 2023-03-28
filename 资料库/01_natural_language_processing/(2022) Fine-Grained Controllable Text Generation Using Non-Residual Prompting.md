# Information
---


# Mainly Idea
---
![[Pasted image 20230328134008.png]]
![[Pasted image 20230328134020.png]]
将Control key用一个新的encoder.

真正预测的时候，考虑前面所有正常的输入hidden，再加上这个control key的hidden,
**注意，previous的hidden没有见过prompt的，（如果直接将他们拼接在一起进行计算，previous的hidden是包含prompt的）**
![[Pasted image 20230328134044.png]]
# Reference
---
-   plug-and-play decoding strategies:
	-   [1912.02164.pdf (arxiv.org)](https://arxiv.org/pdf/1912.02164.pdf)
-   https://aclanthology.org/2022.acl-long.471.mp4

# Attachment
---
![[2022.acl-long.471.pdf]]