import transmissionRPC
import configparser

__author__ = 'Brian Hanquet'
__version__ = '1.0.0'

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    rpc = transmissionRPC.TransmissionRPC(config['global']['transmission_url'])

    data = rpc.send_request('torrent-get', {'fields': ['name', 'files', 'downloadDir']})
    print(data.json()['arguments']['torrents'][1]['files'][1]['name'])
