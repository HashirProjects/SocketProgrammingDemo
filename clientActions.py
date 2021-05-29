import socket

def recvMsg(form, headerSize, connection):
	msgLength= int(connection.recv(headerSize).decode(form)) #gets the next message passed to the socket
	msg= connection.recv(msgLength).decode(form)

	return msg

def sendMsg(form, content, headerSize , connection):
	msg=str(content).encode(form)
	sendLength=len(msg)
	sendLength+= ' '.encode(form) * (headerSize - sendLength)

	connection.send(sendLength) # sends the message to the socket
	connection.send(msg)



def handleClient(connection, address, scores):
	#recieves the score from the client and returns the position in the leaderboard 

	print(f"CLIENT CONNECTED: {address}")

	msg = recvMsg("utf-8", 64, connection)

	scores[address]= int(msg)
	with open("scores.json", "w") as scoresFile:
		json.dump(scores, scoresFile)

	for i in range(len(scores)):
		if address == sorted(scores.items(), key=lambda x: x[1])[i][0]: #returns a list of sorted tuples
			sendMsg("utf-8", i+1, 64, connection)

	connection.close()
	print(f"CLIENT DISCONNECTED: {address}")


def handleServer(client, score):
	#sends the score to the server and receives and prints the position in the leaderboard.

	sendMsg("utf-8", score, 64, client)

	msg = recvMsg("utf-8", 64, client)

	return msg

