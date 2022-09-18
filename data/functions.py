def infix_to_postfix(regex, alphabet, operations):
    operation_order = Stack();
    post_string = ""
    for i in range(len(regex)):
        if regex[i] in alphabet:
            post_string += regex[i]
        elif regex[i] in operations:
            while (not operation_order.is_empty() and has_higher_precedence(operation_order.peek(), regex[i]) and operation_order.peek()!='('):
                post_string += operation_order.pop()
            operation_order.push(regex[i])
        elif regex[i]=='(':
            operation_order.push('(')
        elif regex[i]==')':
            while (not operation_order.is_empty() and operation_order.peek()!='('):
                post_string += operation_order.pop()
            operation_order.pop()

    while (not operation_order.is_empty()):
        post_string += operation_order.pop()
    return post_string
