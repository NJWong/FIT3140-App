from clear import Clear 
from wall import Wall 
from goal import Goal 

def tile_test():
	list1 = []
	list1.append(Clear(0,0))
	list1.append(Clear(1,1))
	list1.append(Clear(3,4))
	list1.append(Wall(0,1))
	list1.append(Goal(0,2))
	list1.append()

	for item in list1:
		item.dummy()


if __name__ =="__main__":
	tile_test()