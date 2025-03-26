def permutationWSpaceUtil(input_string, output_string):
    if len(input_string) == 0:
        print(output_string, end=', ')
        return 
    
    modified_output_string1 = output_string  + '-' + input_string[0]
    modified_output_string2 = output_string  + input_string[0]
    modified_input_string = input_string[1:]

    permutationWSpaceUtil(modified_input_string, modified_output_string1)
    permutationWSpaceUtil(modified_input_string, modified_output_string2)


def permutationWSpace(input_string):
    if len(input_string) == 0:
        print('Invalid String')
        return

    print('permutation with space of',input_string,':')
    modified_output_string = input_string[0]
    modified_input_string = input_string[1:]
    permutationWSpaceUtil(modified_input_string, modified_output_string[0])
    # permutationWSpaceUtil(input_string, '')
    print()

permutationWSpace('ABC')
