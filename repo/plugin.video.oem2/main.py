# Copyright (C) 2023, Roman V. M.   OMAR TEST
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
Example video plugin that is compatible with Kodi 20.x "Nexus" and above
"""
import os
import sys
from urllib.parse import urlencode, parse_qsl

import xbmcgui
import xbmcplugin
from xbmcaddon import Addon
from xbmcvfs import translatePath

# Get the plugin url in plugin:// notation.
URL = sys.argv[0]
# Get a plugin handle as an integer number.
HANDLE = int(sys.argv[1])
# Get addon base path
ADDON_PATH = translatePath(Addon().getAddonInfo('path'))
ICONS_DIR = os.path.join(ADDON_PATH, 'resources', 'images', 'icons')
FANART_DIR = os.path.join(ADDON_PATH, 'resources', 'images', 'fanart')

# Public domain movies are from https://publicdomainmovie.net
# Here we use a hardcoded list of movies simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some website or online service.
VIDEOS = [
    {
        'genre': 'LIVE TV',
        'icon': os.path.join(ICONS_DIR, 'livetv.png'),
        'fanart': os.path.join(FANART_DIR, 'livetv.jpg'),
        'movies': [
            {
                'title': 'WAPA TV PR',
                'url': 'https://live.field59.com/wapa/wapa1/playlist.m3u8',
                'poster': 'https://i.imgur.com/kqq7tD9.png',
                'plot': 'Live Stream WAPA 4 - PR. ',
                'year': 2024,
            },
            {
                'title': 'Telemundo PR',
                'url': 'https://nbculocallive.akamaized.net/hls/live/2037499/puertorico/stream1/master.m3u8',
                'poster': 'https://i.imgur.com/DVASpQj.png',
                'plot': 'Live Stream CANAL 2 - PR. ',
                'year': 2024,
            },
            {
                'title': 'Univision USA',
                'url': 'http://2hubs.ddns.net:25461/Faucon1tvMT/g8pHKUYxwDhx/58627',
                'poster': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Logo_Univision_2019.svg/512px-Logo_Univision_2019.svg.png',
                'plot': 'Live Stream  UNIVISION USA ',
                'year': 2024,
            },
            {
                'title': 'Discovery USA',
                'url': 'http://2hubs.ddns.net:25461/Faucon1tvMT/g8pHKUYxwDhx/57409',
                'poster': 'https://www.bing.com/images/search?view=detailV2&ccid=enCLBbtg&id=735B24E6FF0D8CE0D8F9B9F1DB2112F04B451B41&thid=OIP.enCLBbtgCny7ZHL_h7pcBAHaDc&mediaurl=https%3a%2f%2fbranditechture.agency%2fbrand-logos%2fwp-content%2fuploads%2f2023%2f01%2fDiscovery-Channel-DC.png',
                'plot': 'Live Stream  DISCOVERY USA ',
                'year': 2024,
            },
            {
                'title': 'Tele11 PR',
                'url': 'https://univision-live.cdn.vustreams.com/live/ce88b839-6376-4494-a2ee-83d66bc7cfc1/live.isml/ce88b839-6376-4494-a2ee-83d66bc7cfc1.m3u8',
                'poster': 'https://i.imgur.com/Crt3P4N.png',
                'plot': 'Live Stream CANAL 11 - UNIVISION PR ',
                'year': 2024,
            },
        ],
    },
    {
        'genre': 'Radio',
        'icon': os.path.join(ICONS_DIR, 'radio.png'),
        'fanart': os.path.join(FANART_DIR, 'radio.jpg'),
        'movies': [
            {
                'title': 'La X FM ',
                'url': 'https://stream.eleden.com/livelax/ngrp:livelax_all/playlist.m3u8',
                'poster': 'https://i.imgur.com/i2GnQTq.png',
                'plot': 'LA X FM radio Video Stream',
                'year': 1969,

            },
            {
                'title': 'Carnival of Souls',
                'url': 'https://ia600301.us.archive.org/8/items/CarnivalofSouls/CarnivalOfSouls_512kb.mp4',
                'poster': 'https://publicdomainmovie.net/wikimedia.php?id=Carnival_of_Souls_%25281962_pressbook_cover%2529.jpg',
                'plot': 'Carnival of Souls is a 1962 Independent film horror film starring Candace Hilligoss. Produced and directed by Herk Harvey '
                        'for an estimated $33,000, the film did not gain widespread attention when originally released, '
                        'as a B-movie; today, however, it is a cult classic.',
                'year': 1962,
            },
            {
                'title': 'The Screaming Skull',
                'url': 'https://ia801603.us.archive.org/10/items/TheScreamingSkull/TheScreamingSkull.mp4',
                'poster': 'https://publicdomainmovie.net/wikimedia.php?id=Poster_for_The_Screaming_Skull.jpg',
                'plot': 'A widower remarries and the couple move into the house he shared with his previous wife. '
                        'Only the ghost of the last wife might still be hanging around.',
                'year': 1958,
            },
        ],
    },
    {
        'genre': 'Locals',
        'icon': os.path.join(ICONS_DIR, 'local.png'),
        'fanart': os.path.join(FANART_DIR, 'local.jpg'),
        'movies': [
            {
                'title': 'FOX 35"',
                'url': 'https://lnc-wofl.tubi.video/index.m3u8',
                'poster': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Fox_Networks_Group_US_logo.svg/512px-Fox_Networks_Group_US_logo.svg.png',
                'plot': 'FOX 35 Orlando FL ',
                'year': 2024,
            },
            {
                'title': 'WESH 2 very local News',
                'url': 'https://lnc-wesh.tubi.video/playlist.m3u8',
                'poster': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/NBC_logo_2022_%28vertical%29.svg/512px-NBC_logo_2022_%28vertical%29.svg.png',
                'plot': 'NBC 2 Orlando (WESH)  720p ** only news updates very local**',
                'year': 2024,
            },
            {
                'title': 'WFTV 9  Very Local News Update',
                'url': 'https://amg00327-coxmediagroup-wftvbreaking-ono-hec7b.amagi.tv/playlist/amg00327-coxmediagroup-wftvbreaking-ono/playlist.m3u8',
                'poster': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ABC-2021-LOGO.svg/512px-ABC-2021-LOGO.svg.png',
                'plot': 'ABC 9 Orlando (WFTV)/  News Update',
                'year': 2024,
            },
        ],
    },
]


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :return: plugin call URL
    :rtype: str
    """
    return '{}?{}'.format(URL, urlencode(kwargs))


