import datetime

from lunardate import LunarDate

# 获取农历月
lunar_moth = LunarDate.today().month
# 获取农历日
lunar_day = LunarDate.today().day
# 获取时辰数
chen = (datetime.datetime.now().hour + 1) // 2 % 12
sum = lunar_moth + lunar_day + chen
# 卦象
liuren_list = ["大安", "留连", "速喜", "赤口", "小吉", "空亡"]
print(liuren_list[sum % 6])
