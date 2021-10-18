import sys
import os
import subprocess

WORKING_DIR=os.getcwd()

FULL_BIT_FILE=WORKING_DIR+'/fw/oh/OH_3_2_8_GE21v2.bit'
PRBS_BIT_FILE=WORKING_DIR+'/fw/oh/oh_ge21v2_loopback_120.bit'
ohMask = 1

sys.path.insert(1,WORKING_DIR+'/utils')
from rw_reg import *
from JTAG import *
from SCA import *
from cmd_output import *

def main():
	parseXML()
	load_fw_full()
	#load_fw_prbs()
	for i in range(0,1):
		load_fw_full()
		program_fw_single()
		check_SCA_ASIC()
		check_current_fw()
		load_fw_prbs()
		program_fw_single()
		check_SCA_ASIC()
		check_current_fw()

	program_fw_iter(5)

def check_current_fw():
	print('MAJOR = '+readReg(getNode('GEM_AMC.OH.OH0.FPGA.CONTROL.RELEASE.VERSION.MAJOR')))
        print('MINOR = '+readReg(getNode('GEM_AMC.OH.OH0.FPGA.CONTROL.RELEASE.VERSION.MINOR')))
        print('BUILD = '+readReg(getNode('GEM_AMC.OH.OH0.FPGA.CONTROL.RELEASE.VERSION.BUILD')))
        print('GENERATION = '+readReg(getNode('GEM_AMC.OH.OH0.FPGA.CONTROL.RELEASE.VERSION.GENERATION')))
	return

def load_fw_full():
	subprocess.call(['echo','Loading '+FULL_BIT_FILE])
	subprocess.call(['gemloader','load',FULL_BIT_FILE])
	subprocess.call(['mpoke','0x6a000000','1'])
	subprocess.call(['mpoke','0x6a000004','4914817'])
	return

def load_fw_prbs():
	subprocess.call(['echo','Loading '+PRBS_BIT_FILE])
	subprocess.call(['gemloader','load',PRBS_BIT_FILE])
	subprocess.call(['mpoke','0x6a000000','1'])
	subprocess.call(['mpoke','0x6a000004','939733'])
	return

def program_fw_single():
	ohList = []                                                                                                                               
        for i in range(0,12):                                                                                                                     
                if check_bit(ohMask,i):                                                                                                           
                        ohList.append(i)                                                                                                          
                                                                                                                                                  
        writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.MANUAL_CONTROL.LINK_ENABLE_MASK'), ohMask)                                                     
        writeReg(getNode('GEM_AMC.TTC.GENERATOR.ENABLE'), 0x1)                                                                                    
        writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.CTRL.TTC_HARD_RESET_EN'), 0x0)                                                                 
        subheading('Disabling monitoring')                                                                                                        
        sleep(0.1)

        gpio_dir = 0xff0fe0                                                                                                                       
        gpio_default_out = 0x60                                                                                                                   
        gpio_hr_out = 0xff0fe0                                                                                                                    
                                                                                                                                                  
        subheading('Setting the GPIO direction mask to ' + hex(gpio_dir))                                                                         
        sendScaCommand(ohList, 0x2, 0x20, 0x4, gpio_dir, False)                                                                                   
        sleep(0.1)                                                                                                                                
                                                                                                                                                  
        readData = sendScaCommand(ohList, 0x2, 0x1, 0x1, 0x0, True)                                                                               
        subheading('Read GPIO = %s' % hex(readData[0]))                                                                                           
        sleep(0.1)                                                                                                                                
                                                                                                                                                  
        hr_fail = 0                                                                                                                               
        program_fail = 0                                                                                                                          
                                                                                                                                                  
        for i in range(0,1):                                                                                                                 
		subheading('Starting hard reset')                                                                                                                                                  
                sendScaCommand(ohList, 0x2, 0x10, 0x4, gpio_hr_out, False)                                                                        
                sleep(0.01)                                                                                                                       
                                                                                                                                                  
                readData = sendScaCommand(ohList, 0x2, 0x1, 0x1, 0x0, True)                                                                       
                subheading('Read GPIO = %s' % hex(readData[0]))                                                                                   
                fpga_done = (readData[0] >> 30) & 1                                                                                               
                if (fpga_done != 0):                                                                                                              
                        printRed('FPGA DONE is high, hard reset failed')                                                                          
                        hr_fail += 1                                                                                                              
                sleep(0.01)                                                                                                                       
                                                                                                                                                  
                subheading('Unsetting hard reset')                                                                                                
                sendScaCommand(ohList, 0x2, 0x10, 0x4, gpio_default_out, False)                                                                   
                sleep(0.01)                                                                                                                       
                                                                                                                                                  
                readData = sendScaCommand(ohList, 0x2, 0x1, 0x1, 0x0, True)                                                                       
                subheading('Read GPIO = %s' % hex(readData[0]))                                                                                   
                sleep(0.01)                                                                                                                       
                                                                                                                                                  
                subheading('Executing PROMless programming')                                                                                      
                writeReg(getNode('GEM_AMC.TTC.GENERATOR.SINGLE_HARD_RESET'), 0x1)                                                                 
                sleep(0.1)                                                                                                                        
                                                                                                                                                  
                readData = sendScaCommand(ohList, 0x2, 0x1, 0x1, 0x0, True)                                                                       
                subheading('Read GPIO = %s' % hex(readData[0]))                                                                                   
                fpga_done = (readData[0] >> 30) & 1                                                                                               
                if (fpga_done != 1):                                                                                                              
                        printRed('FPGA DONE is low, programming failed')                                                                          
                        program_fail += 1                                                                                                         
                                                                                                                                                  
        sleep(0.1)                                                                                                                                
                                                                                                                                                  
        subheading('HR Errors: %d, program Errors: %d' % (hr_fail, program_fail))
	
	reset_SCA_ASIC()
	sleep(0.1)

