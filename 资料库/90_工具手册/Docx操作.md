# 设置字体
```
from docx.shared 
import Pt from docx.oxml.ns 
import qn from docx.oxml 
import OxmlElement
# 设置默认字体方法

def set_font(doc):

	# 访问文档的默认样式

	style = doc.styles['Normal']

	# 设置字体

	font = style.font

	font.name = 'Times New Roman'

	# 需要设置字体的字符集，对于中文处理很重要

	font.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

# 应用默认字体设置

set_font(target_doc)
```

```python
import docx

def translate_docx(file_path, output_path):
    doc = docx.Document(file_path)

    for para in doc.paragraphs:
        # print(para._element.xml)
        # for node in para._element.iter():
        #     if node.text and "PUSCH" in node.text:
        #         node.text = node.text.replace("PUSCH", "aaa")
        #         print(node.text)
        #         print("--------------")
        for run in para.runs:
            # 检查run是否仅包含文本
            if "<m:oMath" not in run._element.xml and "<w:drawing" not in run._element.xml:  # OMML标记不在这个run中
                # if "PUSCH" in run.text:
                run.text = " aaa "#run.text.replace("PUSCH", "aaa")
        # para.text = para.text
        # if '<m:oMath' in para._element.xml:
        #     print(para._element.xml)

    doc.save(output_path)

# 使用示例
translate_docx('38213-gh0.docx', 'output_translated.docx')
```