import os
import sys
sys.path.insert(1,os.getcwd()+'/utils')
from oh_fw_programming import *
from SCA import *
from vttx_optical_link import *
from ADC_read import *
from phase_scan import *
from classes import *
import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml import etree
from check_ctp7_comm import *
from configure_gbts import *
from cold_boot_invert_rx import *
from sbit_timing_scan_oh_sbit_hitmap import *



def main():

	ELINKS = []
	
	# Loads SCA Reg Interface
	parseXML()
	# puts CTP7 in proper state for remaining Tests
	#cold_boot_invert_rx()

	# Rice Testing Manual Section 8 encapsulation
#	PF_CTP7 = check_CTP7()

	# load OH FW into CTP7 RAM
#	load_fw_full()
	# Program OH with FW currently Loaded in CTP7 RAM (x1)
#	program_fw_single()
#	print(Colors.MAGENTA + 'PROGRAMMED FULL FW' + Colors.ENDC)
	# Sample RSSI strength before continuing further
#	RSSI_init = readRSSI()
#	print(Colors.WHITE + 'RSSI Reading = ' + str(RSSI_init) + Colors.ENDC)


	# Rice Testing Manual Section 12 Promless Load Path
#	Load_iters = 5
#	print(Colors.MAGENTA + 'Testing FPGA LOAD PATH (x' + str(Load_iters) + ')' + Colors.ENDC)
#	Load_fails = program_fw_iter(Load_iters)
#	PF_GBT_Load = (Load_fails == 0)
#	Success_Load_Cylces = Load_iters - Load_fails


	# Rice Testing Manual Section 13 ADC Readings
#	ADC_OUT = ADC_Test()
#	print(ADC_OUT)

	# Rice Testing Manual Section 11 VTTX Optical Link Health
#	vttx_link_health_test()

	# Switch to PRBS firmware for Loopback Test
#	print(Colors.MAGENTA + 'About to Program prbs FW' + Colors.ENDC)
#	print(Colors.MAGENTA + 'SCA Status = ' + str(check_SCA_ASIC()) + Colors.ENDC)
#	load_fw_prbs()
#	program_fw_single()

	# Rice Testing Manual Section 14 PRBS Loopback Test 
	# FPGA Phase Scan before PRBS Loopback
#	scan_FPGA_integrated()
	# Add METHOD


	# VFAT PHASE SCAN
	print(Colors.MAGENTA + 'About to Program FULL FW' + Colors.ENDC)
    	print(Colors.MAGENTA + 'SCA Status = ' + str(check_SCA_ASIC()) + Colors.ENDC)
#	load_fw_full()
#	program_fw_single()
	# Do VFAT ELINK Phase Scan !![Data to be stored and used late]!!
#	print(Colors.MAGENTA + 'STARTING VFAT PHASE SCAN' + Colors.ENDC)
#    	print(Colors.MAGENTA + 'SCA Status = ' + str(check_SCA_ASIC()) + Colors.ENDC)
#	print(scan_VFAT_integrated(True))	# Also programs best phases
#	VFAT_Phase_Scan(True)
	

	# SBIT TEST
	print(Colors.MAGENTA + 'STARTING VFAT SBIT SCAN' + Colors.ENDC)
	print(Colors.MAGENTA + 'SCA Status = ' + str(check_SCA_ASIC()) + Colors.ENDC)
	VFAT_SBITS_CONTAINER = SBIT_SCAN_MINIMAL(0, 0, 3, True)
	
	for vfat in VFAT_SBITS_CONTAINER:
		print("VFAT"+str(vfat.VFAT)+":")
		print("CENTER:")
		print(vfat.SBIT_CENTER)
		print("BEST DELAY:")
		print(vfat.SBIT_BEST_DLY)
		print("WIDTH:")
		print(vfat.SBIT_WIDTH)
	return



def check_CTP7():
	# Corresponds to Section 8 Procedure from Rice Testing Manual
	gbt_0_config_Pass = gbt_config(0,0,'config',os.getcwd()+'/gbt_config/GBTX_GE21_OHv2_GBT_0_minimal_2020-01-17.txt')
	if(gbt_0_config_Pass):
		print('GBT 0 Configuration SUCCESS')
	else:
		print('GBT 0 Configuration FAIL')

	gbt_1_config_Pass = gbt_config(0,1,'config', os.getcwd()+'/gbt_config/GBTX_GE21_OHv2_GBT_1_minimal_2020-01-31.txt')
	if(gbt_1_config_Pass):
		print('GBT 1 Configuration SUCCESS')
	else:
		print('GBT 1 Configuration FAIL')

	PassFail_Comm = CTP7_Comm_Check()
	if(not PassFail_Comm):
		print('FAIL: CTP7 Communication Failed')
	reset_SCA_ASIC()
	PassFail_SCA = check_SCA_ASIC()

	return (PassFail_Comm and PassFail_SCA) and (gbt_0_config_Pass and gbt_1_config_Pass)

def VFAT_Phase_Scan(verbose=False):
	# Perform the VFAT Phase Scan, {Best Phases are programmed here}
	vfat_Scan_Data = scan_VFAT_integrated(verbose)
	
	# Organize Data
	ALL_PHASE_GOOD = vfat_Scan_Data[0]
	GBT_0_Data = vfat_Scan_Data[1]
	GBT_1_Data = vfat_Scan_Data[2]

	ELINKS_out = []

	# Format GBT_0
	for elink in range(0,6):
		ELINKS_out.append(GBT_ELINK(0,elink,GBT_0_Data[0][elink],GBT_0_Data[1][elink]))		
		if(verbose):                                                                             
                        print('GBT0 ELINK' + str(elink)+' Container Contents:')                                        
                        print(ELINKS_out[-1].LINK_GOOD)
			print(ELINKS_out[-1].SYNC_ERR_CNT)
	# Format GBT_1                                                                                   
        for elink in range(0,6):                                                                         
                ELINKS_out.append(GBT_ELINK(1,elink,GBT_1_Data[0][elink],GBT_1_Data[1][elink]))
		if(verbose):
			print('GBT1 ELINK' + str(elink)+' Container Contents:')
			print(ELINKS_out[-1].LINK_GOOD)
			print(ELINKS_out[-1].SYNC_ERR_CNT)


	return	[ALL_PHASE_GOOD, ELINKS_out]

if __name__ == '__main__':
	main()
