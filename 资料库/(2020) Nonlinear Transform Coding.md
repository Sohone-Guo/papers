Tags: #Tag_语义通信 
# Information
---


# Mainly Idea
---
注意：$-logP(k)$ 
- $P(k)$代表的是k出现的频率
- $-logP(k)$将概率转成最佳bits的长度，看霍夫曼编码（Huffman Coding）的计算过程。
NTC的公式：![[Pasted image 20240821160208.png]]
其中：
- $g_a(x)$: analysis transform
- $g_s(y)$: synthesis transform
- ![[Pasted image 20240821160506.png]]



# Question
---
- Transform Coding?
	- Compressing data source.
- Vivek Goyal attributed the success of TC to a divideand-conquer paradigm: the practical benefit of TC is that it separates the task of decorrelating a source, from coding it.?
	- 源的解相关（Decorrelating the Source）：这一步骤的目标是消除数据之间的相关性，使数据变得更独立。通过这种方式，可以简化数据的结构，使得后续处理变得更加高效。例如，通常可以通过一些变换（如离散余弦变换）来实现解相关，使得数据在变换后呈现出更为独立的特征。
	- 编码（Coding）：在数据经过解相关处理之后，接下来就是对数据进行编码，以便高效地存储或传输。这一步骤会利用数据的统计特性来进行压缩，减少数据的冗余。譬如霍夫曼编码（Huffman Coding）。
- entropy model?
	- 熵编码：熵编码是一种根据各符号出现的概率进行编码的技术。常见的熵编码方法有霍夫曼编码（Huffman Coding）和算术编码（Arithmetic Coding）。这些方法基于符号的概率分布来设计编码方式，使得高概率的符号使用较短的编码，低概率的符号使用较长的编码，从而减少整体编码长度。
	- ![[Pasted image 20240821141130.png]]
	- 霍夫曼编码通过将频率高的符号分配较短的编码，频率低的符号分配较长的编码，从而在整体上减少了编码的总长度。这个过程充分利用了熵编码的思想：更频繁出现的符号使用更短的编码，减少了信息的冗余，达到了数据压缩的目的。
- rate-distortion 什么意思？
	- **Rate-Distortion (R-D)** 是图像压缩和信号处理中的一个重要概念，用于描述压缩效率和质量之间的权衡。具体来说，它涉及在特定的数据传输率下，图像或信号的失真程度。
- Stochastic Rate-Distortion Optimization?
	- **Stochastic Rate-Distortion Optimization (SRDO)** 是一种优化技术，用于在压缩或编码系统中平衡数据压缩的比特率（Rate）和重建误差（Distortion）之间的关系。这个技术广泛应用于信息理论、数据压缩、信号处理和机器学习领域，尤其是在图像、视频压缩以及深度学习的表示学习中。
	- ![[Pasted image 20240821152226.png]]
	- ![[Pasted image 20240821152321.png]]
	- ![[Pasted image 20240821152744.png]]

# Reference
---
- [[(1990) Entropy-constrained vector quantization]]

# Attachment
---
![[2007.03034v2.pdf]]