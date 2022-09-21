import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from run64 import sup
    sup()
elif bit == '32bit':
    from run32 import sup
    sup()
