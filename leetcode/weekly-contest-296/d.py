class TextEditor:

    def __init__(self):
        self.cursor = 0
        self.text = ''

    def addText(self, text: str) -> None:
        left = self.text[:self.cursor]
        right = self.text[self.cursor:]
        self.text = left + text + right
        self.cursor = self.cursor + len(text)

    def deleteText(self, k: int) -> int:
        canDelete = min(k, self.cursor)
        self.text = self.text[:self.cursor - canDelete] + self.text[self.cursor:]
        self.cursor = self.cursor - canDelete
        return canDelete

    def cursorLeft(self, k: int) -> str:
        canMove = min(k, self.cursor)
        self.cursor = self.cursor - canMove
        canView = min(10, self.cursor)
        return self.text[self.cursor - canView:self.cursor]

    def cursorRight(self, k: int) -> str:
        canMove = min(k, len(self.text) - self.cursor)
        self.cursor = self.cursor + canMove
        canView = min(10, self.cursor)
        return self.text[self.cursor - canView:self.cursor]


if __name__ == '__main__':
    # textEditor = TextEditor()  #  The current text is "|". (The '|' character represents the cursor)
    # print(textEditor.addText("leetcode"))  #  The current text is "leetcode|".
    # print(textEditor.deleteText(4))  #  return 4
    #                         #  The current text is "leet|". 
    #                         #  4 characters were deleted.
    # print(textEditor.addText("practice"))  #  The current text is "leetpractice|". 
    # print(textEditor.cursorRight(3))  #  return "etpractice"
    #                         #  The current text is "leetpractice|". 
    #                         #  The cursor cannot be moved beyond the actual text and thus did not move.
    #                         #  "etpractice" is the last 10 characters to the left of the cursor.
    # print(textEditor.cursorLeft(8))  #  return "leet"
    #                         #  The current text is "leet|practice".
    #                         #  "leet" is the last min(10, 4)) = 4 characters to the left of the cursor.
    # print(textEditor.deleteText(10))  #  return 4
    #                         #  The current text is "|practice".
    #                         #  Only 4 characters were deleted.
    # print(textEditor.cursorLeft(2))  #  return ""
    #                         #  The current text is "|practice".
    #                         #  The cursor cannot be moved beyond the actual text and thus did not move. 
    #                         #  "" is the last min(10, 0)) = 0 characters to the left of the cursor.
    # print(textEditor.cursorRight(6))  #  return "practi"
    #                         #  The current text is "practi|ce".
    #                         #  "practi" is the last min(10, 6) = 6 characters to the left of the cursor.

#     ["TextEditor","addText","cursorLeft","deleteText","cursorLeft","addText","cursorRight"]
# [[],[],[],[],[],[],[]]

    # [null,null,"bx",2,"",null,"yackuncqzc"]
    t = TextEditor()
    print(t.addText("bxyackuncqzcqo"))
    print(t.cursorLeft(12))
    print(t.deleteText(3))
    print(t.cursorLeft(5))
    print(t.addText("osdhyvqxf"))
    print(t.cursorRight(10))