def program_fw_iter(num_iter):
	ohList = []
	for i in range(0,12):
		if check_bit(ohMask,i):
			ohList.append(i)

	writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.MANUAL_CONTROL.LINK_ENABLE_MASK'), ohMask)
	writeReg(getNode('GEM_AMC.TTC.GENERATOR.ENABLE'), 0x1)
	writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.CTRL.TTC_HARD_RESET_EN'), 0x0)
	subheading('Disabling monitoring')
	sleep(0.1)

	gpio_dir = 0xff0fe0
	gpio_default_out = 0x60
	gpio_hr_out = 0xff0fe0

	subheading('Setting the GPIO direction mask to ' + hex(gpio_dir))
	sendScaCommand(ohList, 0x2, 0x20, 0x4, gpio_dir, False)
	sleep(0.1)

	readData = sendScaCommand(ohList, 0x2, 0x1, 0x1, 0x0, True)
	subheading('Read GPIO = %s' % hex(readData[0]))
	sleep(0.1)

	hr_fail = 0
	program_fail = 0

	for i in range(num_iter):
        	heading('Starting programming test (iteration #%d)' % i)

	        subheading('Setting hard reset')
	        sendScaCommand(ohList, 0x2, 0x10, 0x4, gpio_hr_out, False)
	        sleep(0.01)

	        readData = sendScaCommand(ohList, 0x2, 0x1, 0x1, 0x0, True)
       		subheading('Read GPIO = %s' % hex(readData[0]))
        	fpga_done = (readData[0] >> 30) & 1
        	if (fpga_done != 0):
        		printRed('FPGA DONE is high, hard reset failed')
        		hr_fail += 1
        	sleep(0.01)

        	subheading('Unsetting hard reset')
        	sendScaCommand(ohList, 0x2, 0x10, 0x4, gpio_default_out, False)
        	sleep(0.01)

		readData = sendScaCommand(ohList, 0x2, 0x1, 0x1, 0x0, True)
        	subheading('Read GPIO = %s' % hex(readData[0]))
        	sleep(0.01)

        	subheading('Executing PROMless programming')
        	writeReg(getNode('GEM_AMC.TTC.GENERATOR.SINGLE_HARD_RESET'), 0x1)
        	sleep(0.1)

        	readData = sendScaCommand(ohList, 0x2, 0x1, 0x1, 0x0, True)
        	subheading('Read GPIO = %s' % hex(readData[0]))
        	fpga_done = (readData[0] >> 30) & 1
        	if (fpga_done != 1):
        		printRed('FPGA DONE is low, programming failed')
        		program_fail += 1

	sleep(0.1)

	subheading('%d iterations done, HR Errors: %d, program Errors: %d' % (num_iter, hr_fail, program_fail))
	
	reset_SCA_ASIC()
	sleep(0.1)
	return hr_fail+program_fail

