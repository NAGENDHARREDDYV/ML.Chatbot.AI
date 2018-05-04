import json

def getMobileData(brand, screenSize, ram):
	'''reads mobile_data1.json and returns mobile db data'''
	f=open("db/mobile_data.json","r")
	s=f.read()
	#print(s)
	mobile_dict = json.loads(s)
	#print(mobile_dict)
	#return mobile_dict[brand][screenSize][ram]['mobiles']
	try:
		brands=mobile_dict[brand]
	except KeyError:
		return None
	
	try:
		screenSizes=brands[screenSize]
	except KeyError:
		return None

	try:
		rams=screenSizes[ram]
	except KeyError:
		return None

	return rams['mobiles']

def getRestaurantData(location, cuisine, category):
	'''reads restaurant_data.json and returns restaurants db data'''
	f=open("db/restaurant_data.json","r")
	s=f.read()
	#print(s)
	res_dict = json.loads(s)
	#print(res_dict)
	#return res_dict[location][cuisine][category]['mobiles']
	try:
		locations=res_dict[location]
	except KeyError:
		return None
	
	try:
		cuisines=locations[cuisine]
	except KeyError:
		return None

	try:
		categories=cuisines[category]
	except KeyError:
		return None

	return categories['restaurants']



'''brand=input("brand:").lower()
screenSize=input("screenSize:").lower()
ram=input("ram:").lower()
print(getMobileData(brand, screenSize, ram))

location=input("location: ").lower()
cuisine=input("cuisine: ").lower()
category=input("category- expensive/inexpensive: ").lower()
print(getRestaurantData(location, cuisine, category))'''