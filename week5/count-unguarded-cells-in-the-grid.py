class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [["" for j in range(n)] for i in range(m)] 
        for guard in guards:
            grid[guard[0]][guard[1]] = "G"
        for wall in walls:
            grid[wall[0]][wall[1]] = "W"
        cnt = 0
        for guard in guards:
            a,b = guard
            a+=1
            while a < m and b < n and grid[a][b] != "W" and grid[a][b] != "G":
                print(a,b)
                if grid[a][b] != "O":
                    cnt += 1
                grid[a][b] = "O"
                a += 1
            a,b = guard
            b+= 1
            while a < m and b < n and grid[a][b] != "W" and grid[a][b] != "G":
                if grid[a][b] != "O":
                    cnt += 1
                grid[a][b] = "O"
                b += 1
            a,b = guard
            a-=1
            while a >= 0 and b >= 0 and grid[a][b] != "W" and grid[a][b] != "G":
                if grid[a][b] != "O":
                    cnt += 1
                grid[a][b] = "O"
                a -= 1
            a,b = guard
            b-=1
            while a >= 0 and b >= 0 and grid[a][b] != "W" and grid[a][b] != "G":
                if grid[a][b] != "O":
                    cnt += 1
                grid[a][b] = "O"
                b -= 1
        print(grid)
        return n*m - cnt - len(guards) - len(walls)