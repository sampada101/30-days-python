from urllib.request import urlopen
import json

file = open('employee_names.txt', 'w')
data = json.loads(urlopen('http://dummy.restapiexample.com/api/v1/employees?fbclid=IwAR1HIRBMTTJw65CA7L4xMUTAibMZI9SlSd4FS6uFPtF8s6LweGvjcgbO9V8').read().decode())
for i in data['data']:
    file.write(f"{i['employee_name']}\n")
    print(i['employee_name'])
