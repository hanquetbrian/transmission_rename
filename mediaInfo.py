import re
import os

class MediaInfo:
    def __init__(self):
        pass

    def getinfo(self, file_name):
        media = MediaRespond()

        if re.search(r'[.\s]s[0-9]{1,2}E[0-9]{1,2}', file_name, re.IGNORECASE):
            media.isTvShow = True
        elif os.path.splitext(file_name)[1] in ['.mkv', '.avi', '.mov', '.mpg', '.mp4']:
            media.isMovie = True


        part = re.split("\s|\.", file_name)
        # print(part)
        return media


class MediaRespond:
    def __init__(self):
        self.title = ''
        self.year = ''
        self.isMovie = False
        self.isTvShow = False
        self.season = 0
        self.episode = 0
        self.resolution = 0
        self.codec = []
        self.language = ''
        self.extra = ''
