from os import listdir

with open("./19计科一班.txt", "r", encoding='utf-8') as f:
    data = f.readlines()
f.close()
for i in range(len(data)):
    data[i] = data[i].strip('\n')

data.append("19jk1")
print(data)

dst_path = 'C:\\Users\\真\\Desktop\\java\\java2'

for file in listdir(dst_path.strip("")):
    for i in range(len(data) - 2):
        if file.find(data[i]) != -1:
            del data[i]

for file in listdir(dst_path):
    for i in range(len(data) - 1):
        if file.find(data[i]) != -1:
            del data[i]

print(data)
