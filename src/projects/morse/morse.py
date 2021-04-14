#!/usr/bin/env python3
"""
`morse` implementation

@authors: Roman Yasinovskyy
@version: 2021.4
"""

from typing import Union
from pythonds3.trees import BinaryTree


class Coder:
    """Morse code encoder and decoder"""

    def __init__(self, file_in: str):
        self.morse_tree = BinaryTree("*")

        with open(file_in) as morse_file:
            for line in morse_file:
                letter, code = line.split()
                self.follow_and_insert(code, letter)
        # self.morse_tree.inorder()  # debug

    def follow_and_insert(self, code_str: str, letter: str) -> None:
        """
        Follow the tree and insert a letter

        @param code_str: morse code sequence
        @param letter: letter corresponding to the `code_str`
        """
        code_len = len(code_str)
        cur_node = self.morse_tree

        for i in range(code_len):
            if code_str[i] == ".":
                if not cur_node.child_left:
                    cur_node.insert_left("⬅")
                cur_node = cur_node.child_left
            if code_str[i] == "-":
                if not cur_node.child_right:
                    cur_node.insert_right("➡")
                cur_node = cur_node.child_right
        cur_node.root = letter

    def follow_and_retrieve(self, code_str: str) -> str:
        """
        Follow the tree and retrieve a letter

        @param code_str: morse code sequence
        @return letter corresponding to the `code_str`
        @raises ValueError if the code is not found
        """
        code_len = len(code_str)
        cur_node = self.morse_tree

        try:
            for i in range(code_len):
                if code_str[i] == ".":
                    cur_node = cur_node.child_left
                elif code_str[i] == "-":
                    cur_node = cur_node.child_right
        except AttributeError:
            raise ValueError(
                f"Could not find {code_str} in the tree"
            ) from AttributeError
        if not cur_node:
            raise ValueError(f"Could not find {code_str} in the tree")
        return cur_node.root

    def find_path(self, tree: BinaryTree, letter: str, path: str) -> Union[bool, str]:
        """
        Find a path to the letter
        Encoder's helper function

        @param tree: Morse tree
        @param letter: letter to encode
        @param path: path to the letter
        @return path to the letter
        """
        # Base Case(s):
        if not tree:
            return None
        elif tree.root == letter:
            return path
        return (
            self.find_path(tree.child_left, letter, path+'.')
            or self.find_path(tree.child_right, letter, path+'-')
        )


    def encode(self, msg: str) -> str:
        """
        Encode a message

        @param msg: text to encode
        @return Morse code representation of the the message
        """
        code = []
        tree = self.morse_tree
        for i in msg.replace(" ", ""):
            out = self.find_path(tree, i, "")
            if not out:
                raise ValueError(f"Could not encode {msg}: {i} is not in the tree")
            code.append(out)
        return " ".join(code)

    def decode(self, code: str) -> str:
        """
        Decode a message

        @param code: Morse code sequence to decode
        @return text corresponding to the code
        """
        code_lst = code.split(' ')
        output = ""
        for i in code_lst:
            try:
                output += self.follow_and_retrieve(i)
            except ValueError:
                # NOTE: Ask why it is supposed to be {code}: {code}
                raise ValueError(
                    f"Could not decode {code}: {code} is not in the tree"
                ) from ValueError
        return output


def main():
    """Main"""
    morse_coder = Coder("../../../data/projects/morse/morse.txt")
    print(morse_coder.encode("HELLO"))

    # test = BinaryTree("*")
    # print(test.root)
    # if not test.child_left and not test.child_right:
    #     print("foo")
    # test.insert_left("E")
    # test.insert_right("T")
    # print(test.child_left.root, test.root, test.child_right.root)
    # morse_coder = Coder("../../../data/projects/morse/test.txt")
    # morse_tree = BinaryTree("*")
    # morse_tree.inorder()


if __name__ == "__main__":
    main()
