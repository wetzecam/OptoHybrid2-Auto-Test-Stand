import sys
import os

from rw_reg import *
from time import *
from mcs import *
from cmd_output import *


class Virtex6Instructions:
    FPGA_ID     = 0x3C9
    USER_CODE   = 0x3C8
    SYSMON      = 0x3F7
    BYPASS      = 0x3FF
    CFG_IN      = 0x3C5
    CFG_OUT     = 0x3C4
    SHUTDN      = 0x3CD
    JPROG       = 0x3CB
    JSTART      = 0x3CC
    ISC_NOOP    = 0x3D4
    ISC_ENABLE  = 0x3D0
    ISC_PROGRAM = 0x3D1
    ISC_DISABLE = 0x3D6


ARTIX7_75T_FIRMWARE_SIZE = 3825768
ARTIX7_75T_FPGA_ID = 0x49c0
VIRTEX6_FIRMWARE_SIZE = 5464972
VIRTEX6_FPGA_ID = 0x6424a093

FIRMWARE_SIZE = ARTIX7_75T_FIRMWARE_SIZE
FPGA_ID = ARTIX7_75T_FPGA_ID

ADDR_JTAG_LENGTH = None
ADDR_JTAG_TMS = None
ADDR_JTAG_TDO = None
ADDR_JTAG_TDI = None


def initJtagRegAddrs():
    global ADDR_JTAG_LENGTH
    global ADDR_JTAG_TMS
    global ADDR_JTAG_TDO
    global ADDR_JTAG_TDI
    ADDR_JTAG_LENGTH = getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.NUM_BITS').real_address
    ADDR_JTAG_TMS = getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TMS').real_address
    ADDR_JTAG_TDO = getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TDO').real_address
    #ADDR_JTAG_TDI = getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TDI').real_address

# freqDiv -- JTAG frequency expressed as a divider of 20MHz, so e.g. a value of 2 would give 10MHz, value of 10 would give 2MHz
def enableJtag(ohMask, freqDiv=None):
    subheading('Disabling SCA ADC monitoring')
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.ADC_MONITORING.MONITORING_OFF'), 0xffffffff)
    sleep(0.01)
    subheading('Enable JTAG module with mask ' + hex(ohMask))
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.ENABLE_MASK'), ohMask)
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.SHIFT_MSB'), 0x0)
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.EXPERT.EXEC_ON_EVERY_TDO'), 0x0)
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.EXPERT.NO_SCA_LENGTH_UPDATE'), 0x0)
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.EXPERT.SHIFT_TDO_ASYNC'), 0x0)

    if freqDiv is not None:
        subheading('Setting JTAG CLK frequency to ' + str(20 / (freqDiv)) + 'MHz (divider value = ' + hex((freqDiv - 1) << 24) + ')')
        ohList = []
        for i in range(0,12):
            if check_bit(ohMask, i):
                ohList.append(i)
        sendScaCommand(ohList, 0x13, 0x90, 0x4, (freqDiv - 1) << 24, False)


def disableJtag():
    subheading('Disabling JTAG module')
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.CTRL.ENABLE_MASK'), 0x0)
#    subheading('Enabling SCA ADC monitoring')
#    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.ADC_MONITORING.MONITORING_OFF'), 0x0)


