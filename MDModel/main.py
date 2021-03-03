
link1 = "<a name =\""
link2 = "</a>"
enter = "\n"
content = "[TOC]" + enter   # 最终要输出的内容
title = "#"
n2 = 10
n3 = 10
for i1 in range(0, 2):
    for j in range(0, 1):   # 每一个级数标题应该加的#个数
        content += title
    content += " "
    if i1 == 0:
        content += link1 + "top" + "\">" + "目录" + link2 + enter
        for i2 in range(0, n2):  # 二级标题
            for j in range(0, 2):  # 每一个级数标题应该加的#个数
                content += title
            content += " "
            content += "[" + str(i2 + 1) + "目录" + "](#" \
                         + str(i2 + 1) + ")" + enter
            for i3 in range(0, n3):  # 三级标题
                for j in range(0, 3):  # 每一个级数标题应该加的#个数
                    content += title
                content += " "
                content += "[" + str(i2 + 1) + "." + str(i3 + 1) \
                           + "目录" + "](#" + str(i2 + 1) + "." + str(i3 + 1) + ")" + enter
    elif i1 == 1:
        content += link1 + str(i1+1) + "\">" + "内容" + link2 + enter
        for i2 in range(0, n2):  # 二级标题
            content += "[🔝](#top)" + enter  # 用于返回目录
            for j in range(0, 2):  # 每一个级数标题应该加的#个数
                content += title
            content += " "
            content += link1 + str(i2 + 1) + "\">" + str(i2 + 1) + "内容" + link2 + enter
            for i3 in range(0, n3):  # 二级标题
                content += "[🔝](#top)" + enter  # 用于返回目录
                for j in range(0, 3):  # 每一个级数标题应该加的#个数
                    content += title
                content += " "
                content += link1 + str(i2 + 1) + "." + str(i3 + 1) + "\">" + str(
                    i2 + 1) + "." + str(i3 + 1) + "内容" + link2 + enter
print(content)
