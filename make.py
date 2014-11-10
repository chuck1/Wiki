#!/usr/bin/env python

import os
import fnmatch

def glob(pat, directory = '.'):
	for root, dirnames, filenames in os.walk('src'):
		for filename in fnmatch.filter(filenames, pat):
			yield os.path.join(root, filename)



print list(glob('*.md'))


