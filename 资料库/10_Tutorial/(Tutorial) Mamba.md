
- [Do we need Attention? - Linear RNNs and State Space Models (SSMs) for NLP](https://www.youtube.com/watch?v=dKJEpOtVgXc)
- [Were RNNs All We Needed? (Paper Explained)](https://www.youtube.com/watch?v=jE9jAZC42NE)
- [MAMBA from Scratch: Neural Nets Better and Faster than Transformers](https://www.youtube.com/watch?v=N6Piou4oYx8&t=1473s)

Linear RNNs: 不使用relu等函数，使用CNN或者Associative Scan(S5)可以并行训练模型，参考([MAMBA from Scratch: Neural Nets Better and Faster than Transformers](https://www.youtube.com/watch?v=N6Piou4oYx8&t=1473s))以及Associative Scan([MAMBA from Scratch: Neural Nets Better and Faster than Transformers - YouTube](https://www.youtube.com/watch?v=N6Piou4oYx8&t=1473s))

实现了RNN的并行训练。

但是Linear RNNs 性能太差了。如何提升性能？（SSM）

多点网络层和d_model个数


# 参考
![[mamba-tiny-master.zip]]