# audacityscriptproject
Project that runs a script with audacity

This program assumes you have an instance of Audacity running. It will record for a specified time, stop recording, export the file
precisely time-stamped to the save directory, and close the track and do it all again. 

## Initial Setup
1. Follow the "Enable mod-script-pipe" instructions here: https://manual.audacityteam.org/man/scripting.html
2. Make sure you have Python version 2.7 or higher installed
3. Make sure you have the right recording device and playback device (under "Audio Setup" in the toolbar)
4. Update config.py
5. Run run.py
6. To stop, you can close Audacity or hit Ctrl+C in your terminal

## Notes
1. I used a Windows 10 64-bit machine with Python 3.11.4 installed directly from the microsoft store
2. If you have issues with reading or writing to the pipe, make sure you have followed everything in step 1 correctly
