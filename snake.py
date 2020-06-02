import pygame
import time
import random

# required function to initialize all framework basics
pygame.init()

# declaring color variables
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (102, 102, 255)

# window size variables
dis_width = 600
dis_height = 500

# initialize display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

# start clock
clock = pygame.time.Clock()
 
# snake variables
snake_block = 10
snake_speed = 10

# font style vars
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# score renderer and tracker
def player_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
# snake renderer 
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
# message renderer
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
# main game loop
def gameLoop():
    game_over = False
    game_close = False

    # variables for snake posiion, start at middle of screen
    x1 = dis_width / 2
    y1 = dis_height / 2

    # temp variables to track snake change
    x1_change = 0
    y1_change = 0

    # the snake list which tracks all the square positions and length tracker
    snake_List = []
    Length_of_snake = 1

    # food positions
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # constant game logic
    while not game_over:

        # game over logic
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            player_score(Length_of_snake - 1)
            pygame.display.update()

            # inputs
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        # input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # snake appending
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # checks if snake ran into itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # calls to renderer functions
        snake(snake_block, snake_List)
        player_score(Length_of_snake - 1)

        # updates display every frame
        pygame.display.update()

        # snake eats fruit
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
