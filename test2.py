import sys
import os
sys.path.insert(1,os.getcwd()+'/utils')
from classes import *
import numpy as np


def main():

    xml_head = XML_HEADER()
    hw_info = HW_Info()
    test_conditions = Test_Condition()
    test_results = Test_Result()
    adc_reading = ADC_Data()


    vector = [[1,2,3,4,5],[6,7,8,9,10]]

    print(np.size(vector))
    print(len(vector))


    print(10**-12)


if __name__ == '__main__':
    main()
