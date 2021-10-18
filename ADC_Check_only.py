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
	parseXML()
#	cold_boot_invert_rx()
#	gbt_config(0,0,'config',os.getcwd()+'/gbt_config/GBTX_GE21_OHv2_GBT_0_minimal_2020-01-17.txt')
#	gbt_config(0,1,'config', os.getcwd()+'/gbt_config/GBTX_GE21_OHv2_GBT_1_minimal_2020-01-31.txt')

#	print('CTP7 Communication:')
#	print(CTP7_Comm_Check())
	reset_SCA_ASIC()
#	load_fw_full()
#	program_fw_single()
	ADC_OUT = ADC_Test()

	print(ADC_OUT)

	RSSI_INIT = readRSSI()

	print(RSSI_INIT)

	#scan_VFAT_integrated()

	#load_fw_prbs()
	#program_fw_single()
	#scan_FPGA_integrated()
	#eset_SCA_ASIC()
	#load_fw_full()
	#program_fw_single()
	#check_SCA_ASIC()
	#check_current_fw()
#	load_fw_prbs()
#	program_fw_single()
	vttx_link_health_test()


if __name__ == '__main__':
	main()
