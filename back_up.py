import os
import time

source = ['~/Developer/Python']

target_dir = '~/Documents/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -q %s %s" % (target, ''.join(source) )

print(zip_command)

if os.system(zip_command) == 0:
    print('Successful backup to ', target)
else:
    print("Backup failed")
