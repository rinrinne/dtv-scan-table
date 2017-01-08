#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os

DELIVERY_SYSTEMS = [
    {
        'type':          'GR',
        'start':    401142857,
        'dulation':   6000000,
        'channel': {
            'start': 1,
            'end':  52,
            'step':  1
        }
    },
    {
        'type':          'BS',
        'start':     11727480,
        'dulation':     19180,
        'channel': {
            'start': 1,
            'end':  23,
            'step':  2
        }
    }
]

def freq(ds, ch):
    return ds['start'] + ds['dulation'] * (ch - 1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('deliverysystem')

    args = parser.parse_args()

    ds = None
    for item in DELIVERY_SYSTEMS:
        if item['type'] == args.deliverysystem:
            ds = item

    if ds is None:
        print 'Not found: {}'.format(args.deliverysystem)
        os.exit(1)

    channels = list()
    for ch in range(ds['channel']['start'], ds['channel']['end'] + 1, ds['channel']['step']):
        channels.append({'ch': ch, 'freq': freq(ds, ch)})

    for c in channels:
        print '{},{}'.format(c['ch'], c['freq'])
