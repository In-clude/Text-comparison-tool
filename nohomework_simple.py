from os import listdir
with open("./花名册.txt", "r", encoding='utf-8') as f:#放置花名册 注意.txt文件应保存为utf-8编码
    data = f.readlines()
for i in range(len(data)):
    data[i] = data[i].strip('\n')

data.append("计科一班")
#print(data)
#dst_path = 'C:\\计科1班python课程设计'
dst_path = input("输入作业文件夹路径：")#输入存放作业文件的文件夹路径 
for file in listdir(dst_path):
    for i in range(len(data) - 1):
        if file.find(data[i]) != -1:
            del data[i]
            break


print(data)#输出未交人员
