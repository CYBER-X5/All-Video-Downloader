#!/bin/python



import requests
import time
import os
import sys
import shutil
import re
from datetime import datetime

columns = shutil.get_terminal_size().columns

def psb(z, end = "\n"):
    z = printAZ(z, True)
    for p in z + end:
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.01)


# Logo
def logo():
    os.system("clear")
    print("\033[94mâ”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”".center(columns+5))
    print("\033[94mâ”‚    \033[92mâ–›â–€â––          â–œ         â–Œâ–›â–€â––      \033[94m   â”‚".center(columns+15))
    print("\033[94mâ”‚    \033[92mâ–Œ â–Œâ–žâ–€â––â–Œ  â–Œâ–›â–€â––â– â–žâ–€â––â–â–€â––â–žâ–€â–Œâ–™â–„â–˜â–™â–€â––â–žâ–€â––\033[94m   â”‚".center(columns+15))
    print("\033[94mâ”‚    \033[92mâ–Œ â–Œâ–Œ â–Œâ–â–â– â–Œ â–Œâ– â–Œ â–Œâ–žâ–€â–Œâ–Œ â–Œâ–Œ  â–Œ  â–Œ â–Œ\033[94m   â”‚".center(columns+15))
    print("\033[94mâ”‚    \033[92mâ–€â–€ â–â–€  â–˜â–˜ â–˜ â–˜ â–˜â–â–€ â–â–€â–˜â–â–€â–˜â–˜  â–˜  â–â–€ \033[94m   â”‚".center(columns+15))
    print("\033[94mâ”‚                              \033[94m          â”‚".center(columns+9))
    print("\033[94mâ”‚ \033[95mAuthor : Emon Mahmud                     \033[94mâ”‚".center(columns+15))
    print("â”‚ \033[95mTool   : All Video Downloader          \033[94mâ”‚".center(columns+9))
    print("â”‚ \033[95mGitHub : https://github.com/CYBER-X5 \033[94mâ”‚".center(columns+9))
    print("â”‚ \033[95mCoder  :  HunterSl4d3              \033[37mV1.0\033[94mâ”‚".center(columns+15))
    print("\033[94mâ””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜".center(columns+5))

# Print with Color (Using this to avoid color code confusion and external lirary)
def printAZ(text, returnT=False):
    printText = text.replace("cWhite", "\033[37m").replace("cGreen", "\033[92m").replace("cRed", "\033[91m").replace("cBlue", "\033[94m")
    if (returnT):
        return printText
    
    print(printText)


# Show Error Message
def errorMsg(errorCode = 0):
    if (errorCode == 2):
        psb("\ncGreen    [cRed!cGreen] cWhiteInvalid Video URL!")
    else:
        print("error")
        psb("\ncGreen    [cRed!cGreen] cWhiteAn Error Occured!")
        psb("cGreen    [cRed!cGreen] cWhiteTry Checking Your Internet Connection or Video URL")
    
    sys.exit("\033[37m")
    exit()

# Get User Option Input
def getOptionNumber(o):
    opList = [str(x) for x in range(1, int(o)+1)]
    op = input(printAZ("\ncGreen    [cWhite*cGreen] cWhiteEnter Your Choice:> cGreen", True))
    if (op[0] == "0"): op = op[1:]
    if not (op in opList):
        psb("\ncGreen    [cRed!cGreen] cWhitePlease Enter a Correct Option!")
        op = getOptionNumber(o)
    
    return op

#Print Video Details
def printDetails(videoTitle, videoSource, videoDuration, videoExt):
    logo()
    psb("\ncGreen    [cWhite*cGreen] Video Title: cWhite" + (videoTitle if videoTitle == "YouTube" else videoTitle.title()))
    psb("cGreen    [cWhite*cGreen] Video Duration: cWhite" + videoDuration)
    psb("cGreen    [cWhite*cGreen] Video Source: cWhite" + videoSource)
    psb("\ncGreen    [cWhite#cGreen] cWhiteChoose Your File Format:\n")
    
    sl = 1
    for qual in videoExt:
        if (len(str(sl)) == 1):
            serial = "0" + str(sl)
        else:
            serial = str(sl)
        
        formate = qual["formate"].upper()
        quality = qual["quality"]
        size = qual["size"]
        if (size == ""):
            size = "UNKNOWN"
        
        printAZ("cGreen    [cWhite" + serial + "cGreen] cWhite" + formate + " cWhite(cGreen" + quality + "cWhite) cBlue[cWhite Size: cGreen" + size + "cBlue]")
        
        sl += 1


