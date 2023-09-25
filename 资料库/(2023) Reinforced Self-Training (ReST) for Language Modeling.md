Tags: #Tag_自然语言处理 #Tag_基础理论 
# Information
---
- [[google]]

# Mainly Idea
---
The quality of the policy learnt offline inevitably depends on the properties of the offline datasets.

# Question
---
- ReST produces a dataset by generating samples from the policy, where are then used to improve the LLM policy using offline RL algorithms.
- Grow step: a policy generates a datasets.
- Improve step: filtered dataset is used to fine-tune the policy.
- Online training: requires sampling from the updated policy.
- Offline training: learn from fixed samples.

# Reference
---


# Attachment
---
![[2308.08998.pdf]]