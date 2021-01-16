def lcm(s):
	x = [w for w in range(min(s),max(s)+1)]
	print(x)
	t = True
	z = 2
	c = 0
	d = 1
	y = 0
	while t:
		c = 0
		for i in range(len(x)):
			if x[i] % z ==  0:
				x[i] = x[i] // z
				c += 1
		if c == 0:
			z += 1
		else:
			d *= z
		for j in x:
			if j == 1:
				y += 1
		if y == len(x):
			t = False
		else:

			y = 0
	return d
print(lcm([1,5]))





