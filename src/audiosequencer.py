import os.path
import json
from glob import glob
import winsound

# Return last played file's index
def lastPlayedIndex(config):
    try:
        return config['storedFiles'].index(config['lastPlayed'])
    # Exceptions can occur when there's no song played before
    # Meaning that config['lastPlayed'] === None
    except ValueError:
        return -1

# Globals
CFG_FILENAME = 'config.json'
config = {'storedFiles': [], 'lastPlayed': None}

# Get config
if os.path.isfile(CFG_FILENAME):
    with open(CFG_FILENAME, 'r') as fp:
        config = json.load(fp)

# Add new audio files to config
for audiofile in glob('./*.wav'):
    if audiofile not in config['storedFiles']:
        config['storedFiles'].append(audiofile)

# Remove files from config that are no longer in directory
for old_audiofile in config['storedFiles']:
    if old_audiofile not in glob('./*.wav'):
        # Change last played if we're deleting this from config
        if old_audiofile == config['lastPlayed']:
            # Set lastPlayed to previous file, so it continues on to the file after the deleted file
            config['lastPlayed'] = config['storedFiles'][lastPlayedIndex(config) - 1]

        # Remove file from config
        del config['storedFiles'][config['storedFiles'].index(old_audiofile)]



# Get next audio file
config['lastPlayed'] = config['storedFiles'][(lastPlayedIndex(config) + 1) % len(config['storedFiles'])]


# Save last config
with open(CFG_FILENAME, 'w') as fp:
    json.dump(config, fp)

# Play audio
winsound.PlaySound(config['lastPlayed'], winsound.SND_FILENAME)
