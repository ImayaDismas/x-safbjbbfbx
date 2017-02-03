data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(data)
data1 = [[13,14,15],[16,17,18]]
print(data1)
data.clear()
data.extend(data1)
print(data)
