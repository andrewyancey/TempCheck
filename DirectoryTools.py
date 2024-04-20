import pathlib as pl
import os

def EnsureDirectory(path):
 
    dir = pl.Path(os.path.split(path)[0])
    file = pl.Path(path)

    if dir.exists() == False:
        print('path does not exist, creating path: ' + str(dir))
        dir.mkdir(parents=True, exist_ok=True)

    if file.exists() == False:
        print('file does not exist, creating file: ' + str(file))
        open(file, 'x')

        
