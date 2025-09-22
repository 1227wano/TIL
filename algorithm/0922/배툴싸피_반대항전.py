import sys
import socket
from collections import deque

##############################
# 메인 프로그램 통신 변수 정의
##############################
HOST = '127.0.0.1'
PORT = 8747
ARGS = sys.argv[1] if len(sys.argv) > 1 else ''
sock = socket.socket()

##############################
# 메인 프로그램 통신 함수 정의
##############################

# 메인 프로그램 연결 및 초기화
def init(nickname):
    try:
        print(f'[STATUS] Trying to connect to {HOST}:{PORT}...')
        sock.connect((HOST, PORT))
        print('[STATUS] Connected')
        init_command = f'INIT {nickname}'

        return submit(init_command)

    except Exception as e:
        print('[ERROR] Failed to connect. Please check if the main program is waiting for connection.')
        print(e)

# 메인 프로그램으로 데이터(명령어) 전송
def submit(string_to_send):
    try:
        send_data = ARGS + string_to_send + ' '
        sock.send(send_data.encode('utf-8'))

        return receive()
        
    except Exception as e:
        print('[ERROR] Failed to send data. Please check if connection to the main program is valid.')

    return None

# 메인 프로그램으로부터 데이터 수신
def receive():
    try:
        game_data = (sock.recv(1024)).decode()

        if game_data and game_data[0].isdigit() and int(game_data[0]) > 0:
            return game_data

        print('[STATUS] No receive data from the main program.')    
        close()

    except Exception as e:
        print('[ERROR] Failed to receive data. Please check if connection to the main program is valid.')

# 연결 해제
def close():
    try:
        if sock is not None:
            sock.close()
        print('[STATUS] Connection closed')
    
    except Exception as e:
        print('[ERROR] Network connection has been corrupted.')

##############################
# 입력 데이터 변수 정의
##############################
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
my_allies = {}  # 아군 정보. 예) my_allies['M'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문

##############################
# 입력 데이터 파싱
##############################

# 입력 데이터를 파싱하여 각각의 리스트/딕셔너리에 저장
def parse_data(game_data):
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0]) if len(header) >= 1 else 0 # 맵의 세로 크기
    map_width = int(header[1]) if len(header) >= 2 else 0  # 맵의 가로 크기
    num_of_allies = int(header[2]) if len(header) >= 3 else 0  # 아군의 수
    num_of_enemies = int(header[3]) if len(header) >= 4 else 0  # 적군의 수
    num_of_codes = int(header[4]) if len(header) >= 5 else 0  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, len(col)):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    my_allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0) if len(ally) >= 1 else '-'
        my_allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0) if len(enemy) >= 1 else '-'
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

# 파싱한 데이터를 화면에 출력
def print_data():
    print(f'\n----------입력 데이터----------\n{game_data}\n----------------------------')

    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()

    print(f'\n[아군 정보] (아군 수: {len(my_allies)})')
    for k, v in my_allies.items():
        if k == 'M':
            print(f'M (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 메가 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(enemies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'X (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])

##############################
# 닉네임 설정 및 최초 연결
##############################
NICKNAME = '서울3_채완호'
game_data = init(NICKNAME)

###################################
# 알고리즘 함수/메서드 부분 구현 시작
###################################

# 출발지와 목적지의 위치 찾기
def find_positions(grid, start_mark, goal_mark):
    # 델타 순회하며 사격 가능한 지역 탐색(최대 사거리에서 쏠 수 있도록)
    rows, cols = len(grid), len(grid[0])
    start = goal = None
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == start_mark:
                start = (row, col)

            elif grid[row][col] == goal_mark:
                goal = (row, col)
    find_shoting_area(grid, goal)
    return start, goal

