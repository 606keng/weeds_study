#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: xlwt_study.py
@time: 2021/03/31
@remark：
"""
import xlwt  # 导入模块


def careat_student():
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook 对象
    worksheet = workbook.add_sheet('sheet1')  # 创建工作表sheet
    worksheet.write(0, 0, 'hello')  # 往表中写内容,第一各参数 行,第二个参数列,第三个参数内容
    workbook.save('students.xls')  # 保存表为students.xls


def create_case():
    import xlwt  # 导入模块
    from xmindparser import xmind_to_dict

    xm = xmind_to_dict("团队学习-我的推课.xmind")[0]['topic']  # 读取xmind数据
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
    worksheet = workbook.add_sheet(xm["title"], cell_overwrite_ok=True)  # 创建工作表，并设置可以重写单元格内容
    row0 = ["testcaseid", '需求名称', '测试用例名称', '执行步骤', '预期结果', '服务名称', '版本', '执行人员']  # 写成excel表格用例的要素
    # 添加excel标题
    for i in range(len(row0)):
        worksheet.write(0, i, row0[i])

    x = 0  # 写入数据的当前行数
    z = 0  # 用例的编号
    # 遍历所有需求
    for i in range(len(xm["topics"])):
        test_module = xm["topics"][i]
        for j in range(len(test_module["topics"])):
            test_suit = test_module["topics"][j]
            for k in range(len(test_suit["topics"])):
                test_case = test_suit["topics"][k]
                z += 1
                c1 = len(test_case["topics"])  # 执行步骤有几个
                for n in range(len(test_case["topics"])):
                    x += 1
                    test_step = test_case["topics"][n]
                    test_except = test_step["topics"][0]
                    worksheet.write(x, 4, f"{n + 1}." + test_except["title"])  # 预期结果
                    worksheet.write(x, 3, f"{n + 1}." + test_step["title"])  # 执行步骤
                worksheet.write_merge(x - c1 + 1, x, 0, 0, z)  # testcaseid
                worksheet.write_merge(x - c1 + 1, x, 1, 1, test_module["title"])  # 测试需求名称
                worksheet.write_merge(x - c1 + 1, x, 2, 2, test_case["title"])  # 测试用例名称
    workbook.save(xm["title"] + ".xls")  # xls名称取xmind主题名称


import xlwt  # 导入模块
from xmindparser import xmind_to_dict
def styles():
    """设置单元格的样式的基础方法"""
    style = xlwt.XFStyle()
    return style


def borders(status=1):
    """设置单元格的边框
    细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13"""
    border = xlwt.Borders()
    border.left = status
    border.right = status
    border.top = status
    border.bottom = status
    return border


def heights(worksheet, line, size=4):
    """设置单元格的高度"""
    worksheet.row(line).height_mismatch = True
    worksheet.row(line).height = size*256


def widths(worksheet, line, size=11):
    """设置单元格的宽度"""
    worksheet.col(line).width = size*256


def alignments(**kwargs):
    """设置单元格的对齐方式
    status有两种：horz（水平），vert（垂直）
    horz中的direction常用的有：CENTER（居中）,DISTRIBUTED（两端）,GENERAL,CENTER_ACROSS_SEL（分散）,RIGHT（右边）,LEFT（左边）
    vert中的direction常用的有：CENTER（居中）,DISTRIBUTED（两端）,BOTTOM(下方),TOP（上方）"""
    alignment = xlwt.Alignment()

    if "horz" in kwargs.keys():
        alignment.horz = eval(f"xlwt.Alignment.HORZ_{kwargs['horz'].upper()}")
    if "vert" in kwargs.keys():
        alignment.vert = eval(f"xlwt.Alignment.VERT_{kwargs['vert'].upper()}")
    alignment.wrap = 1  # 设置自动换行
    return alignment


def fonts(name='宋体', bold=False, underline=False, italic=False, colour='black', height=11):
    """设置单元格中字体的样式
    默认字体为宋体，不加粗，没有下划线，不是斜体，黑色字体"""
    font = xlwt.Font()
    # 字体
    font.name = name
    # 加粗
    font.bold = bold
    # 下划线
    font.underline = underline
    # 斜体
    font.italic = italic
    # 颜色
    font.colour_index = xlwt.Style.colour_map[colour]
    # 大小
    font.height = 20 * height
    return font


def patterns(colors=1):
    """设置单元格的背景颜色，该数字表示的颜色在xlwt库的其他方法中也适用，默认颜色为白色
    0 = Black, 1 = White,2 = Red, 3 = Green, 4 = Blue,5 = Yellow, 6 = Magenta, 7 = Cyan,
    16 = Maroon, 17 = Dark Green,18 = Dark Blue, 19 = Dark Yellow ,almost brown), 20 = Dark Magenta,
    21 = Teal, 22 = Light Gray,23 = Dark Gray, the list goes on..."""
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = colors
    return pattern

def main():
    xm = xmind_to_dict("团队学习-我的推课.xmind")[0]['topic']
    # print(json.dumps(xm, indent=2, ensure_ascii=False))  # indent为显示json格式，ensure_ascii为显示为中文，不显示ASCII码
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
    worksheet = workbook.add_sheet(xm["title"], cell_overwrite_ok=True)  # 创建工作表
    row0 = ["testcaseid", '需求名称', '测试用例名称', '执行步骤', '预期结果', '服务名称', '版本', '执行人员']
    sizes = [10, 11, 30, 60, 50, 11, 11, 11]
    dicts = {"horz": "CENTER", "vert": "CENTER"}

    style2 = styles()
    style2.alignment = alignments(**dicts)
    style2.font = fonts()
    style2.borders = borders()
    style2.pattern = patterns(7)
    heights(worksheet, 0)
    for i in range(len(row0)):
        worksheet.write(0, i, row0[i], style2)
        widths(worksheet, i, size=sizes[i])

    style = styles()
    style.borders = borders()

    x = 0  # 写入数据的当前行数
    z = 0  # 用例的编号
    for i in range(len(xm["topics"])):
        test_module = xm["topics"][i]
        for j in range(len(test_module["topics"])):
            test_suit = test_module["topics"][j]
            for k in range(len(test_suit["topics"])):
                test_case = test_suit["topics"][k]
                z += 1
                c1 = len(test_case["topics"])  # 执行步骤有几个
                for n in range(len(test_case["topics"])):
                    x += 1
                    test_step = test_case["topics"][n]
                    test_except = test_step["topics"][0]
                    worksheet.write(x, 4, f"{n + 1}." + test_except["title"], style)  # 预期结果
                    worksheet.write(x, 3, f"{n + 1}." + test_step["title"], style)  # 执行步骤
                worksheet.write_merge(x - c1 + 1, x, 0, 0, z, style)  # testcaseid
                worksheet.write_merge(x - c1 + 1, x, 1, 1, test_module["title"], style)  # 测试需求名称
                worksheet.write_merge(x - c1 + 1, x, 2, 2, test_case["title"], style)  # 测试用例名称

    workbook.save(xm["title"] + ".xls")  # xls名称取xmind主题名称


if __name__ == "__main__":
    main()

