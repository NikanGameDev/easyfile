export def write(path, text):
	with open(path, "wt") as a:
		a.write(text)
export def writebin(path, bytes):
	with open(path, "wb") as a:
		a.write(bytes)
export def read(path, text):
	with open(path, "rt") as a:
		a.read()
export def read(path, bytes):
	with open(path, "rb") as a:
		a.read()
