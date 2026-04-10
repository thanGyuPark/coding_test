def solution(maps):
    map_arr = []
    n = len(maps)
    cols = len(maps[0])
    
    lever = [0,0]
    exit = [0,0]
    start = [0,0]
    for i,m in enumerate(maps):
        map = list(m)
        if 'S' in map:
            start = [i, map.index('S')]
        if 'L' in map:
            lever = [i, map.index('L')]
        if 'E' in map:
            exit = [i, map.index('E')]
        map_arr.append(map)
    
    time_arr = []
    for i in range(n):
        time_arr.append([float("inf")]*cols)
    
    dir = [[0,1],[0,-1],[1,0],[-1,0]]
    time_arr[start[0]][start[1]] = 0
    queue = [start]
    while queue:
        cur = queue.pop(0)
        if cur == lever:
            break
        for d in dir:
            nr, nc = cur[0]+d[0], cur[1]+d[1]
            if nr < 0 or nc < 0 or nr >= n or nc >= cols:
                continue
            if map_arr[nr][nc] == 'X':
                continue
            if time_arr[nr][nc] != float("inf"):  # 이미 방문
                continue
            time = time_arr[cur[0]][cur[1]] + 1
            if time == float('inf'): time=1
            time_arr[nr][nc] = time
            queue.append([nr, nc])
            
    print(time_arr)
    if time_arr[lever[0]][lever[1]] == float('inf'): return - 1
    
    time_arr2 = [[float("inf")] * cols for _ in range(n)]
    time_arr2[lever[0]][lever[1]] = 0
    queue = [lever]
    while queue:
        cur = queue.pop(0)
        if cur == exit:
            break
        for d in dir:
            nr, nc = cur[0]+d[0], cur[1]+d[1]
            if nr < 0 or nc < 0 or nr >= n or nc >= cols:
                continue
            if map_arr[nr][nc] == 'X':
                continue
            time = time_arr2[cur[0]][cur[1]] + 1
            if time_arr2[nr][nc] != float("inf"):  # 이미 방문
                continue
            if time == float('inf'): time=1
            time_arr2[nr][nc] = time
            queue.append([nr, nc])
            
    if time_arr2[exit[0]][exit[1]] == float('inf'): return -1
    return time_arr[lever[0]][lever[1]] + time_arr2[exit[0]][exit[1]]

# 각 칸은 통로 또는 벽으로 구성
# 벽은 지나갈 수 없음
# 통로중 한 칸에는 출구가 있는데, 레버를 당겨야만 열 수 있음
# 출발지점 -> 레버 -> 출구 이렇게 가는 최소 시간
# 만약 탈출할 수 없다면 -1 반환

# bfs를 통해 레버까지 최단시간 구하기
# bfs를 통해 레버에서 출구까지 최단시간 구하기
# 두 값을 더해줌