#!/usr/bin/env python3
"""
`wordladder` implementation

@authors: Roman Yasinovskyy
@version: 2021.4
"""

import copy
from collections import deque
from typing import List, Set


class Solver:
    """Build a ladder of words"""

    def __init__(self, filename: str):
        """Initialize sets of 3-, 4-, and 5-letter words"""
        self.words3: Set[str] = set()  # 3-letter words
        self.words4: Set[str] = set()  # 4-letter words
        self.words5: Set[str] = set()  # 5-letter words

        with open(filename, "r") as file:
            content = file.readlines()
            for i in content:
                val = i.strip()
                if len(val) == 3:
                    self.words3.add(val)
                elif len(val) == 4:
                    self.words4.add(val)
                else:
                    self.words5.add(val)

    def distance(self, word1: str, word2: str) -> int:
        """
        Find difference between words

        @param word1: 1st word
        @param word2: 2nd word
        @return number of different letters in the same positions
        @raises ValueError if words are not of the same length
        """
        if len(word1) != len(word2):
            raise ValueError("Must use words of the same length")

        # Old Solution:
        # dist = 0
        # for count, i in enumerate(word1):
        #     if i != word2[count]:
        #         dist += 1

        # List Comprehension
        return len(
            [i for i in zip(word1, word2) if i[0] != i[1]]
        )

    def diff_by_one_all(
        self, word: str, all_words: Set[str], used_words: Set[str]
    ) -> List[str]:
        """
        Find all words that differ by 1 letter

        @param word: target word
        @param all_words: all words of the same length as `word`
        @param used_words: all words that are already used and should not be considered
        """

        output: List[str] = list()
        # used_words.add(word)
        for i in all_words:
            distance = self.distance(word, i)
            if distance == 1 and i not in used_words:
                output.append(i)
            used_words.add(i)

        return output

    def build_ladder(self, word_start: str, word_stop: str) -> List[str]:
        """
        Build a word ladder

        @param word_start: 1st word
        @param word_stop: 2nd word
        @return a word ladder as a list
        """
        used_words = []
        used_words.append(word_start)
        queue: deque = deque()
        stack = deque

        word_size = len(word_start)
        if word_size == 3:
            all_words = self.words3
        elif word_size == 4:
            all_words = self.words4
        else:
            all_words = self.words5

        for count, i in enumerate(
                self.diff_by_one_all(word_start, all_words, set(used_words))
        ):
            queue.append(stack())
            queue[count].appendleft(word_start)
            queue[count].appendleft(i)
            used_words.append(i)

        running = len(queue)
        while running > 0:
            item = queue.popleft()
            if item[0] == word_stop:
                return item
            else:
                unused_words = self.diff_by_one_all(item[0], all_words, set(used_words))
                for i in unused_words:
                    clone = copy.deepcopy(item)
                    clone.appendleft(i)
                    used_words.append(i)
                    queue.append(clone)
            running = len(queue)

        # print(used_words)
        # print(
        #     self.diff_by_one_all(
        #         "elf",
        #         self.words3,
        #         {
        #             "elk", "elb", "elf",
        #             "eli", "ilk", "elt",
        #             "alk", "elm", "eld",
        #             "els", "ell", "ebb",
        #             "alb"
        #         }
        #     )
        # )


def main():
    """Main"""
    solver = Solver("/home/adam/Documents/CS-160/ads-class-pub/data/projects/wordladder/words.txt")

    print(
        solver.build_ladder("elk", "elf")
    )

    # print(
    #     solver.diff_by_one_all(
    #         "elk",
    #         {"elf", "eld", "ilk", "elt", "eli", "els", "alk", "elm", "elb", "ell"},
    #         {"elf", "ilk", "eli", "elm", "elb"}
    #     )
    # )


if __name__ == "__main__":
    main()
