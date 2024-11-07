Tags: #Tag_语义通信 
# Information
---


# Mainly Idea
---
•即输入“现实中的任意视频”，其算法能逆向生成对应的“prompt”；这样，在视频通信中，发送端只需传输prompt，接收端利用AIGC可重现出像素级一致的原始视频。

•问题：视频生成Prompt可以理解，但是Prompt如何保证输出的视频是一致的？
- 回答：Stable diffusion网络不变，生成的结果和真实结果进行对比，微调prompt的embedding。获得完全匹配的embedding。
![[Pasted image 20241107121818.png]]
# Question
---
- A gradient decent-based prompt fitting framework?
	- Stable diffusion网络不变，生成的结果和真实结果进行对比，微调prompt的embedding。获得完全匹配的embedding。
- A low-rank decomposition-based bitrate control algorithm?
	- Prompt是Embedding, 不是Text, 所以Embedding需要被压缩，而压缩比例和带宽相关。
- A temporal smoothing-based prompt interpolation algorithm?
	- 每一帧的Embedding是独立的，如何将独立的Embedding变成连续（有关系），猜测有点像插值的方式

# Reference
---


# Attachment
---
![[2024.Promptus Can Prompts Streaming Replace Video Streaming with Stable Diffusion.pdf]]