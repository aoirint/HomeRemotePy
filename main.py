import serial
import json
import sys
import time

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('port', type=str)
parser.add_argument('type', type=str)
parser.add_argument('command', type=str)
args = parser.parse_args()

typ = args.type
data = None

if typ == 'ac':
    cmd = args.command
    data = {
        'type': typ,
        'cmd': cmd,
    }

else:
    print(f'No such type: {typ}')
    exit()

assert data is not None

port = args.port
ser = serial.Serial(port, 38400)
print('Wait connection established...')
time.sleep(3) # Wait connection established

msg = json.dumps(data) + '\n'
print(msg)

try:
    print('Wait transmission done...')
    ser.write(msg.encode('ascii'))
    print(ser.readline().decode('ascii'))
finally:
    ser.close()

