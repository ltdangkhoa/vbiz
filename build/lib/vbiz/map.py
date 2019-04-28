import re
import json


def haha(vtext, cidtext):

    ciddict_file = 'ciddict.json'

    with open(ciddict_file) as json_file:
        ciddict = json.load(json_file)

    print(ciddict)

    print('-------')
    cidtext = cidtext.replace('(cid:', '')
    cids = cidtext.rsplit(')')[:-1]
    # ciddict = dict()
    for i, cid in enumerate(cids):
        ciddict['(cid:' + cid + ')'] = vtext[i]

    with open(ciddict_file, 'w') as outfile:
        json.dump(ciddict, outfile)

    print(ciddict)
    return 'haha'


if __name__ == '__main__':
    vtext = ('ỄẺỮỲWFÙẢÌ0123456789')
    cidtext = ('(cid:1224)(cid:1214)(cid:1266)(cid:483)(cid:58)(cid:41)'
               '(cid:212)(cid:1250)(cid:206)'
               '(cid:19)(cid:20)(cid:21)(cid:22)(cid:23)'
               '(cid:24)(cid:25)(cid:26)(cid:27)(cid:28)')
    haha(vtext, cidtext)
