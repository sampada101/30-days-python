import psutil
print(f'Cpu Usage: {psutil.cpu_percent(interval=2)}')
print(f'Memory usage: {psutil.virtual_memory().percent}')
