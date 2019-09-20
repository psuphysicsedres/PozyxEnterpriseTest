# TODO list

## Header
Produce a header for CSV file so it is easier to work with.

## put all other output on STDERR

## Make better
This code really should write to a file and the parsing should be put in a
separate section, not just in the callback function.  Although, this is
probably not necessary for the success of the project

# Completed Tasks / Diary
tag 0x67d/26477/amy: ()m
tag 0x6a47/27207/brian: ()m

## New Z-coords for anchors
64449: z=0.738 m
50356: z=2.049 m
33186: z=1.724 m
52813: z=2.063 m
12503: z=1.372 m
40312: z=2.024 m
NOTE: These are just for reference.  All previous data from 2019-09-17 through
to today are were taken with other anchor coordinates as recorded in the anchor
configuration backup files.

## Enterprise Testing SRTC 113 2019-09-19T12:40 Low-Speed/High-Accuracy (5 Hz ea.)
tag 0x67d/26477/amy: (5.525,7.352,2.449)m
tag 0x6a47/27207/brian: (8.294,7.433,2.330)m


## Enterprise Testing SRTC 113 2019-09-19T12:25 Low-Speed/High-Accuracy (5 Hz ea.)
tag 0x67d/26477/amy: (2.383,6.826,2.567)m
tag 0x6a47/27207/brian: (9.656,2.218,2.194)m

## Enterprise Testing SRTC 113 2019-09-19T12:00 Low-Speed/High-Accuracy (5 Hz ea.)
room size: (10.324,9.813,3.556) m
tag 0x67d/26477/amy: (2.442,6.970,2.790) m
tag 0x6a47/27207/brian: (4.668,4.819,2.766) m
While the Controller was set to Low/High, I set the tags to match, but
increased the data rate to 5 Hz for each tag.

## Enterprise Testing SRTC 113 2019-09-17 Low-Speed/High-Accuracy
tag location: approximately the same as 2019-09-12
This time we used the Low-Speed/High-Accuracy Settings, which we figured out
requires changing teach tag configuration to match the "Controller".

## try1.py Fix output data type integer for position values

## Enterprise Testing SRTC 113 2019-09-12 High-Speed/Low-Accuracy Settings
tag 1: (7.496,5.28,2.764) m
tag 2: tag 1 + (0.020 , 0,0) m
First Light!
We had to use the High-Speed/Low-Accuracy settings, because we couldn't get it
to work on the Low-Speed/High-Accuracy settings.

