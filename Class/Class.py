def _(func,items):
	i=0
	for item in items:
		if func(item):
			items[i] = item
			i += 1
	del items[i:]


