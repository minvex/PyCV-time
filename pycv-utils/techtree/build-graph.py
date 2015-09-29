from os import listdir
from os.path import isdir
import importlib
import sys

dirname = "../../experiments/"
for algorithm in listdir('algorithms'):
	#buildTree = getattr(algorithm, 'main'
	if isdir("algorithms/" + algorithm):
		m = importlib.import_module("algorithms." + algorithm + ".main") 
		b = m.main(dirname)
		with open("graphs/" + algorithm + ".json", 'w') as f:
			f.write(b.graph)
#for algo in "./algorithms":
#	exec algo > ( "./graphs/" + algo + ".json" )