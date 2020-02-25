#目前世界人口是60亿，如每年按1.5%的比例增长，则多少年后是80亿？


populationNext = 60
i = 0

while 1:
	populationNext = populationNext + (populationNext * 0.015)
	
	i += 1

	if populationNext >= 80:
		print(i)
		break