def check_bit(byteval,idx):
	return ((byteval&(1<<idx))!=0);

def OLD_program_fw():
	# Programs the OH FPGA with whatever is loaded in CTP7 RAM
	# Assumes parseXML() && initJtagRegAddrs() have been called
	if len(sys.argv) < 5:
		print('Usage: sca.py program-fpga <file-type> <filename>')
		print('file-type can be "mcs" or "bit"')
		return

	type = sys.argv[3]
	filename = sys.argv[4]

	if (type != "bit") and (type != "mcs"):
		print('Unrecognized type "' + type + '".. must be either "bit" or "mcs"')
		return

	if type != filename[-3:]:
		print("The type " + type + " doesn't match the file type, which is " + filename[-3:] + "... sorry, exiting..")
		return

	words = []
	if type == "mcs":
		print("Reading the MCS file...")
		bytes = readMcs(filename)
		if len(bytes) < FIRMWARE_SIZE:
			raise ValueError("MCS file is too short.. For Virtex6 we expect it to be " + str(FIRMWARE_SIZE) + " bytes long")

		print("Swapping bytes...")
		for i in range(0, FIRMWARE_SIZE/4):
			words.append((bytes[i*4 + 2] << 24) + (bytes[i*4 + 3] << 16) + (bytes[i*4] << 8) + (bytes[i*4 + 1]))

	elif type == "bit":
		f = open(filename, "rb")
		f.read(119) # skip the header
		print("Reading the bit file")
		bitWords = []
		bitWords = struct.unpack('>{}I'.format(FIRMWARE_SIZE/4), f.read(FIRMWARE_SIZE))
		print("reversing bits")

		# reverse the bits using a lookup table -- that's the fastest way
		bitReverseTable256 = [0x00, 0x80, 0x40, 0xC0, 0x20, 0xA0, 0x60, 0xE0, 0x10, 0x90, 0x50, 0xD0, 0x30, 0xB0, 0x70, 0xF0,
							  0x08, 0x88, 0x48, 0xC8, 0x28, 0xA8, 0x68, 0xE8, 0x18, 0x98, 0x58, 0xD8, 0x38, 0xB8, 0x78, 0xF8,
							  0x04, 0x84, 0x44, 0xC4, 0x24, 0xA4, 0x64, 0xE4, 0x14, 0x94, 0x54, 0xD4, 0x34, 0xB4, 0x74, 0xF4,
							  0x0C, 0x8C, 0x4C, 0xCC, 0x2C, 0xAC, 0x6C, 0xEC, 0x1C, 0x9C, 0x5C, 0xDC, 0x3C, 0xBC, 0x7C, 0xFC,
							  0x02, 0x82, 0x42, 0xC2, 0x22, 0xA2, 0x62, 0xE2, 0x12, 0x92, 0x52, 0xD2, 0x32, 0xB2, 0x72, 0xF2,
							  0x0A, 0x8A, 0x4A, 0xCA, 0x2A, 0xAA, 0x6A, 0xEA, 0x1A, 0x9A, 0x5A, 0xDA, 0x3A, 0xBA, 0x7A, 0xFA,
							  0x06, 0x86, 0x46, 0xC6, 0x26, 0xA6, 0x66, 0xE6, 0x16, 0x96, 0x56, 0xD6, 0x36, 0xB6, 0x76, 0xF6,
							  0x0E, 0x8E, 0x4E, 0xCE, 0x2E, 0xAE, 0x6E, 0xEE, 0x1E, 0x9E, 0x5E, 0xDE, 0x3E, 0xBE, 0x7E, 0xFE,
							  0x01, 0x81, 0x41, 0xC1, 0x21, 0xA1, 0x61, 0xE1, 0x11, 0x91, 0x51, 0xD1, 0x31, 0xB1, 0x71, 0xF1,
							  0x09, 0x89, 0x49, 0xC9, 0x29, 0xA9, 0x69, 0xE9, 0x19, 0x99, 0x59, 0xD9, 0x39, 0xB9, 0x79, 0xF9,
							  0x05, 0x85, 0x45, 0xC5, 0x25, 0xA5, 0x65, 0xE5, 0x15, 0x95, 0x55, 0xD5, 0x35, 0xB5, 0x75, 0xF5,
							  0x0D, 0x8D, 0x4D, 0xCD, 0x2D, 0xAD, 0x6D, 0xED, 0x1D, 0x9D, 0x5D, 0xDD, 0x3D, 0xBD, 0x7D, 0xFD,
							  0x03, 0x83, 0x43, 0xC3, 0x23, 0xA3, 0x63, 0xE3, 0x13, 0x93, 0x53, 0xD3, 0x33, 0xB3, 0x73, 0xF3,
							  0x0B, 0x8B, 0x4B, 0xCB, 0x2B, 0xAB, 0x6B, 0xEB, 0x1B, 0x9B, 0x5B, 0xDB, 0x3B, 0xBB, 0x7B, 0xFB,
							  0x07, 0x87, 0x47, 0xC7, 0x27, 0xA7, 0x67, 0xE7, 0x17, 0x97, 0x57, 0xD7, 0x37, 0xB7, 0x77, 0xF7,
							  0x0F, 0x8F, 0x4F, 0xCF, 0x2F, 0xAF, 0x6F, 0xEF, 0x1F, 0x9F, 0x5F, 0xDF, 0x3F, 0xBF, 0x7F, 0xFF]

		#reversing the bit order
		for word in bitWords:
			words.append(bitReverseTable256[word & 0xff] << 24 | bitReverseTable256[(word >> 8) & 0xff] << 16 | bitReverseTable256[(word >> 16) & 0xff] << 8 | bitReverseTable256[(word >> 24) & 0xff])

		if len(words) < FIRMWARE_SIZE/4:
			raise ValueError("Bit file is too short.. For Virtex6 we expect it to be " + str(FIRMWARE_SIZE) + " bytes long")

	numWords = FIRMWARE_SIZE / 4

	timeStart = clock()
	enableJtag(ohMask, 2)

	fpgaIds = jtagCommand(True, Virtex6Instructions.FPGA_ID, 10, 0x0, 32, ohList)
	sleep(0.0001)
	fpgaIdIdx = 0
	for oh in ohList:
		print('FPGA ID = ' + hex(fpgaIds[fpgaIdIdx]))
		fpgaIdIdx += 1
		#if fpgaIds[oh] != FPGA_ID:
		#    raise ValueError("Bad FPGA-ID (should be " + hex(FPGA_ID) + ")... Hands off...")

	jtagCommand(False, Virtex6Instructions.SHUTDN, 10, None, 0, False)

	# send 400 empty clocks
	wReg(ADDR_JTAG_LENGTH, 0x00)
	for i in range(0, 4):
		wReg(ADDR_JTAG_TMS, 0x00000000)
	for i in range(0, 12):
		wReg(ADDR_JTAG_TDO, 0x00000000)
	wReg(ADDR_JTAG_LENGTH, 0x10)
	wReg(ADDR_JTAG_TDO, 0x00000000)

	sleep(0.01)

	jtagCommand(False, Virtex6Instructions.JPROG, 10, None, 0, False)
	jtagCommand(False, Virtex6Instructions.ISC_NOOP, 10, None, 0, False)
	sleep(0.01)
	jtagCommand(False, Virtex6Instructions.ISC_ENABLE, 10, 0x00, 5, False)

	# 128 empty clocks
	wReg(ADDR_JTAG_LENGTH, 0x00)
	for i in range(0, 4):
		wReg(ADDR_JTAG_TMS, 0x00000000)
		wReg(ADDR_JTAG_TDO, 0x00000000)

	sleep(0.0005)

	jtagCommand(False, Virtex6Instructions.ISC_PROGRAM, 10, None, 0, False)
	sleep(0.001)

	print("sending data...")

	# send the data
	# optimization -- don't use the jtagCommand(), do this instead (looks messy, but it's way faster)
	#   1) enter a DR-shift state
	#   2) setup the TMS and length so that at the end of 32 bit shift it will update DR and go back to shift DR state
	#   3) stuff those bits in there only by calling set-TDO twice per 32bit word -- first with data and then with dummy zeros just to trigger it to send everything (including the extra TMS bits, which are after the 32 bit data word)
	#   4) after sending the last 32bit data word, do not enter back to shift-DR but just return to IDLE

	tms = 0b001
	tdo = 0b000
	wReg(ADDR_JTAG_LENGTH, 3)
	wReg(ADDR_JTAG_TMS, tms & 0xffffffff)
	wReg(ADDR_JTAG_TDO, tdo & 0xffffffff)

	tms = 0b001011 << 31
	wReg(ADDR_JTAG_LENGTH, 37)
	wReg(ADDR_JTAG_TMS, tms & 0xffffffff)
	tms = tms >> 32
	wReg(ADDR_JTAG_TMS, tms & 0xffffffff)

	# send the first byte so that the LENGTH is updated
	wReg(ADDR_JTAG_TDO, words[0])
	wReg(ADDR_JTAG_TDO, 0x0)

	# enter optimized mode that executes JTAG_GO on every TDO shift and doesn't update the LENGTH with every JTAG_GO
	sleep(0.001)
	writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.EXPERT.EXEC_ON_EVERY_TDO'), 0x1)
	writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.EXPERT.NO_SCA_LENGTH_UPDATE'), 0x1)
	writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.EXPERT.SHIFT_TDO_ASYNC'), 0x1)

	cnt = 0
	for i in range(1, numWords - 1):
		wReg(ADDR_JTAG_TDO, words[i])
		#wReg(ADDR_JTAG_TDO, 0x0) # not needed when EXEC_ON_EVERY_TDO is set to 0x1
		#jtagCommand(False, None, 0, (bytes[i*4 + 2] << 24) + (bytes[i*4 + 3] << 16) + (bytes[i*4] << 8) + (bytes[i*4 + 1]), 32, False)
		cnt += 1
		if cnt >= 10000:
		   print("word " + str(i) + " out of " + str(numWords))
		   cnt = 0

	# exit the optimized mode and send the last word (also exit the FSM to IDLE)
	sleep(0.01)
	writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.EXPERT.EXEC_ON_EVERY_TDO'), 0x0)
	writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.EXPERT.NO_SCA_LENGTH_UPDATE'), 0x0)
	writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.EXPERT.SHIFT_TDO_ASYNC'), 0x0)
	tms = 0b011 << 31 #go back to idle and don't enter DR shift again
	wReg(ADDR_JTAG_LENGTH, 34)
	wReg(ADDR_JTAG_TMS, tms & 0xffffffff)
	tms = tms >> 32
	wReg(ADDR_JTAG_TMS, tms & 0xffffffff)
	wReg(ADDR_JTAG_TDO, words[i]) #send the last word
	wReg(ADDR_JTAG_TDO, 0x0)


	print("DONE sending data")

	jtagCommand(False, Virtex6Instructions.ISC_DISABLE, 10, None, 0, False)
	# 128 empty clocks
	wReg(ADDR_JTAG_LENGTH, 0x00)
	for i in range(0, 4):
		wReg(ADDR_JTAG_TMS, 0x00000000)
		wReg(ADDR_JTAG_TDO, 0x00000000)

	sleep(0.0001)

	jtagCommand(False, Virtex6Instructions.BYPASS, 10, None, 0, False)
	jtagCommand(False, Virtex6Instructions.JSTART, 10, None, 0, False)

	# 128 empty clocks
	wReg(ADDR_JTAG_LENGTH, 0x00)
	for i in range(0, 4):
		wReg(ADDR_JTAG_TMS, 0x00000000)
		wReg(ADDR_JTAG_TDO, 0x00000000)

	sleep(0.0005)

	jtagCommand(True, Virtex6Instructions.BYPASS, 10, None, 0, False)

	print("FPGA programming DONE!!")

	disableJtag()

	totalTime = clock() - timeStart
	printCyan('time took to program = ' + str(totalTime))
	return


if __name__ == '__main__':
	main()
