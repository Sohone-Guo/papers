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

# Reference
---


# Attachment
---
![[Scaling Transformer to 1M tokens and beyond with RMT.pdf]]