def get_genres():
    """
    Get the list of video genres

    Here you can insert some code that retrieves
    the list of video sections (in this case movie genres) from some site or API.

    :return: The list of video genres
    :rtype: list
    """
    return VIDEOS


def get_videos(genre_index):
    """
    Get the list of videofiles/streams.

    Here you can insert some code that retrieves
    the list of video streams in the given section from some site or API.

    :param genre_index: genre index
    :type genre_index: int
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[genre_index]


def list_genres():
    """
    Create the list of movie genres in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(HANDLE, 'Public Domain Movies')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(HANDLE, 'movies')
    # Get movie genres
    genres = get_genres()
    # Iterate through genres
    for index, genre_info in enumerate(genres):
        # Create a list item with a text label.
        list_item = xbmcgui.ListItem(label=genre_info['genre'])
        # Set images for the list item.
        list_item.setArt({'icon': genre_info['icon'], 'fanart': genre_info['fanart']})
        # Set additional info for the list item using its InfoTag.
        # InfoTag allows to set various information for an item.
        # For available properties and methods see the following link:
        # https://codedocs.xyz/xbmc/xbmc/classXBMCAddon_1_1xbmc_1_1InfoTagVideo.html
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        info_tag = list_item.getVideoInfoTag()
        info_tag.setMediaType('video')
        info_tag.setTitle(genre_info['genre'])
        info_tag.setGenres([genre_info['genre']])
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&genre_index=0
        url = get_url(action='listing', genre_index=index)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(HANDLE, url, list_item, is_folder)
    # Add sort methods for the virtual folder items
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(HANDLE)


def list_videos(genre_index):
    """
    Create the list of playable videos in the Kodi interface.

    :param genre_index: the index of genre in the list of movie genres
    :type genre_index: int
    """
    genre_info = get_videos(genre_index)
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(HANDLE, genre_info['genre'])
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(HANDLE, 'movies')
    # Get the list of videos in the category.
    videos = genre_info['movies']
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label
        list_item = xbmcgui.ListItem(label=video['title'])
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use only poster for simplicity's sake.
        # In a real-life plugin you may need to set multiple image types.
        list_item.setArt({'poster': video['poster']})
        # Set additional info for the list item via InfoTag.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        info_tag = list_item.getVideoInfoTag()
        info_tag.setMediaType('movie')
        info_tag.setTitle(video['title'])
        info_tag.setGenres([genre_info['genre']])
        info_tag.setPlot(video['plot'])
        info_tag.setYear(video['year'])
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=https%3A%2F%2Fia600702.us.archive.org%2F3%2Fitems%2Firon_mask%2Firon_mask_512kb.mp4
        url = get_url(action='play', video=video['url'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(HANDLE, url, list_item, is_folder)
    # Add sort methods for the virtual folder items
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_VIDEO_YEAR)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(HANDLE)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    # offscreen=True means that the list item is not meant for displaying,
    # only to pass info to the Kodi player
    play_item = xbmcgui.ListItem(offscreen=True)
    play_item.setPath(path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(HANDLE, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if not params:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_genres()
    elif params['action'] == 'listing':
        # Display the list of videos in a provided category.
        list_videos(int(params['genre_index']))
    elif params['action'] == 'play':
        # Play a video from a provided URL.
        play_video(params['video'])
    else:
        # If the provided paramstring does not contain a supported action
        # we raise an exception. This helps to catch coding errors,
        # e.g. typos in action names.
        raise ValueError(f'Invalid paramstring: {paramstring}!')


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
