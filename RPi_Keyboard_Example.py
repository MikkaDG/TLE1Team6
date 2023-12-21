#!/usr/bin/env python3
import pygame
import time

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Define keyboard key constants
SPACE_KEY = pygame.K_SPACE

# Set up the controller
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

# If a joystick/controller is connected
if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def send_space_key():
    write_report(NULL_CHAR*2 + chr(0) + chr(4) + NULL_CHAR*5)
    time.sleep(0.1)
    write_report(NULL_CHAR*8)

# Main loop to handle controller inputs
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            # Button mapping - Press X button on the controller to trigger SPACE key
            if event.button == 2:  # Assuming X button is button index 2
                send_space_key()

    # Limit the frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()
