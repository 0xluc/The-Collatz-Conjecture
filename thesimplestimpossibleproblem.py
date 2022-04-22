import matplotlib.pyplot as plt

def tsip(a):
	plt.clf() #clear the graph cache
	plt.style.use('dark_background') 
	png = "{:03d}".format(a) # 000.png
	plt.title(png)

	x = a
	y = 0
	xgraph = [x]
	ygraph = [0]
	while x != 1:
		if x % 2 == 0:
			x = x/2
			y = y + 1
			xgraph.append(x)
			ygraph.append(y)
		else:
			x = 3*x + 1
			y = y+1
			xgraph.append(x)
			ygraph.append(y)
	plt.plot(ygraph, xgraph,color='blue', linewidth = 2, marker='o', markerfacecolor='red', markersize=5)

	plt.savefig(png) # you can switch this line to plt.show() if you just want to see the graph

	print("The number",a,"has gone through",y,"operations until it reached the value 1")

for i in range(1,1000):
	tsip(i)
