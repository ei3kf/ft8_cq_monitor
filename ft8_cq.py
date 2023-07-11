#!/usr/bin/env python3

import time
import re
import sys

def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def has_worked_before(callsign):
    logbook = "/home/andy/.local/share/WSJT-X/wsjtx_log.adi"
    with open(logbook, "r") as log_book:
        for line in log_book:
            if re.search(r'\b{}\b'.format(callsign), line):
                return True
    return False

if __name__ == '__main__':
    unique_callsigns = []
    log_file = "/home/andy/.local/share/WSJT-X/ALL.TXT"
    with open(log_file, "r") as logfile:
        loglines = follow(logfile)
        for line in loglines:
            stripped = line.strip("\n")
            if " CQ " in stripped:
                try:
                    half_stripped = stripped.split(" CQ ")[1]
                except Exception as e:
                    print(f"Error: {e} {stripped}")
                    sys.exit(1)

                callsign = half_stripped.split(" ")[0]
                if len(callsign) >= 3:
                    if not has_worked_before(callsign) and callsign not in unique_callsigns:
                        unique_callsigns.append(callsign)
                        print(f"{callsign} ==> {stripped}")

    print("")
