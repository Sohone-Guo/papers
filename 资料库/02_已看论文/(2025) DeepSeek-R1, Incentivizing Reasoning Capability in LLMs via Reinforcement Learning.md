Tags: #Tag_基础理论 
# Information
---


# Mainly Idea
---

**DeepSeek-R1-Zero:** 直接使用强化学习训练LLM（无SFT模型），Reward是a rule-based reward system。（譬如根据计算器或者代码执行等获取）
![[Pasted image 20250203121025.png]]
**DeepSeek-R1**：使用long CoT数据集微调LLM（无SFT模型），再使用**DeepSeek-R1-Zero**继续训练模型，采样数据集（其他领域），继续微调模型（Reason任务继续使用R1-Zero，正常任务使用正常的Reward）

# Question
---


# Reference
---


# Attachment
---
![[07_DeepSeek-R1（重点看）.pdf]]