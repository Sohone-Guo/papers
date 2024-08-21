Tags: #Tag_语义通信 
# Information
---


# Mainly Idea
---


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

# Reference
---


# Attachment
---
![[2007.03034v2.pdf]]