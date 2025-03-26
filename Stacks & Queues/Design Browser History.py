# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 

# Example:

# Input:
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
# Output:
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

# Explanation:
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
# browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
# browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
# browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
# browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
# browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
# browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"


from collections import deque


class BrowserHistory:

    def __init__(self, homepage: str):
        # backwardHistory will store all previously visited urls
        self.backwardHistory = deque()
        # forwardHistory will store current url at top and
        # future urls below it
        self.forwardHistory = deque([homepage])

    def visit(self, url: str) -> None:
        self.backwardHistory.append(self.forwardHistory.pop())
        self.forwardHistory.clear()
        self.forwardHistory.append(url)

    def back(self, steps: int) -> str:
        x = min(len(self.backwardHistory), steps)
        for _ in range(x):
            self.forwardHistory.append(self.backwardHistory.pop())
        return self.forwardHistory[-1]
    
    def forward(self, steps: int) -> str:
        x = min(len(self.forwardHistory) - 1, steps)
        for _ in range(x):
            self.backwardHistory.append(self.forwardHistory.pop())
        return self.forwardHistory[-1]
# Time Complexity: O(1)
# Space Complexity: O(N) 

# Another solution using list and two pointer approach
# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.history = [homepage]
#         self.curr = 0
#         self.bound = 0

#     def visit(self, url: str) -> None:
#         self.curr += 1
#         if self.curr == len(self.history):
#             self.history.append(url)
#         else:
#             self.history[self.curr] = url
#         self.bound = self.curr

#     def back(self, steps: int) -> str:
#         self.curr = max(self.curr - steps, 0)
#         return self.history[self.curr]

#     def forward(self, steps: int) -> str:
#         self.curr = min(self.curr + steps, self.bound)
#         return self.history[self.curr]



if __name__ == '__main__':
    browserHistory = BrowserHistory('leetcode.com')
    browserHistory.visit('google.com')
    browserHistory.visit('facebook.com')
    browserHistory.visit('youtube.com')
    print(browserHistory.back(1))
    print(browserHistory.back(1))
    print(browserHistory.forward(1))
    browserHistory.visit('linkedin.com')
    print(browserHistory.forward(2))
    print(browserHistory.back(2))
    print(browserHistory.back(7))
