"""
temperature_list = [36.4, 36.6, 36.2, 37.0, 35.4, 38.5]
for temperature in temperature_list:
    if temperature >= 38:
        print(temperature)
        print("完球了")
"""
temperature_dict = {"111":36.4, "112":36.6, "113":38.5, "114":39.4}

for staff_id, temperature in temperature_dict.items():
    if temperature >= 38:
        print(staff_id)
"""
字典中是键值对
d = {key1:value1, key2:value2}
key1:value1 --> item
"""
# 所有键      print(temperature_dict.values())
# 所有值      print(temperature_dict.items())
# 所有键值对   print(temperature_dict.keys())

'''
for结合range使用
range表示整数数列
eg. range(5,10)  5-->起始值  10-->结束值
结束值不在序列范围内
'''
for i in range(5, 10):
    print(i)
"""
rang 也可以包含三个数
eg. range(5,10,2) 2-->表示步长，也就是每次跨几个数字，不指明默认为1
"""
total = 0
for i in range(1, 101):
    total = total + i
print(total)