array = list(map(int,'3,5,8,2,19,12,7,11'.split(",")))
array=sorted(array)
j = []
j.append(array[0])
j.append(array[1])
print(j)
 
for i in range(2, len(array)):
    if j[i-1]+j[i-2] in array:
        print(j)
        j.append(j[i-1]+j[i-2])
    else:
        break
 
print(j)