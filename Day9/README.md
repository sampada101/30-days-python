## Task: WAP to display get the disk space, %CPU used in your OS
## Approach: Used os module to use system command and parse them
## Solution:
```
import os
os.system('wmic cpu get loadpercentage')
os.system('systeminfo | findstr /C:"Total Physical Memory"')
os.system('systeminfo |find "Available Physical Memory"')

```
## Author: Sampada Regmi
