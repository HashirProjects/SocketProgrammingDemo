import socket

class clientInteraction():
	
	def handleClient(connection, address, scores):
		#recieves the score from the client and returns the position in the leaderboard 

		print(f"CLIENT CONNECTED: {address}")

		msgLength= int(connection.recv(64).decode("utf-8")) #gets the next message passed to the socket
		msg= connection.recv(msgLength).decode("utf-8")

		scores[address]= int(msg)
		for i in range(len(scores)):

			if address == sorted(scores.items(), key=lambda x: x[1], reverse=True)[i][0]: #returns a list of sorted tuples

				returnMsg=str(i).encode("utf-8")
				sendLength=len(returnMsg)
				sendLength+= ' '.encode("utf-8") * (64 - sendLength)

				connection.send(sendLength) # sends the message to the socket
				connection.send(i)

		connection.close()
		print(f"CLIENT DISCONNECTED: {address}")


	def handleServer(client, score):
		#sends the score to the server and receives and prints the position in the leaderboard.

		Msg=str(score).encode("utf-8")
		sendLength=len(returnMsg)
		sendLength+= ' '.encode("utf-8") * (64 - sendLength)

		client.send(sendLength) # sends the message to the socket
		client.send(i)

		msgLength= int(connection.recv(64).decode("utf-8")) #gets the next message passed to the socket
		msg= connection.recv(msgLength).decode("utf-8")

		print(f"YOU ARE AT POSITION {msg} IN THE LEADERBOARD")

