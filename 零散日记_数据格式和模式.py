print('♥吐司记录小工具♥')
print('♥让你的每分每秒都有记录♥')
print('♥建议把程序放到你想保存日记的位置，然后将此程序快捷方式发送到桌面♥' + '\n')
print('♥记录内容为：事件名字，事件开始时间，事件结束时间，做这件事情花费了你多少时间！♥')
confirm = input('看完了没，bro？[按回车键进行下一步]')
# 创建我的每日文件------------------------------------------------------------------
import datetime
import re
today = datetime.date.today()
file_name = '%s'%today + '.txt'
print('文件名为:' + file_name)
# path_file = r"D:\codefiles\toast_quant\Frequent_records" + "\%s"%file_name
# print(path_file)
try:
    lines = []
    with open(file_name, 'r') as ff:
        print('File exists!')
        try:
            lines = ff.readlines() #读取所有行
            # first_line = lines[0] #取第一行
            last_line = lines[-2] #取最后一行
            print(last_line)
        except:
            print("下次不用自己建立文件啦！")
            with open(file_name, 'a+') as ff:
                while True:
                    weather = input("今天天气如何？(晴天、阴天、雨天、雪天)")  
                    if weather != '':
                        print("祝你有一个好心情！")
                        break
                    else:
                        print("不要偷懒，记录一下天气哦！")  
                ff.write("今天是%s" % today + "\n" + "%s"% weather + "\n")
                print('成功记录今天的开头!')
except FileNotFoundError:
    with open(file_name, 'a+') as ff:
        try:
            while True:
                wake_time = str(input("你今天几点起来的呀？"))
                if wake_time != '':
                    print("起来了就好好努力哦！")
                    break
                else:
                    print("不要自责，记录一下起床时间哦！")
            wake_time = re.sub("：", ":", wake_time)
            wake_time = datetime.strptime(input_start_time, "%H:%M")
            print(wake_time)
        except:
            print('please enter like this: 08:00(英文输入法)')
        while True:
            weather = input("今天天气如何？(晴天、阴天、雨天、雪天)")
            if weather != '':
                print("祝你有一个好心情！")
                break
            else:
                print("不要偷懒，记录一下天气哦！")
        ff.write("今天是%s"%today + ",天气：%s"%weather + "\n" + wake_time + '---  wake time' + "\n")
        print('Successfully created!')
# -----------------------------------------------------------------------------------------

# 开始时间
from datetime import datetime, timedelta
import re
while True:
            doing_now = input('你做了什么？')
            if doing_now != '':
                print("恭喜你又完成了一件事情")
                break
            else:
                print("不要乱填哦！")
doing_now = doing_now + '---  ' + 'done'
while True:
    try:
        while True:
            input_start_time = str(input('你是从几点开始做这件事的?例如:08:00(英文输入法)'))
            if input_start_time != '':
                print("恭喜你又完成了一件事情")
                break
            else:
                print("不要乱填时间哦！")
        input_start_time = re.sub("：", ":", input_start_time)
        print(input_start_time)
        start_time = datetime.strptime(input_start_time, "%H:%M")
        break
    except:
        print('please enter like this: 08:00(英文输入法)')

print('The time to start is: ' + input_start_time)
# input_start_time = '14:00'
# start_time=datetime.strptime(input_start_time, "%H:%M")
# start_time1 = datetime.strptime(start_time, "%H:%M:%S")
while True:
    enter_tag = input("这件事的性质为:(学习、工作、娱乐、日常)")
    if enter_tag != '':
        print("恭喜你又完成了一件事情！")
        break
    else:
        print("不要乱写标签哦！")
tag = str(enter_tag)
print_tag = tag + '---  ' + "tag"

# doing_now =
#这里需要新增一个触发程序运行的一个按钮
#如何将时间从1900-01-01 变成 当前时间????
now_time_raw = str(datetime.now().strftime("%H:%M"))
now_time = datetime.strptime(now_time_raw, "%H:%M")

# print(start_time)
print_start_time = str(start_time)
print_now_time = str(now_time)
print('start：'+ ' ---  ' + print_start_time[11:])
print('now：  '+ ' ---  ' + print_now_time[11:])

