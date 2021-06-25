# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 08:35:51 2021

@author: nathan.m
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """

    playlist = []
    size_remain = max_size
    if songs[0][2] > max_size:  # first songdoesn't fit
        return playlist
    playlist.append(songs[0][0])  # add the first song to the playlist
    size_remain -= songs[0][2]  # cut from remaining size
    found = True  # stop flag for the while loop
    while found is True:  # keep searching the whole list till failure
        found = False
        smallsong = (None, size_remain)  # current smallest song that fits
        for e in songs:  # iterate over the songs
            # variables for code readability
            song_name = e[0]
            song_len = e[1]
            song_size = e[2]
            if song_name not in playlist:  # don't add a song twice
                if song_size <= size_remain:  # the song must fit
                    found = True  # a small enough song was found
                    if song_size < smallsong[1]:  # seek a smaller song
                        smallsong = (song_name, song_size)  # smallest and fits
        if found is True:  # a small enough song was found
            playlist.append(smallsong[0])  # add the song to the playlist
            size_remain -= smallsong[1]  # cut from remaining size
    return playlist
    #  check if the first song fits
    #  it fits
    #  add it to the playlist
    #  find the smallest song remaining
    #  check if it fits
    #  add it
    #  it doesn't fit, return an empty list
    


# =============================================================================
# = test cases
max_size = 12.2
songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
print(song_playlist(songs, max_size))
#max_size = 11
#songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
#print(song_playlist(songs, max_size))
# =============================================================================