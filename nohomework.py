import os
import sys

def formate_dir(name_dic, dir_name):  # 格式化文件名
    dir_name = dir_name.replace(' ','') #将提交上的作业的奇怪的分隔符去掉
    dir_name = dir_name.replace('+','')
    dir_name = dir_name.replace('_','')
    dir_name = dir_name.replace('-','')
    for name in name_dic:
        index = dir_name.find(name)
        if index >= 0:
            topic = dir_name[index+len(name):] # 获取名字后面的内容，可能是文件主题
            submit_name.append(name)  # 将提交上的小同学加入名单
            return   name + ' '+ topic # 可以自行改动
    return 'no_name' + dir_name

def find_not_submit(name_dic, submit_name): #看看哪个小同学没有交作业
    no_submmit = []
    for name in name_dic:
        if name  not in submit_name:
            no_submmit.append(name)
    return no_submmit

name_dic = []
submit_name = []
path = "D:\\tx"  # 作业文件夹，替换成你自己的作业文件夹
name_path = "D:\\19计科一班.txt" #同学名单文件夹，同上
fileList = os.listdir(path)
with open(name_path ,'r', encoding='UTF-8') as lines: #编码可能要根据你的系统改变一般这样写没错
    for line in lines:
        name_dic.append(line.strip())   # 获取文件列表

for file_name in fileList:
     new_name = formate_dir(name_dic, file_name) #获得格式化后的文件名
     os.rename(os.path.join(path, file_name), os.path.join(path, new_name)) #修改文件名

# 打印没有提交作业的同学的名单
result = find_not_submit(name_dic, submit_name)
print(result)
