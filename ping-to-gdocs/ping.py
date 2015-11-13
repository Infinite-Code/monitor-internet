import subprocess
import logging


def ping_servers(hostnames):
    return [ping_server(h) for h in hostnames]


def ping_server(hostname):
    try:
        print('ping {}'.format(hostname))
        result = subprocess.check_output(['ping', '-c10', hostname])
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
    else:
        print('ERROR: please enter an address to check')

    pprint.pprint(ping_servers(hostnames))
