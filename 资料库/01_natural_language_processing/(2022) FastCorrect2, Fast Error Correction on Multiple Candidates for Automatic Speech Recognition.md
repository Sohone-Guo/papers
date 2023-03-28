# Information
---


# Mainly Idea
---
![[Pasted image 20230328134959.png]]

- Decoder: 接收到一个调整好的文本进行纠错。
- Encoder:
	- Transformer Encoder: 将候选cancat在一起，输出一个汇总的hidden
	- Duration Predictor: 预测每个一个候选的Duration    
		-  输入：结合transformer encoder汇总的hidden, 和每个候选单独的feature, 作为输入
	- Candidate Predictor: 预测每个候选可能的loss
		-  输入：结合transformer encoder汇总的hidden, 和每个候选单独的feature, 预测loss, 真正的loss是通过decoder端后计算的Loss作为target
-   预测过程：
	-   多个候选, 分别预测duration,和相应可能的loss值，选择loss最低的结果进行decoder。
-   好处：就是duration预测更准参考了其他候选，
# Reference
---
-   Voting effect?
	-   多个候选结果，可以确定哪些词可能是正确的不需要修改
-   duration predictor
	-   类似与长度预测模块
-   Adjust source?
	-   encoder会预测duration, 通过duration的结果，对数据进行删除，添加等操作
# Attachment
---
![[fastcorrect2.pdf]]