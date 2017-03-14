# Stellaris Flair Generator

Stellaris is a space-based Grand Strategy game by Paradox Interactive. Like many games it has a community on Reddit. /u/Brolom suggested that flairs (selectable avatars) might be a nice feature.

Having done some work before trying to extract flags from Europa Universalis IV (another Paradox title) I had some code fragments lying around which work processing these

## Usage

You'll need 
* ImageMagick on your command line
* A copy of the Stellaris base game in a folder called 'Stellaris' at the same level as the script (this is the same contents as C:\Program Files (x86)\Steam\steamapps\common\Stellaris for Steam on Windows users)
* An emtpy dir called 'output' at that same level for temporary PNG files

When run extractor.py produces a veritcal spritesheet based on all the folders listed in the 'sourcepaths' argument.

## Current Extractions

Currently (based on path name) the spritesheet output should contain the icons for 

* Ethics (aka Ethos)
* Governments
* Traits
* Leader Traits

## Current Environment

This script is running on my NAS (CentOS 7) with Python 2.7 and ImageMagick (from EPEL) doing most of the heavy lifting. I did try using Pillow but it didn't like the DDS format, I don't know if that's my error, a shortcoming of DDS support in Pillow, or something awry with the files themselves.

## Future improvements
* More sprites
* ~~More easily changed sprite size~~
* CSS generator for Reddit
* Keep names of files
* Removing need for temp files
* Use of PIL/Pillow?
* Source paths in a config file?
