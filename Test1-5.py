#    FishC 作业及课后练习- By AirZero
while True:
    print('''本程序包括了以下练习:
    0. 编写程序：hello.py，要求用户输入姓名并打印“你好，姓名！”
    1. 编写程序：calc.py 要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”
    2. 请问以下代码会打印多少次“我爱鱼C！”
    3. 完善第二个改进要求（为用户提供三次机会尝试，机会用完或者用户猜中答案均退出循环）并改进视频中小甲鱼的代码。
    4. 我们人类思维是习惯于“四舍五入”法，你有什么办法使得 int() 按照“四舍五入”的方式取整吗？
    5. 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的 BIF 进行灵活运用）
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
        name = input('请输入您的姓名：')
        print('你好,' + name + '!')
    elif work == 1:
        temp = input('请输入1-100之间的数字：')
        num =int(temp)
        if 1 <= num <= 100:
            print('你妹好漂亮')
        else:
            print('你大爷好丑')
    elif work == 2:
        i = 10
        while i:
            print('我爱鱼C!'+str(i))
            i = i - 1
    elif work == 3:
        import random
        secret = random.randint(1,10)
        i = 3
        while i:
            if i == 3:
                temp = input('请输入数字(1-10):')
            else:
                temp = input('请重新输入数字(1-10):')
            while not temp.isdigit():
                temp = input('输入错误,请重新输入数字(1-10):')
            guess = int(temp)
            if guess < secret:
                print('回答错误，答案小了！.', end = '')
            elif guess > secret:
                print('回答错误，答案大了！', end = '')
            elif guess == secret:
                # print('猜对了!')
                break
            i -= 1
        if i == 0:
            print('三次机会用完，正确答案是：'+str(secret))
        elif i > 0:
            print(str(4-i)+'次机会就猜对了，厉害啊!')
    elif work == 4:
        temp = input('请输入一个需要四舍五入的浮点数：')
        num = float(temp)
        # if num - int(num) >= 0.5:
        #     answer = int(num) + 1
        # elif (num - int(num)) <= -0.5:
        #     answer = int(num) -1
        # else:
        #     answer = int(num)
        # 答案有更好的思路，修改下
        if num >=0:
            answer = int(num+0.5)
        else:
            answer = int(num - 0.5)
        print('结果是：'+str(answer))
    elif work == 5:
        temp = input('请输入一个年份：')
        if temp.isdigit():
            year = int(temp)
            if (((year % 4) == 0) and ((year % 100) != 0)) or ((year % 400) == 0):
                print(temp+'年是闰年!')
            else:
                print(temp+'年是平年!')
        else:
            print('请输入正确的年份！')
    else:
        print('无此选项!')
