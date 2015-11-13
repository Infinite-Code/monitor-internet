import datetime
import json
import ping
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('Netowkr-dd9ddf75f19e.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

wks = gc.open("Network Test").sheet1


def upload_data():
    data = get_data()
    start_col = 'B'
    start_row = 2

    st = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(st)

    hr , min = datetime.datetime.now().strftime('%H:%M').split(':')
    col_num = int(hr) * 60 + int(min) + 2
    cur = 0
    for idx, r in enumerate(data['result'], start_row):
        cell_pos = chr(ord(start_col) + cur) + str(idx)
        wks.update_acell(cell_pos, r['avg'])
        cur += 1


def get_data():
    hostnames = [
        '8.8.8.8',  # google dns 1
        'cn.pool.ntp.org',  # china ntp server
    ]
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    results = ping.ping_servers(hostnames)
    return json.dump({
            'timestamp': timestamp,
            'results': results})


if __name__ == '__main__':
    upload_data()
