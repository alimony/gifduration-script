#!/usr/bin/env python
# encoding: utf-8
"""
This script takes an animated GIF file as input and calculates its total
duration, or zero for non-animated GIF files.

Requires the Python Imaging Library (PIL).

Code by Markus Amalthea Magnuson <markus.magnuson@gmail.com>
"""

import sys
import os.path
import Image


if (len(sys.argv) > 1):
    path = sys.argv[1]
else:
    sys.exit("You must specify an input file as first argument.")

im = Image.open(path)
durations = []

try:
    while 1:
        durations.append(im.info["duration"])
        im.seek(im.tell() + 1)
except EOFError:
    for index, duration in enumerate(durations):
        print "Frame %d: %d ms (%0.2f seconds)" % (index + 1, duration, duration / 1000.0)
    print "---"
    total_duration = sum(durations)
    print "Total duration of %s: %d ms (%0.2f seconds)" % (os.path.basename(path), total_duration, total_duration / 1000.0)
