import pygame, random, math

pygame.init()

backgroundColor = 0, 255, 50
running = True
start = True
margin = 2
rect_width = 50
rect_height = 50
num = 10
width, height = ((rect_width + margin) * num) + margin, ((rect_height + margin) * num) + margin
screen = pygame.display.set_mode((width, height))
start_screen = pygame.image.load('start_screen_with_farmer.png')
main_char = pygame.image.load('character_front.jpg')
main_char = pygame.transform.scale(main_char, (45, 45)) #smaller than the actual box so you can see the color of the block you're on
main_char_rect = main_char.get_rect()
main_char_rect.centerx = margin + (rect_width / 2)
main_char_rect.centery = margin + (rect_height / 2)
pressed = 0
grid = []
timestamp = []
score = 0
Crops = ['1. Peas', '2. Carrots', '3. Tomatoes', '4. Potatoes'] 
special_crop = 0 #just an initialization which will be replaced with the real value quickly
start_time = 30
frame_count = 0
#crop sprites
dirt_sprite = pygame.image.load('dirt.jpeg')
potato_sprite = pygame.image.load('potato.png')
tomato_sprite = pygame.image.load('tomato.png')
carrot_sprite = pygame.image.load('carrot.png')
peas_sprite = pygame.image.load('peas.png')
harvest_sprite = pygame.image.load('harvest.png')


clock = pygame.time.Clock()# Clock initialization
#fonts
font_start_game = pygame.font.Font(None, 40)
font_in_game = pygame.font.Font(None, 25)
font_end_game = pygame.font.Font(None, 40)

timestamp_crop_demand = 10

for row in range(num):
    grid.append([])
    timestamp.append([])
    for column in range(num):
        grid[row].append([0,0])
        timestamp[row].append([])

#start screen
while start:
    key_in = pygame.key.get_pressed()
    screen.blit(start_screen, (0,0))
    
    if key_in[pygame.K_ESCAPE]:
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    if key_in[pygame.K_RETURN]:
        start = False
    pygame.display.update()

# main loop
while running:
    screen.fill(backgroundColor)
    key_in = pygame.key.get_pressed()
 
    if key_in[pygame.K_ESCAPE]:
        print("Quitting!")
        print("Score: {}".format(score))
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting!")
            print("Score: {}".format(score))
            pygame.quit()

    column = main_char_rect.centerx // (margin + rect_width)
    row = main_char_rect.centery // (margin + rect_height)

#Character movement
    if key_in[pygame.K_d] and sum(key_in) == 1 and pressed == 0:
        pressed = 1
        # print(left_count)
        main_char_rect.centerx = main_char_rect.centerx + margin + rect_width

        if main_char_rect.right > width:
            main_char_rect.centerx = main_char_rect.centerx - margin - rect_width

    if key_in[pygame.K_a] and sum(key_in) == 1 and pressed == 0:
        pressed = 1
        # print(left_count)
        main_char_rect.centerx = main_char_rect.centerx - margin - rect_width

        if main_char_rect.left < margin:
            main_char_rect.centerx = main_char_rect.centerx + margin + rect_width

    if key_in[pygame.K_s] and sum(key_in) == 1 and pressed == 0:
        pressed = 1
        # print(left_count)
        main_char_rect.centery = main_char_rect.centery + margin + rect_height

        if main_char_rect.bottom > height - margin:
            main_char_rect.centery = main_char_rect.centery - margin - rect_height

    if key_in[pygame.K_w] and sum(key_in) == 1 and pressed == 0:
        pressed = 1
        # print(left_count)
        main_char_rect.centery = main_char_rect.centery - margin - rect_height

        if main_char_rect.top < margin:
            main_char_rect.centery = main_char_rect.centery + margin + rect_height

