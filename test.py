import re

string = "JoJo_s Bizarre Adventure Stardust Crusaders - 25 - _The Fool_ Iggy and _Geb_ N_Doul, Part 1"
print(string[-8:])
print(re.split(r' - ',string))
#print(re.search(r'(?<=\d( |_|\.|)(|-)(| )).*',string))
newstr = re.sub(r'_',' ',string)
nnewstr = re.sub(r'  ',' ',newstr)
print(newstr)
print(nnewstr)
