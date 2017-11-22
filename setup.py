from distutils.core import setup
import py2exe

setup(
    name='AudioSequencer',
    windows=['src/audiosequencer.py'],
    options={
        'py2exe': {
            'compressed': True,
            'bundle_files': 1,
        }
    },
    zipfile = None
)