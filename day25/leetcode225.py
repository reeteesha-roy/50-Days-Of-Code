from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Main queue where the top of the stack is always at the front
        self.q2 = deque()  # Temp queue for juggling during push

    def push(self, x):
        # Step 1: Push to q2
        self.q2.append(x)
        # Step 2: Move everything from q1 to q2 so the new element is in front
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Step 3: Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        # Since q1 has the most recent at front, just pop
        if self.empty():
            return None
        return self.q1.popleft()

    def top(self):
        if self.empty():
            return None
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0
