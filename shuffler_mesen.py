# YOU WILL NEED PYTHON AND MESEN IN PATH
# To use, enter "python shuffler.py" in command prompt at the ROM directory
# You may need to install the keyboard module via "pip install keyboard"

import subprocess
import time
import random
import keyboard

# Launching a ROM
def launch_rom(rom_path):
    subprocess.run(["C:/mesen/mesen.exe", rom_path])

# Loading the previous savestate
def load_last_session():
    subprocess.run(["C:/mesen/mesen.exe", "/LoadLastSession"])

# List of ROMs we'll use for the Shuffler
rom_paths = [
    "ROMPATH1",
    "ROMPATH2",
    "ROMPATH3",
    "ROMPATH4",
    "ROMPATH5"
]

# The main code for the Shuffler
while True:
    # Generate a random order for the ROMs
    random.shuffle(rom_paths)
    
    # Creates a copy of the original ROM list so we can safely delete entries from it
    rom_paths_copy = rom_paths.copy()
    
    for rom_path in rom_paths_copy:
        launch_rom(rom_path)
        load_last_session()  # Loads the previous save state
        # Waits 5-20 seconds before shuffling, change this to change the length of the shuffles
        wait_time = random.randint(5, 20)
        start_time = time.time()
        while time.time() - start_time < wait_time:
            if keyboard.is_pressed('r'):  # Recognizes you pressing R, change this to change the hotkey
                rom_paths.remove(rom_path)  # Remove the current ROM from the cycle
                break  # Deviates from the cycle to delete it
            time.sleep(0.1)  # How long it waits before recognizing an R press again, you probably shouldn't change this