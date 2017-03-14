#!/usr/bin/python

import glob
import subprocess
import os

# Size of each sprite (assuming square)
spritesize = 25

# Paths containing icons we want

sourcepaths = ['Stellaris/gfx/interface/icons/ethics/',
           'Stellaris/gfx/interface/icons/governments/',
           'Stellaris/gfx/interface/icons/traits/',
           'Stellaris/gfx/interface/icons/traits/leader_traits/']

# Compiling a list of every dds file we're after

sourcefiles = []

for s in sourcepaths:
    sourcefiles.extend(glob.glob(s + '*.dds'))

# We don't want the selection icons
sourcefiles.remove('Stellaris/gfx/interface/icons/ethics/ethic_selected.dds')
sourcefiles.remove('Stellaris/gfx/interface/icons/traits/trait_selected.dds')

# Create files
for s in sourcefiles:
    subprocess.call(['convert', s, '-resize', str(spritesize)+'x'+str(spritesize), 'output/'+os.path.basename(os.path.splitext(s)[0]).replace('_', '-')+'.png'])

# Ccompile files into spritesheet (as variable)
spritesheet = subprocess.check_output(['convert', 'output/*.png', '-append', 'spritesheet.png'])
