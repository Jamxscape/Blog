# 把汉字变为阿拉伯数字
# 有错误，比如输出十万到二十万之间的数字时会发生错误，但是正确读法应该为十万，同理十亿也如此。
# 这是由于汉字读法决定的
def chinese2digits(chinese_str):
    t = chinese_str
    if t is None or t.strip() == "":
        raise Exception("input error for %s" % chinese_str)
    t = t.strip()
    t = t.replace("百十", "百一十")
    common_used_numerals = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
                            '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
    total = 0
    r = 1
    for i in range(len(t) - 1, -1, -1):
        val = common_used_numerals.get(t[i])
        if val is None:
            raise Exception("%s can not be accepted." % t[i])
        if val >= 10 and i == 0:
            if val > r:
                r = val
                total = total + val
            else:
                r = r * val
        elif val >= 10:
            if val > r:
                r = val
            else:
                r = r * val
        else:
            total = total + r * val
    return total


a = chinese2digits("一十万零一十")
print(a)