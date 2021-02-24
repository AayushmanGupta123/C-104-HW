import csv

with open('HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    n_num = fileData[i][2]
    newData.append(float(n_num))

n = len(newData)
newData.sort()
if n%2 == 0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2-1])
    median = (median1+median2)/2

else:
    median = newData[n//2]

print("Median Is: " + str(median))