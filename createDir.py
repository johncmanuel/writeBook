import sys
import os
import subprocess
from dotenv import load_dotenv

""" Command: novel <book name> """

load_dotenv()
BOOK_DIR = os.getenv('BOOK_DIR')
TEMPLATES_DIR = os.getenv('TEMPLATES_DIR')
PATH_TO_WORD = os.getenv('PATH_TO_WORD')

folderName = ' '.join(sys.argv[1:])

# Get all file names in templates folder. Use the list as keys for 
# a dictionary containing the values of the appropiate sizes. The user
# can choose from the dictionary which size to use for their books manuscripts.
getFileNames = [f for f in os.listdir(TEMPLATES_DIR) if os.path.isfile(os.path.join(TEMPLATES_DIR, f))]

# This list comprehension removes the file extension names, measurements, 
# and any spaces in between, if any.
getFileNamesAfterFilter = [(os.path.splitext(f)[0]).replace(' ', '').replace('in', '') for f in getFileNames]

sizes = dict(zip(getFileNamesAfterFilter, getFileNames))

novelDir = BOOK_DIR + "\\" + folderName + '\\'

if os.path.exists(novelDir):
    print('Name already taken in your directory.') 
    print('Choose another name or remove the directory that\'s taken.')
    sys.exit()

print('Available book sizes (in inches): ')
print('============================')
for key in sizes:
    print(key)
print('============================')

getSize = input('\nChoose which size you want:')

def copyFileToDir(dictValue, dst):
    from shutil import copy
    src = TEMPLATES_DIR + '\\' + dictValue
    copy(src, dst)

# Create directory in folder
os.mkdir(novelDir)
os.chdir(novelDir)

try:
    getNameOfTemplate = sizes[getSize]
except KeyError:
    print('Please enter the exact size next time!')
    quit()

getNameOfNewFile = novelDir + '\\' + folderName + '.docx' 

copyFileToDir(getNameOfTemplate, novelDir)
os.rename(novelDir + '\\' + getNameOfTemplate, getNameOfNewFile)

print('\n==========================')
print(f'{folderName} created in directory: {novelDir}.')
print('Have fun writing! :))')
print('==========================')

subprocess.Popen([PATH_TO_WORD, getNameOfNewFile])
