import asyncio, time, pygame, sys

BG_COLOR = (40, 42, 54,)
GRID_COLOR = (68, 71, 90)
ALIVE_COLOR = (80, 250, 123)
SCREEN = pygame.display.set_mode((1200, 720))

pygame.init()
pygame.display.set_caption("Pylife")

def update(screen, cells, size, with_progress=False):
    updated_cells = [[0 for _ in range(len(cells[0]))] for _ in range(len(cells))]

    for row in range(len(cells)):
        for col in range(len(cells[0])):
            alive = 0
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if i >= 0 and i < len(cells) and j >= 0 and j < len(cells[0]) and (i != row or j != col):
                        alive += cells[i][j]
            color = ALIVE_COLOR if cells[row][col] else BG_COLOR

            if cells[row][col] == 1:
                if alive < 2 or alive > 3:
                    if with_progress:
                        color = BG_COLOR
                elif 2 <= alive <= 3:
                    updated_cells[row][col] = 1
                    if with_progress:
                        color = ALIVE_COLOR
            else:
                if alive == 3:
                    updated_cells[row][col] = 1
                    if with_progress:
                        color = ALIVE_COLOR

            pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


async def main():
    pygame.init()
    cells = [[0 for _ in range(120)] for _ in range(72)]
    SCREEN.fill(GRID_COLOR)
    update(SCREEN, cells, 20)

    pygame.display.flip()

    running = False  
    while True:
        for Q in pygame.event.get():
            if Q.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif Q.type == pygame.KEYDOWN:
                if Q.key == pygame.K_SPACE:
                    running = not running
                    update(SCREEN, cells, 20)
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 20][pos[0] // 20] = 1
                update(SCREEN, cells, 20)
                pygame.display.update()

        SCREEN.fill(GRID_COLOR)

        if running:
            cells = update(SCREEN, cells, 20, with_progress=True)
            pygame.display.update()

        time.sleep(0.1)
        await asyncio.sleep(0)

asyncio.run(main())