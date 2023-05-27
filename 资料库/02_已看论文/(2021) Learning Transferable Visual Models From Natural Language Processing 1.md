#Tag_自然语言处理 #Tag_计算机视觉 #Tag_多模态 
# Information
---
- 2021
- [[Openai]]
- [[预训练模型]]

# Mainly Idea
---
类似于做image caption, 但是没有直接输出句子

训练：如Figure1. 用对比学习的方式，将句子转成句子向量，
（图片向量，正确句子向量）越近越好，其他越远越好，

预测：预先设计好分类结果，图片的特征计算和那个分类的句子特征最近，就是结果

# Reference
---
- Crowd-Labeled Datasets：这里指得是，人工标注了很多标签得数据集

# Attachment
---
![[CLIP.pdf]]