#####################################
# Video Dowenload Processes Starting Here
#
# 01. Process FaceBook Video Download
# 02. Process Random Website Video Download
# 03. Process YouTube Video/Playlist Download
#### 01. Single Video
#### 02. Video Playlist
#
#####################################

# 01, Process FaceBook Video Download
vidExt = []
def downloadFacebook(videoUrl):
    from bs4 import BeautifulSoup
    
    psb("\ncGreen    [cWhite#cGreen] cWhiteFetching Video DatacGreen: cWhite", end="")
    
    url = "https://www.getfvid.com/downloader"

    headers = {
        "Host": "www.getfvid.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "origin": "https://www.getfvid.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "referer": "https://www.getfvid.com/",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "cookieconsent_status=dismiss",
    }
    
    data = {"url" : videoUrl}
    
    response = requests.post(url, headers=headers, data=data)
    
    if not (response.status_code == 200):
        errorMsg()
    
    responseData = response.text
    
    htmlData = BeautifulSoup(responseData, "html.parser")
    
    try:
        videoLinks = [item['href'] for item in htmlData.find_all('a', attrs={'href' : True, 'download' : True})]
        videoTitle = htmlData.find('input', {'id' : 'title_video'})['value'].replace("-facebookFacebook WatchVideo UnavailableSorry, this video could not be played.Learn more", "").replace("\n", " ")
    except:
        errorMsg()
    
    print("Done")
    
    time.sleep(0.5)
    
    logo()
    psb("\ncGreen    [cWhite#cGreen] cWhiteVideo Title: cGreen" + videoTitle)
    psb("cGreen    [cWhite#cGreen] cWhiteVideo Source: cGreenFaceBook")
    psb("\ncGreen    [cWhite*cGreen] cWhiteChoose Your File Format:\n")
    
    o = 1
    for link in videoLinks:
        qText = htmlData.find('a', {'href' : link}).text
        if ("Audio" in qText):
            vidExt.append("mp3")
        else:
            vidExt.append("mp4")
        
        printAZ("cGreen    [cWhite" + ("0" + str(o) if (len(str(o))) == 1 else str(o)) + "cGreen] cWhite" + qText)
        o += 1
    
    printAZ("cGreen    [cWhite" + ("0" + str(o) if (len(str(o))) == 1 else str(o)) + "cGreen] cWhiteExit")
    op = getOptionNumber(o)
    
    if (op == o):
        sys.exit("\033[37m")
    
    downloadUrl = videoLinks[int(op) - 1]
    downloadPath = "/sdcard/Download/" + videoTitle.replace("\"", "\\\"").replace("/", "\/")[:125] + "_D-Pro." + vidExt[int(op) - 1]
    
    psb("\ncGreen    [cWhite#cGreen] cWhiteStarting Download Process: \ncGreen")
    
    os.system("wget -O \"" + downloadPath + "\" \"" + downloadUrl + "\" -q --show-progress --no-check-certificate")
    os.system("touch -d \"" + str(datetime.now()) + "\" \"" + downloadPath + "\"")
    
    printAZ("\ncGreen    [cWhite#cGreen] cWhiteDownload Complete!")
    printAZ("cGreen    [cWhite#cGreen] cWhiteFile Saved In cGreenDownloads")
    sys.exit("\n\033[37m")


# 02. Process Random Website Video Download

