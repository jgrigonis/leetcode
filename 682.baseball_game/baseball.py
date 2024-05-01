class Solution:
    def __init__(self):
        self.record = []
    def calPoints(self, operations: List[str]) -> int:
        for item in operations:
            if item == "+":
                self.record.append(int(self.record[-2]) + int(self.record[-1]))
            elif item == "C":
                self.record.pop()
            elif item == "D":
                self.record.append(int(self.record[-1]) * 2)
            else:
                self.record.append(int(item))
        return sum(self.record)
