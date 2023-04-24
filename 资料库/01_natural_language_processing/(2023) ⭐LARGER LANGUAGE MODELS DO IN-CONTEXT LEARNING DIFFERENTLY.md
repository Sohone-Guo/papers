# Information
---
- Google Research, Brain Team

# Mainly Idea
---
To Successfully perform In-context-learning (ICL), model can
a) mostly use semantic prior knowledge to predict labels while following the format of in-context exemplars. and / or b) learn the the input-label mappings from the presented exemplars.

结论如下：
- <font color="#00b050">The ability to override semantic priors with input-label mapping emerges with model scale, which should not be taken for granted because larger models presumably have stronger priors that are more challenging to override.</font>

![[Pasted image 20230424133342.png]]

# Reference
---
- ICL with Flipped label: Means semantic prior knowledge and input-label mappings disagree.
- ICL with semantically-unrelated labels: for example, using foo/bar instead of negative/positive.

# Attachment
---
![[2303.03846.pdf]]