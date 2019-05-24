#!/usr/bin/env python3
# Relays are active low, LEDs are lit when NC are closed and NO are open
import serial
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--on_relay', type = int)

args = parser.parse_args()

ser = serial.Serial('/dev/cu.usbserial-00000000', 9600, timeout = 1)

#reply = b''
#while reply == b'':
ser.write(b'\x50')
time.sleep(0.5)
#    reply = ser.read()
# print ('Got: ', reply)
# if reply != b'\xad':
#     print ('Did not receive a supported device, got: ', reply)
#     exit(-1)

ser.write(b'\x51')

#if args.on_relay == 0:
#    ser.write(b'\x02')
#else:
#    print ('invalid args')
#    ser.write(b'\xFF')

#elif args.on_relay == 1:
#    ser.write(b'\x02')

#

# K1 = bit 0, active high
# K2 = bit 1, active high

while True:
    # Turn off K1
    ser.write(b'\x02')
    time.sleep(1)
    # Turn off K2
#    ser.write(b'\x00')
#    time.sleep(1)
    # Turn on K1
    ser.write(b'\x00')
#    time.sleep(1)
    # Turn on both relays
#    ser.write(b'\x03')
    time.sleep(3)
