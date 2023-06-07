import pygame
import math
import sys
from utils import blit_rotate_center

pygame.init()
pygame.font.init()
pygame.display.set_caption("Parking system!")
# Calls ---------------------------------------------------------------------------------------------------------------------------------------------------------------
GRASS = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\grass.jpg")
TRACK = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\track.png")

TRACK_BORDER = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\track-border.png")
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
BACKGROUND_COLOR = (255, 255, 255)

ANTI_COLLISION_BAR = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\anticollisionbar.png")
BAR_POSITION = (289.09, 875.26)


WHITE_CAR = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\white_car.png")
GREEN_CAR = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\green_car.png")
RED_CAR = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\red_car.png")
TAXI = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\taxi.png")
RED_BUS = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\red_bus.png")
GREEN_TRACK = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\green_track.png")
WHITE_TRACK = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\white_track.png")
GREEN_BUS = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\green_bus.png")
BLUE_CAR = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\blue_car.png")
YELLOW_CAR = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\yellow_car.png")

WHITE_CAR_RIGHT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\white_car_right.png")
GREEN_CAR_RIGHT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\green_car_right.png")
RED_CAR_RIGHT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\red_car_right.png")
TAXI_RIGHT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\taxi_right.png")
RED_BUS_RIGHT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\red_bus_right.png")
GREEN_TRACK_RIGHT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\green_track_right.png")
WHITE_TRACK_RIGHT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\white_track_right.png")
GREEN_BUS_RIGHT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\green_bus_right.png")
BLUE_CAR_RIGHT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\blue_car_right.png")
YELLOW_CAR_RIGHT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\yellow_car_right.png")

WHITE_CAR_LEFT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\white_car_left.png")
GREEN_CAR_LEFT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\green_car_left.png")
RED_CAR_LEFT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\red_car_left.png")
TAXI_LEFT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\taxi_left.png")
RED_BUS_LEFT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\red_bus_left.png")
GREEN_TRACK_LEFT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\green_track_left.png")
WHITE_TRACK_LEFT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\white_track_left.png")
GREEN_BUS_LEFT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\green_bus_left.png")
BLUE_CAR_LEFT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\blue_car_left.png")
YELLOW_CAR_LEFT = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\yellow_car_left.png")

MAGLOOP = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\magloop.png")
MAGWIDTH, MAGHEIGHT = MAGLOOP.get_width(), MAGLOOP.get_height()
MAGLOOP_MASK = pygame.mask.from_surface(MAGLOOP)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

RECTANGLEGREEN = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\rectanglegreen.png")
RECTANGLERED = pygame.image.load(r"E:\TIPE\INDUCTIVE LOOP PROJECT\Project\images\rectanglered.png")

x , y = 87.95 , 87.95
initialVel = 10
rotationalVel = 7
FPS = 60
clock = pygame.time.Clock()

slotCoord = [(226.64, 190.79), (226.64, 304.79), (226.64, 416.79), (226.64, 525.79), (226.64, 640.79), (226.64, 752.79), (697.64, 190.79), (697.64, 304.79), (697.64, 416.79), (697.64, 525.79)]
commandCorrdA = [((1137.9965, 392.0456), 'A 01'), ((1137.9965, 455.204899), 'A 02'), ((1137.9965, 521.3642), 'A 03'), ((1137.9965, 597.5235), 'A 04'), ((1137.9965, 669.6828), 'A 05'), ((1137.9965, 742.84210), 'A 06')]
commandCorrdB = [((1334.7007, 392.0456), 'B 01'), ((1334.7007, 455.204899), 'B 02'), ((1334.7007, 521.3642), 'B 03'), ((1334.7007, 597.5235), 'B 04')]

# Definitions ----------------------------------------------------------------------------------------------------------------------------------------------------------
class ControlPanel:
    def __init__(self, commandsA, commandsB, rect_green_image, rect_red_image):
        self.commandsA = commandsA
        self.commandsB = commandsB
        self.rect_green_image = rect_green_image
        self.rect_red_image = rect_red_image
    def draw(self, win, parking_slots):
        for command, comment in self.commandsA:
            slot_id = comment  #slot ID
            slot = [s for s in parking_slots if s.carid == slot_id]
            if slot[0] and slot[0].is_occupied:
                win.blit(self.rect_red_image, command)
            else:
                win.blit(self.rect_green_image, command)

        for command, comment in self.commandsB:
            slot_id = comment  #slot ID
            slot = [s for s in parking_slots if s.carid == slot_id]
            if slot[0] and slot[0].is_occupied:
                win.blit(self.rect_red_image, command)
            else:
                win.blit(self.rect_green_image, command)

