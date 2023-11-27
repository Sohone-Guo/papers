Tags: #Tag_AnomalyDetection
# Information
---


# Mainly Idea
---
![[Pasted image 20231127224804.png]]

# Question
---
- What means imputation-based? The perspective of time series imputation?
	- 一个时间序列数据，随机选取一些点，将剩余点Mask掉，并使用模型进行预测，预测结果和真实数据计算loss，差距如果太大就是异常数据。
- Density ratio-based strategy?
- Anomaly concentration?
	- anomalous points are not uniformly distributed over the whole time series but concerntrating at some regions.

# Reference
---


# Attachment
---
- [ChunjingXiao/DiffAD: Imputation-based Time-Series Anomaly Detection with Conditional Weight-Incremental Diffusion Models (github.com)](https://github.com/ChunjingXiao/DiffAD)
- ![[3580305.3599391.pdf]]