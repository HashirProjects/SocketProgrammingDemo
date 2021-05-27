import socket
from clientActions import handleServer

#uses pynput listener to check how fast the user can do 60 clicks
class game():
	def __init__(self, score):
		self.score=[score]

	def on_click(self):
		self.score[0]+=1
		if self.score[0] >= 59:
			return False #end thread

	def startGame():
		#starts the game


#creates a connection to the port and runs handle server

class clientConnection():
	def __init__():
		pass
		#sets up the socket object

	def getLeaderboardPosition():
		pass
		#calls handleServer