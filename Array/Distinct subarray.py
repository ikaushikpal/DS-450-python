import itertools
n1 = int(input())
n2 = int(input ())
#generate array from n1 to n2
array = [i for i in range(n1,n2+1)]
 
print(array)
ll = [array[i:j+1] for i in range(len(array)) for j in range(i,len(array))]
 
print(ll)
c=0
for i in ll:
    if sum(i)%2!=0:
        print(i)
        c+=1
print(c)