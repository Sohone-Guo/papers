Tags: #Tag_计算机视觉 
# Information
---


# Mainly Idea
---
Current Problem: Generation of irrelevant context, commonly known as "hallucination", as the length of the text increases and the impact of the video diminishes.

生成的文本可能过于关注文本信息，而忽略视频信息，

制作一个attention，区分视频特征的位置，和文本的位置，分别做Attention导致，视频和文本关注的权重一致。
![[Pasted image 20240114194014.png]]
![[Pasted image 20240114194100.png]]

# Question
---


# Reference
---
- Video-language Model: Video+Question(text)→Answer(text)

# Attachment
---
![[Vista-LLAMA.pdf]]