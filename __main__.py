from instadm import InstaDM

if __name__ == '__main__':
	# Auto login
	insta = InstaDM(username='devi.lcode', password='Devil21', headless=False)
	
	# Send message
	insta.sendMessage(user='mishragym', message='Hey !')
	
	# Send message
	#insta.sendGroupMessage(users=['user1', 'user2'], message='Hey !')
