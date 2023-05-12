myList=["Stars","Jupiter","Earth","Moon","Mars","Pluto","Saturn"]
print(myList[0])
print(myList[2])
print(myList[5])
myList.insert(2,"Mercury")
print(myList[2])
myList.append(["Sun","Moon"])
print(myList)
myList.extend(["Stars","Meteors"])
print(myList)
print(myList.index("Earth"))
myList.remove("Saturn")
print(myList)

