import sys
from time import *

def main():

    filename = ""
    if len(sys.argv) < 2:
        print('Usage: mcs.py <mcs_filename>')
        return
    else:
        filename = sys.argv[1]

    timeStart = clock()
    readMcs(filename, 5464972)
    totalTime = clock() - timeStart
    print('time took = ' + str(totalTime))

def readMcs(filename):
    f = open(filename, 'r')

    bytes = []

    block = 0
    prevAddr = -16
    segmented = False
    for line in f:
        # block start
        if line[8] == '4':
            len = int(line[7:9], 16)
            segmented = False if len == 4 else True
            block = int(line[9:13], 16)
            crc = int(line[13:15], 16)
            chksum = (~(len + 2 + block + (block >> 8)) + 1) & 0xff

            if chksum != crc:
                raise ValueError("Bad block CRC in MCS file (block " + hex(block) + "), computed CRC = " + hex(chksum) + " while in file it's " + hex(crc))

            print("BLOCK " + str(block))

        # data
        if line[8] == '0':
            size = int(line[1:3], 16)
            localAddr = int(line[3:7], 16)
            addr = localAddr + (block << 16)
            if segmented:
                addr = localAddr + (block << 4)

            if addr != prevAddr + 16:
                raise ValueError("Address discontinuity detected in the MCS file.. Current addr = " + hex(addr) + ", previous addr = " + hex(prevAddr))
            prevAddr = addr

            chksum = size + localAddr + (localAddr >> 8)
            for i in range(0, size):
                byte = int(line[9 + i * 2 : 9 + i * 2 + 2], 16)
                bytes.append(byte)
                chksum += byte

            chksum = (~chksum + 1) & 0xff
            crc = int(line[9 + size * 2 : 9 + size * 2 + 2], 16)
            if chksum != crc:
                raise ValueError("Bad data CRC in MCS file (block " + hex(block) + ", addr " + hex(localAddr) + "), computed CRC = " + hex(chksum) + " while in file it's " + hex(crc))

        # end of PROM
        elif line[8] == '1':
            break

    f.close()
    return bytes

def hex(number):
    if number is None:
        return 'None'
    else:
        return "{0:#0x}".format(number)

if __name__ == '__main__':
    main()