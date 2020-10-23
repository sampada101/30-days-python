## Task: WAP to display get the disk space, %CPU used in your OS
## Approach: Used psutil module to find memory and CPU usage
## Solution:
```
import psutil
print(f'Cpu Usage: {psutil.cpu_percent(interval=2)}')
print(f'Memory usage: {psutil.virtual_memory().percent}')
```
## Author: Sampada Regmi
