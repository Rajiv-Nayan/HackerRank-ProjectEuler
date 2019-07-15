g, erg = [], []

for _ in range(20):
    g.append([int(grid_t) for grid_t in input().strip().split(' ')])
       
for y in range(20):
    for x in range(20):
        if x < 17:
            erg.append(g[y][x]*g[y][x+1]*g[y][x+2]*g[y][x+3])
        if y < 17:
            erg.append(g[y][x]*g[y+1][x]*g[y+2][x]*g[y+3][x])
        if x >= 3 and y < 17:
            erg.append(g[y][x]*g[y+1][x-1]*g[y+2][x-2]*g[y+3][x-3])
        if x < 17 and y < 17:
            erg.append(g[y][x]*g[y+1][x+1]*g[y+2][x+2]*g[y+3][x+3])
            
print(max(erg))
