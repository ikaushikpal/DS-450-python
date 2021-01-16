class TrieNode:
    def __init__(self, data=None):
        self.data = data
        self.child = [None] * 26
        self.word_count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, data):
        if len(data) == 0:
            return
        currentNode = self.root
        for i in range(len(data)):
            char = data[i]
            index = ord(char) - 97

            if currentNode.child[index] is None:
                currentNode.child[index] = TrieNode(char)
            currentNode = currentNode.child[index]
        currentNode.word_count += 1

    def search(self, key):
        if len(key) == 0:
            return 0
        currentNode = self.root
        for i in range(len(key)):
            char = key[i]
            index = ord(char) - 97
            if currentNode.child[index] is None:
                return 0
            else:
                currentNode = currentNode.child[index]
        return currentNode.word_count

    def __hasChild(self, currentNode):
        for child in currentNode.child:
            if child:
                return True
        return False

    def delete(self, key):
        if len(key) == 0:
            return None
        self.__deleteUtil(key, self.root, 0)

    def __deleteUtil(self, key, __current_node, __current_depth=0):
        if __current_node is None:
            return None

        if __current_depth == len(key):
            if __current_node.word_count > 0:
                __current_node.word_count = 0

            if self.__hasChild(__current_node) == False:
                del __current_node
                return None
            else:
                return __current_node

        index = ord(key[__current_depth]) - 97
        __current_node.child[index] = self.__deleteUtil(
            key, __current_node.child[index], __current_depth + 1
        )

        # if current_node has child then do nothing otherwise del currentNode
        if (
            __current_node != self.root
            and self.__hasChild(__current_node) == False
            and __current_node.word_count == 0
        ):
            del __current_node
            return None
        return __current_node

    def display(self):
        print("Elements of Trie are : ", end="")
        self.__display(self.root)
        print()

    def __display(self, currentNode, output_string=""):
        if currentNode.word_count > 0:
            print(output_string, end=", ")

        for child in currentNode.child:
            if child:
                self.__display(child, output_string + child.data)
        return


if __name__ == "__main__":
    tr = Trie()
    tr.insert("abc")
    tr.insert("abd")
    tr.insert("aba")
    tr.insert("pc")
    tr.insert("android")
    tr.insert("iphone")
    print(tr.search("abc"))
    print(tr.search("ab"))
    # tr.delete('abc')
    # tr.delete('ab')
    # print(tr.search('abc'))
    tr.display()
