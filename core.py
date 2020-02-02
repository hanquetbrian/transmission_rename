import transmissionRPC
import mediaInfo


class Core:
    def __init__(self, transmissionrpc, mediainfo):
        if not isinstance(transmissionrpc, transmissionRPC.TransmissionRPC):
            raise NotImplementedError('transmissionRPC should be a TransmissionRPC object')
        if not isinstance(mediainfo, mediaInfo.MediaInfo):
            raise NotImplementedError('mediaInfo should be a MediaInfo object')
        self._rpc = transmissionrpc
        self._info = mediainfo

    def move_media(self, torrent_ids):
        """
        Move and rename all the media from a torrent
        """
        list_of_files = self._rpc.get_torrent(ids=torrent_ids)
        for name in list_of_files:
            print(name['files'])


