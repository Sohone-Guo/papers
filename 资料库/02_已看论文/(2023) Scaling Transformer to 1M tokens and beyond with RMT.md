#Tag_基础理论 #Tag_自然语言处理 
# Information
---


# Mainly Idea
---
![[Pasted image 20230514224623.png]]
设计了多种测试模型的方法（如下图）：
- 第一个测试记忆的方法：第一句Fact的内容, 之后很多无关的内容，最后一个是Q，需要模型找到Fact回答出来A，来验证Memorize, 这个中间可以很长。
- 第二个测试定位和记忆的方法：此次Fact可以再任何位置，模型需要先定位，再回答问题。
- 第三个是给两个Fact, 让模型回答一个A。
![[Pasted image 20230514224707.png]]
使用现有的Recurrent Memory mechanism使得Transformer可以用更长的输入。
![[Pasted image 20230514231201.png]]
- 红色是输入，蓝色momery, 每个segment是一个Transformer.
- $M_0$ 和 $input_1$ 作为输入， $input_1$和$M_1$是输出，$M_1$作为下一个Segment的输入
- 整体过程可以当成RNN
	- ![[Pasted image 20230514231429.png]]
	- 参考：[Scaling Transformer to 1M tokens and beyond with RMT (Paper Explained) - YouTube](https://www.youtube.com/watch?v=4Cclp6yPDuw&t=326s)
# Reference
---


# Attachment
---
![[Scaling Transformer to 1M tokens and beyond with RMT.pdf]]