#planting different veggies
    if key_in[pygame.K_k]: #peas

        grid[row][column] = [1,1]
        if timestamp[row][column] is not None:
            timestamp[row][column] = pygame.time.get_ticks() / 1000

    if key_in[pygame.K_l]: #carrots

        grid[row][column] = [2,1]
        if timestamp[row][column] is not None:
            timestamp[row][column] = pygame.time.get_ticks() / 1000

    if key_in[pygame.K_SEMICOLON]: #tomatoes

        grid[row][column] = [3,1]
        if timestamp[row][column] is not None:
            timestamp[row][column] = pygame.time.get_ticks() / 1000
    
    if key_in[pygame.K_QUOTE]: #potatoes

        grid[row][column] = [4,1]
        if timestamp[row][column] is not None:
            timestamp[row][column] = pygame.time.get_ticks() / 1000

#harvesting veggies
    if key_in[pygame.K_SPACE] and grid[row][column][1] == 2:
        if grid[row][column][0] == special_crop:
            score += 1 #receive a bonus point for harvesting the crop in demand
        timestamp[row][column] = []
        grid[row][column][1] = 0
        score += 1

    if event.type == pygame.KEYUP:
        pressed = 0

    for row in range(num):
        for column in range(num):
            curr_sprite = dirt_sprite #catch all is dirt
            if grid[row][column][1] == 0:
                curr_sprite = dirt_sprite #dirt
            if grid[row][column] == [1,1]:
                curr_sprite = peas_sprite #green: peas
            if grid[row][column] == [2,1]:
                curr_sprite = carrot_sprite #orange: carrots
            if grid[row][column] == [3,1]:
                curr_sprite = tomato_sprite #red: tomatoes
            if grid[row][column] == [4,1]:
                curr_sprite = potato_sprite #light brown: potatoes
            if timestamp[row][column]:
                if 5 <= (pygame.time.get_ticks()/1000 - timestamp[row][column]) < 10:
                    grid[row][column][1] = 2
                elif (pygame.time.get_ticks()/1000 - timestamp[row][column]) >= 10:
                    grid[row][column][1] = 0
                    score-=1
                    timestamp[row][column] = []
            if grid[row][column][1] == 2:
                curr_sprite = harvest_sprite #blue: ready to harvest
            screen.blit(curr_sprite, [(margin + rect_width) * column + margin,
                                             (margin + rect_height) * row + margin])
    screen.blit(main_char, main_char_rect)

#Demand for crop
    if (start_time - pygame.time.get_ticks()//1000) % 10 == 0 or frame_count == 0:
        random_crop = random.choice(Crops) #selects a new crop every 10 seconds
        crop_demand = "Gathering Information from Market..."
        text_crop = font_in_game.render(crop_demand, True, (250, 250, 250))
        screen.blit(text_crop, [150, 20]) 
        if random_crop == "1. Peas":
            special_crop = 1 
        if random_crop == "2. Carrots":
            special_crop = 2  
        if random_crop == "3. Tomatoes":
            special_crop = 3
        if random_crop == "4. Potatoes":
            special_crop = 4
    if (start_time - pygame.time.get_ticks()//1000) % 10 != 0:
        crop_demand = random_crop + " are in season! [x2]"
        text_crop = font_in_game.render(crop_demand, True, (250, 250, 250))
        screen.blit(text_crop, [150, 20]) 

    # Use python string formatting to format in leading zeros
    time_left = start_time - pygame.time.get_ticks()//1000
    output_string = "Time left: {} | Score: {}".format(time_left, score) 

    # Blit to the screen
    text = font_in_game.render(output_string, True, (250, 250, 250))

    screen.blit(text, [160, 480])

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1

       
    pygame.display.update()

    while time_left <= 0:
        running == False
        screen.fill((0,0,0))
        output_string = "Game Over! | Score: {}".format(score)  
        text = font_end_game.render(output_string, True, (250, 250, 250))
        screen.blit(text, [70, 270])
        if key_in[pygame.K_ESCAPE]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
