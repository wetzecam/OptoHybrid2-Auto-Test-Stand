#!/usr/bin/env python
"""Provides a processing tool for the OH.
    The OH expert just needs to implement the software functionalities to query the OH firmware
    and to replace the dummy variables in the main
"""
import os
import sys
sys.path.insert(1,os.getcwd()+'/utils')
import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml import etree
import string
import datetime
import os
from ADC_read import *
from rw_reg import *

from classes import *


WORKING_DIR = os.getcwd()

__author__ = "Cameron Wetzel / Stefano Colafranceschi"
__copyright__ = "Copyright 2021, CMS GEM"
__credits__ = [""]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Stefano Colafranceschi / Cameron Wetzel"
__email__ = "wetzecam@tamu.edu"
__status__ = "Work in progress"



def main():

    # Perform your software routines to actually test the OH
    #
    # ...to be implemented by TAMU group
    #
    # -----------------   DUMMY DATA  --------------------------------

    parseXML()

    xml_head = XML_HEADER()
    hw_info = HW_Info()
    test_conditions = Test_Condition()

    test_results = Test_Result()
    adc_reading = ADC_Data()

    print(ADC_Test())

    RSSI = readRSSI()
    print(RSSI)

    adc_reading.set_RSSI_Init(readRSSI())
    adc_reading.set_ADC_Readings(ADC_Test())
    adc_reading.set_RSSI_End(readRSSI())
    adc_reading.set_FPGA_Temp(readFPGA_Temp())

    ELINKS = []
    for gbt in range(2):
        for elink in range(6):
            ELINKS.append(GBT_ELINK(gbt,elink,[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,15,0,0]))

    for gbt in range(2):
        if gbt == 0:
            for elink in range(6,10):
                ELINKS.append(GBT_ELINK(gbt,elink,(10**-12),'x'))
        else:
            for elink in range(6,14):
                ELINKS.append(GBT_ELINK(gbt,elink,(10**-12),'x'))

    VFATS = []
    i = 0
    for vfat in range(12):
        VFATS.append(VFAT_SBIT(i,[-1,-1,-1,-1,-1,-1,-1,-1], [0,0,0,0,0,0,0,0], [37,37,37,37,37,37,37,37]))
        i += 1

    # -------------------------------------------------------------~

    # Dummy variables used to produce a template file
    Serial = "dummy_file"
    OutputPath = WORKING_DIR

    # After all variables are gathered than generate the XML header
    root, DataSet = BuildRunCommonXML(xml_head, hw_info, test_conditions,"all","all")
    root, DataSet = FillXML(root, DataSet, test_results, adc_reading, ELINKS, VFATS)
    
    gbt_qc, DataSet = BuildRunCommonXML(xml_head, hw_info, test_conditions,"OH_GBT_QC","GE21 OH GBT")
    gbt_qc, DataSet = Make_GBT_QC_XML(gbt_qc, DataSet, test_results, adc_reading, ELINKS, VFATS)

    gbt_sbit, DataSet = BuildRunCommonXML(xml_head, hw_info, test_conditions,"OH_GBT_SBIT","GE21 OH SBIT")
    gbt_sbit, DataSet = Make_GBT_SBIT_XML(gbt_sbit, DataSet, test_results, adc_reading, ELINKS, VFATS)

    oh_qc, DataSet = BuildRunCommonXML(xml_head, hw_info, test_conditions,"OH_QC","GE21 OH QC Hardware")
    oh_qc, DataSet = Make_OH_QC_XML(oh_qc, DataSet,hw_info, test_conditions, test_results, adc_reading, ELINKS, VFATS)
    WriteRunXML(root, gbt_qc, gbt_sbit, oh_qc, Serial, OutputPath)

def Make_GBT_SBIT_XML(root, DataSet, test_results, adc_reading, ELINKS, VFATS):
    Sbit = ET.SubElement(root,'SBIT')
    for vfat in VFATS:
        head_Vfat = 'VFAT_'+str(vfat.VFAT)
        Vfat_ET = ET.SubElement(Sbit,head_Vfat)
        WriteField = ET.SubElement(Vfat_ET,"SBIT_CENTER")
        WriteField.text = ", ".join(map(str,vfat.SBIT_CENTER))
        WriteField = ET.SubElement(Vfat_ET,"SBIT_BEST_DLY")
        WriteField.text = ", ".join(map(str,vfat.SBIT_BEST_DLY))
        WriteField = ET.SubElement(Vfat_ET,"SBIT_WIDTH")
        WriteField.text = ", ".join(map(str,vfat.SBIT_WIDTH))
    return root,DataSet