def randomDownload(videoUrl):
    psb("\ncGreen    [cWhite#cGreen] cWhiteFetching Video DatacGreen: cWhite", end="")
    
    try:
        response = requests.post("https://api.videodownloaderpro.net/api/convert", json = {"url": videoUrl})
    except:
        errorMsg()
    
    if not (response.status_code == 200):
        errorMsg()
    
    videoData = response.json()
    if ("Convert failed" in videoData):
        errorMsg()
    
    print("Done")
    time.sleep(0.5)
    logo()
    
    videoTitle = videoData["meta"]["title"]
    try:
        videoDuration = videoData["meta"]["duration"]
    except KeyError:
        videoDuration = "UNKNOWN"
    videoSourceUrl = videoData["meta"]["source"]
    dots = [m.start() for m in re.finditer("\.", videoSourceUrl)]
    if (len(dots) == 1):
        videoSource = videoSourceUrl[:dots[0]]
    else:
        videoSource = videoSourceUrl[dots[0]+1:dots[-1]]
    tmpUrlData = videoData["url"]
    
    tmpVidData = []
    # Filtering Uncommon File Formates and Audioless Videos
    for v in tmpUrlData:
        support = ["mp4", "mp3", "m4a"]
        if (v["ext"] in support):
            if ("audio" in v.keys()):
                if not ((v["audio"] == False) and (v["no_audio"] == True)):
                    tmpVidData.append(v)
            else:
                tmpVidData.append(v)
    
    # Making a easy-to-understand Dictionary List
    videoExt = []
    for tmp in tmpVidData:
        try:
            size = tmp["contentLength"]
            size = size / (1024*1024)
            if (size < 1):
                size = str(size * 1024)[:4] + " KB"
            else:
                size = str(size) + " MB"
        except KeyError:
            size = "UNKNOWN"
        formate = tmp["ext"]
        try:
            quality = tmp["quality"]
            if  (formate == "mp4"):
                quality = quality + "p"
            else:
                quality = quality + "Kbps"
        except:
            quality = "UNKNOWN"
        
        data = {"size": size, "formate": formate, "quality": quality, "url": tmp["url"]}
        
        videoExt.append(data)    
    
    printDetails(videoTitle, videoSource, videoDuration, videoExt)
    
    sl = len(videoExt) + 1
    printAZ("cGreen    [cWhite" + ("0" + str(sl) if (len(str(sl))) == 1 else str(sl)) + "cGreen] cWhiteExit")
    
    op = getOptionNumber(sl)
    
    if (op == str(sl)):
        sys.exit("\033[37m")
    
    selected = videoExt[int(op) - 1]
    
    psb("\ncGreen    [cWhite#cGreen] cWhiteConverting VideocGreen: cWhite", end="")
    
    downloadUrl = selected["url"]
    
    time.sleep(1)
    print("Done")

    downloadPath = "/sdcard/Download/" + videoTitle.replace("\"", "\\\"").replace("/", "\/")[:125] + "_D-Pro." + selected["formate"]
    
    psb("\ncGreen    [cWhite#cGreen] cWhiteStarting Download Process: \ncGreen")
    
    os.system("wget -O \"" + downloadPath + "\" \"" + downloadUrl + "\" -q --show-progress --no-check-certificate")
    os.system("touch -d \"" + str(datetime.now()) + "\" \"" + downloadPath + "\"")
    
    printAZ("\ncGreen    [cWhite#cGreen] cWhiteDownload Complete!")
    printAZ("cGreen    [cWhite#cGreen] cWhiteFile Saved In cGreenDownloads")
    sys.exit("\n\033[37m")


# 03. Process YouTube Video/Playlist Download

#### 01. Single Video
# Fetching video Download Data
def fetchYTurl(videoUrl):
    url = "https://yt1s.com/api/ajaxSearch/index"
    data = {"q" : videoUrl,"vt" : "home"}
    
    responseData = requests.post(url, data = data).json()

    try:
        if not (responseData["p"] == "convert"):
            errorMsg()
    except:
        errorMsg()
    
    try:
        videoCode = responseData["vid"]
        videoTitle = responseData["title"]
        videoLinks = responseData["links"]
        tmpTime = responseData["t"]
    except:
        errorMsg()
    
    # Making an easy-to-understand Dictionary List
    videoData = []
    for type in videoLinks:
        for i in videoLinks[type]:
            tmp = videoLinks[type][i]
            data = {"size": tmp["size"], "formate": tmp["f"], "quality": tmp["q"], "code": tmp["k"]}
            
            videoData.append(data)
    
    videoDur = time.strftime("%H:%M:%S", time.gmtime(tmpTime))

    returnData = {"title": videoTitle, "code": videoCode, "source": "YouTube", "duration": videoDur, "extracters": videoData}
    
    return returnData

