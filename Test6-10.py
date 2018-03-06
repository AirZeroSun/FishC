#    FishC 作业及课后练习- By AirZero
while True:
    print('''本程序包括了以下练习:
    0. 请写一个程序打印出 0~100 所有的奇数。
    1. 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。
    2. 请问如何快速将三个变量的值互相交换？
    3. 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。
    4. 编写一个程序，求 100~999 之间的所有水仙花数。
       如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。
    5. 三色球问题
       有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配
    6. 自己动手试试看，并分析在这种情况下，向列表添加数据应当采用哪种方法比较好？
       假设给定以下列表：member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
       要求将列表修改为：member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
       方法一：使用 insert() 和 append() 方法修改列表。
       方法二：重新创建一个同名字的列表覆盖。
    q. 退出!''')
    temp = input('请做出你的选择：')
    if temp.upper() == 'Q':
        print('程序退出!')
        break
    if not temp.isdigit():
        print('输入错误!')
        continue
    work = int(temp)
    #第0题
    if work == 0:
        i = 1
        while i <= 100:
            if i % 2 ==1:
                print(i,end = ' ')
            i += 1
        input('\n按回车键继续')
    elif work == 1:
        i = 1
        while True:
            num = i * 7
            if (num % 6 ==5) and (num % 5 ==4) and (num % 3 ==2) and (num % 2 ==1):
                print('总共有'+str(num)+'步台阶!')
                input('按回车键继续')
                break
            i += 1
    elif work == 2:
        x,y,z = 1,2,3
        print('x,y,z =', x , y ,z)
        x,y,z = z,y,x
        print('after exchange x,y,z =', x, y, z)
        input('按回车键继续')
    elif work == 3:
        password = 'password'
        count = 3
        while count:
            press = input('请输入密码：')
            if '*' in press:
                print('内容有星号,无效.',end = '')
            elif press == password:
                print('密码正确!')
                break
            else:
                count -= 1
                print('密码输入错误,还有'+str(count)+'次机会,',end = '')
        print('游戏结束!')
        input('按回车键继续!')

    elif work == 4:
        count = 0
        for i in range(100, 1000):
            sum = 0
            temp = i
            while temp:
                sum += (temp % 10) ** 3
                temp = temp // 10
            if i == sum:
                print('找到一个水仙花：',i)
                count += 1
        if count == 0:
            print('范围内没有找到合适的!')
        input('按回车键继续')
    elif work == 5:
        print('red\tyellow\tgreen')
        for red in range(4):
            for yellow in range(4):
                for green in range(2,7):
                    if red + yellow + green == 8:
                        print(red, '\t', yellow, '\t', green)
    elif work == 6:
        member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
        score = [88, 90, 85, 90, 88]
        temp = input('请选择方法1或者2')
        method = int(temp)
        if method == 1:
            length = len(score)
            for i in range(length):
                member.insert(i*2+1, score[i])
            print(member)
        elif method == 2:
            newmember = []
            length = len(score)
            for i in range(length):
                newmember.append(member[i])
                newmember.append(score[i])
            print(newmember)
        else:
           print('选择错误')
        input('按回车键继续')
    else:
        print('无此选项!')
