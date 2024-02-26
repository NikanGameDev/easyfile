def write(path, text):
	with open(path, "wt") as a:
		a.write(text)
def writebin(path, bytes):
	with open(path, "wb") as a:
		a.write(bytes)
def read(path):
	with open(path, "rt") as a:
		a.read()
def readbin(path):
	with open(path, "rb") as a:
		a.read()
