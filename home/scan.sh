#!/bin/bash

OUT=/var/run/v4l-utils

export GCONV_PATH=/usr/local/lib/gconv

echo ISDBT Scan
dvbv5-scan -C JP -a 1 -o $OUT/isdbt.conf $HOME_DIR/initials/gr.ch

echo ISDBS-BS Scan
dvbv5-scan -C JP -a 0 -N -T 5 -o $OUT/isdbs-bs.conf $HOME_DIR/initials/bs.ch

#echo ISDBS-CS Scan
#dvbv5-scan -C JP -a 0 -N -T 5 -o $OUT/isdbs-cs.conf $HOME_DIR/initials/cs.ch
