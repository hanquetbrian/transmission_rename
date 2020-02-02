import requests
import json
import error


class TransmissionRPC:
    """
    TransmissionRPC is a class that handle the RPC connexion
    """
    def __init__(self, url):
        self._url = url

        self._sessionId = ''
        self._headers = {'X-Transmission-Session-Id': self._sessionId}
        self._sequence = 0

    def _update_session_id(self, request):
        """
        Update the session id from the request we received
        """
        if isinstance(request, requests.Response):
            self._sessionId = request.headers['X-Transmission-Session-Id']
            self._headers = {'X-Transmission-Session-Id': self._sessionId}
        else:
            raise error.TransmissionError('The request is not the expected object')

    def send_session_request(self):
        """
        Send a request to the server to get the session id
        """
        get_session_id = requests.get(url=self._url)
        if get_session_id.status_code != 409 and get_session_id.status_code != 200:
            raise error.HTTPError(get_session_id.url, get_session_id.status_code, get_session_id.content,
                                  get_session_id.headers)
        if not get_session_id.headers['X-Transmission-Session-Id']:
            raise error.TransmissionError('There is no session-id in the header')
        self._update_session_id(get_session_id)
        return get_session_id.status_code

    def _send_request(self, method, arguments=None):
        """
        Send a request to the server
        To see the request available go to https://github.com/transmission/transmission/blob/2.9x/extras/rpc-spec.txt
        """
        if arguments is None:
            arguments = {}
        query = json.dumps({'tag': self._sequence, 'method': method, 'arguments': arguments})
        self._sequence += 1

        result = requests.post(url=self._url, data=query, headers=self._headers)
        if result.status_code == 409:
            self._update_session_id(result)
            result = requests.post(url=self._url, data=query, headers=self._headers)
        if result.status_code != 200:
            raise error.HTTPError(result.url, result.status_code, str(result.content), result.headers)

        return result

    def get_torrent(self, ids=None, fields=None):
        """
        Get the list of the files which correspond to the given ids
        For more info go to https://github.com/transmission/transmission/blob/46b3e6c8dae02531b1eb8907b51611fb9229b54a/extras/rpc-spec.txt#L142
        """
        if fields is None:
            fields = ['id', 'name', 'downloadDir', 'files']
        elif not isinstance(fields, list):
            raise error.TransmissionError('Fields should be a list of objects, each of which'
                                          'contains the key/value pairs matching the request\'s "fields" argument')
        if ids is None:
            query = {'fields': fields}
        else:
            query = {'fields': fields, 'ids': ids}
        r = self._send_request('torrent-get', query)
        return r.json()['arguments']['torrents']
