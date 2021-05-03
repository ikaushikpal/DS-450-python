from collections import deque


class Minstack:
    def __init__(self):
        self.__mainStack = deque()
        self.__supportStack = deque()
        self.__len = 0

    def push(self, value) -> None:
        if self.__len == 0:
            self.__mainStack.append(value)
            self.__supportStack.append(value)

        elif value < self.__supportStack[-1]:
            self.__supportStack.append(value)
        self.__mainStack.append(value)
        self.__len += 1

    def pop(self):
        if self.__len == 0:
            return None

        popped_value = self.__mainStack.pop()
        if popped_value == self.__supportStack[-1]:
            self.__supportStack.pop()

        self.__len -= 1
        return popped_value

    def minElement(self):
        if self.__len == 0:
            return None

        return self.__supportStack[-1]

    def top(self):
        if self.__len == 0:
            return None

        return self.__mainStack[-1]


if __name__ == "__main__":
    mins = Minstack()
    mins.push(18)
    mins.push(19)
    mins.push(29)
    print(mins.top(), mins.minElement())
    mins.push(15)
    print(mins.top(), mins.minElement())
    mins.push(16)
    print(mins.top(), mins.minElement())
    mins.pop()
    print(mins.top(), mins.minElement())
