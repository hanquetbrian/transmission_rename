import transmissionRPC
import configparser
import core
import mediaInfo

__author__ = 'Brian Hanquet'
__version__ = '1.0.0'

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    rpc = transmissionRPC.TransmissionRPC(config['global']['transmission_url'])

    data = rpc.get_torrent(1)
    # print(data)
    c = core.Core(rpc, mediaInfo.MediaInfo())
    c.move_media(1)

    #print(data.json()['arguments']['torrents'][1]['files'][1]['name'])
