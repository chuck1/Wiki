import markdown
import argparse
import re
import os
import jinja2

parser = argparse.ArgumentParser()
parser.add_argument('md_file')
parser.add_argument('html_file')

args = parser.parse_args()

# read md file

with open(args.md_file, 'r') as f:
	md_str = f.read()

#md_dir = os.path.dirname(args.md_file)
#m = re.findall('\[.*?\]\((.*?)\)',md_text)
#for s in m:
#	src = os.path.join(md_dir, s)
#	print repr(src)


# separate sidebar from center

pat = re.compile('^&&&$', flags=re.MULTILINE)

m = pat.search(md_str)

if m:
	md_sidebar_str = md_str[:m.start(0)]
	md_center_str = md_str[m.end(0):]
else:
	md_sidebar_str = 'sidebar'
	md_center_str = md_str

html_sidebar_str = markdown.markdown(md_sidebar_str, extensions=['extra', 'tables'])
html_center_str = markdown.markdown(md_center_str, extensions=['extra', 'tables'])

# read template string from file

with open('template.html', 'r') as f:
	temp_str = f.read();

template = jinja2.Template(temp_str)

# render template

html_str = template.render(sidebar_str=html_sidebar_str, center_str=html_center_str)

# write html file

with open(args.html_file, 'w') as f:
	f.write(html_str)