def Make_GBT_QC_XML(root, DataSet, test_results, adc_reading, ELINKS, VFATS):
    Elink = ET.SubElement(root,'ELINK_RESULT')
    for gbt in range(2):
        head_gbt = "GBT_"+str(gbt)
        Gbt = ET.SubElement(Elink,head_gbt)
        for elink in ELINKS:
            if(elink.GBT == gbt):
                head_elink = "ELINK_"+str(elink.ELINK)
                Elink_ET = ET.SubElement(Gbt,head_elink)
                if(hasattr(elink,'BER')):
                    WriteField = ET.SubElement(Elink_ET,'BER')
                    WriteField.text = str(elink.BER)
                if(hasattr(elink,'LINK_GOOD')):
                    WriteField = ET.SubElement(Elink_ET,'LINK_GOOD')
                    WriteField.text = ", ".join(map(str,elink.LINK_GOOD))
                if(hasattr(elink,'SYNC_ERR_CNT')):
                    WriteField = ET.SubElement(Elink_ET,'SNYC_ERR_CNT')
                    WriteField.text = ", ".join(map(str,elink.SYNC_ERR_CNT))
    return root,DataSet
def Make_OH_QC_XML(root, DataSet, hw_info, test_conditions, test_results, adc_reading, ELINKS, VFATS):
    Part=ET.SubElement(DataSet,'PART')
    WriteField = ET.SubElement(Part, 'PRODUCTION_OH')
    WriteField.text = str(hw_info.PRODUCTION_OH)
    WriteField = ET.SubElement(Part, 'FPGA_DNA')
    WriteField.text = str(hw_info.FPGA_DNA)
    WriteField = ET.SubElement(Part, 'SCA_SERIAL')
    WriteField.text = str(hw_info.SCA_SERIAL)
    WriteField = ET.SubElement(Part, 'GEB_ID')
    WriteField.text = str(hw_info.GEB_ID)
    WriteField = ET.SubElement(Part, 'FUSING_DATE')
    #stdFormatTimestamp = datetime.datetime.strptime(hw_info.FUSING_DATE,'%Y%m%d_%H-%M')
    #WriteField.text = datetime.datetime.strftime(stdFormatTimestamp,'%Y-%m-%d %H:%M:%S')
    WriteField.text = str(hw_info.FUSING_DATE)
    WriteField = ET.SubElement(Part, 'GBT_0_SERIAL')
    WriteField.text = str(hw_info.GBT_0_SERIAL)
    WriteField = ET.SubElement(Part, 'GBT_1_SERIAL')
    WriteField.text = str(hw_info.GBT_1_SERIAL)
    WriteField = ET.SubElement(Part, 'GBT_0_FUSE_FILE')
    WriteField.text = str(hw_info.GBT_0_FUSE_FILE)
    WriteField = ET.SubElement(Part, 'GBT_1_FUSE_FILE')
    WriteField.text = str(hw_info.GBT_1_FUSE_FILE)
    WriteField = ET.SubElement(Part, 'GBT_0_TEST_FILE')
    WriteField.text = str(hw_info.GBT_0_TEST_FILE)
    WriteField = ET.SubElement(Part, 'GBT_1_TEST_FILE')
    WriteField.text = str(hw_info.GBT_1_TEST_FILE)

    Data = ET.SubElement(DataSet, 'TEST_RESULTS')
    PassFail = ET.SubElement(Data,'PASS_FAIL')
    WriteField = ET.SubElement(PassFail,'ALL_TEST_PASSED')
    WriteField.text = str(test_results.All_TEST_PASSED)
    WriteField = ET.SubElement(PassFail,'CTP7_COMM_GOOD')
    WriteField.text = str(test_results.CTP7_COMM_GOOD)
    WriteField = ET.SubElement(PassFail,'VTTX_OPTICAL_LINK_GOOD')
    WriteField.text = str(test_results.VTTX_OPTICAL_LINK_GOOD)
    WriteField = ET.SubElement(PassFail,'PROMLESS_LOAD_PATH_GOOD')
    WriteField.text = str(test_results.PROMLESS_LOAD_PATH_GOOD)
    WriteField = ET.SubElement(PassFail,'ADC_READINGS_GOOD')
    WriteField.text = str(test_results.ADC_READINGS_GOOD)
    WriteField = ET.SubElement(PassFail,'VFAT_ELINK_PHASE_SCAN_GOOD')
    WriteField.text = str(test_results.VFAT_ELINK_PHASE_SCAN_GOOD)
    WriteField = ET.SubElement(PassFail,'FPGA_ELINK_PRBS_GOOD')
    WriteField.text = str(test_results.FPGA_ELINK_PRBS_GOOD)
    WriteField = ET.SubElement(PassFail,'ALL_SBIT_GOOD')
    WriteField.text = str(test_results.ALL_SBIT_GOOD)

    WriteField = ET.SubElement(Data,'PROMLESS_LOAD_CYCLES')
    WriteField.text = str(test_results.PROMLESS_LOAD_CYCLES)

    ADC_Readings = ET.SubElement(Data,'ADC_READINGS')
    WriteField = ET.SubElement(ADC_Readings,'FPGA_CORE_V')
    WriteField.text = str(adc_reading.FPGA_CORE_V)
    WriteField = ET.SubElement(ADC_Readings,'MGTAVCC')
    WriteField.text = str(adc_reading.MGTAVCC)
    WriteField = ET.SubElement(ADC_Readings,'MGTAVTT')
    WriteField.text = str(adc_reading.MGTAVTT)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_1_V')
    WriteField.text = str(adc_reading.FEAST_1_V)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_1_I')
    WriteField.text = str(adc_reading.FEAST_1_I)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_2_V')
    WriteField.text = str(adc_reading.FEAST_2_V)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_2_I')
    WriteField.text = str(adc_reading.FEAST_2_I)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_3_V')
    WriteField.text = str(adc_reading.FEAST_3_V)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_3_I')
    WriteField.text = str(adc_reading.FEAST_3_I)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_4_I')
    WriteField.text = str(adc_reading.FEAST_4_I)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_5_I')
    WriteField.text = str(adc_reading.FEAST_5_I)
    WriteField = ET.SubElement(ADC_Readings,'GBT_1_TEMP')
    WriteField.text = str(adc_reading.GBT_1_TEMP)
    WriteField = ET.SubElement(ADC_Readings,'GBT_2_TEMP')
    WriteField.text = str(adc_reading.GBT_2_TEMP)
    WriteField = ET.SubElement(ADC_Readings,'VTRX_TEMP')
    WriteField.text = str(adc_reading.VTRX_TEMP)
    WriteField = ET.SubElement(ADC_Readings,'LDO_1v5_TEMP')
    WriteField.text = str(adc_reading.LDO_1v5_TEMP)
    WriteField = ET.SubElement(ADC_Readings,'SCA_TEMP')
    WriteField.text = str(adc_reading.SCA_TEMP)
    WriteField = ET.SubElement(ADC_Readings,'GND_1K_I')
    WriteField.text = str(adc_reading.GND_1K_I)
    WriteField = ET.SubElement(ADC_Readings,'GBT_0_QP_I')
    WriteField.text = str(adc_reading.GBT_0_QP_I)
    WriteField = ET.SubElement(ADC_Readings,'GBT_1_QP_I')
    WriteField.text = str(adc_reading.GBT_1_QP_I)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_1_INIT')
    WriteField.text = str(adc_reading.RSSI_1_INIT)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_2_INIT')
    WriteField.text = str(adc_reading.RSSI_2_INIT)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_1_MID')
    WriteField.text = str(adc_reading.RSSI_1_MID)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_2_MID')
    WriteField.text = str(adc_reading.RSSI_2_MID)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_1_END')
    WriteField.text = str(adc_reading.RSSI_1_END)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_2_END')
    WriteField.text = str(adc_reading.RSSI_2_END)
    WriteField = ET.SubElement(ADC_Readings,'FPGA_TEMP')
    WriteField.text = str(adc_reading.FPGA_TEMP)
    return root,DataSet
