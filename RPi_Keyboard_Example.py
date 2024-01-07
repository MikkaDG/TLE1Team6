#!/usr/bin/env python3
import pygame
import time

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Define ASCII values for each character
CHARACTER_KEYS = {
    'a': 4, 'b': 5, 'c': 6, 'd': 7, 'e': 8, 'f': 9, 'g': 10, 'h': 11,
    'i': 12, 'j': 13, 'k': 14, 'l': 15, 'm': 16, 'n': 17, 'o': 18, 'p': 19,
    'q': 20, 'r': 21, 's': 22, 't': 23, 'u': 24, 'v': 25, 'w': 26, 'x': 27,
    'y': 28, 'z': 29,
    '1': 30, '2': 31, '3': 32, '4': 33, '5': 34, '6': 35, '7': 36, '8': 37,
    '9': 38, '0': 39,
    'ENTER': 40, 'ESC': 41, 'BACKSPACE': 42, 'TAB': 43, 'SPACE': 44, '-': 45,
    '=': 46, '[': 47, ']': 48, '\\': 49, ';': 51, "'": 52, '`': 53, ',': 54,
    '.': 55, '/': 56,
    'CAPSLOCK': 57, 'F1': 58, 'F2': 59, 'F3': 60, 'F4': 61, 'F5': 62, 'F6': 63,
    'F7': 64, 'F8': 65, 'F9': 66, 'F10': 67, 'F11': 68, 'F12': 69,
    'PRINTSCREEN': 70, 'SCROLLLOCK': 71, 'PAUSE': 72, 'INSERT': 73, 'HOME': 74,
    'PAGEUP': 75, 'DELETE': 76, 'END': 77, 'PAGEDOWN': 78, 'RIGHTARROW': 79,
    'LEFTARROW': 80, 'DOWNARROW': 81, 'UPARROW': 82,
    'NUMLOCK': 83, '/': 84, '*': 85, '-': 86, '+': 87, 'ENTER': 88, '1': 89,
    '2': 90, '3': 91, '4': 92, '5': 93, '6': 94, '7': 95, '8': 96, '9': 97,
    '0': 98, '.': 99,
    'APPLICATION': 101,
    'F13': 104, 'F14': 105, 'F15': 106, 'F16': 107, 'F17': 108, 'F18': 109, 'F19': 110,
    'F20': 111, 'F21': 112, 'F22': 113, 'F23': 114, 'F24': 115,
    'EXECUTE': 116, 'HELP': 117, 'MENU': 118, 'SELECT': 119, 'STOP': 120, 'AGAIN': 121,
    'UNDO': 122, 'CUT': 123, 'COPY': 124, 'PASTE': 125, 'FIND': 126, 'MUTE': 127,
    'VOLUMEUP': 128, 'VOLUMEDOWN': 129,
    'LEFTCONTROL': 224, 'LEFTSHIFT': 225, 'LEFTALT': 226, 'LEFT_GUI': 227,
    'RIGHTCONTROL': 228, 'RIGHTSHIFT': 229, 'RIGHTALT': 230, 'RIGHT_GUI': 231
}
button_sounds = {
        0: 'actie_onder', #Kruis
        1: 'actie_rechts', #Rond
        2: 'actie_links', #Vierkant
        3: 'actie_boven', #Driehoek
        9: 'bumper_links', #Bomper links
        10: 'bumper_rechts', #bomper rechts
        8: 'R3', #R3
        7: 'L3', #L3
        16: 'MUTE', #MUTE
        5: 'PS', #PS
        4: 'SELECT', #SELECT
        6: 'OPTIONS', #OPTIONS
        15: 'TOUCHPAD', #TOUCHPAD
        11: 'DP-UP', #DP-UP
        12: 'DP-DOWN', #DP-DOWN
        13: 'DP-LEFT',
        14: 'DP-RIGHT'
            
        }
 
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

def send_char_key(character):
    if character in CHARACTER_KEYS:
        key = CHARACTER_KEYS[character]
        write_report(NULL_CHAR*2 + chr(0) + chr(key) + NULL_CHAR*5)
        time.sleep(0.1)
        write_report(NULL_CHAR*8)

# Main loop to handle controller inputs
running = True
pressed_buttons = set()
axis_threshold = 0.9

# Main loop to handle events
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.JOYBUTTONDOWN:
            print(event.button)
            pressed_buttons.add(event.button)
            # Handle button mappings
            if 0 in pressed_buttons:  
                send_char_key('SPACE')
            if 1 in pressed_buttons:
                send_char_key('q')
            if 2 in pressed_buttons:
                send_char_key('e')
            if 3 in pressed_buttons:
                send_char_key('f')
            if 9 in pressed_buttons:
                send_char_key('PAGEDOWN')
            if 10 in pressed_buttons:
                send_char_key('PAGEUP')
            if 6 in pressed_buttons:
                send_char_key('SPACE')
            if 7 in pressed_buttons:
                send_char_key('SHIFT')
            # Add more button mappings as needed

        elif event.type == pygame.JOYBUTTONUP:
            pressed_buttons.discard(event.button)
        elif event.type == pygame.JOYAXISMOTION:
            # Assuming axis 0 and axis 1 control X and Y movements respectively
            if event.axis == 0:
                x_axis = joystick.get_axis(0)
                if abs(x_axis) > axis_threshold:
                    if x_axis > 0:
                        send_char_key('d')  # Simulate right
                    else:
                        send_char_key('a')  # Simulate left
                
            elif event.axis == 1:
                y_axis = joystick.get_axis(1)
                if abs(y_axis) > axis_threshold:
                    if y_axis > 0:
                        send_char_key('s')  # Simulate down
                    else:
                        send_char_key('w')  # Simulate up

        
            

    # Limit the frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()

 
