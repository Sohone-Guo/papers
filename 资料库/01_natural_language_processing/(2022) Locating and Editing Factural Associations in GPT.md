# Information
---


# Mainly Idea
---
-   发现一个问题：譬如The Space Needle 的特征已经包含了它的localtion信息，而不是The Space Needle is in downtowns ___ 之后才有此信息，
-   这个信息保存在MLP层。
![[Pasted image 20230328134451.png]]
-   如果有新的信息，可以将新的信息插入MLP层中，从而影响输出结果。
-   插入的方法就是：
![[Pasted image 20230328134508.png]]
插入的K,通过网络直接获取，然后选择最大MLP的位置，再此位置上修改W值，
W值由K，和理想V构成，可以通过梯度计算获得想要的V的数值，从而更新W值。
此更新的W值就包含了新的信息。

# Reference
---
- [ROME: Locating and Editing Factual Associations in GPT (Paper Explained & Author Interview) - YouTube](https://www.youtube.com/watch?v=_NMQyOu2HTo)

# Attachment
---
![[2202.05262.pdf]]