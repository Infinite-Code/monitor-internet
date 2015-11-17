#!/usr/bin/env python

import subprocess
import logging


def ping_servers(hostnames, debug=False):
    return [ping_server(h, debug=debug) for h in hostnames]


def ping_server(hostname, debug=False):
    try:
        print('ping {}'.format(hostname))
        result = subprocess.check_output(['/usr/bin/env', 'ping', '-c10', hostname])
        if debug: print(result)
        lines = result.decode('utf8').split('\n')
        packet_loss = None
        avg = None
        for line in lines:
            if 'packet loss' in line:
                packet_loss = float(
                    line.split(',')[2].split()[0].replace('%', ''))
            if 'round-trip' in line:
                avg = float(line.split('=')[1].split('/')[1])
        return {
            'hostname': hostname,
            'packet_loss': packet_loss,
            'avg': avg,
        }
    except subprocess.CalledProcessError:
        logging.exception('FAILED TO PING: {}'.format(hostname))


if __name__ == '__main__':
    import sys
    import pprint

    if len(sys.argv) >= 2:
        hostnames = sys.argv[1:]
        pprint.pprint(ping_servers(hostnames, debug=True))
    else:
        print('ERROR: please enter an address to check')

