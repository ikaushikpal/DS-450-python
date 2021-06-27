# my solution
def countAllBits(num):
    devident = num+1
    i = remainder = quotient = divisor = 0
    value = 1 << i
    counter = 0

    while value <= devident:
        divisor = 1 << (i+1)
        remainder = devident % divisor
        quotient = devident // divisor

        counter += (quotient * value)
        if remainder - value > 0:
            counter += (remainder - value)
        
        i += 1
        value = 1 << i

    return counter



print(countAllBits(8))