class PP:
	def __init__(self, length, width):
		self.length = length
		self.width = width
	def __repr__(self):
		result = ""
		for i in range(self.length):
			result += " "*self.width + "#"*self.width + "\n"
		for i in range(self.width):
			result += "#" * self.width * 3 + "\n"
		return result
if __name__ == "__main__":
	pp = PP(int(input("LENGTH:")), int(input("WIDTH:")))
	print(pp)
