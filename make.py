#!/usr/bin/env python

import os
import fnmatch
import subprocess

import render

def mkdir(dirname):

	try:
		os.makedirs(dirname)
	except OSError as err:
		pass

def glob(pat, directory = '.'):
	for root, dirnames, filenames in os.walk('src'):
		for filename in fnmatch.filter(filenames, pat):
			yield os.path.join(root, filename)


def subst(strings, pat1, pat2):
	for s in strings:
		yield s.replace(pat1, pat2)
		

# gather files

md_files = list(glob('*.md'))
dot_files = list(glob('*.dot'))

html_files = list(subst(md_files, '.md', '.html'))
png_files = list(subst(dot_files, '.dot', '.png'))


head1 = "<head><link href=\"http://kevinburke.bitbucket.org/markdowncss/markdown.css\" rel=\"stylesheet\"></link>"
head2 = "<script type=\"text/javascript\"src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script></head>"


print md_files
print html_files

for d,p in zip(dot_files, png_files):
	
	p = 'build/' + p

	dirname,_ = os.path.split(p)
	mkdir(dirname)

	

	print 'd:', d
	print 'p:', p
	print 'dirname:', dirname

	call = ["dot", d, "-Tpng", "-o" + p]

	print 'call:', call

	subprocess.call(call)

for m,h in zip(md_files, html_files):

	h = 'build/' + h

	dirname,_ = os.path.split(h)
	mkdir(dirname)
	
	with open(h, 'w') as f:
		f.write(head1)
		f.write(head2)

	render.render(m,h)

	#call = ['python', 'render.py ' + m + ' ' + h]
	
	#subprocess.call(call)
	
	




