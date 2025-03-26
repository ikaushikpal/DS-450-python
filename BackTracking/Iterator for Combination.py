# Design the CombinationIterator class:

# CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# next() Returns the next combination of length combinationLength in lexicographical order.
# hasNext() Returns true if and only if there exists a next combination.
 

# Example 1:
# Input
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]

# Explanation
# CombinationIterator itr = new CombinationIterator("abc", 2);
# itr.next();    // return "ab"
# itr.hasNext(); // return True
# itr.next();    // return "ac"
# itr.hasNext(); // return True
# itr.next();    // return "bc"
# itr.hasNext(); // return False


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.generator = self.generate("", 0)
        self.buffer = next(self.generator)

    def generate(self, combi, pos):
        if len(combi) == self.combinationLength:
            yield combi

        if pos >= len(self.characters):
            return
        
        for i in range(pos, len(self.characters)):
            char = self.characters[i]
            yield from self.generate(combi+char, i+1)

    def next(self) -> str:
        res = self.buffer
        try:
            self.buffer = next(self.generator)
        except StopIteration:
            self.buffer = None
        finally:
            return res

    def hasNext(self) -> bool:
        return self.buffer is not None
# Time Complexity: O(2^n)
# Space Complexity: O(nCk)


if __name__ == '__main__':
    itr = CombinationIterator("abc", 2)
    print(itr.next())
    print(itr.hasNext())
    print(itr.next())
    print(itr.hasNext())
    print(itr.next())
    print(itr.hasNext())
