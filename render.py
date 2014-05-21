import markdown
import argparse
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument('md_file')
parser.add_argument('html_file')

args = parser.parse_args()

with open(args.md_file, 'r') as f:
	md_text = f.read()

md_dir = os.path.dirname(args.md_file)

m = re.findall('\[.*?\]\((.*?)\)',md_text)

for s in m:
	src = os.path.join(md_dir, s)
	print repr(src)

html_text = markdown.markdown(md_text, extensions=['extra', 'tables'])

#print html_text

head = [
		"<head>\n",
		"<link href=\"http://kevinburke.bitbucket.org/markdowncss/markdown.css\" rel=\"stylesheet\"></link>\n",
		"<link href=\"http://web.engr.oregonstate.edu/~rymalc/default.css\" rel=\"stylesheet\"></link>\n",
		"<script type=\"text/javascript\"src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script>\n",
		"</head>"]

head = ''.join(head)

html_text = head + html_text

with open(args.html_file, 'w') as f:
	f.write(html_text)



