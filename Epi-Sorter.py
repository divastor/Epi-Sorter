import re, os
from sys import argv

j = 1
n = input("Number of Episodes: ")
if n < 0:
    n = -n
while j <= n:
    # File name
    if j < 10:
        name = 'EPISODE 0' + str(j)
    else:
        name = 'EPISODE ' + str(j)
    # Already exists?
    try:
        os.mkdir(name)
    except:     
        pass
    
    j+=1
    
filenames = os.listdir(os.getcwd())
# - Get every file in directory
print filenames
for fn in filenames:
# - Check every file serially
    episode = re.findall(r'E\d{1,2}', fn, re.I)
    season = re.findall(r'S\d{1,2}', fn, re.I) #not that needful stuff
    if fn.lower() == "subtitles" or fn.lower() == "subs" or fn.lower() == "subtitle" or fn.lower() == "sub":
        fn_filenames = os.listdir(os.getcwd()+"\\"+fn)
        print fn_filenames
        for fnsfn in fn_filenames:
            try:
                episode = re.findall(r'E\d{1,2}', fnsfn, re.I)
                j = int(episode[0][1:])
                if j < 10:
                    name = 'EPISODE 0' + str(j)
                else:
                    name = 'EPISODE ' + str(j)

                os.rename(fn+"\\"+fnsfn, name+'\\'+fnsfn)
            except:
                pass

        continue
    
    try:
        j = int(episode[0][1:])
        if j < 10:
            name = 'EPISODE 0' + str(j)
        else:
            name = 'EPISODE ' + str(j)

        os.rename(fn, name+'\\'+fn)
    except:
        pass
    # Move corresponding episode to appropriate file (episodeName -> EPISODE XX\episodeName) 
    
    
