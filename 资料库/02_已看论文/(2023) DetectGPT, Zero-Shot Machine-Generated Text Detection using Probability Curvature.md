#Tag_自然语言处理 #Tag_基础理论 
# Information
---
- Stanford University

# Mainly Idea
---
- 发现有一个显现，Large language models (LLMs) tends to occupy negative curvature regions of the model's log probability function. Leveraging this observation, they then define a new curvature-based criterion for judging if a passage is generated from a given LLM.
- ![[Pasted image 20230307102836.png]]
- 整体流程：
- 1：用一个其他模型对输入的句子进行各种改写。
- 2：用GPT-3获得每一个改写的p,
- 3：用原句的P和改写后的P进行计算，如果高于阈值则。句子来源于GPT3
![[Pasted image 20230307103039.png]]

# Reference
---
- Occupy negative curvature regions?
	- 负曲率

# Attachment
---
![[2301.11305.pdf]]