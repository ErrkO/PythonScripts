import shutil, os, re, datetime

def Match(regex,string):
    if re.search(regex,string) is not None:
        return True
    return False

def RenameFile(file,rename,log):
    #shutil.move(file,rename)
    #print("Renamed " + file + " to " + rename)
    log.write("Renamed " + file + " to " + rename)

def BuildNewFileName(showname,snum,episode):
    if not Match('.*[A-Za-z]* - s\d*e\d*',episode):

        part = ""
        
        enumber = re.findall(r'\d+',episode)
        if len(enumber) > 1:
            for index in enumber:
                if len(index) >=3:
                    if int(index) >= 100:
                        eptag = "e" + index
                    else:
                        eptag = "e" + index[1:3]
                else:
                    eptag = "e" + enumber[1]
        else:
            eptag = "e" + enumber[0]
            
        print(Match('\d+[A|B]',episode))
        if Match('\d+[A|B]',episode):
            print(episode)
            if Match('\d+A',episode):
                part = "pt1"
            elif Match('\d+B',episode):
                part = "pt2"

        extension = re.search('\.[a-z]{3}',episode)[0]

        noextension = re.split('\.[a-z]{3}',episode)[0]
        shorter = re.split('(\d+\. |\. |\.\d+ - |\d+\.)+',noextension)

        sindex = len(shorter)-1

        print(shorter)
        print(shorter[sindex])
        print(episode)

        if part not in "":
            newfilename = showname + " - " + snum + eptag + " - " + shorter[sindex] + " - " + part + extension
        else:
            newfilename = showname + " - " + snum + eptag + " - " + shorter[sindex] + extension
        print(newfilename)
        return newfilename

    else:
        return ""

for folder in os.listdir(".\\"):

        print("")

        now = datetime.datetime.now()

        date_str = now.year + '-' + now.month + '-' + now.day

        log = open("log-" + date_str + ".txt",'r+b')
        
        if ".py" in folder:
            folder

        elif "Looney" not in folder:
            
            showname = folder
            path = ".\\" + showname

            for season in os.listdir(path):

                print("")
                
                snumber = re.findall(r'\d+',season)
                stag = "s" + snumber[0]
                seasonpath = path + "\\" + season

                for episode in os.listdir(seasonpath):

                    eppath = seasonpath + "\\" + episode

                    newfilename = BuildNewFileName(folder,stag,episode)

                    if newfilename not in "":
                        nfnpath = seasonpath + "\\" + newfilename
                        RenameFile(eppath,nfnpath,log)

exit = input("Press any key to continue...")