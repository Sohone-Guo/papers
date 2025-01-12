Tags: #Tag_CPS平台
# Information
---


# Mainly Idea
---
[[(2019) Radio propagation prediction model using convolutional neural networks by deep learning]]
- 机构：NTT Docomo
- 输入：
	- BS distance map
	- MS distance map
	- •Building heights(fixed map)
- 网络：CNN + Linear
- 问题：
	- 泛用性差
[[(2019) Two-step path loss prediction by artificial neural network for wireless service area planning]]
- 输入：
	- 发射器 (Tx) 的位置（x,y）
	- 接收器(Rx)的位置（x,y）
- 网络：两步骤
	- 第一步骤：区域划分为服务区（S区）、干扰区（I区）和可忽略区（N区）
	- 第二步骤：每个区域训练单独模型
- 问题：
	- 泛用性差
	- 性能较差
[[(2021) RadioUNet, Fast Radio Map Estimation With Convolutional Neural Networks]]
- 数据量（发射器位置和建筑物轮廓可以用黑白图像作为输入特征进行描述。）
	- 56,000 个模拟无线电图，涉及不同的城市位置和不同的发射器位置。
	- 1400 个高精度模拟数据集。
- 输入：
	- 城市地图(即城市环境的几何结构)
	- 发射器位置
- 问题：
	- 解决泛用性问题

# Question
---


# Reference
---


# Attachment
---
![[19_重要_Overview_of_the_First_Pathloss_Radio_Map_Prediction_Challenge.pdf]]