take_minutes = now_time - start_time
print(str(doing_now) +' --- Take ' + str(take_minutes.seconds//60) + ' minutes')



#写入文本---------------------------------------------------------------
content_time = str(take_minutes.seconds//60) + '--------Take ' + str(take_minutes.seconds//60) + ' minutes--------' + "\n" + str(doing_now)
content_start = print_start_time[11:] +  '---  '  + 'start'
content_now = print_now_time[11:] +  '---  '  + 'now'
next_begin_time = str(now_time)
print_next_begin_time = '上次事件的结束时间为：' + next_begin_time[11:]
contents = [content_time, print_tag, content_start, content_now, print_next_begin_time]
# print(str(take_minutes.seconds//60))
# print(str(take_minutes.seconds))
# content_append = [str(take_minutes.seconds//60), str(start_time.hour), str(now_time.hour)]
# print(contents)
with open(file_name, "a+") as file:  # 只需要将之前的p”w"改为“a"即可，代表追加内容
    for content in contents:
        file.write(content + " " + "\n")
    file.write("\n")

print('--------------------------------------')
import time
import sys
print('当前事件已经记录完毕,文件保存在程序所在位置')
print('快开始做下一件事情吧！')
print('不要忘了及时记录你的事情')
print('让你的每分每秒都有回忆')
print('这个程序将在7秒后关闭，下件事结束后再见！')
time.sleep(7)
sys.exit(0)
# -----------------------pass test--------------
# contents = ['12','23','24']
# with open(path_file, "a+") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
#     for content in contents:
#         file.write(content + " " + "\n")
#         print(content)
# -----------------------pass test--------------
# end_time_raw = '23:00'
# end_time=datetime.strptime(end_time_raw, "%H:%M")
# print: 08:00 ~ 10：00❤120 Min❤我洗了个澡❤
# start_time + '~' + now_time + '❤' +
# tss2 = "23:40"
# # 转为数组
# timeArray = time.strptime(tss2, "%H:%M")
# print('timeArray:' + str(type(timeArray)))
# print(timeArray)
# otherStyleTime = time.strftime("%H:%M", timeArray)
# print(type(otherStyleTime))
# print(otherStyleTime)  # 2013/10/10 23:40:00
# seconds = (timeArray - now_time).seconds
#

# ----------------------------------------------------------------------------------
# #计算用时
# from datetime import datetime, timedelta
# a1='09:01:04'
# a2='09:02:50'

# print(type(a1))

# test1=datetime.strptime(a1, "%H:%M:%S")
# test2=datetime.strptime(a2, "%H:%M:%S")

# print(str(type(test1))+str(type(test2)))

# diff=test2-test1

# print(type(diff))
# print('Do it---Take ' + str(diff.seconds//60) + ' minutes')

#邮件功能----------------------------------------------------
# user = '2807778787@qq.com'
# password = 'hsplpzbnkgcoddjb'
# host = 'smtp.qq.com'
# yag = yagmail.SMTP(user=user, password=password, host=host)
# subject = ''
# content = ''
# # myself = 'toast@nwafu.edu.cn'
# guosenyan = '929632514@qq.com'

# def sendEmail(subject, content, who):
#     """
#         发送邮件
#     """
#     subject = subject
#     content = content
#     yag.send(to=who, subject=subject, contents=content)
#     print('发送邮件成功!')


#测试邮件功能-----------------------------------------------------------------------------------------
# import yagmail
# content = ('''
# 08:00 ~ 10:00❤120 Min❤我洗了个澡
# 10:05 ~ 11:00❤55  Min❤what did you do?
# 08:00 ~ 10:00❤120 Min❤我洗了个澡
# 10:05 ~ 11:00❤55  Min❤what did you do?
# 08:00 ~ 10:00❤120 Min❤我洗了个澡
# 10:05 ~ 11:00❤55  Min❤what did you do?
# 08:00 ~ 10:00❤120 Min❤我洗了个澡
# 10:05 ~ 11:00❤55  Min❤what did you do?''')
# print(content)
# sendEmail(who=guosenyan, subject='text_record_your_f*king_life',content=content)
# print('send is ok')
# exit()


# 文件名怎么取----------------------------------------------------------------------
# a = datetime.date.today()
# file_name = '%s'%a + '.txt'
# print(file_name)
# print(type(a))

# -----------------------------------------------------------------------
