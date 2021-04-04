#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: read_xmind.py
@time: 2021/03/31
@remark：
"""

# -*- coding:utf-8 -*-

from xmindparser import xmind_to_dict
import xlwt


class XlwtSeting(object):

    @staticmethod  # 静态方法装饰器，使用此装饰器装饰后，可以直接使用类名.方法名调用（XlwtSeting.styles()），并且不需要self参数
    def template_one(worksheet):
        dicts = {"horz": "CENTER", "vert": "CENTER"}
        sizes = [15, 15, 30, 60, 45, 45, 15, 15]

        se = XlwtSeting()
        style = se.styles()
        style.alignment = se.alignments(**dicts)
        style.font = se.fonts(bold=True)
        style.borders = se.borders()
        style.pattern = se.patterns(7)
        se.heights(worksheet, 0)
        for i in range(len(sizes)):
            se.widths(worksheet, i, size=sizes[i])
        return style

    @staticmethod
    def template_two():
        dicts2 = {"vert": "CENTER"}
        se = XlwtSeting()
        style = se.styles()
        style.borders = se.borders()
        style.alignment = se.alignments(**dicts2)
        return style

    @staticmethod
    def styles():
        """设置单元格的样式的基础方法"""
        style = xlwt.XFStyle()
        return style

    @staticmethod
    def borders(status=1):
        """设置单元格的边框，
        细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13"""
        border = xlwt.Borders()
        border.left = status
        border.right = status
        border.top = status
        border.bottom = status
        return border

    @staticmethod
    def heights(worksheet, line, size=4):
        """设置单元格的高度"""
        worksheet.row(line).height_mismatch = True
        worksheet.row(line).height = size * 256

    @staticmethod
    def widths(worksheet, line, size=11):
        """设置单元格的宽度"""
        worksheet.col(line).width = size * 256

    @staticmethod
    def alignments(wrap=1, **kwargs):
        """设置单元格的对齐方式，
        ：接收一个对齐参数的字典{"horz": "CENTER", "vert": "CENTER"}horz（水平），vert（垂直）
        ：horz中的direction常用的有：CENTER（居中）,DISTRIBUTED（两端）,GENERAL,CENTER_ACROSS_SEL（分散）,RIGHT（右边）,LEFT（左边）
        ：vert中的direction常用的有：CENTER（居中）,DISTRIBUTED（两端）,BOTTOM(下方),TOP（上方）"""
        alignment = xlwt.Alignment()

        if "horz" in kwargs.keys():
            alignment.horz = eval(f"xlwt.Alignment.HORZ_{kwargs['horz'].upper()}")
        if "vert" in kwargs.keys():
            alignment.vert = eval(f"xlwt.Alignment.VERT_{kwargs['vert'].upper()}")
        alignment.wrap = wrap  # 设置自动换行
        return alignment

    @staticmethod
    def fonts(name='宋体', bold=False, underline=False, italic=False, colour='black', height=11):
        """设置单元格中字体的样式，
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

    @staticmethod
    def patterns(colors=1):
        """设置单元格的背景颜色，该数字表示的颜色在xlwt库的其他方法中也适用，默认颜色为白色
        0 = Black, 1 = White,2 = Red, 3 = Green, 4 = Blue,5 = Yellow, 6 = Magenta, 7 = Cyan,
        16 = Maroon, 17 = Dark Green,18 = Dark Blue, 19 = Dark Yellow ,almost brown), 20 = Dark Magenta,
        21 = Teal, 22 = Light Gray,23 = Dark Gray, the list goes on..."""
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = colors
        return pattern


class XmindToXsl(XlwtSeting):

    def __init__(self, name):
        """调用类时，读取xmind文件，并生成excel表格"""
        try:
            self.xm = xmind_to_dict(name)[0]['topic']
        except Exception as e:
            print(f"打开xmind文件失败:{e}")
        self.workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
        self.worksheet = self.workbook.add_sheet(self.xm["title"], cell_overwrite_ok=True)  # 创建工作表

    def save(self, name):
        """保存表格"""
        self.workbook.save(name + ".xls")

    @staticmethod
    def xmind_num(value):
        """获取xmind标题个数"""
        try:
            return len(value["topics"])
        except KeyError:
            return 0

    @staticmethod
    def xmind_title(value):
        """获取xmind标题内容"""
        return value["title"]

    def write_excel(self, result='', performer='', editionname=''):
        """生成excel文件的方法"""
        row0 = ["测试案例路径", '测试案例名称', '测试案例描述', '前置条件', '步骤描述', '预期结果', '优先级']
        style2 = self.template_one(self.worksheet)
        for i in range(len(row0)):
            self.worksheet.write(0, i, row0[i], style2)

        style = self.template_two()

        x = 0  # 写入数据的当前行数
        z = 0  # 用例的编号

        for i in range(self.xmind_num(self.xm)):
            test_module = self.xm["topics"][i]
            print(test_module['title'])
            modnum = self.xmind_num(test_module)
            if modnum != 0:
                for j in range(modnum):
                    test_suit = test_module["topics"][j]
                    suit_num = self.xmind_num(test_suit)
                    if suit_num != 0:
                        for k in range(suit_num):
                            test_case = test_suit["topics"][k]
                            z += 1
                            c1 = self.xmind_num(test_case)  # 执行步骤有几个
                            if c1 != 0:
                                for n in range(c1):
                                    x += 1
                                    test_step = test_case["topics"][n]
                                    test_except = test_step["topics"][0]
                                    self.heights(self.worksheet, x, size=2)
                                    step = f"{n + 1}." + self.xmind_title(test_step)  # 执行步骤
                                    exce = f"{n + 1}." + self.xmind_title(test_except)  # 预期结果
                                    self.worksheet.write(x, 3, step, style)  # 写入执行步骤
                                    self.worksheet.write(x, 4, exce, style)  # 写入预期结果
                                    self.worksheet.write(x, 5, result, style)  # 写入实际结果
                                    self.worksheet.write(x, 6, performer, style)  # 写入执行人
                                mod = self.xmind_title(test_module)  # 测试需求名称
                                case = self.xmind_title(test_case)  # 测试用例名称
                                self.worksheet.write_merge(x - c1 + 1, x, 0, 0, test_module['title'], style)  # 写入测试案例路径
                                self.worksheet.write_merge(x - c1 + 1, x, 1, 1, mod, style)  # 写入测试需求名称
                                self.worksheet.write_merge(x - c1 + 1, x, 2, 2, case, style)  # 写入测试用例名称
                                self.worksheet.write_merge(x - c1 + 1, x, 7, 7, editionname, style)  # 写入版本名称
                            else:
                                print("测试用例没有操作步骤及预期结果")
                    else:
                        print("没有测试用例")
            else:
                print("没有测试套件")

        self.save(self.xm["title"])  # 保存


if __name__ == "__main__":
    names = "团队学习-我的推课.xmind"
    xx = XmindToXsl(names)
    xx.write_excel()
