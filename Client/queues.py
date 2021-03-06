"""Queues Events Manager."""

from socket import socket, AF_INET, SOCK_STREAM

def receive_msg(inst):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', 4242))
    recv = sock.recv(8192).decode()
    inst.guiQueue.put(recv)
    inst.createThread(6)
