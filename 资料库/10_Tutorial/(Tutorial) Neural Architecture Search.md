将候选都列在一层：
![[屏幕截图 2023-11-06 141958.png]]
譬如
Block1是只CNN（3x3）
Block2是CNN(5x5)

训练时候：这两个模块做Softmax后相加
预测时候：只取Softmax最大的模块。