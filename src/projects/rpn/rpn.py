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
    token_list = postfix_expr[:-2].split()

    for token in token_list:
        # if token in "0123456789":
        try:
            if isinstance(int(token), int):
                operand_stack.push(int(token))
        except ValueError:
            if token in ("+", "-", "*", "/", "%", "//", "**"):
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = do_math(token, operand1, operand2)
                operand_stack.push(result)
            else:
                raise TokenError(f"Unknown token: {token}")
    try:
        answer = operand_stack.pop()
    except IndexError:
        raise StackError("Stack is empty") from IndexError

    if not operand_stack.is_empty():
        raise StackError("Stack is not empty")

    return answer


def do_math(oper: str, oper_one: int, oper_two: int):
    """Process arithmetic operations"""
    if oper == "+":
        return oper_one + oper_two
    elif oper == "-":
        return oper_one - oper_two
    elif oper == "*":
        return oper_one * oper_two
    elif oper == "/":
        return oper_one / oper_two
    elif oper == "%":
        return oper_one % oper_two
    elif oper == "//":
        return oper_one // oper_two
    elif oper == "**":
        return oper_one ** oper_two
    else:
        raise SyntaxError("invalid syntax")


def rpn_calc(filename: str) -> int:
    """Read lines from the file and pass them to the postfix_eval"""
    file = open(filename, "rt")
    contents = file.readlines()
    total = 0
    for i in contents:
        print(i)
        try:
            output = postfix_eval(i.strip())
            total += output
        except ZeroDivisionError:
            total += 0
        except StackError:
            total += 0
        except IndexError:
            total += 0
    file.close()
    print(total)
    return total


def main():
    """Main function"""
    # print(postfix_eval("a b + ="))
    # rpn_calc(f"/home/adam/Documents/CS-160/ads-class-pub/data/projects/rpn/rpn_input_2.txt")
    print(postfix_eval("2 1 8 11 ** * // ="))


if __name__ == "__main__":
    main()
