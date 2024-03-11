import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # wait for a request from main program
    message = socket.recv_pyobj()

    # chooses a random string from received list
    randString = random.choice(message)

    # send random string back to main program
    socket.send_pyobj(randString)
