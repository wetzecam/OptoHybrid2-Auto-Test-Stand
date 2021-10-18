import sys
import os
import subprocess

from config import *

from phase_scan import scan_FPGA_integrated

WORKING_DIR=os.getcwd()

sys.path.insert(1,WORKING_DIR+'/utils')
from rw_reg import *
from JTAG import *
from SCA import *
from cmd_output import *

GBT_0_ELINK_PRBS = [6, 7, 8, 9]
GBT_1_ELINK_PRBS = [6, 7, 8, 9, 10, 11, 12, 13]
PRBS_ELINKS = [GBT_0_ELINK_PRBS , GBT_1_ELINK_PRBS]    # index : [GBT][ELINK]


def prbs_loop(MEGA_WRD_CNT_LIMIT, verbose=False):
    stop = False
    prbs_counters = []
    while(not stop):
        endFlag = True
        prbs_counters = read_loopback_counters()
        for gbtSelect in range(0,2):
            for elink in PRBS_ELINKS[gbtSelect]:
                if(verbose):
                    print("GBT%d ELINK%d MWRDCNT = %d" % (gbtSelect, elink, prbs_counters[gbtSelect][elink-6][0]))
                endFlag = endFlag and (prbs_counters[gbtSelect][elink-6][0] >= MEGA_WRD_CNT_LIMIT)
        stop = endFlag
    return prbs_counters

def read_loopback_counters():
    prbs_counters = [[[0]*2 for x in range(len(GBT_0_ELINK_PRBS))] , [[0]*2 for x in range(len(GBT_1_ELINK_PRBS))]]
    for gbtSelect in range(0,2):
        for elink in PRBS_ELINKS[gbtSelect]:
            megaWordCnt = parseInt(readReg(getNode('GEM_AMC.GEM_TESTS.OH_LOOPBACK.GBT_%d.ELINK_%d.MEGA_WORD_CNT' % (gbtSelect, elink))))
            errorCnt = parseInt(readReg(getNode('GEM_AMC.GEM_TESTS.OH_LOOPBACK.GBT_%d.ELINK_%d.ERROR_CNT' % (gbtSelect, elink))))
            #print(str(gbtSelect) + "  " + str(elink))
            prbs_counters[gbtSelect][elink-6] = [megaWordCnt , errorCnt]
    return prbs_counters

def clear_loopback_counters():
    # reset loopback counters
    writeReg(getNode('GEM_AMC.GEM_TESTS.OH_LOOPBACK.CTRL.RESET'), 1)
    sleep(0.1)
    return

def enable_loopback():
    # Put CTP7 into loopback testing mode
    writeReg(getNode('GEM_AMC.GEM_SYSTEM.TESTS.GBT_LOOPBACK_EN'), 1)
    sleep(0.1)
    return

def disable_loopback():
    writeReg(getNode('GEM_AMC.GEM_SYSTEM.TESTS.GBT_LOOPBACK_EN'), 0)
    sleep(0.1)
    return

def select_OH(oh):
    # select the OH to be used
    writeReg(getNode('GEM_AMC.GEM_TESTS.OH_LOOPBACK.CTRL.OH_SELECT'), oh)
    sleep(0.1)
    return