def FillXML(root, DataSet, test_results, adc_reading, ELINKS, VFATS):
    Data = ET.SubElement(DataSet, 'TEST_RESULTS')
    PassFail = ET.SubElement(Data,'PASS_FAIL')
    WriteField = ET.SubElement(PassFail,'ALL_TEST_PASSED')
    WriteField.text = str(test_results.All_TEST_PASSED)
    WriteField = ET.SubElement(PassFail,'CTP7_COMM_GOOD')
    WriteField.text = str(test_results.CTP7_COMM_GOOD)
    WriteField = ET.SubElement(PassFail,'VTTX_OPTICAL_LINK_GOOD')
    WriteField.text = str(test_results.VTTX_OPTICAL_LINK_GOOD)
    WriteField = ET.SubElement(PassFail,'PROMLESS_LOAD_PATH_GOOD')
    WriteField.text = str(test_results.PROMLESS_LOAD_PATH_GOOD)
    WriteField = ET.SubElement(PassFail,'ADC_READINGS_GOOD')
    WriteField.text = str(test_results.ADC_READINGS_GOOD)
    WriteField = ET.SubElement(PassFail,'VFAT_ELINK_PHASE_SCAN_GOOD')
    WriteField.text = str(test_results.VFAT_ELINK_PHASE_SCAN_GOOD)
    WriteField = ET.SubElement(PassFail,'FPGA_ELINK_PRBS_GOOD')
    WriteField.text = str(test_results.FPGA_ELINK_PRBS_GOOD)
    WriteField = ET.SubElement(PassFail,'ALL_SBIT_GOOD')
    WriteField.text = str(test_results.ALL_SBIT_GOOD)

    WriteField = ET.SubElement(Data,'PROMLESS_LOAD_CYCLES')
    WriteField.text = str(test_results.PROMLESS_LOAD_CYCLES)

    ADC_Readings = ET.SubElement(Data,'ADC_READINGS')
    WriteField = ET.SubElement(ADC_Readings,'FPGA_CORE_V')
    WriteField.text = str(adc_reading.FPGA_CORE_V)
    WriteField = ET.SubElement(ADC_Readings,'MGTAVCC')
    WriteField.text = str(adc_reading.MGTAVCC)
    WriteField = ET.SubElement(ADC_Readings,'MGTAVTT')
    WriteField.text = str(adc_reading.MGTAVTT)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_1_V')
    WriteField.text = str(adc_reading.FEAST_1_V)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_1_I')
    WriteField.text = str(adc_reading.FEAST_1_I)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_2_V')
    WriteField.text = str(adc_reading.FEAST_2_V)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_2_I')
    WriteField.text = str(adc_reading.FEAST_2_I)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_3_V')
    WriteField.text = str(adc_reading.FEAST_3_V)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_3_I')
    WriteField.text = str(adc_reading.FEAST_3_I)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_4_I')
    WriteField.text = str(adc_reading.FEAST_4_I)
    WriteField = ET.SubElement(ADC_Readings,'FEAST_5_I')
    WriteField.text = str(adc_reading.FEAST_5_I)
    WriteField = ET.SubElement(ADC_Readings,'GBT_1_TEMP')
    WriteField.text = str(adc_reading.GBT_1_TEMP)
    WriteField = ET.SubElement(ADC_Readings,'GBT_2_TEMP')
    WriteField.text = str(adc_reading.GBT_2_TEMP)
    WriteField = ET.SubElement(ADC_Readings,'VTRX_TEMP')
    WriteField.text = str(adc_reading.VTRX_TEMP)
    WriteField = ET.SubElement(ADC_Readings,'LDO_1v5_TEMP')
    WriteField.text = str(adc_reading.LDO_1v5_TEMP)
    WriteField = ET.SubElement(ADC_Readings,'SCA_TEMP')
    WriteField.text = str(adc_reading.SCA_TEMP)
    WriteField = ET.SubElement(ADC_Readings,'GND_1K_I')
    WriteField.text = str(adc_reading.GND_1K_I)
    WriteField = ET.SubElement(ADC_Readings,'GBT_0_QP_I')
    WriteField.text = str(adc_reading.GBT_0_QP_I)
    WriteField = ET.SubElement(ADC_Readings,'GBT_1_QP_I')
    WriteField.text = str(adc_reading.GBT_1_QP_I)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_1_INIT')
    WriteField.text = str(adc_reading.RSSI_1_INIT)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_2_INIT')
    WriteField.text = str(adc_reading.RSSI_2_INIT)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_1_MID')
    WriteField.text = str(adc_reading.RSSI_1_MID)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_2_MID')
    WriteField.text = str(adc_reading.RSSI_2_MID)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_1_END')
    WriteField.text = str(adc_reading.RSSI_1_END)
    WriteField = ET.SubElement(ADC_Readings,'RSSI_2_END')
    WriteField.text = str(adc_reading.RSSI_2_END)
    WriteField = ET.SubElement(ADC_Readings,'FPGA_TEMP')
    WriteField.text = str(adc_reading.FPGA_TEMP)

    Elink = ET.SubElement(Data,'ELINK_RESULT')
    for gbt in range(2):
        head_gbt = "GBT_"+str(gbt)
        Gbt = ET.SubElement(Elink,head_gbt)
        for elink in ELINKS:
            if(elink.GBT == gbt):
                head_elink = "ELINK_"+str(elink.ELINK)
                Elink_ET = ET.SubElement(Gbt,head_elink)
                if(hasattr(elink,'BER')):
                    WriteField = ET.SubElement(Elink_ET,'BER')
                    WriteField.text = str(elink.BER)
                if(hasattr(elink,'LINK_GOOD')):
                    WriteField = ET.SubElement(Elink_ET,'LINK_GOOD')
                    WriteField.text = ", ".join(map(str,elink.LINK_GOOD))
                if(hasattr(elink,'SYNC_ERR_CNT')):
                    WriteField = ET.SubElement(Elink_ET,'SNYC_ERR_CNT')
                    WriteField.text = ", ".join(map(str,elink.SYNC_ERR_CNT))

    Sbit = ET.SubElement(Data,'SBIT')
    for vfat in VFATS:
        head_Vfat = 'VFAT_'+str(vfat.VFAT)
        Vfat_ET = ET.SubElement(Sbit,head_Vfat)
        WriteField = ET.SubElement(Vfat_ET,"SBIT_CENTER")
        WriteField.text = ", ".join(map(str,vfat.SBIT_CENTER))
        WriteField = ET.SubElement(Vfat_ET,"SBIT_BEST_DLY")
        WriteField.text = ", ".join(map(str,vfat.SBIT_BEST_DLY))
        WriteField = ET.SubElement(Vfat_ET,"SBIT_WIDTH")
        WriteField.text = ", ".join(map(str,vfat.SBIT_WIDTH))

    return root, DataSet

