def permutationWLetterCaseUtil(input_string, output_string):
    if len(input_string) == 0:
        print(output_string, end=', ')
        return 
    
    count = i = 0
    char2 = char1 = ''
    flag = False

    while i<len(input_string):
        if input_string[i].isalpha() and flag == True:
            break
        elif input_string[i].isalpha() and flag == False:
            char1 += input_string[i].lower()
            char2 += input_string[i].upper()
            count += 1
            flag = True
        else:
            char1 += input_string[i]
            char2 += input_string[i]
        i += 1

    if count == 0:
        print(char1, end='')
        return 

    modified_output_string1 = output_string  + char1
    modified_output_string2 = output_string  + char2

    modified_input_string = input_string[i:]

    permutationWLetterCaseUtil(modified_input_string, modified_output_string1)
    permutationWLetterCaseUtil(modified_input_string, modified_output_string2)


def permutationWLetterCase(input_string):
    if len(input_string) == 0:
        print('Invalid String')
        return

    print('permutation with letter case change of',input_string,':')
    permutationWLetterCaseUtil(input_string, '')

    print()

permutationWLetterCase('a1B2')
