#!/usr/bin/env python3
"""Testing Grounds"""

from pythonds3.basic import Stack


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def rev_string(my_str):
    """Reverse characters in a string using a stack"""
    stack = Stack()
    rev_str = ''
    for i in my_str:
        stack.push(i)
    while stack.is_empty() is False:
        rev_str += stack.pop()
    return rev_str


def par_checker(line):
    """Textbook implementation"""
    stack = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol == "(":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        i = i + 1
    return balanced and stack.is_empty()


def par_checker_ext(line):
    """Check if parentheses are balanced"""
    stack = Stack()
    lefts = "([{<"
    rights = ")]}>"
    for i in line:
        if i in "([{<":
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            if lefts.index(stack.pop()) != rights.index(i):
                return False
    return True


def par_checker_file(filename):
    """Check expressions in the file"""
    output = ''
    with open(filename) as file:
        content = file.readlines()
        for i in content:
            val = par_checker(i.strip())
            if val is True:
                output += f'{i.strip()} is balanced\n'
            else:
                output += f'{i.strip()} is NOT balanced\n'
    print(output[:-1])


def base_converter(dec_num, base):
    """Convert a decimal number to any base"""
    try:
        if base not in [2, 8, 16]:
            raise ValueError(f'Cannot convert to base {base}.')
    except ValueError as exception:
        return exception

    digits = "0123456789ABCDEF"
    rems = Stack()

    while dec_num > 0:
        rem = dec_num % base
        rems.push(rem)
        dec_num = dec_num // base

    output = ''
    while not rems.is_empty():
        output += digits[rems.pop()]

    return output


def rpn_calc(postfix_expr):
    """Evaluate a postfix expression"""
    operand_stack = Stack()
    token_list = postfix_expr.split()

    try:
        for token in token_list:
            if token in "0123456789":
                operand_stack.push(int(token))
            elif token in "+-*/":
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = do_math(token, operand1, operand2)
                operand_stack.push(result)
            else:
                raise TokenError(f'Unknown token: {token}')
        answer = operand_stack.pop()
        if operand_stack.is_empty() is False:
            raise StackError("Stack is not empty")
        return answer
    except IndexError:
        raise StackError("Stack is empty") from IndexError


def do_math(oper, oper_one, oper_two):
    """Evaluate a mathematical operation"""
    if oper == "*":  # pylint: disable=no-else-return
        return oper_one * oper_two
    elif oper == "/":
        return oper_one / oper_two
    elif oper == "+":
        return oper_one + oper_two
    elif oper == "-":
        return oper_one - oper_two
    else:
        raise TokenError(f'Unknown token: {oper}')


print(rpn_calc("1 6 0 + +"))
print(rpn_calc("1 6 / 0 -"))
print(rpn_calc("1 6 // 0 **"))
print(rpn_calc("1 6 0 +"))
print(rpn_calc("1 6 0 + - *"))
print(rpn_calc("1 1 + 1 6 + ** 1 9 + 1 9 + * /"))
