# 设置字体
```
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