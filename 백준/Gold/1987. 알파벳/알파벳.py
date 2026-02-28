import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]

states = set()
start = (0, 0, 1 << (ord(board[0][0]) - 65))
states.add(start)

ans = 1

while states:
    new_states = set()
    for r, c, bitmask in states:
        ans = max(ans, bitmask.bit_count())
        
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C:
                idx = ord(board[nr][nc]) - 65
                if not (bitmask & (1 << idx)):
                    new_states.add((nr, nc, bitmask | (1 << idx)))
    
    states = new_states

print(ans)