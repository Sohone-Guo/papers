定义（mAP是AP的平均值，但是AP不是。）：
Average Precision（AP） is NOT the average of precision across the different classes.
The average precision is the mean of the precision scores after each relevant document is retrieved.

AP来源于检索任务，简单理解如下：
检索一个Q，系统反馈很多结果，根据翻找多个页的结果如下。
第一页：前20个结果中的总共正确率：90%
第二页：前40个结果中的总共正确率：70%
第三页：前60个结果中的总共正确率：50%
第四页：前80个结果中的总共正确率：20%
则本系统的Average Precision（AP）为（90%+70%+50%+20%）/4=57.5%
页数越多可以理解Recall越大（所以近似可以理解为Average precision is the area under the Precision-Recall Curve（PR） curve.）。
评价其他系统页只看前80个结果的AP。

当计算目标检测的AP的时候（变相使用），可以理解为，按照预测的正确率从高往低排序，
前1个计算precision和recall
前2个计算precision和recall
前3个计算precision和recall
...
前N个计算precision和recall

上面的Precision平均值就是AP。
所有类别的AP平均就是mAP

当计算多标签分类的时候，也如上。

参考：
1、Average Precision | SpringerLink
2、2206.09504.pdf (arxiv.org)
3、Mean Average Precision (mAP) in Object Detection (learnopencv.com)