def BuildRunCommonXML(xml_head, hw_info, test_conditions, xmltype, xmltype2):
    root = ET.Element('ROOT')
    Header = ET.SubElement(root, 'HEADER')
    Type = ET.SubElement(Header, 'TYPE')
    WriteField = ET.SubElement(Type, 'EXTENSION_TABLE_NAME')
    WriteField.text = xmltype
    WriteField = ET.SubElement(Type, 'NAME')
    WriteField.text = xmltype2
    Run = ET.SubElement(Header, 'RUN')
    WriteField = ET.SubElement(Run, 'RUN_TYPE')
    WriteField.text = xmltype2
    WriteField = ET.SubElement(Run, 'RUN_NUMBER')
    WriteField.text = str(test_conditions.RUN_NUMBER)

    WriteField = ET.SubElement(Run, 'RUN_BEGIN_TIMESTAMP')
    stdFormatTimestamp = datetime.datetime.strptime(test_conditions.RUN_BEGIN_TIMESTAMP,'%Y%m%d_%H-%M')
    WriteField.text = datetime.datetime.strftime(stdFormatTimestamp,'%Y-%m-%d %H:%M:%S')

    WriteField = ET.SubElement(Run, 'RUN_END_TIMESTAMP')
    stdFormatTimestamp = datetime.datetime.strptime(test_conditions.RUN_END_TIMESTAMP,'%Y%m%d_%H-%M')
    WriteField.text = datetime.datetime.strftime(stdFormatTimestamp,'%Y-%m-%d %H:%M:%S')

    WriteField = ET.SubElement(Run, 'LOCATION')
    WriteField.text = test_conditions.LOCATION
    WriteField = ET.SubElement(Run, 'USER')
    WriteField.text = test_conditions.USER

    WriteField = ET.SubElement(Run, 'COMMENT_DESCRIPTION')
    WriteField.text = test_conditions.COMMENT

    # Hardware INFO:
    DataSet = ET.SubElement(root, 'DATA_SET')
    Part = ET.SubElement(DataSet, 'HARDWARE')
    WriteField = ET.SubElement(Part, 'KIND_OF_PART')
    WriteField.text = hw_info.KIND_OF_PART
    WriteField = ET.SubElement(Part, 'VERSION')
    WriteField.text = str(hw_info.VERSION)
    WriteField = ET.SubElement(Part, 'OH_SERIAL_NUMBER')
    WriteField.text = str(hw_info.OH_SERIAL_NUMBER)
    '''WriteField = ET.SubElement(Part, 'PRODUCTION_OH')
    WriteField.text = str(hw_info.PRODUCTION_OH)
    WriteField = ET.SubElement(Part, 'FPGA_DNA')
    WriteField.text = str(hw_info.FPGA_DNA)
    WriteField = ET.SubElement(Part, 'SCA_SERIAL')
    WriteField.text = str(hw_info.SCA_SERIAL)
    WriteField = ET.SubElement(Part, 'GEB_ID')
    WriteField.text = str(hw_info.GEB_ID)
    WriteField = ET.SubElement(Part, 'FUSING_DATE')
    #stdFormatTimestamp = datetime.datetime.strptime(hw_info.FUSING_DATE,'%Y%m%d_%H-%M')
    #WriteField.text = datetime.datetime.strftime(stdFormatTimestamp,'%Y-%m-%d %H:%M:%S')
    WriteField.text = str(hw_info.FUSING_DATE)
    WriteField = ET.SubElement(Part, 'GBT_0_SERIAL')
    WriteField.text = str(hw_info.GBT_0_SERIAL)
    WriteField = ET.SubElement(Part, 'GBT_1_SERIAL')
    WriteField.text = str(hw_info.GBT_1_SERIAL)
    WriteField = ET.SubElement(Part, 'GBT_0_FUSE_FILE')
    WriteField.text = str(hw_info.GBT_0_FUSE_FILE)
    WriteField = ET.SubElement(Part, 'GBT_1_FUSE_FILE')
    WriteField.text = str(hw_info.GBT_1_FUSE_FILE)
    WriteField = ET.SubElement(Part, 'GBT_0_TEST_FILE')
    WriteField.text = str(hw_info.GBT_0_TEST_FILE)
    WriteField = ET.SubElement(Part, 'GBT_1_TEST_FILE')
    WriteField.text = str(hw_info.GBT_1_TEST_FILE)'''

    return root, DataSet