def find_shoting_area(grid, target):
    for k in range(4):
        flag = True
        for r in range(1, 4):
            if flag is False:
                break
            ni = target[0] + (DIRS[k][0] * r)
            nj = target[1] + (DIRS[k][1] * r)
            if 0 <= ni < len(grid) and 0 <= nj < len(grid) and grid[ni][nj] == "G": # 사격 가능한 위치라면
                m_cnt = 0
                n_cnt = 0
                for kk, v in my_allies.items():
                    if kk == 'M':
                        m_cnt = int(v[3])
                        n_cnt = int(v[2])
                if n_cnt > 0:
                    grid[ni][nj] = ["ST", FIRE_CMDS[(k + 2) % 4]]
                else:
                    grid[ni][nj] = ["ST", FIRE_CMDS_M[(k + 2) % 4]]
            elif 0 <= ni < len(grid) and 0 <= nj < len(grid) and grid[ni][nj] == "W":
                continue
            else:
                flag = False
                break


# 경로 탐색 변수 정의
start_num = 1
code_fix = True
get_shell_flag = True
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
FIRE_CMDS_M = {0: "R F M", 1: "D F M", 2: "L F M", 3: "U F M"}
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'
WALL_SYMBOL = 'R'
ENEMY = ['E1', 'E2', 'E3']  # 완호: 적 리스트 추가

# 최초 데이터 파싱
parse_data(game_data)

# 출발지점, 목표지점의 위치 확인
start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)
if not start or not target:
    print("[ERROR] Start or target not found in map")
    close()
    exit()

# 최초 경로 탐색

def find_f(grid):
    result_list = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "F":
                result_list.append((i, j))
def get_data():
    m_tank_data = {}
    for k, v in my_allies.items():
        if k == 'M':
            m_tank_data.update({"M":[v[0], v[1], v[2], v[3]]})
    e_tank_data = {}
    for k, v in enemies.items():
        e_tank_data.update({f"{k}":[v[0]]})
    return m_tank_data, e_tank_data

def bfs(grid, start, target, wall):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [], 0)])
    visited = {start}
    m_cnt = 0
    n_cnt = 0
    for kk, v in my_allies.items():
        if kk == 'M':
            m_cnt = int(v[3])
            n_cnt = int(v[2])
    answer_list = []
    while queue:
        (r, c), actions, t = queue.popleft()

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and len(grid[nr][nc]) == 2:
                # 사격 가능한 지역인 ST에 도달하면 해당 경로 반환
                answer_list.append([t, actions + [MOVE_CMDS[d]] + [grid[nr][nc][1]]])

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != wall and grid[nr][nc] != "W" and grid[nr][nc] != "F" and (nr, nc) not in visited:
                if grid[nr][nc] == "T":
                    visited.add((nr, nc))
                    # 포탄 선택 알고리즘. 메가 포탄 우선해서 사용
                    if m_cnt > 0:
                        queue.append(((nr, nc), actions + [FIRE_CMDS_M[d]] + [MOVE_CMDS[d]], t + 2))
                    else:
                        queue.append(((nr, nc), actions + [FIRE_CMDS[d]] + [MOVE_CMDS[d]], t + 2))
                else:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), actions + [MOVE_CMDS[d]], t + 1))           
    # 거리 기준으로 가장 가까운 경로 선택(사격도 1개 턴에 포함)
    answer_list.sort()
    # 답이 없으면 빈 리스트
    if len(answer_list) == 0:
        return []
    else:
        # 답이 있으면 가장 짧은 거리의 리스트 반환
        return answer_list[0][1]

def bfs_for_f(si, sj, grid):
    my_queue = deque([(si, sj, [])]) # 시작위치, 경로, 경로, 방해물 수
    visited = [[False] * len(grid) for _ in range(len(grid))]
    while len(my_queue) != 0:
        i, j, path = my_queue.popleft()
        for k in range(4):
            ni = i + DIRS[k][0]
            nj = j + DIRS[k][1]
            if 0 <= ni < len(grid) and 0 <= nj < len(grid) and grid[ni][nj] != "R" and grid[ni][nj] != "W" and grid[ni][nj] != "T" and visited[ni][nj] and grid[ni][nj] != "M1" and grid[ni][nj] != "M2" and grid[ni][nj] != "M3" is False:
                # 물, 바위, 나무, 영역 안벗어나고, 방문한거 아니라면
                if grid[ni][nj] == "F": # 창고에 도달하는거라면
                    return path
                else:
                    my_queue.append((ni, nj, path + [MOVE_CMDS[k]]))

