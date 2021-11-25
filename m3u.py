import os
from pathlib import Path
import pathlib

# current working directory
directory = pathlib.Path().absolute()  # An absolute path
paths = []


def listFiles(folder_name):
    file_list = os.listdir(folder_name)
    for file in file_list:
        formed_path = os.path.join(directory, file)
        paths.append(formed_path)
    return paths


# some_path = Path("mine/stuff/somedir/file.txt")
# print(some_path.suffix)


# print(os.path.dirname(os.path.abspath(__file__))) # directory for the running script

list_of_subfolders = [f.name for f in os.scandir(directory) if f.is_dir()]
print('Folders in this directory: ', list_of_subfolders)

files = []
audio_file_type = ['.m4a', '.m4b', '.flac',
                   '.mp3', '.mp4', '.wav', '.wma', '.aac']
list_of_songs = []


def my_play_list():
    for i in list_of_subfolders:
        get_ext_from_path = listFiles(i)

        for f in get_ext_from_path:
            for ext in audio_file_type:
                if (f.endswith(ext)):
                    # Create an .m3u file here
                    playlist = open(os.path.join(
                        directory, i, '00-playlist.m3u'), 'w')
                    head, tail = os.path.split(f)
                    list_of_songs.append(tail)
    for i in list_of_songs:
        playlist.write(i + '\n')
    return list_of_songs


songs = my_play_list()
print('Making a playlist went smooth. Cheers!')
print('*** Songs added to the playlist ***')
for song in songs:
    print(song)

# for entry in os.scandir(directory):
#     for i in audio_file_type:
#         if (entry.path.endswith(i)) and entry.is_file():
#             files.append(entry.path)

# File Handling
# file = open('001-playlist.m3u', 'w')
# list_of_songs = []
# for i in files:
#     head, tail = os.path.split(i)
#     list_of_songs.append(tail)

# for song in list_of_songs:
#     file.write(song + '\n')

# file.write('*** Death to All But Metal ***' + '\n')

# file.close()

# f = open('001-playlist.m3u', 'r')
# print(f.read())

