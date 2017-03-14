#!/usr/bin/python

import os
import glob

# Paths containing icons we want

sources = ['Stellaris/gfx/interface/icons/ethics/',
           'Stellaris/gfx/interface/icons/governments/',
           'Stellaris/gfx/interface/icons/traits/',
           'Stellaris/gfx/interface/icons/traits/leader_traits/']

# Test echo of paths
# print(sources)

# Compiling a list of every dds file we're after

sourcefiles = []

for s in sources:
    sourcefiles.extend(glob.glob(s + '*.dds'))

print sourcefiles