# restoreIdle  -- if True then will restore to IDLE state before doing anything else
# ir           -- instruction register, set it to None if it's not needed to shift the instruction register
# irLen        -- number of bits in the instruction register
# dr           -- data register, set it to None if it's not needed to shift the data register
# drLen        -- number of bits in the data register
# drReadOhList -- read the TDI during the data register shifting from this list of OHs
def jtagCommand(restoreIdle, ir, irLen, dr, drLen, drReadOhList):
    totalLen = 0
    if ir is not None:
        totalLen += irLen + 6       # instruction register length plus 6 TMS bits required to get to the IR shift state and back to IDLE
    if dr is not None:
        totalLen += drLen + 5       # data register length plus 5 TMS bits required to get to the DR shift state and back to IDLE
    if restoreIdle:
        totalLen += 6
    if totalLen > 128:
        raise ValueError('JTAG command request needs more than 128 bits -- not possible. Please break up your command into smaller pieces.')

    tms = 0
    tdo = 0
    len = 0
    readIdx = 0

    if restoreIdle:
        tms = 0b011111
        len = 6

    if ir is not None:
        tms |= 0b0011 << len         # go to IR SHIFT state
        len += 4
        tdo |= ir << len
        tms |= 0b1 << (irLen - 1 + len)  # exit IR shift
        len += irLen
        tms |= 0b01 << len    # update IR and go to IDLE
        len += 2

    if dr is not None:
        tms |= 0b001 << len    # go to DR SHIFT state
        len += 3
        readIdx = len
        tdo |= dr << len
        tms |= 0b1 << (drLen -1 + len) # exit DR shift
        len += drLen
        tms |= 0b01 << len     # update DR and go to IDLE
        len += 2


    debug('Length = ' + str(len))
    debug('TMS = ' + binary(tms, len))
    debug('TDO = ' + binary(tdo, len))
    debug('Read start index = ' + str(readIdx))

    debugCyan('Setting command length = ' + str(len))
    fw_len = len if len < 128 else 0 # in firmware 0 means 128 bits
    #writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.NUM_BITS'), fw_len)
    wReg(ADDR_JTAG_LENGTH, fw_len)

    # ================= SENDING LENGTH COMMAND JUST FOR TEST!! ===================
    #debugCyan('Setting config registers: bit number = ' + hex(fw_len))
    #sendScaCommand(0x13, 0x80, 0x4, 0xc00 | (fw_len << 24), False) # TX falling edge, shift LSB first, and set length
    # ============================================================================

    #raw_input("press any key to send tms and tdo")

    debugCyan('Setting TMS 0 = ' + binary(tms & 0xffffffff, 32))
    #writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TMS'), tms0)
    wReg(ADDR_JTAG_TMS, tms & 0xffffffff)

    debugCyan('Setting TDO 0 = ' + binary(tdo & 0xffffffff, 32))
    #writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TDO'), tdo0)
    wReg(ADDR_JTAG_TDO, tdo & 0xffffffff)

    if len > 32:
        tms = tms >> 32
        debugCyan('Setting TMS 1 = ' + binary(tms & 0xffffffff, 32))
        #writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TMS'), tms1)
        wReg(ADDR_JTAG_TMS, tms & 0xffffffff)

        #raw_input("press any key to send the last TDO")

        tdo = tdo >> 32
        debugCyan('Setting TDO 1 = ' + binary(tdo & 0xffffffff, 32))
        #writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TDO'), tdo1)
        wReg(ADDR_JTAG_TDO, tdo & 0xffffffff)

    if len > 64:
        tms = tms >> 32
        debugCyan('Setting TMS 2 = ' + binary(tms & 0xffffffff, 32))
        #writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TMS'), tms2)
        wReg(ADDR_JTAG_TMS, tms & 0xffffffff)

        tdo = tdo >> 32
        debugCyan('Setting TDO 2 = ' + binary(tdo & 0xffffffff, 32))
        #writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TDO'), tdo2)
        wReg(ADDR_JTAG_TDO, tdo & 0xffffffff)

    if len > 96:
        tms = tms >> 32
        debugCyan('Setting TMS 3 = ' + binary(tms & 0xffffffff, 32))
        #writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TMS'), tms3)
        wReg(ADDR_JTAG_TMS, tms & 0xffffffff)

        tdo = tdo >> 32
        debugCyan('Setting TDO 3 = ' + binary(tdo & 0xffffffff, 32))
        #writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TDO'), tdo3)
        wReg(ADDR_JTAG_TDO, tdo & 0xffffffff)

    # ================= SENDING JTAG GO COMMAND JUST FOR TEST!! ===================
    #debugCyan('JTAG GO!')
    #sendScaCommand(0x13, 0xa2, 0x1, 0x0, False)
    # ============================================================================

    #raw_input("Press any key to read TDI...")

    readValues = []

    if drReadOhList == False:
        return readValues

    for i in drReadOhList:
        debugCyan('Read TDI 0')
        tdi = parseInt(readReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TDI_OH%d' % i)))
        #tdi0_fast = parseInt(rReg(parseInt(ADDR_JTAG_TDI)))
        #print('normal tdi read = ' + hex(tdi0) + ', fast C tdi read = ' + hex(tdi0_fast) + ', parsed = ' + '{0:#010x}'.format(tdi0_fast))
        debug('tdi = ' + hex(tdi))

        if len > 32:
            debugCyan('Read TDI 1')
            tdi1 = parseInt(readReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TDI_OH%d' % i)))
            tdi |= tdi1 << 32
            debug('tdi1 = ' + hex(tdi1))
            debug('tdi = ' + hex(tdi))

        if len > 64:
            debugCyan('Read TDI 2')
            tdi2 = parseInt(readReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TDI_OH%d' % i)))
            tdi |= tdi2 << 64
            debug('tdi2 = ' + hex(tdi2))
            debug('tdi = ' + hex(tdi))

        if len > 96:
            debugCyan('Read TDI 3')
            tdi3 = parseInt(readReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.JTAG.TDI_OH%d' % i)))
            tdi |= tdi3 << 96
            debug('tdi3 = ' + hex(tdi3))
            debug('tdi = ' + hex(tdi))

        readValue = (tdi >> readIdx) & (0xffffffffffffffffffffffffffffffff >> (128  - drLen))
        readValues.append(readValue)
        debug('Read pos = ' + str(readIdx))
        debug('Read = ' + hex(readValue))
    return readValues
