#import numpy as np

N_PHASES = 15
N_SBIT = 8
N_VFAT = 12

class XML_HEADER:
    def __init__(self):
        self.ET_NAME = "OH_QC"
        self.NAME = "OptoHybrid Quality Control"
        return


class HW_Info:
    def __init__(self):
        self.KIND_OF_PART = 'GEM Opto Hybrid V3'
        self.OH_SERIAL_NUMBER = 12345
        self.VERSION = 3
        self.PRODUCTION_OH = True
        self.FPGA_DNA = 12310230131230
        self.SCA_SERIAL = 1141
        self.GEB_ID = 10101
        self.FUSING_DATE = '20210606_00-00'
        self.GBT_0_SERIAL = 1123409
        self.GBT_1_SERIAL = 2530992
        self.GBT_0_FUSE_FILE = 'GBTX_GE21_OHv2_GBT_0_minimal_2020-01-17.txt'
        self.GBT_1_FUSE_FILE = 'GBTX_GE21_OHv2_GBT_1_minimal_2020-01-31.txt'
        self.GBT_0_TEST_FILE = 'GBTX_GE21_OHv2_GBT_0_minimal_2020-01-17.txt'
        self.GBT_1_TEST_FILE = 'GBTX_GE21_OHv2_GBT_1_minimal_2020-01-31.txt'
        return

class Test_Condition:
    def __init__(self):
        self.RUN_TYPE = 'OH Routine'
        self.RUN_NUMBER = 0
        self.RUN_BEGIN_TIMESTAMP = '20210606_00-00'
        self.RUN_END_TIMESTAMP =  '20210606_00-10'
        self.LOCATION = "TAMU"
        self.USER = 'Cameron Wetzel'
        self.COMMENT = "comment description"
        return

class ADC_Data:
    def __init__(self):
        self.RSSI_1_INIT = 512.1
        self.RSSI_2_INIT = 499.8

        self.FPGA_CORE_V = 0.998
        self.MGTAVCC = 1.001
        self.MGTAVTT = 1.299

        self.FEAST_1_V = 1.803
        self.FEAST_1_I = 1.1
        self.FEAST_2_V = 1.499
        self.FEAST_2_I = 0.678
        self.FEAST_3_V = 2.499
        self.FEAST_3_I = 0.345

        self.FEAST_4_I = 0.289
        self.FEAST_5_I = 0.87

        self.GBT_1_TEMP = 38.6
        self.GBT_2_TEMP = 37.5
        self.VTRX_TEMP = 40.1
        self.LDO_1v5_TEMP = 33.6
        self.SCA_TEMP = 41.8

        self.GND_1K_I = 98.67
        self.RSSI_1_MID = 505.3
        self.RSSI_2_MID = 489.7
        self.GBT_0_QP_I = 123
        self.GBT_1_QP_I = 123

        self.FPGA_TEMP = 45.1

        self.RSSI_1_END = 505.3
        self.RSSI_2_END = 489.7
        return
    def set_RSSI_Init(self,RSSI_READING):
        self.RSSI_1_INIT = RSSI_READING[1]
        self.RSSI_2_INIT = RSSI_READING[2]
        return

    def set_RSSI_End(self,RSSI_READING):
        self.RSSI_1_END = RSSI_READING[1]
        self.RSSI_2_END = RSSI_READING[2]
        return
    def set_ADC_Readings(self,ADC_READINGS):
        self.RSSI_1_MID = ADC_READINGS[0][0]
        self.RSSI_2_MID = ADC_READINGS[0][1]

        self.FPGA_CORE_V = ADC_READINGS[2][0]
        self.MGTAVCC = ADC_READINGS[2][1]
        self.MGTAVTT = ADC_READINGS[2][2]

        self.FEAST_1_V = ADC_READINGS[2][3]
        self.FEAST_1_I = ADC_READINGS[3][0]
        self.FEAST_2_V = ADC_READINGS[2][4]
        self.FEAST_2_I = ADC_READINGS[3][1]
        self.FEAST_3_V = ADC_READINGS[2][5]
        self.FEAST_3_I = ADC_READINGS[3][2]

        self.FEAST_4_I = ADC_READINGS[3][3]
        self.FEAST_5_I = ADC_READINGS[3][4]

        self.GBT_1_TEMP = ADC_READINGS[1][2]
        self.GBT_2_TEMP = ADC_READINGS[1][3]
        self.VTRX_TEMP = ADC_READINGS[1][4]
        self.LDO_1v5_TEMP = ADC_READINGS[1][5]
        self.SCA_TEMP = ADC_READINGS[1][1]

        self.GND_1K_I = ADC_READINGS[4]

        # !!!!! NEEDS PROCESS !!!!!!!
        #self.GBT_0_QP_I = 123
        #self.GBT_1_QP_I = 123
        return

    def set_FPGA_Temp(self,FPGA_TEMP_in):
        self.FPGA_TEMP = FPGA_TEMP_in
        return

class Test_Result:
    def __init__(self):
        self.All_TEST_PASSED = True
        self.CTP7_COMM_GOOD = True
        self.VTTX_OPTICAL_LINK_GOOD = True
        self.PROMLESS_LOAD_PATH_GOOD = True
        self.ADC_READINGS_GOOD = True
        self.VFAT_ELINK_PHASE_SCAN_GOOD = True
        self.FPGA_ELINK_PRBS_GOOD = True
        self.ALL_SBIT_GOOD = True

        self.PROMLESS_LOAD_CYCLES = 1000
        return


class GBT_ELINK:
    def __init__(self,gbt,elink,arg_1, arg_2):
        self.GBT = gbt
        self.ELINK = elink

        if elink > 5:
            self.BER = arg_1
        elif len(arg_1) < N_PHASES or len(arg_2) < N_PHASES or len(arg_1) != len(arg_2):
            print('Error Invalid size of Phase Arrays!')
        else:
            self.LINK_GOOD = arg_1
            self.SYNC_ERR_CNT = arg_2
        return

class VFAT_SBIT:
    def __init__(self,vfat,center,best_dly,width):
        if(vfat >= N_VFAT):
            print("ERROR Invalid VFAT Entry!")
        elif len(center) != N_SBIT or len(best_dly) != N_SBIT or len(width) != N_SBIT:
            pritn("ERROR Entries DO NOT match number of S-bits!")
        else:
            self.VFAT = vfat
            self.SBIT_CENTER = center
            self.SBIT_BEST_DLY = best_dly
            self.SBIT_WIDTH = width
