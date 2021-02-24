from collections import Counter
import csv

with open('HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    n_num = fileData[i][2]
    newData.append(float(n_num))

data = Counter(newData)
modeDataForRange = {"50-60": 0, "60-70": 0, "70-80": 0}

for Height,Occurence in data.items():
    if 50<float(Height)<60:
        modeDataForRange["50-60"] += Occurence
    elif 60<float(Height)<70:
        modeDataForRange["60-70"] += Occurence
    elif 70<float(Height)<80:
        modeDataForRange["70-80"] += Occurence

modeRange,modeOccurence = 0,0
for Range,Occurence in modeDataForRange.items():
    if Occurence>modeOccurence:
        modeRange,modeOccurence = [int(Range.split("-")[0]),int(Range.split("-")[1])],Occurence

mode = float((modeRange[0]+modeRange[1])/2)
print("Mode Is: "+str(mode))