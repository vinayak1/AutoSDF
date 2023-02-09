import socket
import getpass

username = getpass.getuser()

hostname = socket.gethostname()

dataroot = '/workspace/AutoSDF/data'
logroot = '/workspace/AutoSDF/logs'
