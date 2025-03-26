string = input()
# w:/a\bc::/12\xyz
# abc:/b1c\xy
LEFT = RIGHT = MIDDLE = False
lcount = rcount = 0
ans = 0
right_start = float('inf')

for j in range(len(string)):
    if not LEFT:
        if 'a' <= string[j] <='z':
            lcount += 1

        elif string[j] == '/':
            LEFT = True
        else:
            continue

    if not MIDDLE:
        if string[j] == '\\':
            MIDDLE = True
        continue
    
    if not RIGHT:
        if 'a' <= string[j] <='z':
            right_start = min(right_start, j)
            rcount += 1
        else:
            RIGHT = True

    if RIGHT == True:
        ans += lcount * rcount
        lcount = rcount
        rcount = 0

        i = right_start
        LEFT = MIDDLE = RIGHT = False
        right_start = float('inf')
    
ans += lcount * rcount
    
print(ans)


# print(pattern.search(string))
