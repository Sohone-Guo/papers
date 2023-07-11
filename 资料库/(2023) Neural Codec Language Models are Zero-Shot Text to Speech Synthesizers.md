Tags: #Tag_语音技术 #Tag_多模态 
# Information
---
-  [[Microsoft]]

# Mainly Idea
---
VALL-E emerges in-context learning capabilities and can be used to synthesize high-quality personlized speech with only a 3-second enrolled recording of an unseen speaker as an acoustic prompt.

![[Pasted image 20230711172958.png]]


# Question
---
- 音频和文本是如何组合的？
	- 音频通过类似VQVAE这种，提取中间值作为Speech Quantization, 本身Decoder端也可以还原音频。参考[[(2022) AudioLM, a Language Modeling Approach to Audio Generation]]
		- ![[Pasted image 20230711174825.png]]

# Reference
---
- [[(2022) AudioLM, a Language Modeling Approach to Audio Generation]]

# Attachment
---
![[Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers.pdf]]