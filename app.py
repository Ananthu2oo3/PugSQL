'''
Created on: 2023-02-24

@author: Ananthakrishnan.G

source:     
    https://pugsql.org/tutorial
'''

import pugsql
import pathlib
import sqlite3 



def startpy():

    queries = pugsql.module(f'{pathlib.Path(__file__).parent.resolve()}/queries/')
    # print(queries)
    queries.connect('sqlite:///test.db')

    queries.create()

    queries.insert(name="test", enter="7:00", exit="12:00")
    queries.insert(name="Santhosh", enter="8:00", exit="12:00")
    queries.insert(name="Baghya", enter="7:30", exit="11:00")
    
    data=(queries.printall())
    for i in data:
        print(i)
    
    
    

if __name__ == '__main__':
    startpy()




