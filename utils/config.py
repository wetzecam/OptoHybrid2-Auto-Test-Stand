import sys
import os

WORKING_DIR=os.getcwd()

CORE_DIR = '/mnt/persistent/texas/full_test'

# 10^12 = 8*10^6[MegaWord] * 0.125*10^6
BER_Acceptance_Criteria = 12500

# Number of iterations for testing OH FPGA Loading Path
PROMLESS_LOAD_CYCLES = 1000

GBT_0_Config_File = WORKING_DIR+"/gbt_config/GBTX_GE21_OHv2_GBT_0_minimal_2020-01-17.txt"
GBT_1_Config_File = WORKING_DIR+"/gbt_config/GBTX_GE21_OHv2_GBT_1_minimal_2020-01-31.txt"
