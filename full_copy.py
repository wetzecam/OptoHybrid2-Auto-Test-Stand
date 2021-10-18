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



def main():
	# Loads SCA Reg Interface
	parseXML()
	# puts CTP7 in proper state for remaining Tests
	cold_boot_invert_rx()

	# Rice Testing Manual Section 8 encapsulation
	PF_CTP7 = check_CTP7()

	# load OH FW into CTP7 RAM
	load_fw_full()
	# Program OH with FW currently Loaded in CTP7 RAM (x1)
	program_fw_single()
	# Sample RSSI strength before continuing further
	RSSI_init = readRSSI()

	# Rice Testing Manual Section 12 Promless Load Path
	Load_iters = 1000
	Load_fails = program_fw_iter(Load_iters)
	PF_GBT_Load = (Load_fails == 0)
	Success_Load_Cylces = Load_iters - Load_fails


	# Rice Testing Manual Section 13 ADC Readings
	ADC_OUT = ADC_Test()
	print(ADC_OUT)

	# Rice Testing Manual Section 11 VTTX Optical Link Health
	vttx_link_health_test()

	# Do VFAT ELINK Phase Scan !![Data to be stored and used late]!!
	scan_VFAT_integrated()

	# Switch to PRBS firmware for Loopback Test
	load_fw_prbs()
	program_fw_single()

	# FPGA Phase Scan before PRBS Loopback
	scan_FPGA_integrated()

	# Rice Testing Manual Section 14 PRBS Loopback Test
	## To Be Implemented !!!!!


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

if __name__ == '__main__':
	main()
