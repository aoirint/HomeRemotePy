import serial
import json
import sys
import time

typ = sys.argv[1]
data = None

if typ == 'ac':
    cmd = sys.argv[2]
    data = {
        'type': typ,
        'cmd': cmd,
    }

else:
    print('No such type')
    exit()

assert data is not None

ser = serial.Serial('/dev/ttyUSB0', 38400)
print('Wait connection...')
time.sleep(3) # Wait connection established

msg = json.dumps(data) + '\n'
print(msg)

try:
    while True:
        print('Wait sent...')
        ser.write(msg.encode('ascii'))
        time.sleep(1) # Wait sent
        print(ser.readline())
finally:
    ser.close()
