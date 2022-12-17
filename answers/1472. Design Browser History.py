class BrowserHistory:
    """
    1472. Design Browser History
    """

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        """
        len   1 2 3
        index 0 1 2
        """

        while self.index + 1 < len(self.history):  # 2 < 2
            self.history.pop()

        self.history.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        """
        index 1 1
        steps 1 2
        result 0 0
        """
        self.index = max(0, self.index - steps)
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        """
        len 3
        index 1
        steps 3
        result 2 0
        """
        self.index = min(len(self.history) - 1, self.index + steps)  # 2  4
        return self.history[self.index]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)