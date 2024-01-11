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


  - Create as .txt file and paste in terminal

PLAY THE GAME
