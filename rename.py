#!/usr/bin/python
import os,re
path = '../S01/'
files = os.listdir(path)
season_num='01'
offset = 0

for f in files:
    # skip all files which are not .mp4
    if not f.endswith(".avi"):
        continue

    # find the first number in the filename
    matches = re.findall("\d+", f)
    if not len(matches):
       print "skipping", f
    num = int(matches[0])

    ep_num = num-offset
    
    if(ep_num<10):
        ep = "0"+str(ep_num)
    else:
        ep = str(ep_num)

    mm = re.findall("(.*) - (.*)",f)
    name = mm[0][1]


    new_file_name = "S%s-E%s-%s" % (season_num, ep,name)
    print "%s ==> %s" % (f, new_file_name)
    #Rename when you are ready with the results
    os.rename(path+f, path+new_file_name)


print "Done"