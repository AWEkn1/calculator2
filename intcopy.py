# 计算器
# 使用函数 print int input while if break else import time sleep...
# import print int input while if break else import time sleep...
# 有单位,图形公式和加减乘除的计算器
import time
print('有单位,图形公式和加减乘除的计算器')
print('注意1.输入数字的时候,一定要输入数字,否则报错别找我。')
while True:
    print('有容量,长度,重量,能量,面积,速度,时间,数据,计算器')  # go
    o = input('请输入第一个单位')
    if o == '容量':
        while True:
            a = int(input('请输入第一个数字'))
            N = input('请输入第一个容量单位')
            if N == '毫升':
                print('有毫升,立方厘米,升,立方米')
                while True:
                    d = input('请输入第二个容量单位')
                    if d == '毫升':
                        print(a)
                        break
                    if d == '立方厘米':
                        print(a)
                        break
                    if d == '升':
                        print(a*0.0001)
                        break
                    if d == '立方米':
                        print(a*0.000001)
                        break
                    else:
                        print('请重新输入！！！')
                        continue
                break
            if N == '立方厘米':
                print('有毫升,立方厘米,升,立方米')
                while True:
                    d = input('请输入第二个容量单位')
                    if d == '毫升':
                        print(a)
                        break
                    if d == '立方厘米':
                        print(a)
                        break
                    if d == '升':
                        print(a*0.0001)
                        break
                    if d == '立方米':
                        print(a*0.000001)
                        break
                    else:
                        print('请重新输入！！！')
                        continue
                break
            if N == '升':
                print('有毫升,立方厘米,升,立方米')
                while True:
                    d = input('请输入第二个容量单位')
                    if d == '毫升':
                        print(a*1000)
                        break
                    if d == '立方厘米':
                        print(a*1000)
                        break
                    if d == '升':
                        print(a)
                        break
                    if d == '立方米':
                        print(a/0.0001)
                        break
                    else:
                        print('请重新输入！！！')
                        continue
                break
            if N == '立方米':
                print('有毫升,立方厘米,升,立方米')
                while True:
                    d = input('请输入第二个容量单位')
                    if d == '毫升':
                        print(a*1000000)
                        break
                    if d == '立方厘米':
                        print(a*1000000)
                        break
                    if d == '升':
                        print(a*1000)
                        break
                    if d == '立方米':
                        print(a)
                        break
                    else:
                        print('请重新输入！！！')
                        continue
                break
        break
    if o == '长度':
        a = int(input('请输入第一个数字'))
        N = input('请输入第一个长度单位')
        if N == '纳米':
            print('有纳米,厘米,微米,毫米,米,公里,英寸,英尺,码,英里,海里')
            while True:
                d = input('请输入第二个容量单位')
                if d == '纳米':
                    print(a)
                    break
                if d == '微米':
                    print(a*0.0001)
                    break
                if d == '毫米':
                    print(a*0.0000001)
                    break
                if d == '厘米':
                    print(a*0.00000001)
                    break
                if d == '米':
                    print(a*0.000000001)
                    break
                if d == '公里':
                    print(a*0.000000000001)
                    break
                if d == '英寸':
                    print(a*0.000000039370079)
                    break
                if d == '英尺':
                    print(a*0.00000000328084)
                    break
                if d == '码':
                    print(a*0.000000001093613)
                    break
                if d == '英里':
                    print(a*0.000000001093613)
                    break
                if d == '海里':
                    print(a*0.000000001093613)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '厘米':
            print('有纳米,厘米,微米,毫米,米,公里,英寸,英尺,码,英里,海里')
            print('英寸,英尺,码,英里,海里,木有哦.')
            while True:
                d = input('请输入第二个容量单位')
                if d == '纳米':
                    print(a*10000000)
                    break
                if d == '微米':
                    print(a*10000)
                    break
                if d == '毫米':
                    print(a*10)
                    break
                if d == '厘米':
                    print(a)
                    break
                if d == '米':
                    print(a*0.000)
                    break
                if d == '公里':
                    print(a*0.0001)
                    break
                if d == '英寸':
                    print(a*0.393701)
                    break
                if d == '英尺':
                    print(a*0.032808)
                    break
                if d == '码':
                    print(a*0.010936)
                    break
                if d == '英里':
                    print(a*0.000006)
                    break
                if d == '海里':
                    print(a*0.000005)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '微米':
            print('有纳米,厘米,微米,毫米,米,公里,英寸,英尺,码,英里,海里')
            print('英寸,英尺,码,英里,海里,木有哦.')
            while True:
                d = input('请输入第二个容量单位')
                if d == '纳米':
                    print(a*1000)
                    break
                if d == '微米':
                    print(a*1)
                    break
                if d == '毫米':
                    print(a*0.001)
                    break
                if d == '厘米':
                    print(a*0.0001)
                    break
                if d == '米':
                    print(a*0.000001)
                    break
                if d == '公里':
                    print(a*0.000000001)
                    break
                if d == '英寸':
                    print(a*0.000039)
                    break
                if d == '英尺':
                    print(a*0.000003)
                    break
                if d == '码':
                    print(a*0.000001)
                    break
                if d == '英里':
                    print(a*0.000000000621371)
                    break
                if d == '海里':
                    print(a*0.000000000539957)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '毫米':
            print('有纳米,厘米,微米,毫米,米,公里,英寸,英尺,码,英里,海里')
            print('英寸,英尺,码,英里,海里,木有哦.')
            while True:
                d = input('请输入第二个容量单位')
                if d == '纳米':
                    print(a*1000000)
                    break
                if d == '微米':
                    print(a*1000)
                    break
                if d == '毫米':
                    print(a*1)
                    break
                if d == '厘米':
                    print(a*0.01)
                    break
                if d == '米':
                    print(a*0.001)
                    break
                if d == '公里':
                    print(a*0.000001)
                    break
                if d == '英寸':
                    print(a*0.03937)
                    break
                if d == '英尺':
                    print(a*0.003281)
                    break
                if d == '码':
                    print(a*0.001094)
                    break
                if d == '英里':
                    print(a*0.000000621371192)
                    break
                if d == '海里':
                    print(a*0.000000539956803)
                    break
                else:
                    print('请重新输入！！！')
                    continue
        if N == '米':
            print('有纳米,厘米,微米,毫米,米,公里,英寸,英尺,码,英里,海里')
            print('英寸,英尺,码,英里,海里,木有哦.')
            while True:
                d = input('请输入第二个容量单位')
                if d == '纳米':
                    print(a*1000000000)
                    break
                if d == '微米':
                    print(a*1000000)
                    break
                if d == '毫米':
                    print(a*1000)
                    break
                if d == '厘米':
                    print(a*100)
                    break
                if d == '米':
                    print(a*1)
                    break
                if d == '公里':
                    print(a*0.0001)
                    break
                if d == '英寸':
                    print(a*39.37008)
                    break
                if d == '英尺':
                    print(a*3.28084)
                    break
                if d == '码':
                    print(a*1.093613)
                    break
                if d == '英里':
                    print(a*0.000621)
                    break
                if d == '海里':
                    print(a*0.00054)
                    break
                else:
                    print('请重新输入！！！')
                    continue
        if N == '公里':
            print('有纳米,厘米,微米,毫米,米,公里,英寸,英尺,码,英里,海里')
            print('英寸,英尺,码,英里,海里,木有哦.')
            while True:
                d = input('请输入第二个容量单位')
                if d == '纳米':
                    print(a*1000000000000)
                    break
                if d == '微米':
                    print(a*1000000000)
                    break
                if d == '毫米':
                    print(a*1000000)
                    break
                if d == '厘米':
                    print(a*100000)
                    break
                if d == '米':
                    print(a*1000)
                    break
                if d == '公里':
                    print(a/1)
                    break
                if d == '英寸':
                    print(a*39370.08)
                    break
                if d == '英尺':
                    print(a*3280.84)
                    break
                if d == '码':
                    print(a*1093.613)
                    break
                if d == '英里':
                    print(a*0.621371)
                    break
                if d == '海里':
                    print(a*0.539957)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '英寸':
            print('有纳米,厘米,微米,毫米,米,公里,英寸,英尺,码,英里,海里')
            print('英寸,英尺,码,英里,海里,木有哦.')
            while True:
                d = input('请输入第二个容量单位')
                if d == '纳米':
                    print(a*25400000)
                    break
                if d == '微米':
                    print(a*25400)
                    break
                if d == '毫米':
                    print(a*25.4)
                    break
                if d == '厘米':
                    print(a*2.54)
                    break
                if d == '米':
                    print(a*0.0254)
                    break
                if d == '公里':
                    print(a*0.000025)
                    break
                if d == '英寸':
                    print(a)
                    break
                if d == '英尺':
                    print(a*0.083333)
                    break
                if d == '码':
                    print(a*0.027778)
                    break
                if d == '英里':
                    print(a*0.000016)
                    break
                if d == '海里':
                    print(a*0.000014)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '英尺':
            print('有纳米,厘米,微米,毫米,米,公里,英寸,英尺,码,英里,海里')
            print('英寸,英尺,码,英里,海里,木有哦.')
            while True:
                d = input('请输入第二个容量单位')
                if d == '纳米':
                    print(a*304800000)
                    break
                if d == '微米':
                    print(a*304800)
                    break
                if d == '毫米':
                    print(a*304.8)
                    break
                if d == '厘米':
                    print(a*30.48)
                    break
                if d == '米':
                    print(a*0.3048)
                    break
                if d == '公里':
                    print(a*0.000305)
                    break
                if d == '英寸':
                    print(a*12)
                    break
                if d == '英尺':
                    print(a)
                    break
                if d == '码':
                    print(a*0.333333)
                    break
                if d == '英里':
                    print(a*0.000189)
                    break
                if d == '海里':
                    print(a*0.000165)
                    break
                else:
                    print('请重新输入！！！')
                    continue
        if N == '码':
            print('有纳米,厘米,微米,毫米,米,公里,英寸,英尺,码,英里,海里')
            print('英寸,英尺,码,英里,海里,木有哦.')
            while True:
                d = input('请输入第二个容量单位')
                if d == '纳米':
                    print(a*914400000)
                    break
                if d == '微米':
                    print(a*914400)
                    break
                if d == '毫米':
                    print(a*914.4)
                    break
                if d == '厘米':
                    print(a*91.44)
                    break
                if d == '米':
                    print(a*0.9144)
                    break
                if d == '公里':
                    print(a*0.000914)
                    break
                if d == '英寸':
                    print(a*36)
                    break
                if d == '英尺':
                    print(a*3)
                    break
                if d == '码':
                    print(a)
                    break
                if d == '英里':
                    print(a*0.000568)
                    break
                if d == '海里':
                    print(a*0.000494)
                    break
                else:
                    print('请重新输入！！！')
                    continue
        if N == '英里':
            print('有纳米,厘米,微米,毫米,米,公里,英寸,英尺,码,英里,海里')
            print('英寸,英尺,码,英里,海里,木有哦.')
            while True:
                d = input('请输入第二个容量单位')
                if d == '纳米':
                    print(a*1609344000000)
                    break
                if d == '微米':
                    print(a*1609344000)
                    break
                if d == '毫米':
                    print(a*1609344)
                    break
                if d == '厘米':
                    print(a*160934.4)
                    break
                if d == '米':
                    print(a*1609.344)
                    break
                if d == '公里':
                    print(a*1.609344)
                    break
                if d == '英寸':
                    print(a*63360)
                    break
                if d == '英尺':
                    print(a*5280)
                    break
                if d == '码':
                    print(a*1760)
                    break
                if d == '英里':
                    print(a)
                    break
                if d == '海里':
                    print(a*0.868976)
                    break
                else:
                    print('请重新输入！！！')
                    continue
        if N == '英里':
            print('有纳米,厘米,微米,毫米,米,公里,英寸,英尺,码,英里,海里')
            print('英寸,英尺,码,英里,海里,木有哦.')
            while True:
                d = input('请输入第二个容量单位')
                if d == '纳米':
                    print(a*1852000000000)
                    break
                if d == '微米':
                    print(a*1852000000)
                    break
                if d == '毫米':
                    print(a*1852000)
                    break
                if d == '厘米':
                    print(a*185200)
                    break
                if d == '米':
                    print(a*1852)
                    break
                if d == '公里':
                    print(a*1.852)
                    break
                if d == '英寸':
                    print(a*72913.39)
                    break
                if d == '英尺':
                    print(a*6076.115)
                    break
                if d == '码':
                    print(a*2025.372)
                    break
                if d == '英里':
                    print(a*1.150779)
                    break
                if d == '海里':
                    print(a)
                    break
                else:
                    print('请重新输入！！！')
                    continue
    if o == '重量':
        a = int(input('请输入第一个数字'))
        N = input('请输入第一个长度单位')
        if N == '毫克':
            print('有毫克,克,公吨')
            while True:
                d = input('请输入第二个容量单位')
                if d == '毫克':
                    print(a)
                    break
                if d == '克':
                    print(a*0.001)
                    break
                if d == '公吨':
                    print(a*0.000000001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '克':
            print('有毫克,克,公吨')
            while True:
                d = input('请输入第二个容量单位')
                if d == '毫克':
                    print(a*1000)
                    break
                if d == '克':
                    print(a/1)
                    break
                if d == '公吨':
                    print(a*0.000001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '公吨':
            print('有毫克,克,公吨')
            while True:
                d = input('请输入第二个容量单位')
                if d == '毫克':
                    print(a*1000000000)
                    break
                if d == '克':
                    print(a*1000000)
                    break
                if d == '公吨':
                    print(a/1)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
    if o == '能量':
        a = int(input('请输入第一个数字'))
        print('有焦耳,千焦耳')
        N = input('请输入第一个长度单位')
        if N == '焦耳':
            while True:
                d = input('请输入第二个容量单位')
                if d == '焦耳':
                    print(a)
                    break
                if d == '千焦耳':
                    print(a*0.0001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '千焦耳':
            while True:
                d = input('请输入第二个容量单位')
                if d == '焦耳':
                    print(a*1000)
                    break
                if d == '千焦耳':
                    print(a/1)
                    break
                else:
                    print('请重新输入！！！')
                    continue
    if o == '面积':
        a = int(input('请输入第一个数字'))
        print('有平方毫米,平方厘米,平方米,公顷,平方公里')
        N = input('请输入第一个长度单位')
        if N == '平方毫米':
            while True:
                d = input('请输入第二个容量单位')
                if d == '平方毫米':
                    print(a)
                    break
                if d == '平方厘米':
                    print(a*0.0001)
                    break
                if d == '平方米':
                    print(a*0.0000001)
                    break
                if d == '公顷':
                    print(a*0.00000000001)
                    break
                if d == '平方公里':
                    print(a*0.0000000000001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '平方厘米':
            while True:
                d = input('请输入第二个容量单位')
                if d == '平方毫米':
                    print(a*100)
                    break
                if d == '平方厘米':
                    print(a/1)
                    break
                if d == '平方米':
                    print(a*0.0001)
                    break
                if d == '公顷':
                    print(a*0.000000001)
                    break
                if d == '平方公里':
                    print(a*0.00000000001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '平方米':
            while True:
                d = input('请输入第二个容量单位')
                if d == '平方毫米':
                    print(a*1000000)
                    break
                if d == '平方厘米':
                    print(a*10000)
                    break
                if d == '平方米':
                    print(a/1)
                    break
                if d == '公顷':
                    print(a*0.00001)
                    break
                if d == '平方公里':
                    print(a*0.0000001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '公顷':
            while True:
                d = input('请输入第二个容量单位')
                if d == '平方毫米':
                    print(a*10000000000)
                    break
                if d == '平方厘米':
                    print(a*100000000)
                    break
                if d == '平方米':
                    print(a*10000)
                    break
                if d == '公顷':
                    print(a/1)
                    break
                if d == '平方公里':
                    print(a*0.001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '平方公里':
            while True:
                d = input('请输入第二个容量单位')
                if d == '平方毫米':
                    print(a*1000000000000)
                    break
                if d == '平方厘米':
                    print(a*10000000000)
                    break
                if d == '平方米':
                    print(a*100000)
                    break
                if d == '公顷':
                    print(a*100)
                    break
                if d == '平方公里':
                    print(a/1)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
    if o == '速度':
        a = int(input('请输入第一个数字'))
        print('有厘米/秒,米/秒,千米/小时')
        print('千米/小时木有')
        N = input('请输入第一个长度单位')
        if N == '厘米/秒':
            while True:
                d = input('请输入第二个容量单位')
                if d == '厘米/秒':
                    print(a)
                    break
                if d == '米/秒':
                    print(a*0.001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '米/秒':
            while True:
                d = input('请输入第二个容量单位')
                if d == '厘米/秒':
                    print(a*100)
                    break
                if d == '米/秒':
                    print(a/1)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if o == '速度':
            a = int(input('请输入第一个数字'))
            print('有瓦特,千瓦')
            N = input('请输入第一个长度单位')
            if N == '千瓦':
                while True:
                    d = input('请输入第二个容量单位')
                    if d == '瓦特':
                        print(a*1000)
                        break
                    if d == '千瓦':
                        print(a)
                        break
                    else:
                        print('请重新输入！！！')
                        continue
                break
            if N == '瓦特':
                while True:
                    d = input('请输入第二个容量单位')
                    if d == '瓦特':
                        print(a)
                        break
                    if d == '千瓦':
                        print(a*0.001)
                        break
                    else:
                        print('请重新输入！！！')
                        continue
                break
    if o == '时间':
        a = int(input('请输入第一个数字'))
        print('有微妙,毫秒,秒,分钟,小时,天,年,周')
        N = input('请输入第一个长度单位')
        if N == '微妙':
            while True:
                d = input('请输入第二个容量单位')
                if d == '微妙':
                    print(a)
                    break
                if d == '毫秒':
                    print(a*0.001)
                    break
                if d == '妙':
                    print(a*0.00001)
                    break
                if d == '分钟':
                    print(a*0.000000016666667)
                    break
                if d == '小时':
                    print(a*0.000000000277778)
                    break
                if d == '天':
                    print(a*0.000000000011574)
                    break
                if d == '周':
                    print(a*0.000000000001653)
                    break
                if d == '年':
                    print(a*0.000000000000032)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '微妙':
            while True:
                d = input('请输入第二个容量单位')
                if d == '微妙':
                    print(a*100)
                    break
                if d == '毫秒':
                    print(a)
                    break
                if d == '妙':
                    print(a*0.001)
                    break
                if d == '分钟':
                    print(a*0.000017)
                    break
                if d == '小时':
                    print(a*0.000000277778)
                    break
                if d == '天':
                    print(a*0.000000011574074)
                    break
                if d == '周':
                    print(a*0.000000001653439)
                    break
                if d == '年':
                    print(a*0.0000000000031688)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '妙':
            while True:
                d = input('请输入第二个容量单位')
                if d == '微妙':
                    print(a*100000)
                    break
                if d == '毫秒':
                    print(a*1000)
                    break
                if d == '妙':
                    print(a)
                    break
                if d == '分钟':
                    print(a*0.016667)
                    break
                if d == '小时':
                    print(a*0.000278)
                    break
                if d == '天':
                    print(a*0.000012)
                    break
                if d == '周':
                    print(a*0.000002)
                    break
                if d == '年':
                    print(a*0.000000031688088)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '分钟':
            while True:
                d = input('请输入第二个容量单位')
                if d == '微妙':
                    print(a*60000000)
                    break
                if d == '毫秒':
                    print(a*60000)
                    break
                if d == '妙':
                    print(a*60)
                    break
                if d == '分钟':
                    print(a)
                    break
                if d == '小时':
                    print(a*0.016667)
                    break
                if d == '天':
                    print(a*0.000694)
                    break
                if d == '周':
                    print(a*0.000099)
                    break
                if d == '年':
                    print(a*0.000002)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '小时':
            while True:
                d = input('请输入第二个容量单位')
                if d == '微妙':
                    print(a*3600000000)
                    break
                if d == '毫秒':
                    print(a*3600000)
                    break
                if d == '妙':
                    print(a*3600)
                    break
                if d == '分钟':
                    print(a*60)
                    break
                if d == '小时':
                    print(a)
                    break
                if d == '天':
                    print(a*0.041667)
                    break
                if d == '周':
                    print(a*0.005952)
                    break
                if d == '年':
                    print(a*0.000114)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '天':
            while True:
                d = input('请输入第二个容量单位')
                if d == '微妙':
                    print(a*86400000000)
                    break
                if d == '毫秒':
                    print(a*86400000)
                    break
                if d == '妙':
                    print(a*86400)
                    break
                if d == '分钟':
                    print(a*1440)
                    break
                if d == '小时':
                    print(a*24)
                    break
                if d == '天':
                    print(a)
                    break
                if d == '周':
                    print(a*0.142857)
                    break
                if d == '年':
                    print(a*0.002738)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '年':
            while True:
                d = input('请输入第二个容量单位')
                if d == '微妙':
                    print(a*31557600000000)
                    break
                if d == '毫秒':
                    print(a*31557600000)
                    break
                if d == '妙':
                    print(a*31557600)
                    break
                if d == '分钟':
                    print(a*525960)
                    break
                if d == '小时':
                    print(a*8766)
                    break
                if d == '天':
                    print(a*365.25)
                    break
                if d == '周':
                    print(a*52.17857)
                    break
                if d == '年':
                    print(a)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == '周':
            while True:
                d = input('请输入第二个容量单位')
                if d == '微妙':
                    print(a*604800000000)
                    break
                if d == '毫秒':
                    print(a*604800000)
                    break
                if d == '妙':
                    print(a*604800)
                    break
                if d == '分钟':
                    print(a*10080)
                    break
                if d == '小时':
                    print(a*168)
                    break
                if d == '天':
                    print(a*7)
                    break
                if d == '周':
                    print(a)
                    break
                if d == '年':
                    print(a*0.019165)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
    if o == '数据':
        a = int(input('请输入第一个数字'))
        print('有位,B,KB,MB,GB,TB')
        N = input('请输入第一个长度单位')
        if N == '位':
            while True:
                d = input('请输入第二个容量单位')
                if d == '位':
                    print(a)
                    break
                if d == 'B':
                    print(a*0.125)
                    break
                if d == 'KB':
                    print(a*0.000125)
                    break
                if d == 'MB':
                    print(a*0.000000125)
                    break
                if d == 'GB':
                    print(a*0.0000000000125)
                    break
                if d == 'TB':
                    print(a*0.00000000000125)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == 'B':
            while True:
                d = input('请输入第二个容量单位')
                if d == '位':
                    print(a*8)
                    break
                if d == 'B':
                    print(a)
                    break
                if d == 'KB':
                    print(a*0.001)
                    break
                if d == 'MB':
                    print(a*0.000001)
                    break
                if d == 'GB':
                    print(a*0.000000001)
                    break
                if d == 'TB':
                    print(a*0.000000000001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == 'KB':
            while True:
                d = input('请输入第二个容量单位')
                if d == '位':
                    print(a*8000)
                    break
                if d == 'B':
                    print(a*1000)
                    break
                if d == 'KB':
                    print(a)
                    break
                if d == 'MB':
                    print(a*0.001)
                    break
                if d == 'GB':
                    print(a*0.000001)
                    break
                if d == 'TB':
                    print(a*0.000000001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == 'MB':
            while True:
                d = input('请输入第二个容量单位')
                if d == '位':
                    print(a*8000000)
                    break
                if d == 'B':
                    print(a*100000)
                    break
                if d == 'KB':
                    print(a*1000)
                    break
                if d == 'MB':
                    print(a)
                    break
                if d == 'GB':
                    print(a*0.001)
                    break
                if d == 'TB':
                    print(a*0.000001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == 'GB':
            while True:
                d = input('请输入第二个容量单位')
                if d == '位':
                    print(a*8000000000)
                    break
                if d == 'B':
                    print(a*1000000000)
                    break
                if d == 'KB':
                    print(a*1000000)
                    break
                if d == 'MB':
                    print(a*1000)
                    break
                if d == 'GB':
                    print(a)
                    break
                if d == 'TB':
                    print(a*0.001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
        if N == 'TB':
            while True:
                d = input('请输入第二个容量单位')
                if d == '位':
                    print(a*8000000000000)
                    break
                if d == 'B':
                    print(a*1000000000000)
                    break
                if d == 'KB':
                    print(a*1000000000)
                    break
                if d == 'MB':
                    print(a*1000000)
                    break
                if d == 'GB':
                    print(a*1000)
                    break
                if d == 'TB':
                    print(a*0.001)
                    break
                else:
                    print('请重新输入！！！')
                    continue
            break
    if o=='计算器':
        time.sleep(1)
        print('计算器 有图形公式和加减乘除的计算器。')
        print('如果有什么问题或建议，请联系我(在彩蛋里哦)。')
        print('按下Enter,go')
        while True:
            w = 3.14
            print('注意1.公式或符号不想用直接按Enter,  (你别两个都不想用)')
            print('2.平行四边形=长方形，所以没有平行四边形', '正方形2=长方形2,所以没有正方形2')
            b = int(input('请输入第一个数字(梯形用上底，圆用半径，三角形用底，长方形/体用长):'))
            print('1=周长 4=长度 2=面积 3=体积')
            print('3.1 表示体积2')
            print('有正方形，长方形，圆，梯形，三角形，长方体，正方体，环形')
            print('例:正方形1=算正方形的周长。')
            a = input("请输入一个公式")
            print('/是除号，*是乘号，-是减号，+是加号，%是整除，**是乘方。')
            q = input("请输入一个符号有(/ * - + % **):")
            c = int(input('请输入第二个数字(梯形用下底，三角形用高，长方形/体用宽，圆用直径):'))
            e = int(input('请输入第三个数字(梯形和长方体是高，其他不用):'))
            k = int(input('请输入第四个数字(梯形是腰，用于梯形周长，其他不用):'))
            print('开始计算')
            time.sleep(2)
            print('计算结果在下一行')
            if a == "正方形1":
                print(4*b)
                break
            if a == "长方形2":
                print(b*c)
                break
            if a == "长方形1":
                d = b+c
                while True:
                    print(d*2)
                    break
                break
            if a == "梯形2":
                d = int(b)+c
                while True:
                    print(d*int(e)/2)
                    break
                break
            if a == "梯形1":
                print(b+c+e+k)
                break
            if a == "圆1":
                print(w*c)
                break
            if a == "圆2":
                print(w*b)
                break
            if a == "三角形1":
                print(b+b+b)
                break
            if a == "三角形2":
               print(b*c/2)
            if a == "长方体1":
                jh = b+int(e)+c
                while True:
                        print(jh*4)
                        break
                break
            if a == "长方体2":
                    lk = b*c+c*e+c*a
                    while True:
                        print(lk*2)
                        break
                    break
            if a == "长方体4":
                    print(b*q)
                    break
            if a == "长方体3":
                lk = b*c+c*e+c*a
                while True:
                    mb = lk*2
                    while True:
                       print(mb*k)
                       break

            if a == "长方体3.1":
                print(b*c*k)
            if a == "正方体1":
                print(b*12)
                break
            if a == "正方体2":
                print(b*b*6)
                break
            if a == "正方体4":
                print(b*b)
                break
            if a == "环形2":
                erw = w*b
                iuy = w*c
                while True:
                    print(erw-iuy)
                    break
                break
            if a == "正方体3":
                cz = b*b*6
                while True:
                    print(cz*e)
                    break
                break
            if a == "正方体3.1":
                print(b*b*b)
            if q == "+":
                print(b+c)
                break
            if q == "-":
                print(b-c)
                break
            if q == "*":
                print(b*c)
                break
            if q == "/":
                print(b/c)
                break
            if q == "%":
                print(b % c)
                break
            if q == "**":
                print(b**c)
                break
            else:
                print('请重新输入！(注意事项看那没！！！)')
                time.sleep(1)
                print('注意1.小数和分数不可计算， 数字， 公式或符号不想用直接按Enter,  (你别都不想用)')
                print('2.平行四边形=长方形，所以没有平行四边形')
                time.sleep(10)
                continue
        time.sleep(119)
        print('两分钟之后关闭窗口')
        print('作者AWEkn1')
        time.sleep(1)
    if o == "AWEkn1":
        print('这是一个彩蛋')
        time.sleep(1)
        print('bilibili:AWEgh1 UID;517169863 ')
        print('Xbox:AWEkn1')
        print('giee:AWEkn1')
        print('github:AWEkn1')
        print('邮箱:a13579003@outlook.com/3502384248@qq.com')
        print('qq:3502384248')
        print('alingmuich.com')
    else:
        print('请重新输入！！！')
        continue    
time.sleep(120)
print('作者AWEkn1')
# 介绍:
# 有单位,图形公式和加减乘除的计算器。
# AWEkn1
# stop
