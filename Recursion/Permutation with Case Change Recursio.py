def permutationWCaseChangeUtil(input_string, output_string):
    if len(input_string) == 0:
        print(output_string, end=', ')
        return 
    
    modified_output_string1 = output_string  + input_string[0].upper()
    modified_output_string2 = output_string  + input_string[0]

    modified_input_string = input_string[1:]

    permutationWCaseChangeUtil(modified_input_string, modified_output_string1)
    permutationWCaseChangeUtil(modified_input_string, modified_output_string2)


def permutationWCaseChange(input_string):
    if len(input_string) == 0:
        print('Invalid String')
        return

    print('permutation with case change of',input_string,':')
    permutationWCaseChangeUtil(input_string, '')

    print()

permutationWCaseChange('ab')
