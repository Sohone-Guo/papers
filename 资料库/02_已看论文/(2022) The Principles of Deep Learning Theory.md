#Tag_基础理论 #Tag_书集资料 
# Information
---


# Mainly Idea
---
# Chapter 0 Initialization

## The First-Principles

- We already understand the microscopic laws - how a network computes.
- But at the macroscopic - why it computes one particular function rather than another, that emerge from the statistical properties of these gigantic deep learning models.

## The Theoretical Minimum

- simply think of a neural network as a parameterized function: $f(x,\theta)$.
    - [Q1]: why it is a good strategy to have an initialization distribution$p(\theta)$?
    - [A1]: 统一步伐更新？更好模拟infinite wide 的一个确定的分布
- we just the parameter vector as $\theta$ $\rightarrow$ $\theta*$, $f(x, \theta*)$ is close to a desired target function $f(x)$.
    - data pair: $(x, f(x))$ # training data
    - $f(x, \theta*) \approx f(x)$ # function approximation
    - justments to the parameters is called training
    - particular procedure used to tune them is called a leanring algorithm
- Taylor expand: ![e6381cfc4f1e847123f8d1c00804d1a4.png](en-resource://database/3618:1)

    -   Problem 1: contains an infinite number of terms. As the difference between the trained and initialized parameters $\theta* \rightarrow \theta$, becomes large.
    -   Problem 2: ![3a4bdf3a15a6ee74233103d3c905104c.png](en-resource://database/3620:1) is tractable.
    -   Problem 3: And $\theta*$ can depend on everything ![b6a82dcbf1c2f2d7e75c17f14bebb796.png](en-resource://database/3622:1)
    
    
## A Principle of Sparsity
- 网络无线宽，比网络无线深更好分析，
    - 为什么？
- 当网络无线宽的时候，
    - 因为初始化的参数因为无线宽，可以确定为一个函数，这个函数到taget是一个固定值，所以![6ec31f456216eabb28bdbde60da58f66.png](en-resource://database/3624:1)
    - 初始化参数也可以确定![ae3b9e7f9efbe1f2dc9cdcf50c9d5cbf.png](en-resource://database/3626:1)
    - dependancy的参数 也可以确定![09adffb04038a87ad412451c8c15439e.png](en-resource://database/3628:1)
    
- 效果不好
    - 原因①：From the theoretical perspective, the problem with this limit is the washing out of the fine details at each neuron due to the consideration of an infinite number of incoming signals.
    - 原因②：In particular, such an infinite accumulation completely eliminates the subtle correlations between neurons that get amplified over the course of training for representation learning.

# Reference
---


# Attachment
---
![[The Principles of Deep Learning Theory(2022).pdf]]