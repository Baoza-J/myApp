import os
import re
#获取文件名称
dirs = os.listdir() 

print(dirs)
for dir in dirs:
    try:
        #获得旧文件的数字和小数点部分
        temp = re.findall(r'[0-9.]*', dir) 
        temp = temp[0] 

        #重命名
        os.rename(dir, temp)
    except FileNotFoundError:
        print('有部分文件不匹配')
dirs = os.listdir()
print(dirs) # 打印修改后的文件名称
