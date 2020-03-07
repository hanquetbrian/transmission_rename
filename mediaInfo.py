import re
import datetime

__AVAILABLE_RES = ['2160p', '4k', '1080p', '1080i', '720p', '576p', '576i', '480p', '480i']
__AVAILABLE_CODEC = ['264', '265', 'HEVC', 'AAC', 'mp3', 'ac-3', 'DTS', 'TrueHD', 'FLAC']
__AVAILABLE_EXTENSION = ['mkv', 'avi', 'mov', 'mpg', 'mp4']
__AVAILABLE_LANGUAGE = ['VOSTFR', 'French', 'English', 'Spanish', 'Hindi']
__INFO_TO_KEEP = ['BluRay', 'UHD', 'HDTV', 'HDR', 'bit']


def getinfo(file_name):
    """
    Get the info of a media from a file name
    """
    print(file_name)
    extension = file_name.split('.')[-1]
    if extension not in __AVAILABLE_EXTENSION:
        return False

    # Separate the filename in parts
    file_name_parts = _get_filename_parts(file_name)
    print(file_name_parts)
    media = MediaRespond()
    media.extension = extension
    file_name_parts.remove(extension)

    # get the year of the media
    year_info = re.findall(r'(.*?)\|?(2[0-9]{3})', '|'.join(file_name_parts), re.IGNORECASE)
    if year_info:
        for year in year_info:
            if int(year[1]) <= datetime.datetime.now().year:
                file_name_parts.remove(year[1])
                media.year = int(year[1])
                media.title = _format_title(year[0])
                for title_part in year[0].split('|'):
                    file_name_parts.remove(title_part)

    # get the season and episode of the tv show
    episode = re.search(r'(.*?)\|?s([0-9]{1,2})E([0-9]{1,2})', '|'.join(file_name_parts), re.IGNORECASE)

    if episode:
        media.isTvShow = True
        if not media.title:
            media.title = _format_title(episode.group(1))
        media.season = int(episode.group(2))
        media.episode = int(episode.group(3))
        for part in episode.group(0).split('|'):
            file_name_parts.remove(part)
    else:
        media.isMovie = True

    # Get resolution, codec and extra tag
    for part in list(file_name_parts):
        res = [res for res in __AVAILABLE_RES if res.lower() in part.lower()]
        codec = [ele for ele in __AVAILABLE_CODEC if ele.lower() in part.lower()]
        extra = [t for t in __INFO_TO_KEEP if t.lower() in part.lower()]

        if res:
            media.resolution.append(res[0])
            file_name_parts.remove(part)
        if codec:
            media.codec.append(part)
            file_name_parts.remove(part)
        if extra:
            media.extra.append(part)
            file_name_parts.remove(part)

    media.language = _get_language(file_name_parts)

    return media


def _format_title(name):
    """
    return a title in the correct format
    """
    new_name = name.lower().split('|')
    new_name = [s.capitalize() for s in new_name]
    new_name = ' '.join(new_name)

    return new_name


def _get_filename_parts(name):
    """
    Filter what we don't want in the filename and return the filename in array
    """
    new_name = re.sub(r'www\.\w+\.\w{2,4}', '', name, flags=re.IGNORECASE)
    new_name = re.sub(r'\[.*\]', '', new_name, flags=re.IGNORECASE)
    new_name = re.sub(r'^[.\-_*$]+', '', new_name, flags=re.IGNORECASE)
    new_name = re.sub(r'[)(]', '', new_name, flags=re.IGNORECASE)
    new_name = re.sub(r'[.\-_\s]+', '|', new_name, flags=re.IGNORECASE)

    return new_name.split('|')


def _get_language(parts_filename):
    """
    Get the language of the filename
    """
    language = []
    for part in parts_filename:
        lang = [lang for lang in __AVAILABLE_LANGUAGE if part.lower().startswith(lang[0:2].lower())]
        if lang:
            language.append(lang[0])
    return language


class MediaRespond:
    def __init__(self):
        self.title = ''
        self.year = ''
        self.isMovie = False
        self.isTvShow = False
        self.season = 0
        self.episode = 0
        self.resolution = []
        self.codec = []
        self.language = []
        self.extra = []
        self.extension = ''

    def get_file_name(self):
        new_file_name = [self.title, str(self.year)]
        if self.isTvShow:
            new_file_name.append('S{:02d}E{:02d}'.format(self.season, self.episode))
        new_file_name.append('.'.join(self.language))
        new_file_name.append('.'.join(self.resolution))
        new_file_name.append('.'.join(self.codec))
        new_file_name.append('.'.join(self.extra))
        new_file_name.append(self.extension)
        return '.'.join([name.replace(' ', '.') for name in new_file_name if name])

    def __str__(self):
        s = 'Title: ' + self.title
        s += '\nYear: ' + str(self.year)
        s += '\nSeason: ' + str(self.season)
        s += '\nEpisode: ' + str(self.episode)
        s += '\nResolution: ' + str(self.resolution)
        s += '\nCodec: ' + str(self.codec)
        s += '\nLanguage: ' + str(self.language)
        s += '\nExtra: ' + str(self.extra)
        s += '\nIs movie: ' + str(self.isMovie)
        s += '\nIs tv show: ' + str(self.isTvShow)
        return s
