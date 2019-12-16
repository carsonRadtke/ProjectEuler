def routes(x, y):
	def _routes(x, y, l):
		if (l[x][y] == None):
			l[x][y] = _routes(x-1, y, l) + _routes(x, y-1, l)
		return l[x][y]

	lst = list()
	for i in range(0, 21):
		tmp = list()
		for j in range(0, 21):
			if (i == 0 or j == 0):
				tmp.append(1)
			else:
				tmp.append(None)
		lst.append(tmp)

	return _routes(x, y, lst)

print(routes(20,20))
