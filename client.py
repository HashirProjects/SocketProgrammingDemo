import socket
import pynput
import time
import clientActions

#uses pynput listener to check how fast the user can do 60 clicks
class game():
	def __init__(self):
		self.clicks=[0]
		self.score=0

	def on_click(self):
		self.clicks[0]+=1
		if self.clicks[0] >= 59:
			return False #end thread

	def startGame(self):
		#starts the game and collects the score
		listener = pynput.mouse.Listener(on_click=self.on_click)
		listener.start()
		print("CLICK AS FAST AS YOU CAN. YOU WIN WHEN YOU REACH 60 CLICKS")
		startTime= time.time()
		listener.join()
		endTime= time.time()
		self.score= endTime - startTime

#creates a connection to the port and runs handle server

class clientConnection():
	def __init__(self,serverIp, port):
		self.address= (serverIp, port)
		self.client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect(self.address)
		#sets up the socket object

	def getLeaderboardPosition(self, score):

		position = clientActions.handleServer(self.client, score)

		print(f"YOUR SCORE WAS {score}")
		print(f"YOU ARE AT POSITION {position} IN THE LEADERBOARD")

user=clientConnection("192.168.1.42", 5050)
user.getLeaderboardPosition(1000)