def find_my_p(grid, start_mark):
    # 델타 순회하며 사격 가능한 지역 탐색(최대 사거리에서 쏠 수 있도록)
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == start_mark:
                return row, col
            
def find_a(mi, mj, grid):
    for k in range(4):
        ni = mi + DIRS[k][0]
        nj = mj + DIRS[k][1]
        if 0 <= ni < len(grid) and 0 <= nj < len(grid) and grid[ni][nj] in e_list:
            m_cnt = 0
            n_cnt = 0
            for kk, v in my_allies.items():
                if kk == 'M':
                    m_cnt = int(v[3])
                    n_cnt = int(v[2])
            if m_cnt > 0:
                return True, [FIRE_CMDS_M[(k + 2) % 4]]
            elif n_cnt > 0:
                return True, [FIRE_CMDS[(k + 2) % 4]]
    return False, []
            
def find_positions(grid, start_mark, goal_mark, enemy):
    # 델타 순회하며 사격 가능한 지역 탐색(최대 사거리에서 쏠 수 있도록)
    rows, cols = len(grid), len(grid[0])
    start = goal = None

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == start_mark:
                start = (row, col)
            elif grid[row][col] == goal_mark:       # 완호: 포탑부터 goal로 지정
                goal = (row, col)
                
                
    find_shoting_area(grid, goal)

    return start, goal
# DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
# MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
# FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
# FIRE_CMDS_M = {0: "R F M", 1: "D F M", 2: "L F M", 3: "U F M"}




###################################
# 알고리즘 함수/메서드 부분 구현 끝
###################################

# 반복문: 메인 프로그램 <-> 클라이언트(이 코드) 간 순차로 데이터 송수신(동기 처리)
while game_data is not None:
    ##############################
    # 알고리즘 메인 부분 구현 시작
    ##############################
    shot_flag = False
    e_list = ["E1", "E2", "E3","X"]

    mi, mj = find_my_p(map_data, "M")
    m_tank, e_data = get_data()
    shot_flag, shot_action = find_a(mi, mj, map_data)
    # 4방향 사주경계 후 쏠 것이 있으면 쏴
    if shot_flag is True:
        actions = shot_action

    if get_shell_flag is True and shot_flag is False:
        actions = bfs_for_f(mi, mj, map_data)
        if len(codes) == 1 and code_fix is True:
            result = []
            for s_chr in codes[0]:
                result.append(chr(ord("A") + ((ord(s_chr) + 22)) % 26))
            word = "G " + "".join(map(str, result))
            actions.append(word)
    elif shot_flag is False:
        start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL, ENEMY)
        actions = bfs(map_data, start, target, WALL_SYMBOL) if start and target else []
        pass

    # 필수 부분
    output = actions.pop(0) if actions else 'A'
    game_data = submit(output)
    last_cnt = int(m_tank["M"][2]) + int(m_tank["M"][3])
    # submit()의 리턴으로 받은 갱신된 데이터를 다시 파싱
    if game_data:
        parse_data(game_data)
    m_tank, e_data = get_data()
    print("현재 포탑 수:", int(m_tank['M'][2]) + int(m_tank['M'][3]))
    if int(m_tank['M'][2]) + int(m_tank['M'][3]) > 105:
        get_shell_flag = False

    ##############################
    # 알고리즘 메인 구현 끝
    ##############################

# 반복문을 빠져나왔을 때 메인 프로그램과의 연결을 완전히 해제하기 위해 close() 호출
close()