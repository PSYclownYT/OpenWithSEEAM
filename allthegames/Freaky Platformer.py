import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

os.chdir("../GameAssets/CrueltyMaze/28_finish")
os.system('python main.py')
