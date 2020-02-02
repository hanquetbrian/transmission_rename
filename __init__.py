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

    path = data[0]['downloadDir'] + '/' + data[0]['files'][0]['name']
    print(path)

    # c = core.Core(rpc, mediaInfo.MediaInfo())
    # c.move_media(1)

    media = mediaInfo.MediaInfo()
    # media.getinfo('Mr.Robot.S04E11.eXit.1080p.10bit.AMZN.WEB-DL.AAC5.1.HEVC-Vyndros')
    media.getinfo('Guardians.of the Galaxy Vol 2.2017.1080p.BluRay.x264-SPARKS[EtHD].mkv')


    #print(data.json()['arguments']['torrents'][1]['files'][1]['name'])
