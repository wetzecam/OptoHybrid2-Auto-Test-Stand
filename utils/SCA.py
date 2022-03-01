from time import *
from rw_reg import *
from mcs import *
from time import *
import array
import struct

def sendScaCommand(ohList, sca_channel, sca_command, data_length, data, doRead):
    #print('fake send: channel ' + hex(sca_channel) + ', command ' + hex(sca_command) + ', length ' + hex(data_length) + ', data ' + hex(data) + ', doRead ' + str(doRead))
    #return

    d = data

    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.MANUAL_CONTROL.SCA_CMD.SCA_CMD_CHANNEL'), sca_channel)
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.MANUAL_CONTROL.SCA_CMD.SCA_CMD_COMMAND'), sca_command)
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.MANUAL_CONTROL.SCA_CMD.SCA_CMD_LENGTH'), data_length)
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.MANUAL_CONTROL.SCA_CMD.SCA_CMD_DATA'), d)
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.MANUAL_CONTROL.SCA_CMD.SCA_CMD_EXECUTE'), 0x1)
    sleep(0.00015)
    reply = []
    if doRead:
        for i in ohList:
            reply.append(parseInt(readReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.MANUAL_CONTROL.SCA_REPLY_OH%d.SCA_RPY_DATA' % i))))
    return reply

def check_SCA_ASIC_bool():
    #returns true if test passes
    passFAIL = True

    if parseInt(readReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.STATUS.READY'))) != 1:
        print("SCA ASIC not READY!")
        passFAIL =  False
    else :
        print("SCA ASIC GOOD!")

    return passFAIL

def reset_SCA_ASIC():
    # reset SCA
    writeReg(getNode('GEM_AMC.SLOW_CONTROL.SCA.CTRL.MODULE_RESET'), 1)
