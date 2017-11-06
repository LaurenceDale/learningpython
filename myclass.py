class myClass:
	number = 0
	name = 'noname'

def Main():
	me = myClass()
	me.name = 'Laurence'
	me.number = 1337

	friend = myClass()
	friend.name = 'bro'
	friend.number = 3

	print 'name: ' + me.name + ', favorite number: ' + str(me.number)
	print 'name: ' + friend.name + ', favorite number: ' + str(friend.number)

if __name__ == '__main__':
	Main()
