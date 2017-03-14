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

# Opening a file for the CSS and putting the header in
f = open('spritesheet.css', 'w')

f.write(""".flair {
    background: url(%%spritesheet%%) no-repeat -9999px;
    border: 0;
    padding: 0;
}
""")
f.close()

# Counter for checking sprite offsets
counter = 0

# Create files
for s in sourcefiles:
    print(s)
    cleanname = os.path.basename(os.path.splitext(s)[0]).replace('_', '-')
    # Append CSS section to file, using a heredoc is a little ugly....
    f = open('spritesheet.css', 'a')
    f.write(""".flair-{2} {{
    width: {0}px;
    height: {0}px;
    background-position: 0px {1}px;
}}
""".format(spritesize, spritesize*counter*-1,cleanname))
    subprocess.call(['convert', s, '-resize', '{0}x{0}'.format(spritesize), 'output/{0}.png'.format(cleanname)])
    counter +=1

# Ccompile files into spritesheet
spritesheet = subprocess.check_output(['convert', 'output/*.png', '-append', 'spritesheet.png'])
