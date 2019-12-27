from typing import List


class Solution(object):
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def visit(pos_i, pos_j, now_idx):
            if 0 <= pos_j < n and 0 <= pos_i < m and not visited[pos_i][pos_j] and board[pos_i][pos_j] == word[now_idx]:
                visited[pos_i][pos_j] = True
                if search(pos_i, pos_j, now_idx + 1):
                    return True
                visited[pos_i][pos_j] = False

        def search(pos_i=0, pos_j=0, now_idx=0):
            if now_idx == 0:
                for i in range(m):
                    for j in range(n):
                        if board[i][j] == word[now_idx]:
                            visited[i][j] = True
                            if search(i, j, now_idx + 1):
                                return True
                            visited[i][j] = False
            elif now_idx == len(word):
                return True
            else:
                if visit(pos_i, pos_j + 1, now_idx) or visit(pos_i, pos_j - 1, now_idx) or \
                        visit(pos_i + 1, pos_j, now_idx) or visit(pos_i - 1, pos_j, now_idx):
                    return True
            return False

        return search()


if __name__ == '__main__':
    print(
        Solution().exist([
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ], "ABCB")
    )
