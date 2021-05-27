import socket
import threading
from clientActions import clientInteraction

class serverConnection():

	def __init__(self, serverIp, port):

		self.address= (serverIp, port)
		self.server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind(self.address)

		self.scores={}


	def startServer(self):

		print("STARTING SERVER ...")
		while True:
			connection, clientAddress = self.server.accept()
			clientThread= threading.Thread(target=clientInteraction.handleClient, args=[connection,clientAddress,self.scores])
			clientThread.start()

server= serverConnection(socket.gethostbyname(socket.gethostname()),5050)
server.startServer()