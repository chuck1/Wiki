import sys
import re


# start to end or start to subgraph start
#reg1 = re.compile('^digraph {.*?[{}]', flags = re.DOTALL | re.MULTILINE)
reg1 = re.compile('^digraph {', flags = re.DOTALL | re.MULTILINE)

# subgraph start to (end | subgraph start | subgraph end)
reg2 = re.compile('.*?[{}]')

html = {
		'(?<=\w)\n':';',
		'(?<!\w)\n':'',
		'\s':'+',
		'=':'%3D',
		'>':'%3E',
		'\[':'%5B',
		'\]':'%5D',
		'_':'%5F',
		'"':'%22'
		}

def scan_close(str):
	print "scan_close \"{0}\"".format(repr(str))
	
	m = reg2.search(str)
	
	if m:
		e = m.end(0)
		body = str[:e]
		tail = str[e:]
		
		print "body {0}".format(repr(body))

		if body[-1] == '{':
			body2, tail = scan_close(tail)
			body3, tail = scan_close(tail)
			body = body + body2 + body3
		
		return body,tail
	else:
		ValueError('invalid graph')
	


def smoosh(lines):
	line = "".join(lines)
	line = re.sub('[\n\s]','',line)
	return line

def escape(line):
	for k,v in html.items():
		line = re.sub(k,v,line)
	return line

if len(sys.argv) < 3:
	print "usage: {0} <in> <out>".format(sys.argv[0])
	sys.exit(1)

with open(sys.argv[1],'r') as f:
	file = f.read()

while True:
	m = reg1.search(file)
	
	if not m:
		break

	s = m.start(0)
	e = m.end(0)

	head = file[:s]
	body = m.group(0)
	tail = file[e:]

	print "match",m.start(0),m.end(0),repr(str)
	
	
	
	body2, tail = scan_close(tail)
	body = body + body2
	
	
	
	
	print repr(body)

	body = escape(body)

	print repr(body)
	
	#print file
	
	prefix = "![](https://chart.googleapis.com/chart?cht=gv&chl="
	postfix = "&chs=450x450)"

	file = head + prefix + body + postfix + tail


with open(sys.argv[2], 'w') as f:
	f.write(file)


