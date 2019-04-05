# 16SegDisplayDecoder

Created by Aditya Vidyadharan

Edit .pld file using WINCUPL and program PLD with .jed file using Wellon

MSI circuit using 2 cascaded counters to provide 6 bit input to PLD. Input is decoded by PLD to rotate through letters of alphabet and numbers on 16 segment display.

Circuit details: 
* Function generator provides clock 
* (x2) 4-bit counters cascaded to provide 6-bit input 
* (x2) PLDs connected to 6-bit input and outputs connected to 16-segment display
* 16 Segment Display
