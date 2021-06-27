import heapq


class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f'Character {self.char} and frequency {self.frequency}'

    def __lt__(self, otherObj):
        return self.frequency < otherObj.frequency
    
    def __gt__(self, otherObj):
        return self.frequency > otherObj.frequency


class HuffmanCoding:
    def __init__(self):
        self.messageSize = 0
        self.tableSize = 0
        self.root = None
        self.ASCII_Encoding = 0
    
    def createNodes(self, minHeap, arr, freq):
        for i in range(len(arr)):
            newNode = Node(arr[i], freq[i])
            heapq.heappush(minHeap, newNode)
            self.ASCII_Encoding += freq[i]

        self.tableSize += 8 * len(minHeap)
        self.ASCII_Encoding *= 8

    def printEncode(self, root, string):
        if not root.left and not root.right:
            print(f"{root.char} : {string}")
            self.tableSize += len(string)
            self.messageSize += len(string) * root.frequency
            return
        
        self.printEncode(root.left, string+'0')
        self.printEncode(root.right, string+'1')

    def printDetails(self):
        print("=" * 40)
        print(f"To perform Huffman Encoding")
        print(f"Message Size = {self.messageSize} bits")
        print(f"Table/Tree Size = {self.tableSize} bits")
        print(f"Total Size = {self.totalEncodingSize} bits")
        print(f"ASCII Encoding Size = {self.ASCII_Encoding} bits")
        print(f"Total bits saved = {self.ASCII_Encoding - self.totalEncodingSize} bits")
        print("=" * 40)

    def encode(self, arr, freq):
        minHeap = []
        self.createNodes(minHeap, arr, freq)
        

        while len(minHeap) != 1:
            leftNode = heapq.heappop(minHeap)
            rightNode = heapq.heappop(minHeap)

            parentFreq = leftNode.frequency + rightNode.frequency
            parentNode = Node(None, parentFreq)

            parentNode.left = leftNode
            parentNode.right = rightNode

            heapq.heappush(minHeap, parentNode)
        
        self.root = heapq.heappop(minHeap)

        print("Printing Encoding Table : ")
        self.printEncode(self.root, '')
        self.totalEncodingSize = self.messageSize + self.tableSize

        self.printDetails()


if __name__ == '__main__':
    huff = HuffmanCoding()

    arr = ['A', 'B', 'C', 'D', 'E']
    freq = [3, 5, 6, 4, 2]

    huff.encode(arr, freq)

    chars = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [ 5, 9, 12, 13, 16, 45]

    huff.encode(chars, freq)