import os
import shutil
os.system('python run.py gen')
try:
    os.mkdir("../submission")
except:
    print("The folder submission already created")

for file in os.listdir('../target'):
    src=os.path.join('../target',file)
    dest=os.path.join("../submission",file)
    shutil.copy(src,dest)

lexPath='test/LexerSuite.py'
parPath='test/ParserSuite.py'
d96='main/d96/parser/D96.g4'

shutil.copy(lexPath,'../submission/LexerSuite.py')
shutil.copy(parPath,'../submission/ParserSuite.py')
shutil.copy(d96,'../submission/D96.g4')