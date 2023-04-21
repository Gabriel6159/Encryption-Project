'''
For some reason when I try to multiply two numbers on line 34, the program spits out an error
It says that charNum is a NoneType variable, and I have no idea why
'''
#Extras if time:
#	Spaces can be a range of numbers multiplied by key or a symbol not used
#	encryption thing in math module
#	add fancy user interface stuff
#Key is a class
charList=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z',',','.','?',' ','-',':',';','(',')','[',']',"'",'$','!','@','#','%','^','&','*','=','+','_','/','<','>','1','2','3','4','5','6','7','8','9','0']
translate=[96621, 85176, 51578, 40025, 85009, 68488, 47828, 59844, 77011, 14508, 87030, 52496, 24778, 75276, 10496, 72109, 92165, 55647, 71374, 26857, 69507, 46554, 40196, 61950, 64970, 16497, 31844, 50081, 46858, 89744, 55558, 16503, 87246, 37369, 92408, 12133, 30486, 40010, 85201, 28803, 66263, 38617, 69730, 11987, 54091, 56776, 14046, 46609, 81196, 21992, 46863, 78943, 12722, 54081, 46113, 90634, 19807, 79900, 51849, 89614, 58739, 80577, 78654, 72818, 15499, 23438, 13959, 83925, 73204, 51189, 49322, 87313, 72840, 54554, 10547, 78939, 39540, 95015, 79447, 45918, 71512, 87657, 24733, 46241, 92435, 63909, 49341, 57261]
class Key:
	def __init__(self,key,length,firstChar):
		self.key=key
		self.length=length
		self.firstChar=firstChar
	def keyNum(self):
		transKey=0
		for char in self.key:
			if char.isdigit():
				transKey+=charToInt(char)
		return transKey
	def getKey(self):
		return self.key
	def firstCharNum(self):
		return charToInt(self.firstChar)
#Gives each character a numerical value
def charToInt(char):
	for n in range(0,len(charList)):
		if char==charList[n]:
			return translate[n]
def intToChar(number):
	for n in range(0,len(translate)):
		if number==translate(n):
			return charList(n)
#Encodes numbers derived from characters
def charNumEncode(charNum):
	step1=charNum*keyObj.keyNum() #For some reason charNum is of type NoneType
	step2=keyObj.firstCharNum()**2
	step3=(step1+step2)/keyObj.firstCharNum()
	return step3
def charNumDecode(charNum):
	step1=charNum*key.Obj.firstCharNum()
	step2=step1-(keyObj.firstCharNum()**2)
	step3=step2/keyObj.keyNum()
	return step3
#Initializes variables
output=''
char=""
number=0
encodeNum=0

#User initializes these variables
print('This program allows you to Encrypt or Decrypt a specified file. It only accepts .txt files. You can also specify whether the original file should be deleted or not. \n')
encodeDecode=input('Encrypt or Decrypt? (E or D): ')
#key=input('Enter Key: ')
key='32df9v0283uj' #Hardcoded Key
keyObj=Key(key,len(key),key[0])
filename='EncodeThis'#input('Enter File Name (do not add extension): ')
filename=filename+'.txt'
eraseFile='N'#input('Erase original file? (Y or N): ')
userFile=open(filename,'r')

#Reads and encodes selected file
if encodeDecode=='E' or encodeDecode=='e':
	for line in userFile:
		for char in line:
			if char!=None:
				number=charToInt(char)
				encodedChar=charNumEncode(number)
				output+=str(encodedChar)+' '
else:
	for line in userFile:
		userFileContent=line.split()	
		for item in userFileContent:
			if item!=None:
				decodedChar=charNumDecode(item)

#Cleaning up
if eraseFile=='Y' or eraseFile=='y':
	userFile=open(filename,'w')
	userFile.write(' ')
	userFile.close()
if encodeDecode=='E' or encodeDecode=='e':
	status='Encrypted'
else:
	status='Decrypted'
outFileName=status+filename
outFile=open(outFileName,'w')
print(filename,status,' with key: ',keyObj.key)

#Clears Variables and closes files
userFile.close()
d = dir()
for var in d:
	if not var.startswith('__'):
		del globals()[var]


