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


def do_math(oper: str, oper_one: int, oper_two: int) -> int:
    """Process arithmetic operations"""
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


def rpn_calc(filename: str) -> int:
    """Read lines from the file and pass them to the postfix_eval"""
    # TODO: Read lines from the file and pass them to the postfix_eval
    file = open(filename, "rt")
    file.close()


def main():
    """Main function"""
    checksum = rpn_calc("data/projects/rpn/rpn_input_1.txt")
    print(f"Checksum is {checksum:.2f}")


if __name__ == "__main__":
    main()
