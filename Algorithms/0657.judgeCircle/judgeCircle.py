class Solution(object):
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for i in range(0, len(moves)):
            if moves[i] == "R":
                x -= 1
            elif moves[i] == "L":
                x += 1
            elif moves[i] == "U":
                y += 1
            elif moves[i] == "D":
                y -= 1
        if x == 0 and y == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(
        Solution().judgeCircle(
            "LR"
        )
    )
