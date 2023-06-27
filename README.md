# audacityscriptproject
Project that runs a script with audacity

This program assumes you have an instance of Audacity running. It will record for a specified time, stop recording, export the file
precisely time-stamped to the save directory, and close the track and do it all again. 

## Initial Setup
1. Follow the directions here: https://manual.audacityteam.org/man/scripting.html - Make sure you have python installed
The main part of these directions I just decided to paste jere:

Enable mod-script-pipe
The plugin module "mod-script-pipe" is not enabled by default in Audacity, so must be enabled in Audacity preferences.

After enabling it for the first time, you will need to restart Audacity. You can then check that it is enabled and was started by revisiting the preferences page.

Run Audacity
Go into Edit > Preferences > Modules
Choose mod-script-pipe (which should show New) and change that to Enabled.
Restart Audacity
Check that it now does show Enabled.
This establishes that Audacity is finding mod-script pipe, and that the version is compatible.

3. Update config.py
4. Run run.py
5. To stop, you can close Audacity or hit Ctrl+C in your terminal

## Notes
1. I used a Windows 10 64-bit machine with Python 3.11.4 installed directly from the microsoft store
2. If you have issues with reading or writing to the pipe, make sure you have followed everything in step 1 correctly
