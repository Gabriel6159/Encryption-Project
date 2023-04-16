#Goal- Let cars, truck, and motorcycle class inherit from Vehicle and be able to add them to VehicleInventory
#Issue- too many arguements when attempting to use super()

#Global variables for price calculation
tax=1.065
liscensePlate=15.50
motorPlate=13.50
dealerMarkup=2000
title=8.25

#Classes
class Vehicle:
	def __init__(self,make,model,year,VIN,price):
		self.make=make
		self.model=model
		self.year=year
		self.VIN=VIN
		self.price=price
#	Getters	
	def getMake(self):
		return self.make
	def getModel(self):
		return self.model
	def getYear(self):
		return self.year
	def getVIN(self):
		return self.VIN
	def getPrice(self):
		return self.price
#	Setters
	def setMake(self,newMake):
		self.make=newMake
		print('Done')
	def setModel(self,model):
		self.model=model
		print('Done')
	def setYear(self,newYear):
		self.year=newYear
		print('Done')
	def setVIN(self,newVIN):
		self.VIN=VIN
		print('Done')
	def setPrice(self,newPrice):
		self.price=newPrice
		print('Done')
#	Methods
	def display_details(self):
		print (
		'Make: '+self.make+'\n',
		'Model: '+self.model+'\n',
		'Year: '+str(self.year)+'\n',
		'VIN: '+str(self.VIN)+'\n',
		'Price: '+str(self.price)
		)

class Car(Vehicle):
	def __init__(self,make,model,year,VIN,price,doorCount,fuelType):
		self.doorCount=doorCount
		self.fuelType=fuelType
		super().__init__(self,make,model,year,VIN,price)
#	Getters	
	def getDoorCount(self):
		return self.doorCount
	def getFuelType(self):
		return self.fuelType
#	Setters
	def setDoorCount(self,newCount):
		self.doorCount=newCount
		print('Done')
	def setFuelType(self,newType):
		self.fuelType=newType
		print('Done')
#	Methods
	def calculatePrice(self):
		return (self.price*tax)+liscensePlate+title
	def display_details(self):
		print (
		'Make: '+self.make+'\n',
		'Model: '+self.model+'\n',
		'Year: '+str(self.year)+'\n',
		'VIN: '+str(self.VIN)+'\n',
		'Price: '+str(self.price)+'\n',
		'Doors: '+str(self.doorCount)+'\n',
		'Fuel: '+self.fuelType
		)
class Truck(Vehicle):
	def __init__(self,make,model,year,VIN,price,bedLength,dually):
		self.bedLength=bedLength
		self.dually=dually
		super().__init__(self,make,model,year,VIN,price)
#	Getters
	def getBedLength(self):
		return self.bedLength
	def getDually(self):
		return self.dually
#	Setters
	def setBedLength(self,newLength):
		self.bedLength=newLength
		print('Done')
	def setDually(self,newDually):
		self.dually=newDually
		print('Done')
#	Methods
	def calculatePrice(self):
		return (self.price*tax)+liscensePlate+title
	def display_details(self):
		print (
		'Make: '+self.make+'\n',
		'Model: '+self.model+'\n',
		'Year: '+str(self.year)+'\n',
		'VIN: '+str(self.VIN)+'\n',
		'Price: '+str(self.price)+'\n',
		'Bed Length: '+str(self.bedLength)+'\n',
		'Dually?: '+self.dually
		)
class Motorcycle(Vehicle):
	def __init__(self,make,model,year,VIN,price,topSpeed,wheels):
		self.topSpeed=topSpeed
		self.wheels=wheels
		super().__init__(self,make,model,year,VIN,price)
#	Getters
	def getTopSpeed(self):
		return self.topSpeed
	def getWheels(self):
		return self.wheels
#	Setters
	def setTopSpeed(self,newSpeed):
		self.topSpeed=newSpeed
		print('Done')
	def setWheels(self,newWheels):
		self.wheels=newWheels
		print('Done')
#	Methods
	def calculatePrice(self):
		return (self.price*tax)+motorPlate+title+dealerMarkup
	def display_details(self):
		print (
		'Make: '+self.make+'\n',
		'Model: '+self.model+'\n',
		'Year: '+str(self.year)+'\n',
		'VIN: '+str(self.VIN)+'\n',
		'Price: '+str(self.price)+'\n',
		'Top Speed: '+str(self.topSpeed)+'\n',
		'Wheels: '+str(self.wheels)
		)
class VehicleInventory:
	def __init__(self,inventory=[]):
		self.inventory=inventory
	def getVehicleInventory(self):
		return self.inventory
	def addVehicle(self,newVehicle):
		self.inventory.append(newVehicle)
	def removeVehicle(self,removeVehicle):
		for item in self.inventory:
			if item==remove:
				self.inventory.remove(removeVehicle)
				print('Done')


f150_Lightning=Vehicle('Ford','F-150 Lightning',2023,1893904904,55974)
f150_Lightning.display_details()
prius=Car(4,'Regular','Toyota','Prius',2023,183843029,27450)

prius.display_details()

