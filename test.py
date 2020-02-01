from requests import get
from requests import HTTPError
from requests import exceptions
import error
import transmissionRPC

t = transmissionRPC.TransmissionRPC('http://localhost:9091/transmission/rpc')
t.send_session_request()
