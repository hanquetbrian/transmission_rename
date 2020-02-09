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
    # print(path)

    # c = core.Core(rpc, mediaInfo.MediaInfo())
    # c.move_media(1)

    media = mediaInfo
    # m = media.getinfo('Mr.Robot.S04E11.eXit.1080p.10bit.AMZN.WEB-DL.AAC5.1.HEVC-Vyndros.avi')
    m = media.getinfo('Thor.Ragnarok.2017.4K.HDR.2160p.Engx265.mkv')
    # m = media.getinfo('www.movcr.tv.-The.flash.2014.S05E22.720p.HDTV.x264AAC-GUN.mkv')
    # m = media.getinfo('Guardians.of the Galaxy Vol 2.2017.1080p.BluRay.x264-SPARKS[EtHD].mkv')
    if m:
        print(m)

        print(m.get_file_name())
    else:
        print('please enter a correct file')


    #print(data.json()['arguments']['torrents'][1]['files'][1]['name'])
