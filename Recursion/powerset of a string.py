def powerSets(input_string, output_string, index):
    if index == len(input_string):
        if output_string == '':
            print("' '",end=', ')
        else:
            print(output_string, end=', ')
        return

    powerSets(input_string, output_string, index+1)
    output_string += input_string[index]
    powerSets(input_string, output_string, index+1)


def solve(input_string, output_string):
    if len(input_string) == 0:
        if output_string == '':
            print("' '",end=', ')
        else:
            print(output_string, end=', ')
        return

    modified_output_string = output_string + input_string[0]
    input_string = input_string[1:]

    solve(input_string, output_string)
    solve(input_string, modified_output_string)



solve('ABC','')