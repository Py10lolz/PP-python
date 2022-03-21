# Special branch for making custom pp made up of wha emoji (pojav discord server)
class PP:
	def __init__(self, length, width):
		self.length = length
		self.width = width
	def __repr__(self):
		result = ""
		for i in range(self.length):
			result += ":air:"*self.width + ":wha:"*self.width + "\n"
		for i in range(self.width):
			result += ":wha:" * self.width * 3 + "\n"
		return result
if __name__ == "__main__":
	pp = PP(int(input("LENGTH:")), int(input("WIDTH:")))
	print(pp)