def WriteRunXML(root,GBT_QC_DATA,GBT_SBIT_DATA,OH_QC_DATA, Serial, OutputPath):
    mydata = ET.tostring(root) #encoding='utf-8', method='xml')
    mydata = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    myfile = open( OutputPath + "/" + Serial + ".xml", "w")
    myfile.write(mydata)
    print("Output file is writen.")
    myfile.close()
    
    mydata = ET.tostring(GBT_QC_DATA) #encoding='utf-8', method='xml')
    mydata = minidom.parseString(ET.tostring(GBT_QC_DATA)).toprettyxml(indent="   ")
    GBT_QC = open(OutputPath+"/"+Serial+".OH_GBT_QC.xml","w")
    GBT_QC.write(mydata)
    GBT_QC.close()
    
    mydata = ET.tostring(GBT_SBIT_DATA) #encoding='utf-8', method='xml')
    mydata = minidom.parseString(ET.tostring(GBT_SBIT_DATA)).toprettyxml(indent="   ")
    GBT_SBIT = open(OutputPath+"/"+Serial+".OH_GBT_SBIT.xml","w")
    GBT_SBIT.write(mydata)
    GBT_SBIT.close()
    
    mydata = ET.tostring(OH_QC_DATA) #encoding='utf-8', method='xml')
    mydata = minidom.parseString(ET.tostring(OH_QC_DATA)).toprettyxml(indent="   ")
    OH_QC = open(OutputPath+"/"+Serial+".OH_QC.xml","w")
    OH_QC.write(mydata)
    OH_QC.close()
    print("new files")

if __name__ == '__main__':
    main()
