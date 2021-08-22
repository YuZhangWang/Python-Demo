'''
if:
elif:
else:

条件组合
and or not
'''
'''
#if、elif、else例子
PM = eval(input("请输入PM2.5数值:"))
if 0 <= PM < 35:
    print("空气优质。快去户外运动！")
elif 35 <= PM < 75:
    print("空气良好，适度户外活动！")
else:
    print("空气污染，请小心！")
    
#分数匹配的错误例子
score = eval(input())
if score >= 60.0:
    grade = 'D'
elif score >= 70.0:
    grade = 'C'
elif score >= 80.0:
    grade = 'B'
elif score >= 90.0:
    grade = 'A'
print(grade)
'''
# 身体质量BMI
height, weight = eval(input("请输身高(米)和体重(公斤)[用逗号隔开]:"))
bmi = weight / pow(height, 2)
print("BMI数值为:{:.2f}".format(bmi))
who, dom = "", ""
# WHO标准
if bmi < 18.5:
    who = "偏瘦"
elif 18.5 <= bmi < 25:
    who = "正常"
elif 25 <= bmi < 30:
    who = "偏胖"
else:
    who = "肥胖"
# 国内标准
if bmi < 18.5:
    dom = "偏瘦"
elif 18.5 <= bmi < 24:
    dom = "正常"
elif 24 <= bmi < 28:
    dom = "偏胖"
else:
    dom = "肥胖"

print("国际标准为:{},国内标准为:{}".format(who, dom))
