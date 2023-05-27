#Tag_语音技术 #Tag_自然语言处理 
# Information
---
- Google Brain
- MIT

# Mainly Idea
---
Mainly Idea
- Trains the model to disccretize input continuous speech signals into a finite set of discriminative speech tokens.
- Trains the model to learn contexturalized speech representations via solving a masked prediction task consuming the discretized tokens.

![[Pasted image 20230414134518.png]]

- Contrastive: 参考Reference Contrastive Loss

# Reference
---
- Contrastive Loss: ![[Pasted image 20230414134459.png]]
	- Q: 参考wav2vec 2.0, P2页中Quantization module部分，由Codebook获取。使用Codebook的方式，论文中使用了Gumber Softmax, ![[Pasted image 20230414134916.png]]

# Attachment
---
![[gumbel_vector_quantizer 1.py]]
![[kmeans_vector_quantizer 1.py]]

![[2108.06209v2 1.pdf]]

![[2006.11477.pdf]]