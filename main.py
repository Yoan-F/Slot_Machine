import pygame, numpy
pygame.init()

#class location of fruit img
class Location(pygame.sprite.Sprite):

    def __init__(self, loc_x, loc_y):
        super().__init__()
        self.image = pygame.image.load('assets/pomme_dore.png')
        self.rect = self.image.get_rect()
        self.rect.x = loc_x
        self.rect.y = loc_y

    def set_img(self, image):
        self.image = image

#Play fonction
def play():

    global tokens

    result = numpy.random.choice(fruits, 3, p=proba_fruits)
    left_fruit = dic_fruit[result[0]]
    center_fruit = dic_fruit[result[1]]
    right_fruit = dic_fruit[result[2]]
    #change image
    location_left.set_img(left_fruit)
    location_center.set_img(center_fruit)
    location_right.set_img(right_fruit)
    # check if and what you win
    if result[0] == result[1] == result[2]:
        fruit = result[0]
        tokens_win = dic_fruits_tokens[fruit]
        tokens += tokens_win
        print(f"3 {fruit} are displayed ! You win {tokens_win} tokens !")

#Create window
width = 800 #largeur
height = 460 #hauteur
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slot Machine")
pygame.display.set_icon(pygame.image.load("assets/pomme_dore.png"))
background = [255, 255, 255] #white

#Payeur token
tokens = 1000

#dictionary of fruits
dic_fruit = {
    "Pineapple": pygame.image.load('assets/ananas.png'),
    "Cherry": pygame.image.load('assets/cerise.png'),
    "Orange": pygame.image.load('assets/orange.png'),
    "Watermelon": pygame.image.load('assets/pasteque.png'),
    "Golden-Apple": pygame.image.load('assets/pomme_dore.png')
}
img_test = pygame.image.load('assets/orange.png')

# List of fruits
fruits = ['Pineapple', 'Cherry', 'Orange', 'Watermelon', 'Golden-Apple']
dic_fruits_tokens = {
    "Pineapple": 50,
    "Cherry": 15,
    "Orange": 5,
    "Watermelon": 150,
    "Golden-Apple": 10000
}
proba_fruits = [0.2, 0.25, 0.4, 0.1, 0.05]

#Load of locations
height_location = height / 2 + 30
location_x_center = width / 3 + 72
location_x_left = location_x_center - img_test.get_width() - 22
location_x_right = location_x_center + img_test.get_width() + 20

locations = pygame.sprite.Group()
location_left = Location(location_x_left, height_location)
location_center = Location(location_x_center, height_location)
location_right = Location(location_x_right, height_location)

#location on group
locations.add(location_left)
locations.add(location_center)
locations.add(location_right)

#load background image
background_img = pygame.image.load('assets/slot.png')
#load text of tokens
font = pygame.font.SysFont("arial", 30)

# loop for window
run = True
while run:

    window.fill(background)
    window.blit(background_img, (10, 0))
    locations.draw(window)
    #number of token
    txt_tokens = font.render(str(tokens) + " token(s)", True, (0, 0, 0))
    window.blit(txt_tokens, (10, 10))

    pygame.display.flip()

    for event in pygame.event.get():
        #check if playeur close window
        if event.type == pygame.QUIT:
            run = False
            quit()
        #check if user push key
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE and tokens >= 10:
               play() #call fonction
               tokens -= 10