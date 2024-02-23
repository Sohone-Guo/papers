

# Q1: 强化学习是什么？

Actor和环境互动，为什么不直接获取全部资料呢？on-policy(actor to train and actor for interacting is the same)? off-policy(not same，利用PPO解决)?
A: 自己随机采样资料，在一些过程步骤很长的游戏下，我们很难通过随机采样获取，譬如接近成功的数据，只能获取大量前期的数据。而强化学习在搜索到前期步骤后，不同时期可搜索到不同任务。

Example1:
==收集2组资料：==
- ==数据①：一个机器人按照当前policy玩一个游戏的全部State和Actor，以及最后的得分。==
- ==数据②：一个机器人按照当前policy玩一个游戏的另一组全部State和Actor，以及最后的得分。==
==得分高的一组，譬如数据①，里面的Actor作为target, 训练Policy，更新模型。==
==将数据②，作为远离的target，训练policy，更新模型==

Example2: Cumulated reward, 让模型眼光长远，不要局限当前r
![[Pasted image 20240223112918.png]]

Q: 只有最后一个有R怎么办？如Example1， 整体学习
# Q2：NLP中的强化学习是什么？


# Q3：强化学习与GAN的区别？

监督学习，或者GAN，都是对任务结果的直接监督，譬如分别任务，使用分类的结果。
GAN虽然是判别器进行监督，但是判别器可以通过梯度获取具体任务标签的方向。

强化学习，不是直接作用与结果（reward是黑盒子不能反推定义具体哪个错误）。

# Q4: 文本任务使用强化学习和判别器的区别是？

强化学习：结果比较好的样例，就多学点。
判别器：如果让差的结果变成好的。


# Reference
---
- [【機器學習2021】概述增強式學習 (Reinforcement Learning, RL) (一) – 增強式學習跟機器學習一樣都是三個步驟 (youtube.com)](https://www.youtube.com/watch?v=XWukX-ayIrs)
	- ![[Pasted image 20240223111734.png]]
	- ![[Pasted image 20240223111757.png]]
	- ![[Pasted image 20240223112849.png]]
- [【機器學習2021】概述增強式學習 (Reinforcement Learning, RL) (二) – Policy Gradient 與修課心情 (youtube.com)](https://www.youtube.com/watch?v=US8DFaAZcp4)
	- ![[Pasted image 20240223124920.png]]
- [DRL Lecture 2: Proximal Policy Optimization (PPO) (youtube.com)](https://www.youtube.com/watch?v=OAKAZhFmYoI)