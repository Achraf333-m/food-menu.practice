import os

text = input('wanna turn off the laptop? Y/N')


if text == 'no':
    quit()

elif text == 'yes':
    os.system('shutdown /s /t 1')