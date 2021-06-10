'''

convenience functions to help speed up the work

'''

import os
import pickle as pl
import time
from copy import deepcopy

import inspect
# find path of the file doing the importing
for frame in inspect.stack()[1:]:
    if frame.filename[0] != '<':
        importing_dir = frame.filename
        break

class getpath(str):
    '''
If file lives in .../MtgFi/a/b/c.txt, just write:

getpath("a","b","c.txt")

this returns the path: .../MtgFi/a/b/c.txt


On Windows, both give you the same result:


getfile(r"\a\b\c.txt")
getfile("a","b","c.txt")

    '''
    def __new__(cls, *args, custom=False):
        if custom:
            paths = []
        else:
            paths = [os.path.dirname(importing_dir)]
        
        for arguments in args:
            if arguments == '..':
                paths[0] = os.path.split(paths[0])[0]
            else:
                paths.append(arguments)
        
        path = os.sep.join(paths)
        return str.__new__(cls, path)
    
    def __init(self):
        super().__init__(self)
    
    def add(self, *args):
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])
        return getpath(path, custom=True)
    
    def __truediv__(self, *args):
        '''
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])

        return getpath(path)
        '''
        current_path = deepcopy(self.__str__())

        paths = [current_path]
        
        for arguments in args:
            if arguments == '..':
                paths[0] = os.path.split(paths[0])[0]
            else:
                paths.append(arguments)
        
        path = os.sep.join(paths)
        return getpath(path, custom=True)
    
    def ls(self, *args):
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])

        files_and_stuff = os.listdir(path)
        
        return files_and_stuff
    
    def up(self, num, *args):
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])

        times_up = ['..' for i in range(num+1)]
        return getpath(path, *times_up, custom=True)


def pickle(data, path):
    '''
pickle(data, 'path/to/pickled/file')


    '''

    with open(path, 'wb') as file_handler:
        pl.dump(data,file_handler)


def unpickle(path):
    '''
unpickle('path/to/pickled/file')

    '''
    with open(path, 'rb') as file_handler:
        return pl.load(file_handler)


class Timer(object):
    '''

Useful for timing stuff

timer = Timer()

# first process
timer.start()
process1()
timer.stop()
print(timer.elapsed())

# second process
timer.start()
process2()
timer.stop()
print(timer.elapsed())

    '''
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()
    
    def stop(self):
        self.end_time = time.time()
        print(self.elapsed())
    
    def elapsed(self):
        return self.end_time - self.start_time


def make_folders(path):
    '''

make folders if the path doesn't exist
literally the same thing as os.mkdirs :)

    '''

    # use recursion to make folders

    if not os.path.exists(path):
        split_path = os.path.split(path)
        head = split_path[0]
        make_folders(head)

        os.mkdir(path)

    else:
        # once it finds the first existing folder
        # start making folders
        return'''

convenience functions to help speed up the work

'''

import os
import pickle as pl
import time
from copy import deepcopy

import inspect
# find path of the file doing the importing
for frame in inspect.stack()[1:]:
    if frame.filename[0] != '<':
        importing_dir = frame.filename

class getpath(str):
    '''
If file lives in .../MtgFi/a/b/c.txt, just write:

getpath("a","b","c.txt")

this returns the path: .../MtgFi/a/b/c.txt


On Windows, both give you the same result:


getfile(r"\a\b\c.txt")
getfile("a","b","c.txt")

    '''
    def __new__(cls, *args, custom=False):
        if custom:
            paths = []
        else:
            paths = [os.path.dirname(importing_dir)]
        
        for arguments in args:
            if arguments == '..':
                paths[0] = os.path.split(paths[0])[0]
            else:
                paths.append(arguments)
        
        path = os.sep.join(paths)
        return str.__new__(cls, path)
    
    def __init(self):
        super().__init__(self)
    
    def add(self, *args):
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])
        return getpath(path, custom=True)
    
    def __truediv__(self, *args):
        '''
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])

        return getpath(path)
        '''
        current_path = deepcopy(self.__str__())

        paths = [current_path]
        
        for arguments in args:
            if arguments == '..':
                paths[0] = os.path.split(paths[0])[0]
            else:
                paths.append(arguments)
        
        path = os.sep.join(paths)
        return getpath(path, custom=True)
    
    def ls(self, *args):
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])

        files_and_stuff = os.listdir(path)
        
        return files_and_stuff
    
    def up(self, num, *args):
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])

        times_up = ['..' for i in range(num+1)]
        return getpath(path, *times_up, custom=True)