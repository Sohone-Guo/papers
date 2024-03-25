#Tag_计算机视觉 #Tag_自然语言处理 #Tag_多模态 
# Information
---
- Chenfei Wu
- Miscrosoft

# Mainly Idea
---
- 使用ChatGPT（InstructGPT）Incorporate a variety of Visual Foundataion Models.
- 主要工作是Prompt Manager
	- Tell ChatGPT the capability of each VFM and specifies the input-output formas.
	- Converts different visual information, for instance, png images, the depth images and mask matrix, to language format to help ChatGPT understand.
	- Handles the histories priorities, and conflicts of different Visual Foundation Models

不要需要重训连ChatGPT, 只需要将工具和工具用法设计到Prefix中，就可以。

# Reference
---
- Chain-of-Thought (CoT) 
	- Few-Shot CoT: 给一些样例
	- Zero-Shot CoT: 不需要给样例
- 有没有训练ChatGPT?
	- 直接使用ChatGPT,没有使用Finetune等
- 如何使用其他VFM的模型？
	- 预先定义了一个很长的Prefix, 里面包含了工具和工具用法，需要ChatGPT根据输入，结合Prefix进行选择工具的输出
[Announcing OpenChatKit (together.ai)](https://www.together.ai/blog/openchatkit)

# Attachment
---
![[Visual ChatGPT, Talking, Drawing and Editing with Visual Foundation Models.pdf]]