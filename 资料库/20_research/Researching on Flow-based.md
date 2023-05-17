# 2015
---
- [[(2015) NICE, NON-LINEAR INDEPENDENT COMPONENTS ESTIMATION]].
	- 主要原理和信息
		1. 定义了Flow-based的理论来源: We take the view that a good representation is one in which the distribution of the data is easy to model.
		2. A key novelty (Easy determinant of the Jacobian; Easy inverse)
			1. Split $x$ to $(x_1, x_2)$
		3. Coupling Layer: additive coupling layer and combining coupling layers.
	- 优缺点
		1. 优点：Easy determinant of the Jacobian; Easy inverse
		2. 缺点：特征提取和Transform太简单，不足以复杂特征。
# 2016
---
- [[(2016) Variational inference with normalizing flows]]
	- 基于Hierarchy of L layers of Gaussian latent variables
	- 通过Normalization FIow增加Variational inference 的准确性
	- Flow-based模块参考了[[(2015) NICE, NON-LINEAR INDEPENDENT COMPONENTS ESTIMATION]]
- [[(2016) Improved variational inference with inverse autoregressive flow]]
	- IVF: 最早的Autoregressive Flow,

# 2017
---
-  [[(2017) Density estimation using Real NVP]]
	- 可以函数的Coupling部分太简单，提出一个X拆分多个部分后，其通过函数组合的可能性。
- [[(2017) Masked autoregressive flow for density estimation]]
	- 参考了[[(2016) Improved variational inference with inverse autoregressive flow]]， [[(2017) Density estimation using Real NVP]]
	- Mask是快速实现Autoregression提升速度,. 再将autoregressive看成Flow, 实现Estimation.
	- 个人感觉是change variable使得映射变简单了。

# 2018
---
- [[(2018) Glow, Generative Flow with Invertible 1x1 Convolutions]]
	- 可以函数的Coupling部分太简单，提出一个X拆分多个部分后，其通过1x1的Con函数自动学习组合的可能性。
- [[(2018) Neural autoregressive flows]]
	- 链接的论文：
		- [[(2017) Masked autoregressive flow for density estimation]]
		- [[(2016) Improved variational inference with inverse autoregressive flow]]
	- 主要贡献
		- 优化了affine transformations
	- Autoregressive Flow
- [[(2018) Unsupervised Learning of Syntactic Structure with Invertible Neural Projections]]

# 2019
---
- [[(2019) Discrete Flows, Invertible Generative Models of Discrete Data]]
	- 链接论文：[[(2017) Density estimation using Real NVP]]
	- 第一篇Normalizing flow applied to discrete distributions.
	- 其他论文总结
		- Autoregressive flows: $\mu$ 是从过去生成的结果中获取 [[(2016) Variational inference with normalizing flows]]; [[(2017) Masked autoregressive flow for density estimation]]; [[(2016) Improved variational inference with inverse autoregressive flow]]
		- Bipartite flows: $\mu$ 是从部分$x$中获取 [[(2017) Density estimation using Real NVP]]
- [[(2019) FlowSeq, Non-Autoregressive Conditional Sequence Generation with Generative Flow]]
	- Split along time dimension First
- [[(2019) Neural Density Estimation and Likelihood-free Inference]]
- [[(2019) Sum-of-Squares Polynomial Flow]]
	- Autoregression Flow
- [[(2019) Block neural autoregressive flow]]
- [[(2019) Flow++, Improving flow-based generative models with variational dequantization and architecture design]]
-  [[(2019) Unconstrained Monotonic Neural Networks]]
- [[(2019) Neural Importance Sampling]]
- [[(2019)  Cubic-Spline Flows]],
- [[(2019) Neural Spline Flows]].
- [[(2019) Invertible Residual Networks]]
- [[(2019) Residual Flows for Invertible Generative Modeling]]
- [[(2019) Sylvester Normalizing Flows for Variational Inference]]
- [[(2019) Density Matching for Bilingual Word Embedding]]

# 2020
---
- [[(2020) Invertible generative modeling using linear rational splines]],
- [[(2020) Targeted free energy estimation via learned mappings]]

