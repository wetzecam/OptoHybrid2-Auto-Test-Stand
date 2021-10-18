#!/bin/env python
import sys
import os
import array
import struct

WORKING_DIR=os.getcwd()

sys.path.insert(1,WORKING_DIR+'/utils')
from rw_reg import *
from JTAG import *
from SCA import *
from cmd_output import *


########################################################################################################################################

def Trigger_reset():
    writeReg(getNode('GEM_AMC.TRIGGER.CTRL.MODULE_RESET'), 1)
    return

def read_vttx_optical_link(verbose=False):
    Link_CNT = []
    Delta_Link_CNT = []
    Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_MISSED_COMMA_CNT'))))
    Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_MISSED_COMMA_CNT'))))
    Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_OVERFLOW_CNT'))))
    Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_OVERFLOW_CNT'))))
    Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_UNDERFLOW_CNT'))))
    Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_UNDERFLOW_CNT'))))
    if verbose:
        print('VTTX Optical Link Readings First Read:')
        readKW('GEM_AMC.TRIGGER.OH0') # prints status for log file

    sleep(3)
    Delta_Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_MISSED_COMMA_CNT'))) - Link_CNT[0])
    Delta_Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_MISSED_COMMA_CNT'))) - Link_CNT[1])
    Delta_Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_OVERFLOW_CNT'))) - Link_CNT[2])
    Delta_Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_OVERFLOW_CNT'))) - Link_CNT[3])
    Delta_Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_UNDERFLOW_CNT'))) - Link_CNT[4])
    Delta_Link_CNT.append(parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_UNDERFLOW_CNT'))) - Link_CNT[5])
    if verbose:
        print('VTTX Optical Link Readings Second Read (3s Delay):')
        readKW('GEM_AMC.TRIGGER.OH0') # prints status for log file
    return [Link_CNT , Delta_Link_CNT]

def check_vttx_optical_link_result(VTTX_Result, verbose=False):
    PF_Flag = True
    ErrorMessage = []
    regs = ['GEM_AMC.TRIGGER.OH0.LINK0_MISSED_COMMA_CNT', 'GEM_AMC.TRIGGER.OH0.LINK1_MISSED_COMMA_CNT', 'GEM_AMC.TRIGGER.OH0.LINK0_OVERFLOW_CNT', 'GEM_AMC.TRIGGER.OH0.LINK1_OVERFLOW_CNT','GEM_AMC.TRIGGER.OH0.LINK0_UNDERFLOW_CNT','GEM_AMC.TRIGGER.OH0.LINK1_UNDERFLOW_CNT']
    expectedValue = 2   # Should be less Than 2 for all Readings
    for ii in range(len(VTTX_Result[0])):
        if VTTX_Result[0][ii] > expectedValue:
            PF_Flag = False
            ErrorMessage.append(regs[ii] + ' = ' + str(VTTX_Result[0][ii]))

    for ii in range(len(VTTX_Result[1])):
        if VTTX_Result[1][ii] > 0:
            PF_Flag = False
            ErrorMessage.append(regs[ii] + ' Incremented by: ' +str(VTTX_Result[1][ii]+'  Between Reads'))

    return [PF_Flag, ErrorMessage]


########################################################################################################################################

def vttx_link_health_test():

    PASS = True

#    writeReg(getNode('GEM_AMC.GEM_SYSTEM.CTRL.LINK_RESET'), 1)
#    sleep(0.25)
    writeReg(getNode('GEM_AMC.TRIGGER.CTRL.CNT_RESET'), 1)
    writeReg(getNode('GEM_AMC.TRIGGER.CTRL.MODULE_RESET'), 1)
    print('Sleeping, to build up Bits Tx\'d for VTTX Health Test...')
    sleep(300)
    print('Done Sleeping!')
    # verify error counters are 0 or low value, not increment
    PASS = check_vttx_link()

    word = ''
    if PASS:
        word = 'PASSED'
    else :
        word = 'FAILED'

    print('Test VTTX Optical Links with CTP7: %s' % word)

    return PASS


def check_vttx_link():
    #returns true if test passes
    passFail = True

    link0_missed = parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_MISSED_COMMA_CNT')))
    link1_missed = parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_MISSED_COMMA_CNT')))
    link0_overflow = parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_OVERFLOW_CNT')))
    link1_overflow = parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_OVERFLOW_CNT')))
    link0_underflow = parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_UNDERFLOW_CNT')))
    link1_underflow = parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_UNDERFLOW_CNT')))

    # wait a few seconds to ensure no increment
    sleep(1)

    cntChange = link0_missed - parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_MISSED_COMMA_CNT')))
    if cntChange != 0:
        print('FAIL: GEM_AMC.TRIGGER.OH0.LINK0_MISSED_COMMA_CNT incremented by, %d' % cntChange)
        passFail = False

    cntChange = link1_missed - parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_MISSED_COMMA_CNT')))
    if cntChange != 0:
        print('FAIL: GEM_AMC.TRIGGER.OH0.LINK1_MISSED_COMMA_CNT incremented by, %d' % cntChange)
        passFail = False

    cntChange = link0_overflow - parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_OVERFLOW_CNT')))
    if cntChange != 0:
        print('FAIL: GEM_AMC.TRIGGER.OH0.LINK0_OVERFLOW_CNT incremented by, %d' % cntChange)
        passFail = False

    cntChange =  link1_overflow - parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_OVERFLOW_CNT')))
    if cntChange != 0:
        print('FAIL: GEM_AMC.TRIGGER.OH0.LINK1_OVERFLOW_CNT incremented by, %d' % cntChange)
        passFail = False

    cntChange = link0_underflow - parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK0_UNDERFLOW_CNT')))
    if cntChange != 0:
        print('FAIL: GEM_AMC.TRIGGER.OH0.LINK0_UNDERFLOW_CNT incremented by, %d' % cntChange)
        passFail = False

    cntChange = link1_underflow - parseInt(readReg(getNode('GEM_AMC.TRIGGER.OH0.LINK1_UNDERFLOW_CNT')))
    if cntChange != 0:
        print('FAIL: GEM_AMC.TRIGGER.OH0.LINK1_UNDERFLOW_CNT incremented by, %d' % cntChange)
        passFail = False


    print('readKW GEM_AMC.TRIGGER.OH0')
    readKW('GEM_AMC.TRIGGER.OH0') # prints status for log file

    return passFail
