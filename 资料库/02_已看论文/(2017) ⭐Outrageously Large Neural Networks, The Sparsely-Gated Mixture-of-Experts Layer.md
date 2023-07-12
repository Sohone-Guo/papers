Tags: #Tag_基础理论 #Tag_MoE #Tag_自然语言处理 
# Information
---


# Mainly Idea
---
Dramatically increasing model capacity without a proportional increase in compuation.

# Question
---
- 如何保证模型会在多个Expert中选择一个，而不是每次都只选择一个？(called as balancing expert utilization)
	- Soft constraint approach: ![[Pasted image 20230712141110.png]]
	- CV: 数据越接近，数值越小

# Reference
---
![[Pasted image 20230712141318.png]]
- [mixture-of-experts/moe.py at master · davidmrau/mixture-of-experts (github.com)](https://github.com/davidmrau/mixture-of-experts/blob/master/moe.py)
# Attachment
---
![[Outrageously Large Neural Networks, The Sparsely-Gated Mixture-of-Experts Layer.pdf]]