class ParkingSlot:
    def __init__(self, id, x, y, width, height, image):
        self.carid = id
        self.rect = pygame.Rect(x, y, width, height)
        self.image = image
        self.is_occupied = False
    def check_collision(self, car_rect):
        if self.rect.colliderect(car_rect):
            self.is_occupied = True
        else:
            self.is_occupied = False
    def generate_field_from_image(self,image_path, field_width, field_height, density):
        pygame.init()
        screen = pygame.display.set_mode((field_width, field_height))
        pygame.display.set_caption("Generated Field")
        mag_loop_image = pygame.image.load(image_path).convert_alpha()
        field_surface = pygame.Surface((field_width, field_height))

        loop_width, loop_height = mag_loop_image.get_size()
        for x in range(loop_width):
            for y in range(loop_height):
                if mag_loop_image.get_at((x, y))[3] > 0:
                    field_x = x + (field_width - loop_width) // 2
                    field_y = y + (field_height - loop_height) // 2
                    if (0 <= field_x < field_width) and (0 <= field_y < field_height):
                        field_surface.set_at((field_x, field_y), (255, 255, 255))  # Set field color to white

        rect_width, rect_height = 50, 50
        rect_x = (field_width - rect_width) // 2
        rect_y = (field_height - rect_height) // 2
        rect_speed = 5

        field_color_start = pygame.Color(255, 255, 255)  # Start color (white)
        field_color_end = pygame.Color(0, 0, 255)  # End color (blue)
        color_transition_time = 2000  # Transition time in milliseconds
        color_timer = pygame.time.get_ticks()
        field_color = field_color_start

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                rect_x -= rect_speed
            if keys[pygame.K_RIGHT]:
                rect_x += rect_speed
            if keys[pygame.K_UP]:
                rect_y -= rect_speed
            if keys[pygame.K_DOWN]:
                rect_y += rect_speed

            rect_center_x = rect_x + rect_width // 2
            rect_center_y = rect_y + rect_height // 2
            if field_surface.get_at((rect_center_x, rect_center_y)) == (255, 255, 255):  # Check if the rect is inside the field
                current_time = pygame.time.get_ticks()
                elapsed_time = current_time - color_timer
                if elapsed_time >= color_transition_time:
                    color_timer = current_time
                    field_color = field_color_end
                else:
                    color_progress = elapsed_time / color_transition_time
                    field_color = field_color_start.lerp(field_color_end, color_progress)

            field_surface.fill(field_color)
            screen.blit(field_surface, (0, 0))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(rect_x, rect_y, rect_width, rect_height))

            pygame.display.flip()

        pygame.quit()
    def draw(self, screen):
        if not self.is_occupied:
            screen.blit(self.image, (self.rect.x, self.rect.y))
    
