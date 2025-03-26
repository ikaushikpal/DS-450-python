# def generateString(count, value):
#     valuePair = {'1':'one',
#                 '2':'two',
#                 '3':'three',
#                 '4':'four',
#                 '5':'five',
#                 '6':'six',
#                 '7':'seven',
#                 '8':'eight',
#                 '9':'nine',
#                 '0':'zero'
#                 }
#     returnString = ''
#     if count // 3 > 0:
#         times = count // 3
#         count = count % 3
#         msg = f'triple {valuePair[value]} ' * times
#         returnString += msg

#     if count // 2 > 0:
#         times = count // 2
#         count = count % 2
#         msg = f'double {valuePair[value]} ' * times
#         returnString += msg
    
#     if count > 0:
#         msg = f'{valuePair[value]} '
#         returnString += msg

#     return returnString

# def getPhoneNumber(s):
#     if len(s) == 0:
#         return ''

#     i = 0
#     outputString = ''
    
#     while i < len(s):
#         count, value = 0, s[i]
#         while i < len(s) and s[i] == value:
#             count += 1
#             i += 1
#         outputString += generateString(count, value)
    
#     return outputString[:-1]

def getPhoneNumber(s):
    valuePair = {'one':'1',
                'two':'2',
                'three':'3',
                'four':'4',
                'five':'5',
                'six':'6',
                'seven':'7',
                'eight':'8',
                'nine':'9',
                'zero':'0'
                }

    tokens = s.split()
    outputString = ''
    i = 0

    while i < len(tokens):
        if tokens[i] in valuePair:
            outputString += valuePair[tokens[i]]
        elif tokens[i] == 'triple':
            outputString += valuePair[tokens[i+1]] * 3
            i += 1
        elif tokens[i] == 'double':
            outputString += valuePair[tokens[i+1]] * 2
            i += 1
        i += 1
        
    return outputString


if __name__ == '__main__':
    s = 'two one nine six eight one six zero'
    print(getPhoneNumber(s))