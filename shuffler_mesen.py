#YOU WILL NEED PYTHON INSTALLED TO PATH
#to use this, navigate command prompt to the folder where you saved this file, and enter
#python shuffler_nes_template.py
#you are free to change the name of the file, but it will change what you need to type in command prompt


import subprocess
import time
import random
import keyboard

# Function to launch a specific ROM
def launch_rom(rom_path):
    subprocess.run(["C:/mesen/mesen.exe", rom_path])

# Function to load the last session
def load_last_session():
    subprocess.run(["C:/mesen/mesen.exe", "/LoadLastSession"])

# Main loop
while True:
    # List of paths to the ROMs
    rom_paths = [
        "ROMPATH1.nes",
        "ROMPATH2.nes",
        "ROMPATH3.nes",
        "ROMPATH4.nes",
        "ROMPATH5.nes"
    ]

    # Generate a random order for the ROMs
    random.shuffle(rom_paths)
    
    for rom_path in rom_paths:
        launch_rom(rom_path)
        load_last_session()  # Load the last session
        # Wait for random time between 5 to 20 seconds
        wait_time = random.randint(5, 20)
        start_time = time.time()
        while time.time() - start_time < wait_time:
            if keyboard.is_pressed('r'):  # If 'r' key is pressed, remove the current ROM from the cycle
                rom_paths.remove(rom_path)
                break
            time.sleep(0.1)  # Check every 0.1 second for key press
