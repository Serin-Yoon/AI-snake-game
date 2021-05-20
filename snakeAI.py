import heapq

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Node(object):
    def __init__(self, board, coords, nodeID, parent, f, g, head, direction):
        self.board = board
        self.coords = coords
        self.f = f
        self.g = g
        self.head = head
        self.info = {'id': nodeID, 'parent': parent, 'direction': direction}

    def __lt__(self, other):
        if self.f == other.f:
            return self.g > other.g
        else:
            return self.f < other.f

    def __eq__(self, other):
        if not other:
            return False
        if not isinstance(other, Node):
            return False
        return self.f == other.f

# A* Algorithm 적용한 인공지능
class SnakeAI(object):
    def __init__(self, direction):
        self.coords = [] # 뱀 몸통 데이터
        self.path = None
        self.nodeID = 0
        self.direction = self.getDirection(direction) # 뱀 이동 방향 데이터
        self.board = self.getBoard() # 절대 좌표

    # pixel 좌표 => 절대 좌표 변환 함수
    def getBoard(self):
        board = [[0 for x in range(27)] for y in range(27)]
        for i in range(27):
            board[0][i] = board[26][i] = board[i][0] = board[i][26] = 2
        return board

    def getXY(self, coord):
        x = (coord[0] - 10) // 20 + 1
        y = (coord[1] - 90) // 20 + 1
        return x, y

    # 뱀 이동 방향 데이터 함수
    def getDirection(self, direction):
        move = [UP, DOWN, LEFT, RIGHT]
        return move.index(direction)

    # 보드 초기화 함수
    def clearBoard(self):
        for x in range(1, len(self.board) - 1, 1):
            for y in range(1, len(self.board[0]) - 1, 1):
                self.board[y][x] = 0

    # 보드 상에 뱀 좌표, 먹이 절대 좌표 표시
    def denoteXY(self, coords, coord):
        self.coords.clear()
        x, y = self.getXY(coord)
        self.goal = x, y
        self.board[y][x] = 1
        self.head = self.getXY(coords[0])

        for coord in coords:
            x, y = self.getXY(coord)
            self.coords.append((x, y))
            self.board[y][x] = 2

    # 이동 방향 데이터 요구 함수
    def getNextDirection(self, coords, coord):
        if not self.path:
            self.findPath(coords, coord)
        if self.path:
            return self.path.pop()
        else:
            return -1

    # Node 생성 시 필요한 coords 데이터 복사 함수
    def copyCoords(self, coords):
        coordies = []

        for coord in coords:
            coordies.append(coord)

        return coordies

    # Node 생성 시 필요한 board 데이터 복사 함수
    def copyBoard(self, coords):
        board = self.getBoard()

        for coord in coords:
            x, y = coord
            board[y][x] = 2
        x, y = self.goal
        board[y][x] = 1

        return board

    # 뱀 머리 노드 - 먹이 노드 거리 계산 함수
    def getHeuristic(self, x, y):
        x1, y1 = self.goal
        return (abs(x - x1) + abs(y - y1))

    # 경로 추적 함수
    def findPath(self, coords, coord):
        self.clearBoard()
        self.denoteXY(coords, coord)
        self.path = self.aStar()

    # A* Algorithm 구현 함수
    """
    뱀 머리 좌표, 몸통 좌표로 노드 생성하고 확장해나감
    확장된 노드 => open 힙큐에 삽입 (자동 오름차순 정렬)
    노드 하나씩 꺼내 먹이 노드에 도달했는지 확인하고
    도달하지 못한 경우 경로 추적 위해 close 리스트에 삽입, 노드 확장
    """
    def aStar(self):
        # h (확정된 가중치로부터 목표까지의 추정 가중치) g (시작 노드로부터 확정된 가정치)
        h = self.getHeuristic(self.head[0], self.head[1])
        g = 0
        node = Node(self.board, self.coords, 0, 0, h, g, self.coords[0], self.direction)
        open = []
        close = []
        self.expandNode(open, node)

        while open:
            node = heapq.heappop(open)

            # 먹이 위치가 뱀 몸통에 가려져 있는 경우 핸들링
            if g < node.g:
                g = node.g
            if g - node.g > 1:
                continue

            if node.head == self.goal:
                return self.makePath(close, node.info)

            close.append(node.info)
            self.expandNode(open, node)

        if close:
            path = [close[0]['direction']]
            return path

        return

    # 뱀 몸통이 구부러져 공간이 있는 경우 경로 추적 함수
    # (공간이 2칸 이상이면 들어갔다 나올 수 있으므로 방문 가능)
    def isHole(self, x, y, direction, board):
        if y - 1 >= 0 and direction > 1:
            if x == 25 and board[y - 1][x] == 2:
                return 10

        if y + 1 < 27 and direction > 1:
            if board[y + 1][x] == 2 and x == 1:
                return 10

        if y + 1 < 27 and y - 1 >= 0 and direction > 1:
            if board[y + 1][x] == 2 and board[y - 1][x] == 2:
                return 10
            if (board[y + 1][x] == 2 or board[y - 1][x] == 2):
                return 0

        if x - 1 >= 0 and direction < 2:
            if y == 25 and board[y][x - 1] == 2:
                return 10

        if x + 1 < 27 and direction < 2:
            if board[y][x + 1] == 2 and y == 1:
                return 10

        if x + 1 < 27 and x - 1 >= 0 and direction < 2:
            if board[y][x + 1] == 2 and board[y][x - 1] == 2:
                return 10
            if (board[y][x + 1] == 2 or board[y][x - 1] == 2):
                return 0

        return 3

    # 노드 확장 함수
    def expandNode(self, open, nodes):
        moves = [UP, DOWN, LEFT, RIGHT]
        x, y = nodes.head

        for i in range(4):
            dx, dy = moves[i]
            x1 = x + dx
            y1 = y + dy
            if nodes.board[y1][x1] < 2:
                coords = self.copyCoords(nodes.coords)
                head = (x1, y1)
                coords.insert(0, head)
                coords.pop()
                board = self.copyBoard(coords)
                h = self.getHeuristic(x1, y1)
                if h > 0:
                    h1 = self.isHole(x1, y1, i, board)
                    h += h1
                g = nodes.g + 1
                self.nodeID += 1
                id = self.nodeID
                parent = nodes.info['id']
                node = Node(board, coords, id, parent, g + h, g, head, i)
                heapq.heappush(open, node)

    # 먹이 노드 도달 시 경로 추적 함수
    def makePath(self, closed, information):
        path = [information['direction']]

        while closed:
            info = closed.pop()
            if info['id'] == information['parent']:
                path.append(info['direction'])
                information = info

        return path