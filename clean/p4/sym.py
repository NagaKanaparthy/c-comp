from to import Token
class SymbolTable(object):
	def __init__(self):
		self.depth = 0
		self.table = []
#	Depth Controller
	def IncreaseDepth(self):
    		self.depth += 1
		self.table.append({})
	def Pop(self):
		self.table.pop()
		self.depth -= 1
#	operations
	def Insert(self, token):
		if(self.depth >= len(self.table)):
			self.table.append({})
		if(token.getValue().strip() not in self.table[self.depth]):
			self.table[self.depth][token.getValue()] = token
	def Search(self, token, depth=None):
		if(depth is None):
			depth = self.depth
		elif(depth < 0):
			return None
		if(token.getValue().strip() in self.table[depth].keys()):
			return self.table[depth][name]
		else:
			return self.Search(name, depth-1)
class Function(object):
	def __init__(self,name="",params=[]):
		self.name = name
		self.params = params