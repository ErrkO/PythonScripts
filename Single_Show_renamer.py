import shutil, os, re

def GetEpisodeNameFromEpisode(episode):
    return re.split(' - ',episode)[2]

def FixPart(episode):
    if ", Part" in episode:
        size = len(episode)
        newname = episode[0:size-8]
        newpart = " - " + episode[-6:]
        return newname + newpart
    else:
        return episode

def GetEpisodeNameWithNoExtension(episode):
    size = len(episode)
    return episode[0:size-4]

def GetEpisodeNameFromUser():
    episodename = input("Please enter the episode name: ")

    while not ContainsBadChars(episodename):
        print("Please enter a valid episode name")
        episodename = input("Please enter the episode name: ")

    return episodename

def CopyAndRename(file,newfile):
    shutil.copy(file,newfile)
    print("Copied " + file + " to " + newfile)

def GetEpisodeNumberByUser():
    enumber = input("Please enter the episode number: ")

    while not is_Number(enumber):
        print("Please enter a valid number")
        enumber = input("Please enter the episode number: ")

    return "e" + enumber

def GetEpisodeNumberByIndex(episode,index):
    numbers = re.findall(r'\d+',episode)

    enumber = numbers[index]

    return "e" + enumber

def GetEpisodeNumberIndex(episode):
    print(episode)
    numbers = re.findall(r'\d+',episode)
    #print(re.findall(r'\d+',episode))
    #print(numbers)

    i = 0

    for number in numbers:
        linenumber = i+1
        print(str(linenumber) + ". " + str(number))
        i = linenumber

    choice = input("Please enter the number you want to use: ")

    ic = -1

    while not is_Number(choice) and not isValidChoice(ic,i):
        print("Please enter a valid number")
        choice = input("Please enter the number you want to use: ")
        if is_Number(choice):
            ic = int(choice)

    ichoice = int(choice) - 1

    return ichoice

def GetEpisodeNumber(episode):
    print(episode)
    numbers = re.findall(r'\d+',episode)
    #print(re.findall(r'\d+',episode))
    #print(numbers)

    i = 0

    for number in numbers:
        linenumber = i+1
        print(str(linenumber) + ". " + str(number))
        i = linenumber

    choice = input("Please enter the number you want to use: ")

    ic = -1

    while not is_Number(choice) and not isValidChoice(ic,i):
        print("Please enter a valid number")
        choice = input("Please enter the number you want to use: ")
        if is_Number(choice):
            ic = int(choice)

    ichoice = int(choice)

    enumber = numbers[ichoice-1]

    return "e" + enumber

def GetShowName():
    showname = input("Please enter the show name: ")

    while not ContainsBadChars(showname):
        print("Please enter a valid show name")

        showname = input("Please enter the show name: ")     
        
    return showname

def GetSeasonNumber():

    snumberstr = input("Please enter the season number: ")

    while not is_Number(snumberstr):

        print("Please enter a valid number")

        snumberstr = input("Please enter the season number: ")

    snumber = "s" + snumberstr
        
    return snumber

def GetExtension(episode):
    return episode[-4:]

def CreateNewEpisodeName(showname,snumber,enumber,ename,extension):
    return showname + " - " + snumber + enumber + " - " + ename + extension

def is_Number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def isValidChoice(choice,index):
    if choice <= index and choice >= 0:
        return True
    else:
        return False

def isValidChoicestr(choice):
    if "y" in choice or "Y" in choice:
        return True
    else:
        return False

def ContainsBadChars(str):
    badcharacters = ["\\","/",":","\"","*","|",",","="]

    if str in badcharacters:
        return False
    else:
        return True

def ClearScreen():
    print("\n" * 100)

def ChangePart(showname,snumber,enumber,ename,extension):
    flag = False
    ic = -1

    while not flag:
        print("1. Show Name")
        print("2. Season Number")
        print("3. Episode Number")
        print("4. Episode Name")
        choice = input("Which part do you want to change? ")

        while not is_Number(choice) and not isValidChoice(ic,4):
            print("Please enter a valid number")
            choice = input("Please enter the number you want to use: ")
            if is_Number(choice):
                ic = int(choice)

        ichoice = int(choice)

        if ichoice is 1:
            newsname =  GetShowName()
            newsnumber = snumber
            newenumber = enumber
            newename = ename
        elif ichoice is 2:
            newsname =  showname
            newsnumber = GetSeasonNumber()
            newenumber = enumber
            newename = ename
        elif ichoice is 3:
            newsname =  showname
            newsnumber = snumber
            newenumber = GetEpisodeNumberByUser()
            newename = ename
        elif ichoice is 4:
            newsname =  showname
            newsnumber = snumber
            newenumber = enumber
            newename = GetEpisodeNameFromUser()

        oldname = CreateNewEpisodeName(showname,snumber,enumber,ename,extension)
        newname = CreateNewEpisodeName(newsname,newsnumber,newenumber,newename,extension)

        print("Old Name: " + oldname)
        print("New Name: " + newname)
        choice = input("Is the new name correct? (Y/n): ")

        if isValidChoicestr(choice):
            return newname

def Match(regex,string):
    if re.search(regex,string) is not None:
        return True
    return False

def RemoveUnderScore(file):
    if "_" in file:
        newstr = re.sub(r'_',' ',file)
        nnewstr = re.sub(r'  ',' ',newstr)
        return nnewstr
    else:
        return file

def ConsistantFiles(episode):
    choice = input("Are the files consistant? (Y/n): ")

    if isValidChoicestr(choice):
        enchoice = GetEpisodeNumberIndex(episode)
        scrapechoice = input("Would you like to scrape the Episode name? (Y/n): ")
        return [enchoice,scrapechoice]

    else:
        return ["",""]

def RenameEpisodeLoop(showname,snumber,ep,choicearray,flag):

    ClearScreen()
    path = ".\\"
    episode = RemoveUnderScore(ep)

    if ".py" not in episode and not Match('.*[A-Za-z]* - s\d*e\d*',episode):
        
        ogname = ep
        if flag:
            enumber = GetEpisodeNumberByIndex(episode,choicearray[0])
        else:
            enumber = GetEpisodeNumber(episode)
        extension = GetExtension(episode)
        noextension = GetEpisodeNameWithNoExtension(episode)
        print(noextension)

        if flag:
            choice = choicearray[1]
        else:
            choice = input("Would you like to scrape the Episode name? (Y/n): ")

        if isValidChoicestr(choice):
            epname = GetEpisodeNameFromEpisode(noextension)
        else:
            epname = GetEpisodeNameFromUser()

        ogpath = path + ogname
        #print(ogpath)

        epname = FixPart(epname)
        
        newname = CreateNewEpisodeName(showname,snumber,enumber,epname,extension)
        print(newname)

        choice = input("Is this name correct? (Y/n): ")

        if not isValidChoicestr(choice):
            newname = ChangePart(showname,snumber,enumber,epname,extension)

        newpath = path + newname

        CopyAndRename(ogpath,newpath)

    else:
        print("Skipped " + episode)


def Main():

    showname = GetShowName()
    print(showname)
    snumber = GetSeasonNumber()
    print(snumber)
    flag = False

    for episode in os.listdir(".\\"):

        if not flag:
            choicearray = ConsistantFiles(episode)
            flag2 = True
            flag = True
        
        RenameEpisodeLoop(showname,snumber,episode,choicearray,flag2)

    print("Done")


Main()
