#! /usr/bin/env python
"""ntplib test script.
Send a request to a NTP server, and analyse the response.
"""

import sys
from time import ctime

import ntplib


if len(sys.argv) > 1:
    hostname = sys.argv[1]
else:
    sys.stdout.write('NTP server ? ')
    hostname = sys.stdin.readline().strip()

client = ntplib.NTPClient()
response = client.request(hostname, version=3)

print('Version number : %d' % response.version)
print('Offset : %f' % response.offset)
print('Stratum : %s (%d)' % (ntplib.stratum_to_text(response.stratum),
    response.stratum))
print('Precision : %d' % response.precision)
print('Root delay : %f ' % response.root_delay)
print('Root dispersion : %f' % response.root_dispersion)
print('Delay : %f' % response.delay)
print('Leap indicator : %s (%d)' % (ntplib.leap_to_text(response.leap),
    response.leap))
print('Poll : %d' % response.poll)
print('Mode : %s (%d)' % (ntplib.mode_to_text(response.mode), response.mode))
print('Transmit timestamp : ' + ctime(response.tx_time))
print('Reference timestamp : ' + ctime(response.ref_time))
print('Original timestamp : ' + ctime(response.orig_time))
print('Receive timestamp : ' + ctime(response.recv_time))
print('Destination timestamp : ' + ctime(response.dest_time))
print('Reference clock identifier : ' + ntplib.ref_id_to_text(response.ref_id,
    response.stratum))
