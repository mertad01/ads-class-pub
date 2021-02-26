#!/usr/bin/env python3
"""
Reverse Polish Notation
"""

from pythonds3.basic import Stack


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


def postfix_eval(postfix_expr: str) -> int:
    """Evaluate an expression"""
    if len(postfix_expr) == 1:
        raise StackError("Stack is empty")
    operand_stack = Stack()
    token_list = postfix_expr[:-2].split()

    try:
        for token in token_list:
            if token in "0123456789":
                operand_stack.push(int(token))
            elif token in ("+", "-", "*", "/", "%", "//", "**"):
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
        raise StackError("pop from empty list") from IndexError


def do_math(oper: str, oper_one: int, oper_two: int) -> int:
    """Process arithmetic operations"""
    answer = 0
    if oper == "*":  # pylint: disable=no-else-return
        answer = oper_one * oper_two
    elif oper == "/":
        answer = oper_one / oper_two
    elif oper == "+":
        answer = oper_one + oper_two
    elif oper == "-":
        answer = oper_one - oper_two
    elif oper == "**":
        answer = oper_one ** oper_two
    elif oper == "//" and oper_two == 0:
        if oper_two == 0:
            raise ZeroDivisionError('integer division or modulo by zero')
        answer = oper_one % oper_two
    elif oper == "//":
        if oper_two == 0:
            raise ZeroDivisionError('integer division or modulo by zero')
        answer = oper_one // oper_two
    else:
        raise TokenError(f'invalid syntax')
    return answer


def rpn_calc(filename: str) -> int:
    """Read lines from the file and pass them to the postfix_eval"""
    file = open(filename, "rt")
    contents = file.readlines()
    for i in contents:
        try:
            output = postfix_eval(i.strip())
        except ZeroDivisionError:
            print("division by zero")
        except TokenError as exception:
            print(exception.args[0])
        except StackError as exception:
            print(exception.args[0])
    file.close()
    return output


def main():
    """Main function"""
    # print(postfix_eval("1 6 0 % %"))
    do_math("a", "/", 2)
    # checksum = rpn_calc("/home/adam/Documents/CS-160/ads-class-pub/data/projects/rpn/rpn_input_1.txt")
    # print(f"Checksum is {checksum:.2f}")


if __name__ == "__main__":
    main()
