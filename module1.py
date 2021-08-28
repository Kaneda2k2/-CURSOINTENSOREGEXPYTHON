
#print(spam.strip())


##  SE ELIMINAN LOS ESPACIOS
##spam="                Hello,World                 "
##def deleteSpace(Cadena):
##    print(Cadena.strip())
##deleteSpace(spam)


#Expresiones regulares
##txt='415-555-4242'
##def isPhoneNumber(txt):
##    if len(txt) != 12:
##        return False
##
##    for i in range(0,3):
##        if not txt[i].isdecimal():
##            return False
##
##    if txt[3] != "-":
##        return False
##
##    for i in range(4,7):
##        if not txt[i].isdecimal():
##            return False
##    if txt[7] !="-":
##        return False
##
##    for i in range(8,12):
##        if not txt[i].isdecimal():
##            return False
##    return True
##
##
##print(isPhoneNumber(txt))
##
##
##
##message="call me at 412-232-4422 tomorrow . 415-555-9999"
##for i in range(len(message)):
##    chunk=message[i:i+12]
##    if isPhoneNumber(chunk):
##        print ("Phone number found:" + chunk)
##print("Done")


##
##import re
##
##phoneNumRegex = re.compile(r'(\d{3}-\d{3}-\d{4}?)')
##mo = phoneNumRegex.search('My number is 415-555-4242.  ')
##print('Phone number found: ' + mo.group())




#USANDO EXPRESIONES REGULARES
##import re
##
##heroRegex = re.compile(r"Batman|Tina Fey")
##
##mo1=heroRegex.search("Batman and Tina Fey")
##
##print(mo1.group())
##
##mo2 = heroRegex.search('Tina Fey and Batman')
##
##print(mo2.group())
##


##import re
##batRegex=re.compile(r"Bat(man|mobile|copter|bat)")
##
##mo = batRegex.search("Batmobile lost a wheel")
##
##
##print(mo.group())
##print(mo.group(1))
##
##
##import re
##
##batRegex=re.compile(r"Bat(wo)?man")
##mo1=batRegex.search("The Adventures of Batman")
##mo2=batRegex.search("The Adventures of Batwoman")
##print(mo1.group())
##print(mo2.group())


##import re
##phoneRegex = re.compile (r"(\d{3}-)?\d{3}-\d{4}")
##
##mo1=phoneRegex.search("My number is 415-123-2235")
##mo2=phoneRegex.search("My number is 123-2235")
##print(mo1.group())
##print(mo2.group())
##
##
##import re
##batRegex=re.compile(r"Bat(wo)*man")
##mo1=batRegex.search("The Adventures of Batwoman")
##mo2=batRegex.search("The Adventures of Batwowowowowowowoman")
##print(mo1.group())
##print(mo2.group())


##import re
###greedyMode
##greedyRegex=re.compile(r"(Ha){3,5}")
##mo1=greedyRegex.search("HaHaHaHa")
##print(mo1.group())
###nongreedyMode
##nomgreedyRegex=re.compile(r"(Ha){3,5}?")
##mo2=nomgreedyRegex.search("HaHaHaHa")
##print(mo2.group())

###########################REGEX CON FINDALL ################################

##import re
##phoneNumRegex=re.compile(r"\d{3}-\d{3}-\d{4}")
##mo=phoneNumRegex.search("cell:415-555-9999 Work: 212-555-0000")
##print(mo.group())
##phoneNumRegex1=re.compile(r"\d{3}-\d{3}-\d{4}")
##mo1=phoneNumRegex1.findall("cell:415-555-9999 Work: 212-555-0000")
##print(mo1)

##phoneNumRegex1=re.compile(r"\d{3}-\d{3}-\d{4}")
##mo1=phoneNumRegex1.findall("cell:415-555-9999 Work: 212-555-0000")
##print(mo1)

##import re
##phoneNumRegex1=re.compile(r"(\d{3})-(\d{3})-(\d{4})")
##mo1=phoneNumRegex1.findall("cell:415-555-9999 Work: 212-555-0000")
##print(mo1)

