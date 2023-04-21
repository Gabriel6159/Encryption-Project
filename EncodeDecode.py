'''
For some reason when I try to multiply two numbers on line 38, the program spits out an error
It says that charNum is a NoneType variable, and I have no idea why
'''
#Extras if time:
#	Spaces can be a range of numbers multiplied by key or a symbol not used
#	encryption thing in math module
#	add fancy user interface stuff
#Key is a class
charList=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z',',','.','?',' ','-',':',';','(',')','[',']',"'",'$','!','@','#','%','^','&','*','=','+','_','	','/','<','>','1','2','3','4','5','6','7','8','9','0']
translate=[62870, 28843, 74415, 79187, 76794, 54492, 87980, 42159, 48728, 67409, 64116, 99315, 10236, 40528, 14389, 80359, 61460, 15988, 14228, 74688, 95523, 60498, 90755, 55723, 33767, 18099, 85402, 24640, 56315, 67634, 58253, 32566, 41366, 10016, 91929, 78292, 54453, 69143, 53827, 81241, 81176, 72843, 88030, 54877, 21789, 77985, 37618, 60138, 85550, 39229, 58116, 80927, 29307, 78299, 86306, 13533, 98228, 98175, 84568, 71261, 60879, 99984, 66576, 27513, 23978, 79640, 13388, 37810, 15164, 69054, 12469, 32458, 13139, 66883, 61423, 68991, 36234, 40576, 74661, 25283, 30795, 75537, 18427, 24259, 98192, 71752, 92272, 11527, 65589]
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
#Gives each item a corresponding character or integer with a for loop
def charToInt(char):
	for n in range(0,len(charList)):
		if char==charList[n]:
			return translate[n]
def intToChar(number):
	for n in range(0,len(translate)):
		if number==translate[n]:
			return charList[n]
#Encodes numbers derived from characters
def charNumEncode(charNum):
	print(charNum)
	step1=charNum*keyObj.keyNum() #For some reason charNum is of type NoneType
	step2=keyObj.firstCharNum()**2
	step3=(step1+step2)/keyObj.firstCharNum()
	return step3
def charNumDecode(charNum):
	step1=float(charNum)*keyObj.firstCharNum()#Entire decrypted file was none
	step2=step1-(keyObj.firstCharNum()**2)
	step3=step2/keyObj.keyNum()
	return step3
#Initializes variables
output=''
char=""
number=0
encodeNum=0

#User must initialize these variables
print('This program allows you to Encrypt or Decrypt a specified file. It only accepts .txt files. You can also specify whether the original file should be deleted or not. \n')
encodeDecode=input('Encrypt or Decrypt? (E or D): ')
#key=input('Enter Key: ')
key='32df9v0283uj' #Hardcoded Key
keyObj=Key(key,len(key),key[0])
filename='EncodeThis'#input('Enter File Name (do not add extension): ')
filename+='.txt'
eraseFile='N'#input('Erase original file? (Y or N): ')
userFile=open(filename,'r')

#Reads selected file and sends each character through translator
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
				output+=str(intToChar(decodedChar))
#Cleaning up old files
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
outFile.write(output)
outFile.close()
print(filename,status,' with key: ',keyObj.key)

#Clears Variables and closes files
userFile.close()
d = dir()
for var in d:
	if not var.startswith('__'):
		del globals()[var]


