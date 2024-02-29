class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def possibleMoves(i: int,j: int) -> List[List[int]]:
            moves = []
            if len(board) == 1:
                if j == 0:
                    moves.extend([[i,j+1]])
                elif j<len(board[0])-1 and j>0:
                    moves.extend([[i,j-1],[i,j+1]])
                elif j == len(board[0])-1:
                    moves.extend([[i,j-1]])
            elif len(board[0]) == 1:
                if i == 0:
                    moves.extend([[i+1,j]])
                elif i<len(board[0])-1 and i>0:
                    moves.extend([[i-1,j],[i+1,j]])
                elif i == len(board[0])-1:
                    moves.extend([[i-1,j]])
            else:
                if i>0 and j>0 and i<len(board)-1 and j<len(board[0])-1:
                    moves.extend([[i-1,j],[i+1,j],[i,j-1],[i,j+1]])
                elif i==0 and j==0:
                    moves.extend([[i+1,j],[i,j+1]])
                elif i==len(board)-1 and j==len(board[0])-1:
                    moves.extend([[i-1,j],[i,j-1]])
                elif i==0 and j==len(board[0])-1:
                    moves.extend([[i,j-1],[i+1,j]])
                elif j==0 and i==len(board)-1:
                    moves.extend([[i,j+1],[i-1,j]])
                elif j==0 and i<len(board)-1 and i>0:
                    moves.extend([[i-1,j],[i+1,j],[i,j+1]])
                elif j==len(board[0])-1 and i<len(board)-1 and i>0:
                    moves.extend([[i-1,j],[i+1,j],[i,j-1]])
                elif i==0 and j<len(board[0])-1 and j>0:
                    moves.extend([[i,j-1],[i+1,j],[i,j+1]])
                elif i==len(board)-1 and j<len(board[0])-1 and j>0:
                    moves.extend([[i,j-1],[i-1,j],[i,j+1]])
            return moves
        rows = len(board)
        cols = len(board[0])
            
        if rows*cols < len(word):
            return False
        chars = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                chars[board[i][j]] += 1
        for i in word:
            if not i in chars:
                return False


        def backtrack(visited,x,y):
            if len(visited) == len(word):
                tmp = []
                for i in visited:
                    tmp.append(board[i[0]][i[1]])
                if "".join(tmp) == word:
                    return True
            if word[len(visited)-1] != board[visited[-1][0]][visited[-1][1]]:
                    return
            moves = possibleMoves(x,y)
            for i in range(len(moves)):
                if moves[i] in visited:
                    continue
                
                visited.append(moves[i])
                cur = backtrack(visited,moves[i][0],moves[i][1])
                if cur:
                    return True
                visited.pop()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack([[i,j]],i,j):
                        return True
        return False

