FilesRenamer
============

Basic implementation of files renamer based on python using regular expressions.

http://www.andresgonzalez.co

How to use it
=============

Clone the repo inside the folder you want to rename files.

Example:

I have a folder with the following folders inside:

S01  S02  S03  S04  S05

1) Clone the repo to have something like this:

FilesRenamer  S01  S02  S03  S04  S05

2) To edit files inside S01 edit Filesrenamer/rename.py and edit the following parameters

path = '../S01/'
season_num='01'
offset = 0

3)Execute the python script:

python rename.py

4) You will have files Converted from:

Anything 99 - Title.extension => S01-E99-Title.extension

5) It will display how the files will be renamed.

6) If you are ready with results, uncomment the following line:

    #Rename when you are ready with the results
    os.rename(path+f, path+new_file_name)
    
7) Enjoy!
