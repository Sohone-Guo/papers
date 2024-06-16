Tags: #Tag_计算机视觉 
# Information
---


# Mainly Idea
---
虽然说是Reward但是不是真的强化学习。

Duffsion生成噪音，噪音-输入通过reward模型，是的reward分值最小化。
因为噪音是预测出来的结果，所以可以更新模型，

Reward是事前人工标注训练数据获取的结果。
论文伪代码：
![[Pasted image 20240616223204.png]]

真实代码：
![[Pasted image 20240616223332.png]]

# Question
---


# Reference
---
- [ImageReward/ImageReward/ReFL.py at main · THUDM/ImageReward · GitHub](https://github.com/THUDM/ImageReward/blob/main/ImageReward/ReFL.py)
# Attachment
---
![[2304.05977v4.pdf]]