#TABLA DE CHARACTER CLASS
#\d --------------------- cualquier numero de 0 al 9
#\D----------------------Cualquier caracter que no sea de 0 al 9
#\w----------------------Cualquier letra,numero,digito " palabra"
#\W---------------------cualquiere caracheter que no sea letra,numero,o underscore
#\s --------------------cualquier space,tab,or newline character " " space characteres
#\S---------------------Cualquier character que no sea space.tab-o newline
###.------------->sirve para rellenar  r".at")   cat hat sap. etc
##^------------->ocurrir al prinpio del texto
##$----------------->ocurrir al final del texto
##*---------------------->zero o mas
##+......................>uno o mas
##?--------------------zero o uno del groupo
##The {n} matches exactly n of the preceding group.
## The {n,} matches n or more of the preceding group.
## The {,m} matches 0 to m of the preceding group.
## The {n,m} matches at least n and at most m of the preceding group.
## {n,m}? or *? or +? performs a non-greedy match of the preceding group.
## ^spam means the string must begin with spam.
## spam$ means the string must end with spam.
## The . matches any character, except newline characters.
## \d, \w, and \s match a digit, word, or space character, respectively.
##\D, \W, and \S match anything except a digit, word, or space character,
##respectively.
## [abc] matches any character between the brackets (such as a, b, or c).
## [^abc] matches any character that isn’t between the brackets.
##{
##}
##[
##]
##\
##|
##(
##)
##
##import re
##
##xmasRegex=re.compile(r"\d+\s\w+")
##print(xmasRegex.findall("12 drummers, 11 pippers,10 lords,9 l"))


########################MAKING YOUR OWN CHARACTER CLASESS
###Puedes defiinir tus clases usanso brackets
##import re
##vowelRegex=re.compile(r"[aeiouAEIOU]")
##m=vowelRegex.findall("Robocop eats baby food. BABY FOOD.")
##print(m)
########################################################

##import re
##begingWithHello = re.compile(r"^Hello")
##print(begingWithHello.search("Hello, World"))
##print(begingWithHello.search("He saud hello")== None)

##import re
##
##endsWithNumber=re.compile(r"\d$")
##m=endsWithNumber.search("oasdoafop a 3")
##a=endsWithNumber.search("your number is forty two.")==None
##print(m)
##print(a)

##import re
##
##wholeStringIsNum=re.compile("^\d+$")
##m=wholeStringIsNum.search("1234567890")
##a=wholeStringIsNum.search("12p´ç, 34567890")==None
##print(m,a)

###########################COMODINES ##################################
##import re
######
##atRegex = re.compile(r".at")
##m=atRegex.findall("The cat in the hat sat on the flat mat.")
##print(m)
##


##################HACIEMDO COMODIN DE TODO CON DOLLAR.
##import re
##nameRegex=re.compile(r"First Name: (.*) Last Name: (.*)")
##mo=nameRegex.search("First Name: Al Last Name: Sweigart")
##print(mo.group(1))
##print(mo.group(2))

##(.*?)
##import re
##noNewLineRegex=re.compile(".*")
##m=noNewLineRegex.search("Serve the public trust.\nPRotect the innocent.\nUphold the law.").group()
##print(m)
##
##
##newlineRegex=re.compile(".*",re.DOTALL)   # para incluir a continuacion de un salto de linea?
##a=newlineRegex.search("Serve the public trust.\nProtect the innocent,\nUphold the law.").group()
##print(a)




#######################################CASO INSENSITIVE MATCHING

##import re
##
##regex1=re.compile("RoboCop")
##regex2=re.compile("ROBOCOP")
##regex3=re.compile("robOcop")
##regex4=re.compile("RoboCop")
##
##robocop=re.compile(r"robocop", re.I)
##print(robocop.search("robocop is part man.parch magine").group())
##print(robocop.search("Robocop is part man.parch magine").group())
##print(robocop.search("RoboCop is part man.parch magine").group())

##############################CONTINUARA