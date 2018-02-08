#Maps and lists
numbers=[0,2,4]
numbers.append(5)
for x in numbers:
	print x

map={"slot":6, "cat":4, "dog":2}
print map.items() 
print map ["slot"]
for k,v in map.items():
	print k,v 
	