# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import datetime
import subprocess
from mhmovie.code import *
from moviepy.audio.io.AudioFileClip import AudioFileClip

from moviepy.video.io.VideoFileClip import VideoFileClip


def GetVideoTime():
    path = "./Video"
    time_list = []
    files = os.listdir(path)

    for f in files:
        is_found = True
        if f.__contains__(".xml") and (f.__contains__("camera") or f.__contains__("screenshare")):
            f = open(path + '/' + f, "r")

            lines = f.readlines()
            last_line = lines[-1]

            for line in lines:
                if line.__contains__(":"):
                    time = datetime.time(int(line[40:42]), int(line[43:45]), int(line[46:48]))
                    time_list.append((time, f.name[0:-4]))
                    break
                elif line is last_line:
                    break

    new_list = TimeSec(time_list)
    new_list.sort()

    min_time = new_list[0][0]

    for item in new_list:
        item[0] -= min_time

    return new_list


def TimeSec(time_list):
    newList = []
    for t in time_list:
        newList.append([(t[0].hour * 3600 + t[0].minute * 60 + t[0].second), (t[1])])
    return newList

def EditVideo():
    audio = (AudioFileClip("./Video/cameraVoip_1_3.avi"))
    clip = (VideoFileClip("./Video/screenshare_0_2.avi", audio=False).set_audio(audio))
    clip.write_videofile("bruh.mp4")


def ConvertVideo(time_list):
    for time in time_list:
        str = ("ffmpeg -i {0}.flv -ar 22050 -b 2048k {0}.avi").format(time[1])
        subprocess.run(str)

def main():
    t = GetVideoTime()
    for bruh in t:
        print(bruh)
    #ConvertVideo(t)
    EditVideo()

if __name__ == "__main__":
    main()