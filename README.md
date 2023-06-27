# audacityscriptproject
Project that runs a script with audacity

This program assumes you have an instance of Audacity running. It will record for a specified time, stop recording, export the file
precisely time-stamped to the save directory, and close the track and do it all again. 

## Initial Setup
1. Follow the directions here: https://manual.audacityteam.org/man/scripting.html - Make sure you have python installed
2. Update config.py
3. Run run.py
4. To stop, you can close Audacity or hit Ctrl+C in your terminal

## Notes
1. I used a Windows 10 64-bit machine with Python 3.11.4 installed directly from the microsoft store
2. If you have issues with reading or writing to the pipe, make sure you have followed everything in step 1 correctly
