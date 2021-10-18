Loading /mnt/persistent/texas/full_test/fw/oh/OH_3_2_8_GE21v2.bit
Buffering
Zeroing 1
Zeroing 2
Writing 1
Writing 2
Verifying -- Reading
Verifying -- Comparing
Done
Loading shared library: /mnt/persistent/texas/shared_libs/librwreg.so
Parsing /mnt/persistent/texas/gem_amc_top.xml ...
[94m

>>>>>>> HELLO, I'M YOUR GBT CONTROLLER :) <<<<<<<
[0m
[93m ---- Configuring OH0 GBT0 ---- [0m
Wrote 369 registers to OH0 GBT0
time took = 0.026667s
GBT 0 Configuration SUCCESS
[94m

>>>>>>> HELLO, I'M YOUR GBT CONTROLLER :) <<<<<<<
[0m
[93m ---- Configuring OH0 GBT1 ---- [0m
Wrote 369 registers to OH0 GBT1
time took = 0.026487s
GBT 1 Configuration SUCCESS
readKW OH_LINKS.OH0.GBT
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT0_READY				0x00000001
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT1_READY				0x00000001
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT2_READY				0x00000000
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT0_WAS_NOT_READY			0x00000000
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT1_WAS_NOT_READY			0x00000000
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT2_WAS_NOT_READY			0x00000000
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT0_RX_HAD_OVERFLOW		0x00000000
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT1_RX_HAD_OVERFLOW		0x00000000
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT2_RX_HAD_OVERFLOW		0x00000000
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT0_RX_HAD_UNDERFLOW		0x00000000
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT1_RX_HAD_UNDERFLOW		0x00000000
0x65800400 r 	GEM_AMC.OH_LINKS.OH0.GBT2_RX_HAD_UNDERFLOW		0x00000000
Check GBTx transmission to CTP7: PASSED
0x66c00400 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.READY			0x00000001
0x66c00404 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.CRITICAL_ERROR		0x00000000
0x66c00408 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.NOT_READY_CNT_OH0	0x00000002
Check SCA ASIC: PASSED
0x66c00400 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.READY			0x00000001
0x66c00404 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.CRITICAL_ERROR		0x00000000
0x66c00408 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.NOT_READY_CNT_OH0	0x00000002
[95mPROGRAMMED FULL FW[0m
[97mRSSI Reading = [True, 378.5714285714285, 241.57509157509136][0m
[95mTesting FPGA LOAD PATH (x5)[0m
[93m ---- 5 iterations done, HR Errors: 0, program Errors: 0 ---- [0m
VTRX Strength:	RSSI1	RSSI2
    [uA] 	[92m377.472527473[0m	[92m243.772893773[0m
Temperature:	FPGA	SCA	U2	U3	U22	U8
    [C] 	[92m37.0357849121[0m	[92m31.8758931624[0m	[92m28.5872715365[0m	[92m28.6599555556[0m	[92m28.6599555556[0m	[92m27.9331153652[0m
Voltages:	1.0V	AVCC	AVTT	1.8V	1.5V	2.5V
    [V] 	[92m0.996336996337[0m	[92m1.0021978022[0m	[92m1.19365079365[0m	[92m1.85592185592[0m	[92m1.52771672772[0m	[92m2.4547008547[0m
Currents:	FEAST1	FEAST2	FEAST3	FEAST4	FEAST5
    [A] 	[92m1.20634920635[0m	[92m1.63614163614[0m	[92m0.610500610501[0m	[92m0.537240537241[0m	[92m1.00610500611[0m
Current Mirror Calibration [uA]: 96.947497
=============================
[[377.47252747252736, 243.77289377289378], [37.03578491210942, 31.875893162393197, 28.587271536523929, 28.659955555555541, 28.659955555555541, 27.933115365239246], [0.99633699633699635, 1.0021978021978022, 1.1936507936507939, 1.855921855921856, 1.5277167277167276, 2.4547008547008549], [1.2063492063492063, 1.6361416361416363, 0.61050061050061044, 0.53724053724053722, 1.0061050061050061], 96.947496947496944]
readKW GEM_AMC.TRIGGER.OH0
0x66000400 None 	GEM_AMC.TRIGGER.OH0					
0x66000400 r 	GEM_AMC.TRIGGER.OH0.TRIGGER_RATE			0x02638e98
0x66000404 r 	GEM_AMC.TRIGGER.OH0.TRIGGER_CNT				0x02e13d04
0x66000440 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_0_RATE			0x00000000
0x66000444 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_1_RATE			0x02638e98
0x66000448 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_2_RATE			0x00000000
0x6600044c r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_3_RATE			0x00000000
0x66000450 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_4_RATE			0x00000000
0x66000454 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_5_RATE			0x00000000
0x66000458 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_6_RATE			0x00000000
0x6600045c r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_7_RATE			0x00000000
0x66000460 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_8_RATE			0x00000000
0x66000480 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_0_CNT			0x00000000
0x66000484 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_1_CNT			0x02e279e2
0x66000488 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_2_CNT			0x000000Loading /mnt/persistent/texas/full_test/fw/oh/oh_ge21v2_loopback_120.bit
Buffering
Zeroing 1
Zeroing 2
Writing 1
Writing 2
Verifying -- Reading
Verifying -- Comparing
Done
00
0x6600048c r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_3_CNT			0x00000000
0x66000490 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_4_CNT			0x00000000
0x66000494 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_5_CNT			0x00000000
0x66000498 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_6_CNT			0x00000000
0x6600049c r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_7_CNT			0x00000000
0x660004a0 r 	GEM_AMC.TRIGGER.OH0.CLUSTER_SIZE_8_CNT			0x00000000
0x66000680 r 	GEM_AMC.TRIGGER.OH0.LINK0_SBIT_OVERFLOW_CNT		0x00000000
0x66000680 r 	GEM_AMC.TRIGGER.OH0.LINK1_SBIT_OVERFLOW_CNT		0x00000000
0x66000684 r 	GEM_AMC.TRIGGER.OH0.LINK0_MISSED_COMMA_CNT		0x00000000
0x66000684 r 	GEM_AMC.TRIGGER.OH0.LINK1_MISSED_COMMA_CNT		0x00000000
0x6600068c r 	GEM_AMC.TRIGGER.OH0.LINK0_OVERFLOW_CNT			0x00000000
0x6600068c r 	GEM_AMC.TRIGGER.OH0.LINK1_OVERFLOW_CNT			0x00000000
0x66000690 r 	GEM_AMC.TRIGGER.OH0.LINK0_UNDERFLOW_CNT			0x00000000
0x66000690 r 	GEM_AMC.TRIGGER.OH0.LINK1_UNDERFLOW_CNT			0x00000000
0x66000694 r 	GEM_AMC.TRIGGER.OH0.LINK0_SYNC_WORD_CNT			0x00000000
0x66000694 r 	GEM_AMC.TRIGGER.OH0.LINK1_SYNC_WORD_CNT			0x00000000
Test VTTX Optical Links with CTP7: PASSED
[95mAbout to Program prbs FW[0m
0x66c00400 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.READY			0x00000001
0x66c00404 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.CRITICAL_ERROR		0x00000000
0x66c00408 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.NOT_READY_CNT_OH0	0x00000002
[95mSCA Status = True[0m
[94m

>>>>>>> HELLO, I'M YOU GBT CONTROLLER :) <<<<<<<
[0m
[93m ---- Configuring OH0 GBT0 ---- [0m
Wrote 369 registers to OH0 GBT0
time took = 0.025831s

Phase        e-link 6     e-link 7     e-link 8     e-link 9     
0            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
1            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
2            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
3            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
4            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
5            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
6            [91m249326572    [0m[92m0            [0m[92m0            [0m[91m380201398    [0m
7            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
8            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
9            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
10           [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
11           [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
12           [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
13           [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
14           [92m0            [0m[91m1166001      [0m[92m0            [0m[91m399962725    [0m
[94m

>>>>>>> HELLO, I'M YOU GBT CONTROLLER :) <<<<<<<
[0m
[93m ---- Configuring OH0 GBT1 ---- [0m
Wrote 369 registers to OH0 GBT1
time took = 0.025638s

Phase        e-link 6     e-link 7     e-link 8     e-link 9     e-link 10    e-link 11    e-link 12    e-link 13    
0            [92m0            [0m[92m0            [0m[92m0            [0m[91m241849       [0m[92m0            [0m[92m0            [0m[92m0            [0m[91m49743        [0m
1            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
2            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
3            [91m393311628    [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
4            [91m155935791    [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
5            [92m0            [0m[91m148          [0m[91m19951500     [0m[92m0            [0m[91mNO LOCK      [0m[92m0            [0m[92m0            [0m[92m0            [0m
6            [92m0            [0m[91m1374         [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[91m389630663    [0m[92m0            [0m
7            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[91mNO LOCK      [0m[92m0            [0m[91m5362513      [0m
8            [92m0            [0m[92m0            [0m[92m0            [0m[91m301882       [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
9            [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
10           [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
11           [91m321212901    [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
12           [91m115284       [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m
13           [92m0            [0m[91m357918520    [0m[91mNO LOCK      [0m[92m0            [0m[91mNO LOCK      [0m[92m0            [0m[92m0            [0m[92m0            [0m
14           [92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[92m0            [0m[91m22           [0m[92m0            [0m
[[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', False)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 8, ' Center = ', 10.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', False)
('Best Window: Width = ', 14, ' Center = ', 6.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 15, ' Center = ', 7.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', False)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', False)
('Best Window: Width = ', 7, ' Center = ', 10.0)
[[8, 10.0], [14, 6.0], [15, 7.0], [7, 10.0]]
[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', False)
('Current Phase = ', 4, ' Status = ', False)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', False)
('Current Phase = ', 12, ' Status = ', False)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 6, ' Center = ', 7.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', False)
('Current Phase = ', 6, ' Status = ', False)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', False)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 6, ' Center = ', 9.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', False)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', False)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 7, ' Center = ', 9.0)
('Current Phase = ', 0, ' Status = ', False)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', False)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 7, ' Center = ', 4.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', False)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', False)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 7, ' Center = ', 9.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', False)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 7, ' Center = ', 3.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', False)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', False)
('Best Window: Width = ', 7, ' Center = ', 10.0)
('Current Phase = ', 0, ' Status = ', False)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', False)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 7, ' Center = ', 11.0)
[[6, 7.0], [6, 9.0], [7, 9.0], [7, 4.0], [7, 9.0], [7, 3.0], [7, 10.0], [7, 11.0]]
[94m

>>>>>>> HELLO, I'M YOU GBT CONTROLLER :) <<<<<<<
[0m
[93m ---- Configuring OH0 GBT0 ---- [0m
Wrote 369 registers to OH0 GBT0
time took = 0.03618s
[93m ---- Setting phase = 0 for elink 0 ---- [0m
[92m COMMUNICATION GOOD on elink 0 VFAT0:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 0 for elink 1 ---- [0m
[92m COMMUNICATION GOOD on elink 1 VFAT1:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 0 for elink 2 ---- [0m
[92m COMMUNICATION GOOD on elink 2 VFAT2:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 0 for elink 3 ---- [0m
[92m COMMUNICATION GOOD on elink 3 VFAT3:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 0 for elink 4 ---- [0m
[92m COMMUNICATION GOOD on elink 4 VFAT4:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 0 for elink 5 ---- [0m
[92m COMMUNICATION GOOD on elink 5 VFAT5:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 10 for elink 6 ---- [0m
[93m ---- Setting phase = 6 for elink 7 ---- [0m
[93m ---- Setting phase = 7 for elink 8 ---- [0m
[93m ---- Setting phase = 10 for eliLoading /mnt/persistent/texas/full_test/fw/oh/OH_3_2_8_GE21v2.bit
Buffering
Zeroing 1
Zeroing 2
Writing 1
Writing 2
Verifying -- Reading
Verifying -- Comparing
Done
nk 9 ---- [0m
[94m

>>>>>>> HELLO, I'M YOU GBT CONTROLLER :) <<<<<<<
[0m
[93m ---- Configuring OH0 GBT1 ---- [0m
Wrote 369 registers to OH0 GBT1
time took = 0.031543s
[93m ---- Setting phase = 0 for elink 0 ---- [0m
[92m COMMUNICATION GOOD on elink 0 VFAT6:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 0 for elink 1 ---- [0m
[92m COMMUNICATION GOOD on elink 1 VFAT7:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 0 for elink 2 ---- [0m
[92m COMMUNICATION GOOD on elink 2 VFAT8:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 0 for elink 3 ---- [0m
[92m COMMUNICATION GOOD on elink 3 VFAT9:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 0 for elink 4 ---- [0m
[92m COMMUNICATION GOOD on elink 4 VFAT10:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 0 for elink 5 ---- [0m
[92m COMMUNICATION GOOD on elink 5 VFAT11:  Phase = 0, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 7 for elink 6 ---- [0m
[93m ---- Setting phase = 9 for elink 7 ---- [0m
[93m ---- Setting phase = 9 for elink 8 ---- [0m
[93m ---- Setting phase = 4 for elink 9 ---- [0m
[93m ---- Setting phase = 9 for elink 10 ---- [0m
[93m ---- Setting phase = 3 for elink 11 ---- [0m
[93m ---- Setting phase = 10 for elink 12 ---- [0m
[93m ---- Setting phase = 11 for elink 13 ---- [0m
[95mAbout to Program FULL FW[0m
0x66c00400 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.READY			0x00000001
0x66c00404 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.CRITICAL_ERROR		0x00000000
0x66c00408 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.NOT_READY_CNT_OH0	0x00000002
[95mSCA Status = True[0m
[95mSTARTING VFAT PHASE SCAN[0m
0x66c00400 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.READY			0x00000001
0x66c00404 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.CRITICAL_ERROR		0x00000000
0x66c00408 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.NOT_READY_CNT_OH0	0x00000002
[95mSCA Status = True[0m
Wrote 369 registers to OH0 GBT0
time took = 0.026691s
[92m GOOD:  Phase = 0, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 2, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 3, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 4, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 5, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 9, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 10, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 11, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 12, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 13, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 14, VFAT0 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 0, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 2, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 3, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 4, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 5, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 9, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 10, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 11, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 12, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 13, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 14, VFAT1 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 0, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 2, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 3, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 4, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 5, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 9, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 10, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 11, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 12, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 13, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 14, VFAT2 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 0, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 2, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 3, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=15, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 4, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 5, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 9, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 10, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 11, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 12, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 13, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 14, VFAT3 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 0, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 2, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 3, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 4, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 5, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 9, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 10, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 11, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 12, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 13, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 14, VFAT4 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 0, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 2, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 3, VFAT5 LINK_GOOD=0, SYNC_ERR_CNT=15, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 4, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 5, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 9, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 10, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 11, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 12, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 13, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 14, VFAT5 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
Wrote 369 registers to OH0 GBT1
time took = 0.026599s
[92m GOOD:  Phase = 0, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 2, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 3, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 4, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 5, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 9, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 10, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 11, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 12, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 13, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 14, VFAT6 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 0, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 2, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 3, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 4, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 5, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 9, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 10, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 11, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 12, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 13, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 14, VFAT7 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 0, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 2, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 3, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 4, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 5, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 9, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 10, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 11, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 12, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 13, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 14, VFAT8 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 0, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 2, VFAT9 LINK_GOOD=0, SYNC_ERR_CNT=15, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 3, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 4, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 5, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 9, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 10, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=15, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 11, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 12, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 13, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 14, VFAT9 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 0, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 2, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 3, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 4, VFAT10 LINK_GOOD=0, SYNC_ERR_CNT=15, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 5, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 9, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 10, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 11, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 12, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=0 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 13, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 14, VFAT10 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 0, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 1, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 2, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 3, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=15, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 4, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 5, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 6, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 7, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 8, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 9, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 10, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[91m >>>>>>>> BAD <<<<<<<<  Phase = 11, VFAT11 LINK_GOOD=0, SYNC_ERR_CNT=15, CFG_RUN_GOOD=0 [0m
[92m GOOD:  Phase = 12, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 13, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[92m GOOD:  Phase = 14, VFAT11 LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 15, ' Center = ', 7.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 15, ' Center = ', 7.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', False)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', False)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 7, ' Center = ', 7.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', False)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 11, ' Center = ', 9.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', False)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 13, ' Center = ', 6.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', False)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 11, ' Center = ', 9.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', False)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 9, ' Center = ', 4.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 15, ' Center = ', 7.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', False)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 9, ' Center = ', 4.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', False)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', False)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 7, ' Center = ', 6.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', True)
('Current Phase = ', 4, ' Status = ', False)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', True)
('Current Phase = ', 12, ' Status = ', False)
('Current Phase = ', 13, ' Status = ', False)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 7, ' Center = ', 8.0)
('Current Phase = ', 0, ' Status = ', True)
('Current Phase = ', 1, ' Status = ', True)
('Current Phase = ', 2, ' Status = ', True)
('Current Phase = ', 3, ' Status = ', False)
('Current Phase = ', 4, ' Status = ', True)
('Current Phase = ', 5, ' Status = ', True)
('Current Phase = ', 6, ' Status = ', True)
('Current Phase = ', 7, ' Status = ', True)
('Current Phase = ', 8, ' Status = ', True)
('Current Phase = ', 9, ' Status = ', True)
('Current Phase = ', 10, ' Status = ', True)
('Current Phase = ', 11, ' Status = ', False)
('Current Phase = ', 12, ' Status = ', True)
('Current Phase = ', 13, ' Status = ', True)
('Current Phase = ', 14, ' Status = ', True)
('Best Window: Width = ', 7, ' Center = ', 7.0)
[94m

>>>>>>> HELLO, I'M YOU GBT CONTROLLER :) <<<<<<<
[0m
[93m ---- Configuring OH0 GBT0 ---- [0m
Wrote 369 registers to OH0 GBT0
time took = 0.0362s
[93m ---- Setting phase = 7 for elink 0 ---- [0m
[92m COMMUNICATION GOOD on elink 0 VFAT0:  Phase = 7, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 7 for elink 1 ---- [0m
[92m COMMUNICATION GOOD on elink 1 VFAT1:  Phase = 7, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 7 for elink 2 ---- [0m
[92m COMMUNICATION GOOD on elink 2 VFAT2:  Phase = 7, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 9 for elink 3 ---- [0m
[92m COMMUNICATION GOOD on elink 3 VFAT3:  Phase = 9, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 6 for elink 4 ---- [0m
[92m COMMUNICATION GOOD on elink 4 VFAT4:  Phase = 6, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 9 for elink 5 ---- [0m
[92m COMMUNICATION GOOD on elink 5 VFAT5:  Phase = 9, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[94m

>>>>>>> HELLO, I'M YOU GBT CONTROLLER :) <<<<<<<
[0m
[93m ---- Configuring OH0 GBT1 ---- [0m
Wrote 369 registers to OH0 GBT1
time took = 0.026651s
[93m ---- Setting phase = 4 for elink 0 ---- [0m
[92m COMMUNICATION GOOD on elink 0 VFAT6:  Phase = 4, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 7 for elink 1 ---- [0m
[92m COMMUNICATION GOOD on elink 1 VFAT7:  Phase = 7, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 4 for elink 2 ---- [0m
[92m COMMUNICATION GOOD on elink 2 VFAT8:  Phase = 4, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 6 for elink 3 ---- [0m
[92m COMMUNICATION GOOD on elink 3 VFAT9:  Phase = 6, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 8 for elink 4 ---- [0m
[92m COMMUNICATION GOOD on elink 4 VFAT10:  Phase = 8, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[93m ---- Setting phase = 7 for elink 5 ---- [0m
[92m COMMUNICATION GOOD on elink 5 VFAT11:  Phase = 7, LINK_GOOD=1, SYNC_ERR_CNT=0, CFG_RUN_GOOD=1 [0m
[95mSTARTING VFAT SBIT SCAN[0m
0x66c00400 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.READY			0x00000001
0x66c00404 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.CRITICAL_ERROR		0x00000000
0x66c00408 r 	GEM_AMC.SLOW_CONTROL.SCA.STATUS.NOT_READY_CNT_OH0	0x00000002
[95mSCA Status = True[0m

####################################################################################################
Scanning VFAT 0
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [91mx [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [91mx [91mx [0m
Sbit1: [91mx [91mx [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [91mx [91mx [0m
Sbit2: [91mx [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [91mx [91mx [91mx [0m
Sbit3: [91mx [91mx [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [91mx [91mx [0m
Sbit4: [91mx [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [91mx [91mx [0m
Sbit5: [91mx [91mx [91mx [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit6: [91mx [91mx [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit7: [91mx [91mx [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
min center = 16
sot :           best_dly= 2
bit0: center=-1 best_dly= 1 width= 28 (2.184000 ns)
bit1: center=-1 best_dly= 1 width= 27 (2.106000 ns)
bit2: center=-2 best_dly= 0 width= 27 (2.106000 ns)
bit3: center=-1 best_dly= 1 width= 27 (2.106000 ns)
bit4: center=-2 best_dly= 0 width= 28 (2.184000 ns)
bit5: center= 2 best_dly= 4 width= 32 (2.496000 ns)
bit6: center= 1 best_dly= 3 width= 33 (2.574000 ns)
bit7: center= 1 best_dly= 3 width= 33 (2.574000 ns)

####################################################################################################
Scanning VFAT 1
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit1: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit2: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit3: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit4: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit5: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit6: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit7: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
min center = 17
sot :           best_dly= 1
bit0: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit1: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit2: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit3: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit4: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit5: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit6: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit7: center=-1 best_dly= 0 width= 37 (2.886000 ns)

####################################################################################################
Scanning VFAT 2
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit1: [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit2: [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit3: [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit4: [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [0m
Sbit5: [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit6: [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit7: [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
min center = 18
sot :           best_dly= 18
bit0: center= 0 best_dly= 0 width= 36 (2.808000 ns)
bit1: center= 0 best_dly= 0 width= 36 (2.808000 ns)
bit2: center= 0 best_dly= 0 width= 36 (2.808000 ns)
bit3: center= 0 best_dly= 0 width= 35 (2.730000 ns)
bit4: center= 0 best_dly= 0 width= 35 (2.730000 ns)
bit5: center= 0 best_dly= 0 width= 35 (2.730000 ns)
bit6: center= 0 best_dly= 0 width= 35 (2.730000 ns)
bit7: center= 0 best_dly= 0 width= 35 (2.730000 ns)

####################################################################################################
Scanning VFAT 3
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit1: [91mx [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit2: [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit3: [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit4: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit5: [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit6: [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit7: [91mx [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [92m- [0m
min center = 17
sot :           best_dly= 1
bit0: center= 0 best_dly= 1 width= 35 (2.730000 ns)
bit1: center= 0 best_dly= 1 width= 35 (2.730000 ns)
bit2: center= 0 best_dly= 1 width= 36 (2.808000 ns)
bit3: center= 0 best_dly= 1 width= 36 (2.808000 ns)
bit4: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit5: center= 0 best_dly= 1 width= 36 (2.808000 ns)
bit6: center= 0 best_dly= 1 width= 36 (2.808000 ns)
bit7: center= 0 best_dly= 1 width= 34 (2.652000 ns)

####################################################################################################
Scanning VFAT 4
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit1: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit2: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit3: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit4: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit5: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit6: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit7: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [0m
min center = 17
sot :           best_dly= 1
bit0: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit1: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit2: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit3: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit4: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit5: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit6: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit7: center= 0 best_dly= 1 width= 36 (2.808000 ns)

####################################################################################################
Scanning VFAT 5
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit1: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit2: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit3: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit4: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit5: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit6: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit7: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
min center = 17
sot :           best_dly= 1
bit0: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit1: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit2: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit3: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit4: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit5: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit6: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit7: center=-1 best_dly= 0 width= 37 (2.886000 ns)

####################################################################################################
Scanning VFAT 6
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit1: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit2: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit3: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit4: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit5: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit6: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit7: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
min center = 17
sot :           best_dly= 1
bit0: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit1: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit2: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit3: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit4: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit5: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit6: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit7: center=-1 best_dly= 0 width= 37 (2.886000 ns)

####################################################################################################
Scanning VFAT 7
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit1: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit2: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit3: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit4: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit5: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit6: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit7: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
min center = 17
sot :           best_dly= 1
bit0: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit1: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit2: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit3: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit4: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit5: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit6: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit7: center=-1 best_dly= 0 width= 37 (2.886000 ns)

####################################################################################################
Scanning VFAT 8
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit1: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit2: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit3: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit4: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit5: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit6: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit7: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
min center = 17
sot :           best_dly= 1
bit0: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit1: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit2: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit3: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit4: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit5: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit6: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit7: center=-1 best_dly= 0 width= 37 (2.886000 ns)

####################################################################################################
Scanning VFAT 9
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [0m
Sbit1: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [0m
Sbit2: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [0m
Sbit3: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [0m
Sbit4: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [91mx [91mx [91mx [0m
Sbit5: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [91mx [0m
Sbit6: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [91mx [0m
Sbit7: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [91mx [91mx [91mx [0m
min center = 15
sot :           best_dly= 3
bit0: center=-1 best_dly= 2 width= 34 (2.652000 ns)
bit1: center=-2 best_dly= 1 width= 33 (2.574000 ns)
bit2: center=-2 best_dly= 1 width= 33 (2.574000 ns)
bit3: center=-2 best_dly= 1 width= 33 (2.574000 ns)
bit4: center=-3 best_dly= 0 width= 30 (2.340000 ns)
bit5: center=-2 best_dly= 1 width= 32 (2.496000 ns)
bit6: center=-2 best_dly= 1 width= 32 (2.496000 ns)
bit7: center=-3 best_dly= 0 width= 30 (2.340000 ns)

####################################################################################################
Scanning VFAT 10
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit1: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit2: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit3: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit4: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit5: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [0m
Sbit6: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [91mx [0m
Sbit7: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [91mx [91mx [91mx [0m
min center = 16
sot :           best_dly= 2
bit0: center=-1 best_dly= 1 width= 37 (2.886000 ns)
bit1: center=-1 best_dly= 1 width= 37 (2.886000 ns)
bit2: center=-1 best_dly= 1 width= 37 (2.886000 ns)
bit3: center=-1 best_dly= 1 width= 37 (2.886000 ns)
bit4: center=-1 best_dly= 1 width= 37 (2.886000 ns)
bit5: center=-2 best_dly= 0 width= 33 (2.574000 ns)
bit6: center=-2 best_dly= 0 width= 32 (2.496000 ns)
bit7: center=-2 best_dly= 0 width= 32 (2.496000 ns)

####################################################################################################
Scanning VFAT 11
####################################################################################################

       2 1 0 F E D C B A 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2
Sbit0: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [0m
Sbit1: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [0m
Sbit2: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [0m
Sbit3: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [0m
Sbit4: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [0m
Sbit5: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [0m
Sbit6: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [0m
Sbit7: [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m| [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [92m- [91mx [91mx [0m
min center = 17
sot :           best_dly= 1
bit0: center=-1 best_dly= 0 width= 35 (2.730000 ns)
bit1: center=-1 best_dly= 0 width= 37 (2.886000 ns)
bit2: center=-1 best_dly= 0 width= 35 (2.730000 ns)
bit3: center=-1 best_dly= 0 width= 35 (2.730000 ns)
bit4: center= 0 best_dly= 1 width= 36 (2.808000 ns)
bit5: center= 0 best_dly= 1 width= 36 (2.808000 ns)
bit6: center= 0 best_dly= 1 width= 36 (2.808000 ns)
bit7: center=-1 best_dly= 0 width= 35 (2.730000 ns)

bye now..
