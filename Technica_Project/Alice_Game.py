import pygame
import random
import sys
import time  # time tracking (for moving objects)

# initializes game
pygame.init()

# game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alice in DisasterLand")  # name

WHITE = (255, 209, 220)  # pink background
BLACK = (180, 140, 240)  # purple text
BLUE = (0, 0, 255)

font = pygame.font.Font(None, 30)  # text size
game_title_image = pygame.image.load("game_title.png")  # text png
instructions_image = pygame.image.load("instructions.png")  # text png
background_image = pygame.image.load("background.png")  # loads the background image
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # scales to fit window size

# loads images for objects
images = {
   "bandaid": pygame.image.load("bandaid.png"),
   "bandaid2": pygame.image.load("bandaid2.png"),
   "battery": pygame.image.load("battery.png"),
   "battery2": pygame.image.load("battery2.png"),
   "flashlight": pygame.image.load("flashlight.png"),
   "flashlight2": pygame.image.load("flashlight2.png")
}
for key in images:
   images[key] = pygame.transform.scale(images[key], (150, 150)) #resizes objects

# game requirements
needed_items = {
    "bandaid": 5,
    "battery": 2,
    "flashlight": 2
}

# displays text
def display_text(text, x, y, color=BLACK):
   rendered_text = font.render(text, True, color)
   screen.blit(rendered_text, (x, y))

# shows needed items
def show_needed_items():
    # positions of items (3), in the middle
    bandaid_pos = (WIDTH // 2 - 225, HEIGHT // 2 - 50)
    battery_pos = (WIDTH // 2 - 75, HEIGHT // 2 - 50)
    flashlight_pos = (WIDTH // 2 + 75, HEIGHT // 2 - 50)

    screen.blit(background_image, (0, 0))  # draw background
    display_text("Gather 5 Bandaids, 2 Batteries and 2 Flashlights!", WIDTH // 2 - 230, HEIGHT // 2 - 150, BLUE)
    display_text("Click the screen to continue", WIDTH // 2 - 130, HEIGHT // 2 - 110, BLUE)
    screen.blit(images["bandaid"], bandaid_pos)
    screen.blit(images["battery"], battery_pos)
    screen.blit(images["flashlight"], flashlight_pos)
    pygame.display.flip()

    # waits for player click
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False  # starts game after a click

# starts the game
def start_game():
   clock = pygame.time.Clock() #game clock
   lives = 3
   objects = list(images.keys()) #all the object names
   falling_objects = [] #list of falling items
   caught_items = {"bandaid": 0, "battery": 0, "flashlight": 0}
   speed = 10 #object speed
   last_speed_increase = time.time() #time fot speed increase

#creating a new falling object
   def create_falling_object():
       item = random.choice(objects) #random object falling
       x_pos = random.randint(50, WIDTH - 50) #random position
       y_pos = 0 # starts from top 
       return {"item": item, "x": x_pos, "y": y_pos, "image": images[item]}

   falling_objects.append(create_falling_object())

#checls if player won
   def has_won():
       for item, count in needed_items.items():
           if caught_items[item] < count: #not enough items
               return False
       return True #all items collected

#game loop
   while lives > 0 and not has_won():
       screen.blit(background_image, (0, 0))  # the background image
       screen.blit(instructions_image, (20, 2 - 55)) #replaces instructions text with image
       display_text(f"Lives: {lives}", 70, 85, BLACK) #displays lives
       display_text(f"Bandaids: {caught_items['bandaid']}/{needed_items['bandaid']}", 70, 115, BLACK) #displays batteries
       display_text(f"Batteries: {caught_items['battery']}/{needed_items['battery']}", 70, 145, BLACK)
       display_text(f"Flashlights: {caught_items['flashlight']}/{needed_items['flashlight']}", 70, 175, BLACK)

       if time.time() - last_speed_increase > 5: #increases speed every 5 seconds
           speed += 1 #increase
           last_speed_increase = time.time() #updates

       for obj in falling_objects: #this is for moving objects down
           obj["y"] += speed #actually moves down
           screen.blit(obj["image"], (obj["x"], obj["y"])) #draws object

           if obj["y"] > HEIGHT: #this is for when object reaches bottom
               falling_objects.remove(obj) #removes object
               falling_objects.append(create_falling_object()) #adds new one

        #handle events
       for event in pygame.event.get():
           if event.type == pygame.QUIT: #quits game
               pygame.quit()
               sys.exit()
           elif event.type == pygame.MOUSEBUTTONDOWN: #click mouse
               mouse_pos = pygame.mouse.get_pos() #gets click position, for objects
               for obj in falling_objects:
                   if obj["x"] < mouse_pos[0] < obj["x"] + 150 and obj["y"] < mouse_pos[1] < obj["y"] + 150:
                       item = obj["item"]
                       if item in needed_items and "2" not in item:
                           caught_items[item] += 1
                           print(f"Caught {item}! Total: {caught_items[item]}")
                       else:
                           lives -= 1
                           print("Wrong item! Lost a life.")
                       falling_objects.remove(obj)
                       falling_objects.append(create_falling_object())
                       break

       pygame.display.flip()
       clock.tick(30)

   if has_won():
       display_text("You caught all items! You win!", 50, 300, BLUE)
   else:
       display_text("Game Over! Returning to home screen...", 50, 300, BLUE)
   pygame.display.flip()
   pygame.time.delay(2000)

# main menu and game loop
def main():
   running = True
   while running:
       screen.blit(background_image, (0, 0))  # Draw the background image
       game_title_x = (WIDTH - game_title_image.get_width()) // 2
       game_title_y = 0
       description_y = game_title_y + game_title_image.get_height() + 20
       screen.blit(game_title_image, (game_title_x, game_title_y))

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
           elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
               show_needed_items()
               start_game()
               running = False

       pygame.display.flip()

   pygame.quit()
   sys.exit()

# run the game
if __name__ == "__main__":
   main()
