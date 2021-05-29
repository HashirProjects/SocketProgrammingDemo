import socket
import threading
import clientActions
import json

class serverConnection():

	def __init__(self, serverIp, port):

		self.address= (serverIp, port)
		self.server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind(self.address)

		scoresFile = open("scores.json")
		self.scores=json.load(scoresFile)


	def startServer(self):

		print("STARTING SERVER ...")
		connected= True
		while connected:
			self.server.listen(1)
			connection, clientAddress = self.server.accept()
			clientThread= threading.Thread(target=clientActions.handleClient, args=[connection,clientAddress,self.scores])
			clientThread.start()

server= serverConnection(socket.gethostbyname(socket.gethostname()),5050)
server.startServer()