# Fetching Video Url
def downloadYouTube(videoUrl):
    psb("\ncGreen    [cWhite#cGreen] cWhiteFetching Video DatacGreen: cWhite", end="")
    videoData = fetchYTurl(videoUrl)
    
    videoTitle = videoData["title"]
    videoCode = videoData["code"]
    videoSource = videoData["source"]
    videoDuration = videoData["duration"]
    videoExt = videoData["extracters"]
    
    print("Done")
    
    time.sleep(0.5)
    printDetails(videoTitle, videoSource, videoDuration, videoExt)
    sl = len(videoExt) + 1
    printAZ("cGreen    [cWhite" + ("0" + str(sl) if (len(str(sl))) == 1 else str(sl)) + "cGreen] cWhiteExit")
    
    op = getOptionNumber(sl)
    if (op == str(sl)):
        sys.exit("\033[37m")
    
    selected = videoExt[int(op) - 1]
    psb("\ncGreen    [cWhite#cGreen] cWhiteConverting VideocGreen: cWhite", end="")
    
    url = "https://yt1s.com/api/ajaxConvert/convert"
    data = {"vid" : videoCode,"k" : selected["code"]}
    responseData = requests.post(url, data=data).json()
    
    if not (responseData["c_status"] == "CONVERTED"):
        errorMsg()
    
    downloadUrl = responseData["dlink"]
    print("Done")
    
    downloadPath = "/sdcard/Download/" + videoTitle.replace("\"", "\\\"").replace("/", "\/")[:125] + "_D-Pro." + selected["formate"]
    
    psb("\ncGreen    [cWhite#cGreen] cWhiteStarting Download Process: \ncGreen")
    
    os.system("wget -O \"" + downloadPath + "\" \"" + downloadUrl + "\" -q --show-progress --no-check-certificate")
    os.system("touch -d \"" + str(datetime.now()) + "\" \"" + downloadPath + "\"")
    
    printAZ("\ncGreen    [cWhite#cGreen] cWhiteDownload Complete!")
    printAZ("cGreen    [cWhite#cGreen] cWhiteFile Saved In cGreenDownloads")
    sys.exit("\033[37m")

#### 02. Video Playlist

# Downloader for Videos from Playlist
def downloadFromList(video, formate, retrying=False):
    videoUrl = video["url"]
    videoTitle = video["title"]
    ext = formate["formate"]
    ext2 = "none"
    if (ext == "mp3"):
        ext2 = "m4a"
    quality = formate["qualNo"]
    
    if not (retrying):
        psb("\ncGreen[cWhite Fetching cGreen] cWhite" + videoTitle + "cGreen: cWhite", end = "")
    
    try:
        response = requests.post("https://api.videodownloaderpro.net/api/convert", json = {"url": videoUrl})
    except:
        print("Error")
        psb("cGreen[cWhite*cGreen] cWhiteRetryingcGreen: cWhite", end = "")
        downVid(video, formate)
        return
    
    if not (response.status_code == 200):
        print("Error")
        psb("cGreen[cWhite*cGreen] cWhiteRetryingcGreen: cWhite", end = "")
        downVid(video, formate)
        return
    
    videoData = response.json()["url"]
    
    tmpVidData = []
    for v in videoData:
        support = ["mp4", "mp3", "m4a"]
        if (v["ext"] in support):
            if ("audio" in v.keys()):
                if not ((v["audio"] == False) and (v["no_audio"] == True)):
                    tmpVidData.append(v)
            else:
                tmpVidData.append(v)
    
    formfilt = []
    for v in tmpVidData:
        if (v["ext"] == ext) or (v["ext"] == ext2):
            formfilt.append(v)
    
    quallist = []
    for v in formfilt:
        quallist.append(v["quality"])
    
    quallist.sort()
    if not (quality in quallist):
        quality = quallist[-1]
    
    for v in formfilt:
        if (v["quality"] == quality):
            downloadUrl = v["url"]
            break
    
    printAZ("DonecGreen")
    
    downloadPath = "/sdcard/Download/" + videoTitle.replace("\"", "\\\"").replace("/", "\/")[:125] + "_D-Pro." + ext
    
    os.system("wget -O \"" + downloadPath + "\" \"" + downloadUrl + "\" -q --show-progress --no-check-certificate")
    os.system("touch -d \"" + str(datetime.now()) + "\" \"" + downloadPath + "\"")
    
    psb("cGreen[cWhite#cGreen] cWhiteSystem Sleeping:  cGreen", end="")
    for i in [5, 4, 3, 2, 1, 0]:
        sys.stdout.write("\b" + str(i))
        sys.stdout.flush()
        time.sleep(1)
    
    print("")

