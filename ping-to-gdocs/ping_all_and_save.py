from datetime import datetime
import ping
import json


def run():
    hostnames = [
        '8.8.8.8',  # google dns 1
        'cn.pool.ntp.org',  # china ntp server
    ]
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    results = ping.ping_servers(hostnames)
    with open('data/{}.json'.format(timestamp), 'w') as fd:
        json.dump({
            'timestamp': timestamp,
            'results': results,
        }, fd)


if __name__ == '__main__':
    run()
