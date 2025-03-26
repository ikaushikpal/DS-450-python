MOD = 10**9+7

def valueFromList(head):
    value = 0
    current_node = head

    while current_node:
        value = (value * 10) + current_node.data
        current_node = current_node.next
    
    return value

def multiplyTwoList(head1, head2):
    val1 = valueFromList(head1)
    val2 = valueFromList(head2)

    return (val1*val2) % MOD
