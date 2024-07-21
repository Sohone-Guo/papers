Tags: #Tag_自然语言处理 
# Information
---


# Mainly Idea
---
正常乘积是matmul, float x float 会有很多计算量，
如果不是float x float 而是binary x binary, 但是计算量没有变化
binary我们知道结果，{-1, 0, 1}所以我们可以将乘积改正选择的方式
# Question
---


# Reference
---
- [Scalable MatMul-free Language Modeling (Paper Explained) (youtube.com)](https://www.youtube.com/watch?v=B45FlSQ8ITo&t=10s)
- **Binary (二进制)**: 这是一种只使用两个数字的数值系统，通常是 0 和 1。在计算机科学中，二进制系统是最基础的，因为计算机的内部运算和数据存储都基于这种系统。
    
    例如，二进制数 `1010` 转换为十进制是 `10`。
    
- **Ternary (三进制)**: 这是一个使用三个数字的数值系统，通常是 0、1 和 2。三进制系统在某些数学和计算领域中也有应用，但它不像二进制那样普遍用于计算机内部处理。

# Attachment
---
![[Scalable MatMul-free Language Modeling.pdf]]