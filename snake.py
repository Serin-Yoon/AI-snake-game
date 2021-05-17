import random, pygame, sys
from pygame.locals import *

FPS = 15
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20

CELL_WIDTH = WINDOW_WIDTH // CELL_SIZE
CELL_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

# 색상 RGB 설정
BLACK = (0, 0, 0)
BGCOLOR = (250, 243, 243)
GRIDCOLOR = (225, 229, 234)
SNAKECOLOR = (167, 187, 199)
FOODCOLOR = (218, 127, 143)
TITLECOLOR1 = (0, 97, 168)
TITLECOLOR2 = (41, 120, 181)
TITLECOLOR3 = (138, 182, 214)

# 방향키 설정
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# 뱀 머리 index
HEAD = 0

# 메인 함수
def main():
    global CLOCK # FPS 초당 프레임 변수
    global DISPLAY # 화면 해상도 (WIDTH * HEIGHT)
    global FONT # 글꼴

    pygame.init()
    CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    FONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('2021-1 Artificial Intelligence Project') # 타이틀 설정

    # 시작 화면
    showStart()

    while True:
        runGame()
        showGameOver()

# 게임 진행 함수
def runGame():
    # 시작 좌표 랜덤 설정
    startX = random.randint(5, CELL_WIDTH - 6)
    startY = random.randint(5, CELL_HEIGHT - 6)

    # 초기 뱀 길이 3
    snakeCoords = [
        {'x': startX, 'y': startY},
        {'x': startX - 1, 'y': startY},
        {'x': startX - 2, 'y': startY}
    ]

    # 초기 이동 방향 설정
    direction = RIGHT

    # 먹이 위치 랜덤 배치
    food = getRandomLocation()

    # 게임 실행
    while True:
        # 이벤트 핸들링
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # 뱀 머리 화면 모서리에 닿았는지 확인
        if snakeCoords[HEAD]['x'] == -1 or snakeCoords[HEAD]['x'] == CELL_WIDTH or snakeCoords[HEAD]['y'] == -1 or snakeCoords[HEAD]['y'] == CELL_HEIGHT:
            return

        # 뱀 머리 자기 자신 일부에 닿았는지 확인
        for snakeBody in snakeCoords[1:]:
            if snakeBody['x'] == snakeCoords[HEAD]['x'] and snakeBody['y'] == snakeCoords[HEAD]['y']:
                return

        # 뱀 머리가 먹이에 닿았는지 확인
        if snakeCoords[HEAD]['x'] == food['x'] and snakeCoords[HEAD]['y'] == food['y']:
            # 먹이 위치 랜덤 재배치
            food = getRandomLocation()
        else:
            # 닿지 않은 경우 뱀 길이가 늘어나는 걸 막고자 꼬리 삭제
            del snakeCoords[-1]

        # 방향 이동 설정
        if direction == UP:
            newHead = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': snakeCoords[HEAD]['x'] - 1, 'y': snakeCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': snakeCoords[HEAD]['x'] + 1, 'y': snakeCoords[HEAD]['y']}

        snakeCoords.insert(0, newHead)

        DISPLAY.fill(BGCOLOR) # 게임 배경 색상
        drawGrid() # 그리드 그리기
        drawSnake(snakeCoords) # 뱀 배치
        drawFood(food) # 음식 배치
        drawScore(len(snakeCoords) - 3) # 점수 배치 (뱀 초기 길이 3 빼줌)
        pygame.display.update()
        CLOCK.tick(FPS)

# 시작 안내 멘트 출력 함수
def drawPressKeyMsg():
    pressKeyMessage = FONT.render("Press ' ENTER ' to play!", True, BLACK)
    pressKeyRect = pressKeyMessage.get_rect()
    pressKeyRect.topleft = (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 30)
    DISPLAY.blit(pressKeyMessage, pressKeyRect)

# 키 입력 확인 함수
def checkKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvent = pygame.event.get(KEYUP)
    if len(keyUpEvent) == 0:
        return None
    if keyUpEvent[0].key == K_ESCAPE:
        terminate()

    return keyUpEvent[0].key

# 시작 화면 함수
def showStart():
    titleFont1 = pygame.font.SysFont("arial", 80, True, False)
    titleFont2 = pygame.font.SysFont("arial", 60, True, False)
    titleFont3 = pygame.font.SysFont("arial", 30, True, False)

    title1 = titleFont1.render('AI Snake', True, TITLECOLOR1)
    title2 = titleFont2.render('made with A* Algorithm', True, TITLECOLOR2)
    title3 = titleFont3.render('Computer Education 2019312616 Serin Yoon', True, TITLECOLOR3)

    titleRect = title1.get_rect()
    titleRect2 = title2.get_rect()
    titleRect3 = title3.get_rect()

    titleRect.centerx = round(WINDOW_WIDTH // 2)
    titleRect.y = 100

    titleRect2.centerx = round(WINDOW_WIDTH // 2)
    titleRect2.y = 200

    titleRect3.centerx = round(WINDOW_WIDTH // 2)
    titleRect3.y = 320

    while True:
        # 배경 색상 설정
        DISPLAY.fill(BGCOLOR)

        # 타이틀 출력
        DISPLAY.blit(title1, titleRect)
        DISPLAY.blit(title2, titleRect2)
        DISPLAY.blit(title3, titleRect3)

        # 시작 안내 멘트
        drawPressKeyMsg()

        if checkKeyPress():
            pygame.event.get()
            return

        pygame.display.update()
        CLOCK.tick(FPS)

# 게임 종료 함수
def terminate():
    pygame.quit()
    sys.exit()

# 랜덤 위치 출력 함수
def getRandomLocation():
    return {'x': random.randint(0, CELL_WIDTH - 1), 'y': random.randint(0, CELL_HEIGHT - 1)}

# 게임 종료 화면 출력 함수
def showGameOver():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 120)
    gameSurf = gameOverFont.render('Game', True, BLACK)
    overSurf = gameOverFont.render('Over', True, BLACK)

    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()

    gameRect.midtop = (WINDOW_WIDTH // 2, 110)
    overRect.midtop = (WINDOW_WIDTH // 2, 240)

    DISPLAY.blit(gameSurf, gameRect)
    DISPLAY.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkKeyPress() # clear out any key presses in the event queue

    while True:
        if checkKeyPress():
            pygame.event.get()
            return

# 점수 표시 함수
def drawScore(score):
    scoreSurf = FONT.render('Score: %s' % (score), True, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (10, 10)
    DISPLAY.blit(scoreSurf, scoreRect)

# 뱀 표시 함수
def drawSnake(snakeCoords):
    for coord in snakeCoords:
        x = coord['x'] * CELL_SIZE
        y = coord['y'] * CELL_SIZE
        snakeSegmentRect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(DISPLAY, SNAKECOLOR, snakeSegmentRect)
        snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELL_SIZE - 8, CELL_SIZE - 8)
        pygame.draw.rect(DISPLAY, SNAKECOLOR, snakeInnerSegmentRect)

# 먹이 표시 함수
def drawFood(coord):
    x = coord['x'] * CELL_SIZE
    y = coord['y'] * CELL_SIZE
    foodRect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(DISPLAY, FOODCOLOR, foodRect)

# 그리드 그리기 함수
def drawGrid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE): # draw vertical lines
        pygame.draw.line(DISPLAY, GRIDCOLOR, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE): # draw horizontal lines
        pygame.draw.line(DISPLAY, GRIDCOLOR, (0, y), (WINDOW_WIDTH, y))

if __name__ == '__main__':
    main()