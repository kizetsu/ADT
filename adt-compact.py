#!/usr/bin/env python3

import os
import sys
import json
import config



def initTree():
    Tree = {}
    lsWebdir = 'ls '+config.WEBPATH
    DrupalDirs = []
    dirCount = 0

    dir = os.popen(lsWebdir).readlines()
    for x in range(0,len(dir)):
        if not "." in dir[x]:
            DrupalDirs.append(dir[x])

    for y in range(0,len(DrupalDirs)):
        lsDrupalDir = 'ls '+config.WEBPATH+'/'+DrupalDirs[y][:-1]
        thisDir = os.popen(lsDrupalDir).readlines()

        for item in thisDir:
            if 'sites' in item:
                actualDir = DrupalDirs[y][:-1]
                dirCount += 1
                Tree[actualDir] = { 'path': config.WEBPATH+actualDir }
                lsSite = 'ls '+Tree[actualDir]['path']+'/sites/'
                siteDir = os.popen(lsSite).readlines()
                sitesetup = False
                sites = []

                for z in range(0,len(siteDir)):
                    if not ("\." in siteDir[z] or 
                            "\.\." in siteDir[z] or
                            ".php" in siteDir[z] or
                            ".txt" in siteDir[z] or 
                            "all" in siteDir[z] or 
                            "default" in siteDir[z]):
                        sitesetup = True
                        sites.append(siteDir[z][:-1])
                if sitesetup:
                    Tree[actualDir]['setup'] = 'multisite'
                    Tree[actualDir]['sites'] = sites
                else:
                    Tree[actualDir]['setup'] = 'singlesite'
    return Tree



def writeTree(newTree):
    try:
        with open("data/Tree",'w') as StoreTree:
            json.dump(newTree, StoreTree)
        StoreTree.close()
    except IOError:
        print('WARNING: IO Exception Error: File "data/Tree" does not exist.')
        try:
            os.popen('touch data/Tree')
            writeTree(newTree)
        except IOError:
            print('ERROR: IO Exception Error: File "data/Tree" could not be touched')
            sys.exit(1)



def loadLog():
    # load log file if exist
    try:
        LogFile = open(config.LOGPATH+'adt.log')
    except IOError:
        print('WARNING: IO Exception Error: File "',config.LOGPATH,'adt.log" does not exist.')
        print('INFO: Creating new log file.')
        try:
            os.popen('touch '+config.LOGPATH+'adt.log')
        except IOError:
            print('ERROR: IO Exception Error: File "',config.LOGPATH,'adt.log" could not be touched')
            sys.exit(1)
    return LogFile



def loadTree():
    # load Tree
    try:
        TreeFile = open("data/Tree")
    except IOError:
        print('WARNING: IO Exception Error: File "data/Tree" does not exist.')
        print('INFO: Initialising new Tree.')
        TreeFile = initTree()
        writeTree(TreeFile)
    return TreeFile



def main():
    # load all needed files
    LogFile = loadLog()
    TreeFile = loadTree()
    # init actual Tree to check for updates
    iTree = initTree()
    writeTree(iTree)
    # close opened Files
    TreeFile.close()
    LogFile.close()



if __name__ == "__main__":
    main()



########################
#   Aufbau des Array   #
########################
#
#Tree = {
#    'Site1': {
#        'setup': 'single',
#        'sites': [
#            'site1.com',
#        ]
#    },
#    'Site2': {
#        'setup': 'multi',
#        'sites': [
#            'site2.com',
#            'site2.de',
#            'site2.ru'
#        ]
#    }
#}
