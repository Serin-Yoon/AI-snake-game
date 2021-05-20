import pygame
import sys
import random
from pygame.locals import *
from snakeAI import *

# 색상 RGB 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
SNAKECOLOR = (167, 187, 199)
HEADCOLOR = (41, 120, 181)
FOODCOLOR = (218, 127, 143)
BGCOLOR = (225, 229, 234)
SCREENCOLOR = (250, 243, 243)

FPS = 100

WINDOW_WIDTH = 520
WINDOW_HEIGHT = 600
SCREEN_SIZE = 500

GRID_SIZE = 20
GRID_WIDTH = SCREEN_SIZE // GRID_SIZE
GRID_HEIGHT = SCREEN_SIZE // GRID_SIZE

MARGIN = 10
TOP_MARGIN = 90

# 뱀 클래스
class Snake(object):
    def __init__(self):
        self.color = SNAKECOLOR
        self.create()

    # 뱀 생성
    def create(self):
        self.length = 2 # 초기 뱀 길이 2
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT]) # 초기 방향 랜덤 설정
        self.coords = [(SCREEN_SIZE // 2, SCREEN_SIZE // 2 + TOP_MARGIN - 10)]

    def control(self, direction):
        if (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        else:
            self.direction = direction

    # 뱀 이동 설정
    def move(self):
        cur = self.coords[0]
        x, y = self.direction

        new = (((cur[0] - MARGIN) + (x * GRID_SIZE)) % SCREEN_SIZE,
               ((cur[1] - TOP_MARGIN) + (y * GRID_SIZE)) % SCREEN_SIZE)
        new = (new[0] + MARGIN, new[1] + TOP_MARGIN)

        self.coords.insert(0, new)

        if len(self.coords) > self.length:
            self.coords.pop()

        if new in self.coords[1:]:
            return False

        return True

    # 뱀 그리드 배치
    def draw(self):
        head = self.coords[0]
        for c in self.coords:
            drawRect(c[0] + 1, c[1] + 1, GRID_SIZE - 1, GRID_SIZE - 1, self.color)

        drawRect(c[0] + 1, c[1] + 1, GRID_SIZE - 1, GRID_SIZE - 1, SNAKECOLOR)
        drawRect(head[0] - 1, head[1], GRID_SIZE -  1, GRID_SIZE - 1, HEADCOLOR)

    # 뱀 먹이 먹었을 시
    def eat(self):
        self.length += 1


class Feed(object):
    def __init__(self):
        self.color = FOODCOLOR
        self.create()

    def create(self):
        self.coord = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE + MARGIN,
                      random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE + TOP_MARGIN)

    def draw(self):
        drawRect(self.coord[0], self.coord[1], GRID_SIZE, GRID_SIZE, self.color)


def main():
    global CLOCK # FPS 초당 프레임 변수
    global DISPLAY # 화면

    snake = Snake()
    feed = Feed()

    pygame.init()

    CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    DISPLAY.fill(BGCOLOR)
    pygame.display.set_caption('2021-1 Artificial Intelligence Project')
    pygame.display.flip()

    while True:
        runGame(snake, feed)
        gameOver()

# 게임 진행 함수
def runGame(snake, feed):

    screenRect, screenSurf = drawRect(MARGIN, TOP_MARGIN, SCREEN_SIZE, SCREEN_SIZE, SCREENCOLOR)
    infoRect, infoSurf = drawRect(MARGIN, MARGIN, SCREEN_SIZE, TOP_MARGIN - 20)

    path = None
    keys = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
    sa = SnakeAI(snake.direction)

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                terminate()
            if e.type == KEYDOWN:
                if e.key in keys:
                    execEvent(snake, e.key)

        path = sa.getNextDirection(snake.coords, feed.coord)
        if path >= 0:
            execEvent(snake, keys[path])

        if not snake.move():
            snake.draw()
            return

        renderRect(screenSurf, screenRect, SCREENCOLOR)
        renderRect(infoSurf, infoRect, BGCOLOR)

        eatCheck(snake, feed, sa)
        drawGrid()
        showTitle()
        showGameInfo(snake.length)

        pygame.display.update(screenRect)
        pygame.display.update(infoRect)

        CLOCK.tick(FPS)

# 먹이 먹었는지 확인하는 함수
def eatCheck(snake, feed, sa):
    snake.draw()
    feed.draw()

    if snake.coords[0] == feed.coord:
        snake.eat()

        while True:
            feed.create()
            if feed.coord not in snake.coords:
                break
    return

# 방향키 인식 함수
def execEvent(snake, key):
    event = {K_UP: UP, K_DOWN: DOWN, K_LEFT: LEFT, K_RIGHT: RIGHT}
    snake.control(event[key])

# 게임 종료 함수
def terminate():
    pygame.quit()
    sys.exit()

def renderRect(surf, rect, color):
    surf.fill(color)
    DISPLAY.blit(surf, rect)

def drawRect(left, top, width, height, color=BLACK):
    surf = pygame.Surface((width, height))
    rect = pygame.Rect(left, top, width, height)
    renderRect(surf, rect, color)
    return (rect, surf)

# 글씨 띄우기 함수
def makeText(font, text, color, bgcolor, x, y):
    surf = font.render(text, True, color, bgcolor)
    rect = surf.get_rect()
    rect.center = (x, y)
    DISPLAY.blit(surf, rect)
    return rect

# 타이틀 띄우기 함수
def showTitle():
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = ('AI Snake made with A* Algorithm')
    x = (MARGIN + SCREEN_SIZE) // 2
    y = 35
    return makeText(font, text, BLACK, BGCOLOR, x, y)

# 점수 띄우기 함수
def showGameInfo(length):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = ("Score: " + str(length - 2))
    x = (MARGIN + SCREEN_SIZE) // 2
    y = 70
    return makeText(font, text, BLACK, BGCOLOR, x, y)

# 그리드 그리기 함수
def drawGrid():
    for x in range(MARGIN + GRID_SIZE, WINDOW_WIDTH - MARGIN, GRID_SIZE):
        pygame.draw.line(DISPLAY, BGCOLOR, (x, TOP_MARGIN), (x, 600))
    for y in range(TOP_MARGIN, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(DISPLAY, BGCOLOR, (0, y), (600, y))

# 게임 종료 안내 함수
def gameOver():
    font = pygame.font.Font('freesansbold.ttf', 100)

    x = (SCREEN_SIZE // 2) + MARGIN
    y = (WINDOW_HEIGHT // 2) - 30
    makeText(font, 'Game', GRAY, None, x, y)

    y = (WINDOW_HEIGHT // 2) + 80
    makeText(font, 'Over', GRAY, None, x, y)

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                terminate()
        CLOCK.tick(FPS)


if __name__ == '__main__':
    main()
