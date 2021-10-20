from os import listdir

with open("./21人工智能一班.txt", "r", encoding='utf-8') as f: #学生名单txt文件，一行一个
    data = f.readlines()
f.close()
for i in range(len(data)):
    data[i] = data[i].strip('\n')

data.append("21ai1")
print(data)

dst_path = 'C:\\Users\\java2' #作业文件夹

for file in listdir(dst_path.strip("")):
    for i in range(len(data) - 2):
        if file.find(data[i]) != -1:
            del data[i]

for file in listdir(dst_path):
    for i in range(len(data) - 1):
        if file.find(data[i]) != -1:
            del data[i]

print(data)
