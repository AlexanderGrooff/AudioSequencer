# Audio Sequencer

## How it works
Works by putting .wav files in the `dist` directory, and executing the audiosequencer.exe. 
Every time the audiosequencer is run, it indexes any .wav files in the directory and saves these in the configuration file. 
After this, it runs the next .wav file that is up, and loops back to the start when it ran the whole list of saved .wav files.

When adding any new .wav files after already having ran the audiosequences, it will append these new files to the end of the list. 

## Build
Runs on Python 3.4.
Build via `python setup.py py2exe`
