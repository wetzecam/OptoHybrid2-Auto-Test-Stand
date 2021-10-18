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


from loopback import *

MWRD_LIMIT = 100

def main():
	ELINKAA = GBT_ELINK(0,6,10, 10)
	parseXML()
	gbt_config(0,0,'config',os.getcwd()+'/gbt_config/GBTX_GE21_OHv2_GBT_0_minimal_2020-01-17.txt')
	gbt_config(0,1,'config', os.getcwd()+'/gbt_config/GBTX_GE21_OHv2_GBT_1_minimal_2020-01-31.txt')

	print(PRBS_Loopback_Test(True))

	return



def PRBS_Loopback_Test(Verbose = False):
	FPGA_ELINKS = []	# Container for Output ELINK Objects
	# SCA Reset for Extra Safety
	reset_SCA_ASIC()
	sleep(1)
	# Load PRBS firmware to CTP7
	load_fw_prbs()
	print("fw loaded!!!")
	# Program the PRBS firmware to OH FPGA
	program_fw_single()
	print("fw programmed!!!")
	# Double Check the Firmware
	if(Verbose):
		check_current_fw()
	# Do Phase Scan on FPGA (integrated => best phase is programmed within)
	#scan_FPGA_integrated()
	# Make sure to Select OptoHybrid
	select_OH(0)
	# clear Loopback Counters before starting...
	clear_loopback_counters()
	# Enable Loopback Mode
	enable_loopback()

	# Start PRBS Loop, Runs until all MWRD Count >= MWRD_LIMIT
	PRBS_counts = prbs_loop(MWRD_LIMIT, Verbose)

	# Disable Loopback Mode once Limits are reached
	disable_loopback()

	# Convert Data to ELINK Containers for DB output
	for gbt in range(0,2):
		for elink in PRBS_ELINKS[gbt]:
			FPGA_ELINKS.append(GBT_ELINK(gbt,elink, (PRBS_counts[gbt][elink-6][1]/(7*PRBS_counts[gbt][elink-6][0]*10**6)), PRBS_counts[gbt][elink-6][0] ))

	return FPGA_ELINKS

if __name__ == '__main__':
	main()
