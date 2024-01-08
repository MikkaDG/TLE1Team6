import sys
import pygame
import os
import time


pygame.init()
pygame.mixer.init()

pygame.joystick.init()

# Check the number of connected joysticks
num_joysticks = pygame.joystick.get_count()
print("Number of connected joysticks:", num_joysticks)

# Initialize each joystick
for i in range(num_joysticks):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    print("Joystick {} name:".format(i), joystick.get_name())

# Example: Assigning each joystick to a player
joystick = pygame.joystick.Joystick(0)
joystick1 = pygame.joystick.Joystick(1)


print(f"Initialized {joystick.get_name()} and {joystick1.get_name()}")

# Folder containing sound files
folder_path='/home/team6/sounds/'

# List to hold loaded sounds
sounds = {}

# Loop through files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.wav'):  # You can adjust the file extension as needed
        file_path = os.path.join(folder_path, filename)
        sound_name = os.path.splitext(filename)[0]  # Extract the name without extension

        # Load the sound and store it in the dictionary with the name
        sound = pygame.mixer.Sound(file_path)
        sounds[sound_name] = sound
        
        button_sounds = {
        0: 'actie_onder', #Kruis
        1: 'actie_rechts', #Rond
        2: 'actie_boven', #Driehoek
        3: 'actie_links', #Vierkant
        4: 'bumper_links', #Bomper links
        5: 'bumper_rechts', #bomper rechts
        6: 'trigger_links', #trigger links
        7: 'trigger_rechts' #trigger rechts
            
        }
# Define controller state for each button
controller_states = {i: False for i in range(joystick.get_numbuttons())}
controller_states_1 = {i: False for i in range(joystick1.get_numbuttons())}

# State to track if we are waiting for a button press
waiting_for_button = False

try:
    time.sleep(5)
    sounds['welkom'].play()
    pygame.time.wait(int(sounds['welkom'].get_length() * 1000))
    sounds['extra_uitleg'].play()
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONUP:
                if event.joy == 0:
                   print(f"Button {event.button} pressed on {joystick.get_name()}")
                else:
                   print (f"Button {event.button} pressed on {joystick1.get_name()}")

                if not waiting_for_button:
                    # Check if the PS button on the controller is pressed
                    if event.button == 10:  # PS button on PlayStation controller
                        print("Press another button to toggle")
                        sounds['psknop_toggle'].play();
                        waiting_for_button = True
                        if event.button in button_sounds:
                            sound_name = button_sounds[event.button]
                else:
                    # Toggle the state of the pressed button
                    if event.button != 10:
                        if event.joy == 0:
                           controller_states[event.button] = not controller_states[event.button]
                           print(f"Button {event.button} toggled to {controller_states[event.button]}")
                        else:
                           controller_states_1[event.button] = not controller_states_1[event.button]
                           print(f"Button {event.button} toggled to {controller_states_1[event.button]}")
                        waiting_for_button = False
                        if event.button in button_sounds:
                            sound_name = button_sounds[event.button]
                            if sound_name in sounds:
                                for sound in sounds.values():
                                    sound.stop()
                                # Play the appropriate sound based on the button press
                                sounds['je_hebt'].play()  # First sound
                                pygame.time.wait(int(sounds['je_hebt'].get_length() * 1000))
                                
                                sounds[sound_name].play()  # Button-specific sound
                                pygame.time.wait(int(sounds[sound_name].get_length() * 1000))
                        
                                if controller_states[event.button]:
                                    sounds['uitgeschakeld'].play()  # Last sound
                                    pygame.time.wait(int(sounds['uitgeschakeld'].get_length() * 1000))
                                else:
                                    sounds['ingeschakeld'].play()  # Last sound
                                    pygame.time.wait(int(sounds['ingeschakeld'].get_length() * 1000))

                    elif event.type == pygame.JOYBUTTONUP and not controller_states[event.button] and not waiting_for_button:
                       # Handle button release only if it's not toggled
                       print(f"Button {event.button} released")
                
        
except KeyboardInterrupt:
    print("Exiting...")
finally:
    pygame.quit()
