import csv


data = [     
	['name', 'age', 'city'],     
	['Alice', 25, 'New York'],     
	['Bob', 30, 'Los Angeles'],     
	['Charlie', 35, 'Chicago'] 
]

with open('output.csv', 'w', newline='') as file:     
	writer = csv.writer(file)     
	writer.writerows(data)
