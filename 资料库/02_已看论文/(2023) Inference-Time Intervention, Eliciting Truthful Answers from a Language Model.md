Tags: #Tag_自然语言处理 
# Information
---


# Mainly Idea
---
Only solve the mistake where the model in certain sense, "knows" the correct answer. (A wrong answer in one context, correct answer in a different context)

- prob(LogisticRegression): 训练一个分类器（训练1000条，测试假设有100条正确QA对，和100条错误QA对），对每一个层的每一个点将获得（使用上面数据进行分类器训练）既可以对每一个head都进行预测正确和错误的关系。（可以判断head对正确和错误数据的判断力）
- activation: 可以理解为attention-head之后的数值
- Truthful direction为：关于其中一个head的truthful direction, 使用当前head的prob分类器，将正确标签的参数值进行均值计算，减去，错误标签的参数值进行均值计算，则为方向。
- Dataset: Label正确为1，错误为0
# Question
---
- ITI operates by shifting model activations during inference, following a set of directions across a limited number of attention heads?
- Truthfulness, helpfulness and demonstrate?
- Generation accuracy and probe accuarcy?
# Reference
---
- Kadavath et al. (2022) find language models can generate and then slf-evaluate their own ansers with high accuracy.

# Attachment
---
![[honest_llama-master.zip]]

![[2306.03341.pdf]]