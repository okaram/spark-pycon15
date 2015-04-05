import os
import re

from itertools import chain

word_separators="[; >:,\.]"
def flatmap(f,list):
	return chain.from_iterable(map(f,list))

def path_to_folder(path):
	fields=path.split(os.sep) # os.sep is / for unix, \\ for Windows
	return fields[len(fields)-2]

def file_to_words(fileContents):
	lines=fileContents.splitlines()
	# find first empty line and go from there
	firstEmpty=lines.index("")
	useful_lines=lines[firstEmpty+3:len(lines)]
	return filter(lambda x: x.isalnum(),flatmap(line_to_words,useful_lines))

def line_to_words(line):
	return filter(lambda x: x!="",re.split(word_separators,line))
