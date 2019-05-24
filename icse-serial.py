#!/usr/bin/env python3
# Relays are active low, LEDs are lit when NC are closed and NO are open
import serial
import time
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--on_relay', type = str, help = 'relay to turn on (1, 2, 12')
parser.add_argument('-f', '--off_relay', type = str, help = 'relay to turn off (1, 2, 12')
parser.add_argument('-d', '--device', help = 'serial device to turn on', default = '/dev/serial0')

args = parser.parse_args()

ser = serial.Serial(args.device, 9600, timeout = 1)

def prepare_relay():
    ser.write(b'\x50')
    time.sleep(0.5)
    ser.write(b'\x51')
    ser.write(b'\x00')

#ser.write(b'\x50')
#time.sleep(0.5)
#    reply = ser.read()
# print ('Got: ', reply)
# if reply != b'\xad':
#     print ('Did not receive a supported device, got: ', reply)
#     exit(-1)

if args.on_relay == '1':
    prepare_relay()
#    ser.write(b'\x00')
    ser.write(b'\x01')
elif args.on_relay == '2':
    prepare_relay()
    ser.write(b'\x02')
elif args.on_relay == '12':
    prepare_relay()
    ser.write(b'\x03')

elif args.off_relay != None:
    prepare_relay()
    ser.write(b'\x00')
