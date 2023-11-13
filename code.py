import uinput
from evdev import InputDevice, categorize, ecodes
import os

# Set up the PS5 controller
ps5_controller = InputDevice('/dev/input/eventX')  # Replace 'eventX' with the appropriate event device for your PS5 controller

# Set up the virtual controller
events = [
    uinput.BTN_A,
    uinput.BTN_B,
    # ... define other buttons and axes as needed
]

virtual_device = uinput.Device(events)

# Specify the path to the sound file
sound_file_path = "sounds/button_press.wav"

# Listen for input events continuously
try:
    print("Listening for controller input... Press Ctrl+C to exit.")
    for event in ps5_controller.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)

            if key_event.keystate == key_event.key_up:
                # Button release event
                button_code = ecodes.KEY[event.code]
                virtual_device.emit(uinput.EV_KEY, button_code, 0)  # Button release
            elif key_event.keystate == key_event.key_down:
                # Button press event
                button_code = ecodes.KEY[event.code]
                virtual_device.emit(uinput.EV_KEY, button_code, 1)  # Button press

                # Play sound effect
                os.system(f"aplay {sound_file_path}")

except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Clean up resources if needed
    ps5_controller.close()
    virtual_device.close()
