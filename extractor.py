#!/usr/bin/python

import glob
import subprocess
import base64

# Pillow can't read the DDS files
#from PIL import Image

# Size of each sprite (assuming square)
spritesize = 25

# Paths containing icons we want

sourcepaths = ['Stellaris/gfx/interface/icons/ethics/',
           'Stellaris/gfx/interface/icons/governments/',
           'Stellaris/gfx/interface/icons/traits/',
           'Stellaris/gfx/interface/icons/traits/leader_traits/']

# Test echo of paths
# print(sources)

# Compiling a list of every dds file we're after

sourcefiles = []

for s in sourcepaths:
    sourcefiles.extend(glob.glob(s + '*.dds'))

# We don't want the selection icons
sourcefiles.remove('Stellaris/gfx/interface/icons/ethics/ethic_selected.dds')
sourcefiles.remove('Stellaris/gfx/interface/icons/traits/trait_selected.dds')

# Test conversion to PNG

# Counter to ensure rational filenames
counter=0

# Create files
for s in sourcefiles:
    #print(s)
    subprocess.call(['convert', s, '-resize', str(spritesize)+'x'+str(spritesize), 'output/'+str(counter).zfill(4)+'.png'])
    counter += 1

# Ccompile files into spritesheet (as variable)
spritesheet = subprocess.check_output(['convert', 'output/*.png', '-append', 'png:-'])
print(base64.b64encode(spritesheet))
