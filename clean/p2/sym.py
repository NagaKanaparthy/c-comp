class SymbolTable(object):
	depth = 0
	table = []
	def Insert(self, name, item):
		if len(self.table) <= self.depth:
			self.table.append({})
		self.table[self.depth][name] = item
	def IncreaseDepth(self):
    		self.depth += 1
		self.table.append({})
	def Pop(self):
		self.table.pop()
		self.depth -= 1
	def Search(self, name, depth=None):
		if depth is None:
			depth = self.depth
		elif depth < 0:
			return None

		if name in self.table[depth].keys():
			return self.table[depth][name]
		else:
			return self.Search(name, depth-1)
