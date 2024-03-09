# Shuffler Reborn
A tool to let you shuffle between different games every few seconds.

## What is Shuffler Reborn?
Shuffler Reborn is a program that lets you shuffle between 5 games at random intervals and in random order, allowing you to progress all games in the most chaotic ways imaginable. The project is inspired by **DougDoug's Shufflemania**.

## Compatibility
This code uses the Load Last Save feature found in Mesen, thus is currently only accepted in Mesen 0.9.9. However, versions for other console games are considered, including:
- Mesen S (SNES/GB/GBC)
- Mesen 2.0 (NES/SNES/GB/GBC/MS)
- Project64 (N64)
- Dolphin (GC/Wii)

## Prerequisites
- Python
- Mesen 0.9.9
- NES ROMs

## Installation
1. Check the PATH on your computer. If Python is not installed, reinstall Python via the installer, checking the box "Install Python to PATH".
2. Add the Mesen emulator to PATH.
3. Open the Python code with a basic text editor like Notepad, and change the filepath of the ROMs to where your own ROMs are, as well as the filepath of your Mesen emulator.
4. You're done! To run the code, open the command prompt at the directory where your code is saved and enter "python shuffler_mesen.py"!

## Customization
**Consistent starts**
If you want to compete against another person or simply replicate a challenge, you can do so thanks to the code utilizing the Load Last Save feature in Mesen. Before shuffling, open the roms you will use, load the save you need, and power off.

**Changing the amount of ROMs**
Since none of the code relies on how much ROMs exist, you can add as many ROMs as you want in the cycle.