class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
        self.rect = self.img.get_rect()
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()
    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()
    def stop(self):
        self.vel = 0
        self.move()
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        new_x = self.x - horizontal
        new_y = self.y - vertical

        if TRACK_BORDER.get_rect().collidepoint(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.rect.x = self.x
            self.rect.y = self.y
    def collide(self, mask, x=x, y=y):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi
    def get_position(self):
            return self.x, self.y

class GreenCar(AbstractCar):
    IMG = GREEN_CAR
    START_POS = (473.47, 892.46)
    CAR_NAME = 'GREEN_CAR'
    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()
    def bounce(self):
        self.vel = -self.vel
        self.move()

class RedBus(GreenCar):
    CAR_NAME = 'RED_BUS'
    IMG = RED_BUS

class GreenBus(GreenCar):
    CAR_NAME = 'GREEN_BUS'
    IMG = GREEN_BUS

class GreenTrack(GreenCar):
    CAR_NAME = 'GREEN_TRACK'
    IMG = GREEN_TRACK

class WhiteTrack(GreenCar):
    CAR_NAME = 'WHITE_TRACK'
    IMG = WHITE_TRACK

class RedCar(GreenCar):
    CAR_NAME = 'RED_CAR'
    IMG = RED_CAR

class BlueCar(GreenCar):
    CAR_NAME = 'BLUE_CAR'
    IMG = BLUE_CAR

class YellowCar(GreenCar):
    CAR_NAME = 'YELLOW_CAR'
    IMG = YELLOW_CAR

class Taxi(GreenCar):
    CAR_NAME = 'TAXI'
    IMG = TAXI

class WhiteCar(GreenCar):
    CAR_NAME = 'WHITE_CAR'
    IMG = WHITE_CAR

def draw(win, images, car, parking_slots):
    for img, pos in images:
        win.blit(img, pos)
    car.draw(win)
    for slot in parking_slots:
        if not slot.is_occupied :
            slot.draw(win)
        else:
            pass
    pygame.display.update()
def move_car(car):
    keys = pygame.key.get_pressed()
    moved = False
    if keys[pygame.K_a]:
        car.rotate(left=True)
    if keys[pygame.K_d]:
        car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        car.move_backward()
    if keys[pygame.K_SPACE]:
        car.stop()
    if not moved:
        car.reduce_speed()
def full_park(ParkedCars, images, occupied_slots_ids):
    full_parked_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    full_parked_surface.fill((151, 173, 159, 20))

    font = pygame.font.SysFont(None, 80)
    text_surface = font.render("Le Parc Est Plein", True, (255, 255, 255))  # Render the text onto a surface
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)  # Center the text on the screen

    full_parked_surface.blit(text_surface, text_rect)

    button_width = 120
    button_height = 40
    button_color = (255, 227, 84)
    button_text_color = (255, 255, 255)
    button_radius = 100
    button_font = pygame.font.SysFont(None, 40)

    exit_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 50, button_width, button_height)
    reset_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 100, button_width, button_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
                elif reset_button.collidepoint(mouse_pos):
                    for car in ParkedCars:
                        images.remove((car[2], car[1]))
                        occupied_slots_ids.remove(car[0])
                    main() 
        pygame.draw.rect(full_parked_surface, button_color, exit_button, border_radius=button_radius)
        pygame.draw.rect(full_parked_surface, button_color, reset_button, border_radius=button_radius)

        exit_text = button_font.render("Exit", True, button_text_color)
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        full_parked_surface.blit(exit_text, exit_text_rect)

        reset_text = button_font.render("Reset", True, button_text_color)
        reset_text_rect = reset_text.get_rect(center=reset_button.center)
        full_parked_surface.blit(reset_text, reset_text_rect)

        WIN.blit(full_parked_surface, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
def correspondante_image(NAMEIMGParked, park_id, XParked, YParked):
    NAMEIMGParked = NAMEIMGParked
    for K in range(1,7):
                        if park_id[-1] == f'A 0{K}':
                            if str(NAMEIMGParked) == 'GREEN_CAR':
                                NAMEIMGParked = GREEN_CAR_LEFT
                                XParked += -20
                                YParked += 25
                            if str(NAMEIMGParked) == 'WHITE_TRACK':
                                XParked += -48
                                YParked += 48
                                NAMEIMGParked = WHITE_TRACK_LEFT
                            if str(NAMEIMGParked) == 'WHITE_CAR':
                                NAMEIMGParked = WHITE_CAR_LEFT
                                XParked += -20
                                YParked += 25
                            if str(NAMEIMGParked) == 'TAXI':
                                NAMEIMGParked = TAXI_LEFT
                                XParked += -20
                                YParked += 25
                            if str(NAMEIMGParked) == 'RED_CAR':
                                NAMEIMGParked = RED_CAR_LEFT
                                XParked += -10
                                YParked += 15
                            if str(NAMEIMGParked) == 'RED_BUS':
                                XParked += -40
                                YParked += 40
                                NAMEIMGParked = RED_BUS_LEFT
                            if str(NAMEIMGParked) == 'GREEN_TRACK':
                                XParked += -40
                                YParked += 40
                                NAMEIMGParked = GREEN_TRACK_LEFT
                            if str(NAMEIMGParked) == 'BLUE_CAR':
                                NAMEIMGParked = BLUE_CAR_LEFT
                                XParked += -10
                                YParked += 15
                            if str(NAMEIMGParked) == 'GREEN_BUS':
                                XParked += -40
                                YParked += 40
                                NAMEIMGParked = GREEN_BUS_LEFT
                            if str(NAMEIMGParked) == 'YELLOW_CAR':
                                NAMEIMGParked = YELLOW_CAR_LEFT
                                XParked += -20
                                YParked += 25                
                        if park_id[-1] == f'B 0{K}':
                            if str(NAMEIMGParked) == 'GREEN_CAR':
                                XParked += -20
                                YParked += 25
                                NAMEIMGParked = GREEN_CAR_RIGHT
                            if str(NAMEIMGParked) == 'WHITE_TRACK':
                                XParked += -48
                                YParked += 48
                                NAMEIMGParked = WHITE_TRACK_RIGHT
                            if str(NAMEIMGParked) == 'WHITE_CAR':
                                XParked += -20
                                YParked += 35
                                NAMEIMGParked = WHITE_CAR_RIGHT
                            if str(NAMEIMGParked) == 'TAXI':
                                XParked += -20
                                YParked += 25
                                NAMEIMGParked = TAXI_RIGHT
                            if str(NAMEIMGParked) == 'RED_CAR':
                                XParked += -20
                                YParked += 25
                                NAMEIMGParked = RED_CAR_RIGHT
                            if str(NAMEIMGParked) == 'RED_BUS':
                                XParked += -48
                                YParked += 48
                                NAMEIMGParked = RED_BUS_RIGHT
                            if str(NAMEIMGParked) == 'GREEN_TRACK':
                                XParked += -48
                                YParked += 48
                                NAMEIMGParked = GREEN_TRACK_RIGHT
                            if str(NAMEIMGParked) == 'BLUE_CAR':
                                XParked += -20
                                YParked += 25
                                NAMEIMGParked = BLUE_CAR_RIGHT
                            if str(NAMEIMGParked) == 'GREEN_BUS':
                                XParked += -42
                                YParked += 48
                                NAMEIMGParked = GREEN_BUS_RIGHT
                            if str(NAMEIMGParked) == 'YELLOW_CAR':
                                XParked += -20
                                YParked += 25
                                NAMEIMGParked = YELLOW_CAR_RIGHT
    return NAMEIMGParked, XParked, YParked
# Main ----------------------------------------------------------------------------------------------------------------------------------------------------------
cars = [GreenCar(initialVel, rotationalVel),RedCar(initialVel, rotationalVel),WhiteCar(initialVel, rotationalVel),Taxi(initialVel,
        rotationalVel),GreenTrack(initialVel, rotationalVel),RedBus(initialVel, rotationalVel),WhiteTrack(initialVel, rotationalVel), 
        BlueCar(initialVel, rotationalVel),YellowCar(initialVel, rotationalVel),GreenBus(initialVel, rotationalVel)] 

def main():
    images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (TRACK_BORDER, (87.95, 87.95)), (ANTI_COLLISION_BAR, BAR_POSITION)]
    run = True
    parking_slots = []
    
    j = 1
    for coord in slotCoord:
        if j <= 6 :
            slot = ParkingSlot(f'A 0{j}', coord[0], coord[1], MAGWIDTH, MAGHEIGHT, MAGLOOP)
        else:
            slot = ParkingSlot(f'B 0{j-6}', coord[0], coord[1], MAGWIDTH, MAGHEIGHT, MAGLOOP)
        parking_slots.append(slot)
        j += 1

    control = ControlPanel(commandCorrdA, commandCorrdB, RECTANGLEGREEN, RECTANGLERED)
    parkIsFull = False
    occupied_slots_ids = []
    ParkedCars = []
    i = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    park_id = [slot.carid for slot in parking_slots 
                    if slot.is_occupied and slot.carid not in occupied_slots_ids]
                    occupied_slots_ids.append(park_id[0])
                    XParked, YParked = cars[i].get_position()
                    NAMEIMGParked = cars[i].CAR_NAME
                    NAMEIMGParked, XParked, YParked = correspondante_image(NAMEIMGParked,
                     park_id, XParked, YParked)
                    ParkedCars.append([park_id[0], (XParked,YParked), NAMEIMGParked])
                    images.append((NAMEIMGParked, (XParked,YParked)))
                    i+=1
        if len(occupied_slots_ids) == 10 :
            parkIsFull = True
        try:
            move_car(cars[i])
            cars[i].move()
            for slot in parking_slots:
                slot.check_collision(cars[i].rect)
            for slot in parking_slots:
                    if slot.carid in occupied_slots_ids:
                        slot.is_occupied = True
            WIN.fill((255, 255, 255))
            for img, pos in images:
                WIN.blit(img, pos)
            
            draw(WIN, images, cars[i], parking_slots)
            for slot in parking_slots:
                    if slot.carid in occupied_slots_ids:
                        slot.is_occupied = True
            control.draw(WIN, parking_slots)
            if cars[i].collide(TRACK_BORDER_MASK) != None:
                cars[i].bounce()
        except:
            pass
        if parkIsFull :
            full_park(ParkedCars, images, occupied_slots_ids)
            pygame.time.wait(5000)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__' :
    main()

