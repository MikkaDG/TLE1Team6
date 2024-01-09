Controller Splitter(dev):
- Setup Rasbperry Pi as USB/IP Host:
      https://wiki.archlinux.org/title/USB/IP
  - Test:
      usbip list -l
  
  - Bind both controllers:
      - usbip bind -b 1-1.1
      - usbip bind -b 1-1.2

-Setup PC/LAPTOP as USB/IP client:
    https://github.com/cezanne/usbip-win
  - cd into directory:
      usbip attach -r <usbip server ip> -b 1-1.1
      usbip attach -r <usbip server ip> -b 1-1.2

Now using Joyshockmapper:
  https://github.com/JibbSmart/JoyShockMapper/releases/tag/v3

  -Both controllers connected should work and be recognized
    Fortnite file:
# Configuration for Fortnite with flick stick
# Jibb Smart
# (Any line that starts with # is ignored by JoyShockMapper)
# First, reset to defaults so we don't have to set values we don't care about
RESET_MAPPINGS

# Calibrate. Flick stick relies on good calibration; gyro and stick sens make more sens with it, too
REAL_WORLD_CALIBRATION = 1.7906
IN_GAME_SENS = 0.075
# Please set IN_GAME_SENS to your in game mouse speed setting whenever you change it

# Button mappings
LLEFT = A
LRIGHT = D
LUP = W
LDOWN = S
LEFT_STICK_MODE = OUTER_RING
LRING = LSHIFT    # auto run
LEFT = G          # edit building
RIGHT = F         # repair / upgrade
UP = M            # map
DOWN = I          # inventory
GYRO_OFF = E
ZL = F1           # wall
ZL,W = F2         # floor
ZL,N = F3         # ramp
ZL,E = F4         # roof
ZL,S = F5         # trap
ZR = 2            # weapon select mode
ZR,W = 3
ZR,N = 4
ZR,E = 5
ZR,S = 6
R = LMOUSE
L = RMOUSE
N = 1             # pickaxe
E = LCONTROL NONE # toggle crouch / gyro off
W = R E           # reload use
S = SPACE
L3 = LSHIFT       # sprint
R3 = MMOUSE       # spot target
+ = ESC
- = TAB

# Include mouse settings
GyroConfigs/_3Dmouse.txt

  - Create as .txt file and paste in terminal

PLAY THE GAME
