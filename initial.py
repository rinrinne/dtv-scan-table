#!/usr/bin/python

import os
import os.path

def entry(ds, ch):
    entry = None
    if ds == 'gr':
        entry_base = '''
[CHANNEL]
    DELIVERY_SYSTEM = ISDBT
    FREQUENCY = {}
    BANDWIDTH_HZ = 6000000

'''[1:]

        entry = entry_base.format(ch['freq'])
    elif t == 'bs':
        entry_base = '''
[CHANNEL]
    DELIVERY_SYSTEM = ISDBS
    FREQUENCY = {}
    STREAM_ID = {}

'''[1:]

        entry = entry_base.format(ch['freq'], ch['tsid'])

    return entry

if __name__ == '__main__':
    types = list()
    for f in os.listdir('lch/'):
        types.append(os.path.splitext(f)[0])

    channels = dict()
    for t in types:
        pchs = dict()
        with open(os.path.join('pch', '{}.ch'.format(t)), 'r') as f:
            for line in f:
                item = line.strip().split(',')
                pchs[item[0]] = item[1]

        channels[t] = list()
        with open(os.path.join('lch', '{}.ch'.format(t)), 'r') as f:
            for line in f:
                item = line.strip().split(',')
                channel = dict()
                channel['freq'] = pchs[item[0]]
                channel['tsid'] = item[1]
                channels[t].append(channel)


    os.mkdir('initials')

    for t in channels:
        with open(os.path.join('initials', '{}.ch'.format(t)), 'w') as f:
            for ch in channels[t]:
                f.write(entry(t, ch))