# Fetch Playlist Data
def downloadPlaylist(playlistUrl):
    psb("\ncGreen    [cWhite#cGreen] cWhiteFetching Playlist DatacGreen: cWhite", end="")
    
    try:
        playlistData = requests.get("https://youtubemultidownloader.org/scrapp/backend/yt-get.php?url=" + playlistUrl).json()
    except:
        errorMsg()
    
    if (playlistData["status"] == False):
        errorMsg()
    
    videoList = playlistData["items"]
    print("Done")
    
    time.sleep(0.5)
    logo()
    videoFormates = {"1": {"formate": "mp4", "quality": "240p", "qualNo": "240"}, "2": {"formate": "mp4", "quality": "360p", "qualNo": "360"}, "3": {"formate": "mp4", "quality": "720p", "qualNo": "720"}, "4": {"formate": "mp3", "quality": "128kbps", "qualNo": "128"}}
    
    psb("\ncGreen    [cWhite*cGreen] Video Source: cWhiteYouTube")
    psb("cGreen    [cWhite*cGreen] Note: cWhiteClosest Quality will be Downloaded If the Choosen Quality doesn't exist")
    psb("\ncGreen    [cWhite#cGreen] cWhiteChoose Your File Format: \n")
    
    for i in videoFormates:
        printAZ("cGreen    [cWhite0" + i + "cGreen] cWhite" + videoFormates[i]["formate"].upper() + " (cGreen" + videoFormates[i]["quality"] + "cWhite) cBlue[cWhite Size: cGreen Auto cBlue]")
    printAZ("cGreen    [cWhite05cGreen] cWhiteExit")
    
    op = str(getOptionNumber(5))
    if (op == "5"):
        sys.exit("\033[37m")
    
    for video in videoList:
        downloadFromList(video, videoFormates[op])
    
    printAZ("\ncGreen    [cWhite#cGreen] cWhitePlaylist Download Complete!")
    printAZ("cGreen    [cWhite#cGreen] cWhiteFiles Saved In cGreenDownloads")
    sys.exit("\n\033[37m")

# Process URL
def processUrl(videoUrl = None):
    if not (videoUrl):
        videoUrl = input(printAZ("\ncGreen    [cWhite*cGreen] cWhiteEnter Your Video/Playlist URL:> cGreen", True))
    
    if not (videoUrl.startswith("http://")) and not (videoUrl.startswith("https://")):
        errorMsg(2)
    
    if ("facebook.com" in videoUrl.lower()) or ("fb.watch" in videoUrl.lower()):
        downloadFacebook(videoUrl)
    elif ("youtube.com/playlist?list=" in videoUrl.lower()):
        downloadPlaylist(videoUrl)
    elif ("youtube.com" in videoUrl.lower()) or ("youtu.be" in videoUrl.lower()):
        downloadYouTube(videoUrl)
    else:
        randomDownload(videoUrl)

if (__name__ == "__main__"):
    try:
        videoUrl = sys.argv[1]
        processUrl(videoUrl)
    except IndexError:
        logo() # Removable
        processUrl()