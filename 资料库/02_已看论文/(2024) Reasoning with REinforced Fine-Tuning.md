Tags: #Tag_基础理论 
# Information
---


# Mainly Idea
---
Reasoning的任务就是一个问题需要拆分步骤回答，常用方法是Chain-of-Thought, 但是CoT依赖数据集，通用性不好。
所提方案是SFT微调之后，再使用Reinforced 方式继续训练，大概是sample出来CoT的数据，挑选质量高的进行训练。
因为微调后的模型可以对问题进行拆分步骤了，Reinforced方式就可以再拆分步骤里面挑选比好的进行泛用性学习。
![[{256180CF-A93B-421A-9E82-68B0EDE06593}.png]]
![[Pasted image 20241211111754.png]]
# Question
---
- Where an abundance of reasoning paths are automatically sampled given the question and the rewards are naturally derived from the ground-truth answers. (如何做到的？)
	- 因为微调CoT数据后的模型可以对问题进行拆分步骤了，Reinforced方式就可以再拆分步骤里面挑选比好的进行泛用性学习。

# Reference
---


# Attachment
---
![[2024.Reasoning with REinforced Fine-Tuning.pdf]]