import glob, os, re
os.chdir("events")
variables=[]
vpath = {}
final = "### All the Variables ##\n\n"
for file in glob.glob("*.vsndevts"):
    f = open("C:/Users/username/Desktop/sevi/events/"+file, "r")
    data= f.read()
    for match in re.finditer("(?!\t).*= (?!\n\t{)", data):
        item= match.group(0).replace(" = ","")
        if item not in variables:
            variables.append(item)
            vpath[item] = "\t\tin file = " + file + "\n\t\t\tmatched from " + str(match.start()) + " to " + str(match.end()) + "\n"
        if item in variables:
            vpath[item] = vpath[item] + "\t\tin file = " + file + "\n\t\t\tmatched from " + str(match.start()) + " to " + str(match.end()) + "\n"
            
for item in variables:
    final=final + "\t" + item + ":\n" + vpath[item] + "\n"
f2 = open("C:/Users/username/Desktop/sevi/output.txt", "w")
f2.write(final)
f2.close()