# 2021
---
- [[(2021) Continuous Language Generative Flow]]
	- normalizing flow [[(2016) Variational inference with normalizing flows]] , is widely explored in computer vision and representation learning but less explored for NLG tasks.
	- Flow models have been shown to be capable of improving probability density estimation, including variational inference  [[(2016) Variational inference with normalizing flows]] and exact density estimation [[(2015) NICE, NON-LINEAR INDEPENDENT COMPONENTS ESTIMATION]].
	- Generative flow is one type of flow model and first proposed by  [[(2015) NICE, NON-LINEAR INDEPENDENT COMPONENTS ESTIMATION]]., [[(2017) Density estimation using Real NVP]]; [[(2018) Glow, Generative Flow with Invertible 1x1 Convolutions]].
	- Taking advantage of its invertible structure, it can perform an exact density estimation of the input distribution. Thus, during generation, we can sample from its latent space and then generate new examples through its invertible decoder. Generative flow shows strong performance on image generation, attribute manipulation, and latent space inference [[(2018) Glow, Generative Flow with Invertible 1x1 Convolutions]].
	- Some recent works have developed density estimation models targeted on character-level discrete data  [[(2019) Discrete Flows, Invertible Generative Models of Discrete Data]]
	- explored using the flow architecture as an extra data encoder that provides latent features to support nonautoregressive text generation [[(2019) FlowSeq, Non-Autoregressive Conditional Sequence Generation with Generative Flow]].
	- Autoregressive flows were previously developed [[(2017) Masked autoregressive flow for density estimation]]; [[(2018) Neural autoregressive flows]] for stronger density estimation ability. However, the autoregressive language flow model we develop here aims for better text generation quality.
- [[(2021) Normalizing Flows for Probabilistic Modeling and Inference]]
	- The thesis of [[(2019) Neural Density Estimation and Likelihood-free Inference]]  and the survey by [[(2020 Normalizing Flows, An Introduction and Review of Current Methods)]] have made steps in establishing this broader understanding.
	- Autoregression Flow: [[(2019) Sum-of-Squares Polynomial Flow]]; [[(2016) Improved variational inference with inverse autoregressive flow]]; [[(2017) Masked autoregressive flow for density estimation]]
		- Affine transformers are popular in the literature, having been used in models such as [[(2015) NICE, NON-LINEAR INDEPENDENT COMPONENTS ESTIMATION]], [[(2017) Density estimation using Real NVP]], [[(2016) Improved variational inference with inverse autoregressive flow]], [[(2017) Masked autoregressive flow for density estimation]], and [[(2018) Glow, Generative Flow with Invertible 1x1 Convolutions]].
		- Combination-based transformers: Variants of combination based transformers have been used in models such as [[(2018) Neural autoregressive flows]], [[(2019) Block neural autoregressive flow]], and [[(2019) Flow++, Improving flow-based generative models with variational dequantization and architecture design]]
		- Integration-based transformers: Another way to dene a non-affine transformer is byrecognizing that the integral of some positive function is a monotonically increasing function. [[(2019) Unconstrained Monotonic Neural Networks]]
		- Spline-based transformers: So far, we have discussed non-affine transformers that can be made arbitrarily  exible, but don't have an analytic inverse. One way to overcome this limitation is by implementing the transformer as a monotonic spline, The following options have been explored thus far, in order of increasing exibility: linear and quadratic splines [[(2019) Neural Importance Sampling]], cubic splines[[(2019)  Cubic-Spline Flows]], linear-rational splines [[(2020) Invertible generative modeling using linear rational splines]], and rational-quadratic splines [[(2019) Neural Spline Flows]].
	- Linear Flows: [[(2018) Glow, Generative Flow with Invertible 1x1 Convolutions]]; [[(2019) Neural Spline Flows]]
	- Residual Flows: [[(2019) Invertible Residual Networks]]; [[(2019) Residual Flows for Invertible Generative Modeling]]
		- Planar Flow: [[(2016) Variational inference with normalizing flows]]
		- Sylvester Flow: [[(2019) Sylvester Normalizing Flows for Variational Inference]]
		- Radial Flow: [[(2016) Variational inference with normalizing flows]]
	- Application: 
		- Text: [[(2019) Discrete Flows, Invertible Generative Models of Discrete Data]] take this approach, showing performance in character-level language modeling competitive to RNNs while having superior generation runtime; [[(2020) Targeted free energy estimation via learned mappings]]; [[(2019) Density Matching for Bilingual Word Embedding]]; [[(2018) Unsupervised Learning of Syntactic Structure with Invertible Neural Projections]]

# 2022
---
- [[(2022) FastFlows, Flow-Based Models for Molecular Graph Generation]]
- 
# 2023
---
- [[(2023) Flow Matching for Generative Modeling]]
- [[(2023) Normalizing Flow-based Neural Process for Few-Shot Knowledge Graph Completion]]


# 后续方向
---

|  方向 | 难易度  | 解决的问题  | 可能方案 |
|---|---|---|---|
| Encoder→Flow-based→Decoder  | 易  | 输入输出再没有Cross-attention的情况输出不一致情况  |结构化Flow-based|
| Flow-based as Decoder | 难 | Autoregressive Flow-based on NLP  | - |
| Autoregression decoder with Flow-based  | 中 | 解决少数据情况，分布不稳定，语法问题  | - |
