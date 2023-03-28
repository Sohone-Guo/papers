# Information
---
- [[Alibaba Group]]
- [[视频生成任务]]

# Mainly Idea
---
- 为了简化Fusion图片维度很大的问题
	- 使用Encoder将图片压缩到一个隐层空间后，再进行Fusion
	- 使用Decoder将Fusion的隐层空间转化为图片
- 整体架构图如下![[Pasted image 20230216130423.png]]
-  如何结合文本和<span style="background:#ff4d4f">图片</span>信息的？
	- 结合的方式就是通过，Cross Attn, sample作为query, CLIP等作为hiddens.
- 具体算法的内容
	- CLIP: 用于当前的文本信息, 具体论文参考 [[03_multimodal/(2021) Learning Transferable Visual Models From Natural Language Processing]]
	- BLIP: 用于将历史的文本和历史生成的图片结合起来

# Reference
---


# Attachment
---
![[synthesizing coherent story with auto-regressive latent diffusion models.pdf]]

![[ARLDM-main.zip]]