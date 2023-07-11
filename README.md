# ft8_cq_monitor

Small Python script that monitors the WSJT-X/ALL.TXT file for CQs, if a new station is logged calling CQ then print the details on screen.  I wanted to have some sort of method that would notify me that there was new activity on the 8M(40Mhz) amateur radio band on FT8.

$ ./ft8_cq.py 
G0KUC ==> 230711_204730     5.357 Rx FT8      6  0.1  817 CQ G0KUC IO91
IK2SHQ ==> 230711_205245     5.357 Rx FT8     -3  0.0  625 CQ IK2SHQ JN55
DB1TH ==> 230711_205615     5.357 Rx FT8     -7  0.3 2430 CQ DB1TH JN68
SP2CHY ==> 230711_210000     5.357 Rx FT8      9  0.2  567 CQ SP2CHY JO94
EW8CW ==> 230711_210400     5.357 Rx FT8     -1  0.1 1795 CQ EW8CW KO52
OE6TNO ==> 230711_210615     5.357 Rx FT8     -3  0.0  708 CQ OE6TNO JN77

ToDo
* Rather than print the CQ event to screen, push it to email or someother notification thingy so I can be alerted of a new station to work on amateur radio.

  
