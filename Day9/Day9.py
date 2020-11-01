import os
os.system('wmic cpu get loadpercentage')
os.system('systeminfo | findstr /C:"Total Physical Memory"')
os.system('systeminfo |find "Available Physical Memory"')
