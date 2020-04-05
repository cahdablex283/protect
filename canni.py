# -*- coding: utf-8 -*-
#CANNIBAL===Version SB
#============================================
import linepy
from linepy import *
from akad.ttypes import *
from datetime import datetime
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
#from gtts import gTTS
from googletrans import Translator
import youtube_dl
from time import sleep
#from zalgo_text import zalgo
from threading import Thread,Event
#import requests,uvloop
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
#loop = uvloop.new_event_loop()
#=====================================
# ᴘʀɪᴍᴇʀʏ ᴅᴀɴ ɢᴍᴀɪʟ
#=====================================
# ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ
cl = LINE("EP72ChTag70xrhsQlrX0.pk5PrpEGJWVMcGOSZIplCa.WTimRbPpo6XJ0R9IbNj4cQjneZY52iU0tJ7BNIAY2Xk=")
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))
print ("╔══════════════════\n╠ ʟᴏɢɪɴ sᴜᴄᴄᴇs\n╚══════════════════")
#======================================================
oepoll = OEPoll(cl)
call = cl
creator = ["u3cae6944f7a08f0be60a0a2cce23cb70"]
owner = ["u3cae6944f7a08f0be60a0a2cce23cb70"]
admin = ["u3cae6944f7a08f0be60a0a2cce23cb70"]
staff = ["u3cae6944f7a08f0be60a0a2cce23cb70"]
#==============================================================================
lineProfile = cl.getProfile()
mid = cl.getProfile().mid
KAC = [cl] #,kk,kc,kb,ke]
ABC = [cl] #,kk,kc,kb,ke]
Bots = [mid]
AbiOleng = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Bots = Team = AbiOleng
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)
#===============================================================================
protectcancel = []
welcome = []
targets = []
protectname = []
userTemp = {}
userKicked = []
dict = {}
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
warmode = []
ghost = []
offbot = []
msg_image={}
msg_video={}
msg_sticker={}
detectUnsend = []
simisimi = []
#===============================================================================
settings = {
    "autoBlock": False,
    "autoRead": False,
    "welcome": True,
    "leave": True,
    "mid": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": True,
    "checkPost": False,
    "setKey": "",
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy":False,
        "status":False,
        "target": {}
    }, 
    "unsendMessage":True,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":False,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 2,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "abi":{},
    "likeOn": True,
    "Timeline": True,
    "invite":False,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':False,
    'autoAdd':True,
    'autoCancel':{"on":True, "members":1},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "detectMention1":False,
    "autoResponPm":False,
    "MentionKick":False,
    "welcomeOn":False,
    "sticker":False,  
    "selfbot":True,
    "mention":"ɢᴀʙᴜɴɢ sɪɴɪ ᴋᴀᴋ",
    "Respontag":"ᴀᴅᴀ ᴀᴘᴀ ɴɢᴇᴛᴀɢ ᴛᴇʀᴜs, ᴋᴀʟᴏ ᴋᴀɴɢᴇɴ ᴘᴍ ᴀᴊᴀ, ʙɪᴀʀ ɢᴜᴀ ᴅᴇsᴀʜɪɴ 😂",
    "welcome":"sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴀᴡᴀɴ ᴅᴀʀɪ ᴀʟᴀᴍ ɢʜᴏɪʙ 😂",
    "leave":"ɢᴏᴏᴅ ʙʏᴇ \nsᴇᴇ ʏᴏᴜ ɴᴇxᴛ ᴛɪᴍᴇ",
    "comment":"ᴀᴜᴛᴏ ʟɪᴋᴇ ʙʏ:  Cannibal ",
    "comment1":"ᴀᴜᴛᴏ ʟɪᴋᴇ ʙʏ:  Cannibal ",
    "message":"ɴᴀʜ ᴋᴀɴ ᴀᴋʜɪʀ ɴʏᴀ ᴀᴅᴅ ᴊᴜɢᴀ",
}

protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "protect":[],
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
biProfile = cl.getProfile()
myProfile["displayName"] = biProfile.displayName
myProfile["statusMessage"] = biProfile.statusMessage
myProfile["pictureStatus"] = biProfile.pictureStatus

    
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
unsendOpen = codecs.open("unsend.json","r","utf-8")
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)
unsend = json.load(unsendOpen)
mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
        
def backupData():
	try:
		backup = read
		f = codecs.open('read.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		backup = tagme
		f = codecs.open('tag.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		backup = settings
		f = codecs.open('setting.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		backup = unsend
		f = codecs.open('unsend.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		return True
	except Exception as error:
		logError(error)
		return False      

        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendLineMusic(to):
    contentMetadata = {
        'countryCode': 'ID',
        'i-installUrl': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'a-packageName': 'com.spotify.music',
        'linkUri': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'type': 'mt',
        'previewUrl':"http://dl.profile.line-cdn.net/{}".format(client.profile.pictureStatus),
        'a-linkUri': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'text': cl.profile.displayName,
        'id': 'mt000000000a6b79f9',
        'subText': cl.profile.statusMessage
    }
    return cl.sendMessage(to, cl.profile.displayName, contentMetadata, 19)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        client.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = client.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            client.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
                        
def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        userid = "https://line.me/ti/p/~" + cl.profile.userid
                        cl.sendFooter(tmp, "Spam is over , Now Bots Actived !", str(userid), "http://dl.profile.line-cdn.net/"+cl.getContact(mid).pictureStatus, line.getContact(mid).displayName)
                    except Exception as error:
                        logError(error)
                        
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
                        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return cl.sendMessage(to, "ғᴏᴛᴏ ᴛɪᴅᴀᴋ ᴅɪ ᴋᴇᴛᴀʜᴜɪ")
    elif settings['changeProfileVideo']['video'] == None:
        return cl.sendMessage(to, "ᴠɪᴅɪᴏ ᴛɪᴅᴀᴋ ᴅɪ ᴋᴇᴛᴀʜᴜɪ")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "ғᴀɪʟɪᴇᴅ ᴜᴘᴅᴀᴛᴇ ᴘʀᴏғɪʟ")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
    
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def backupProfile():
    profile = cl.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = cl.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
    
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╭──────────────\n│ᴅᴀғᴛᴀʀ ᴊᴀɴᴅᴀ「{}」\n╰──────────────\n✍️1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                textx += "──────────────\n✍️%i.  " % (num)
                num=(num+1)
            else:
                try:
                    no = "╰───────────[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╰────────[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ ɪɴғᴏ ] ᴇʀᴏʀ :\n" + str(error))
        
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print(error)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n [ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n [ ᴅᴏɴᴇ ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ ɪɴғᴏ ] ᴇʀᴏʀ :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "ᴀɴɢɢᴏᴛᴀ ᴍᴀsᴜᴋ「{}」\nʜᴀʟʟᴏ  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nɴᴀᴍᴀ ɢʀᴏᴜᴘ : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "│%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╰──[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╰──[ ᴅᴏɴᴇ ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ ɪɴғᴏ ] ᴇʀᴏʀ :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\nᴊᴀᴍ : "+datetime.strftime(timeNow,'%H:%M:%S')+" ᴡɪʙ\nɢʀᴏᴜᴘ : "+str(len(gid))+"\nғʀɪᴇɴᴅ : "+str(len(teman))+"\nxᴘɪʀᴇᴅ : ɪɴ "+hari+"\nᴠᴇʀsɪ : ᴀʙɪ sᴏᴀᴋ ᴀɴᴅ ғᴛᴋ\nᴛᴀɴɢɢᴀʟ : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nʀᴜɴᴛɪᴍᴇ : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ ɪɴғᴏ ] ᴇʀᴏʀ :\n" + str(error))
        
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ ɪɴғᴏ ] ᴇʀᴏʀ :\n" + str(error))

        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")      

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e              
        
def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost
def sendTextTemplate(to, text):
    data = {
            "type": "flex",
            "altText": "Cannibal Killer",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#00008B"
    }
  },
  "type": "bubble",
  "size": "micro",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "xs",
                "margin": "none",
                "color": "#7CFC00",
                "wrap": True,
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
 
def sendTextTemplate8(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} Cannibal Killer".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "size": "micro",
  "hero": {
    "type": "image",
    "url": "https://i.top4top.io/p_1521lty361.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://line.me/ti/p/~aryopandelaki"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Cannibal Killer",
        "color": "#0000CD",
        "weight": "bold",
        "size": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": text,
                "wrap": True,
                "color": "#666666",
                "size": "xs",
                "flex": 5
              }
            ]
          }
        ]
      }
    ],
    "backgroundColor": "#40E0D0"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "secondary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "ᴄʀᴇᴀᴛᴏʀ",
          "uri": "http://line.me/ti/p/~aryopandelaki"
        }
      },
      {
        "type": "spacer",
        "size": "xs"
      }
    ],
    "flex": 0,
    "backgroundColor": "#00008B"
  },
  "styles": {
    "body": {
      "separator": True,
      "separatorColor": "#7CFC00"
    },
    "footer": {
      "separator": True,
      "separatorColor": "#7CFC00"
    }
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate7(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} Cannibal Killer".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xs",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#FFD700"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://h.top4top.io/p_1521lty361.png",
    "size": "full",
    "margin": "md"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴄʀᴇᴀᴛᴏʀ",
        "size": "sm",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "https://line.me/ti/p/~aryopandelaki"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴏʀᴅᴇʀ",
        "size": "sm",
        "wrap": True,
        "weight": "bold",
        "color": "#FF00FF",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "Cannibal Killer",
        "size": "sm",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate6(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} Cannibal Killer".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xs",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#FFD700"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://i.top4top.io/p_1521lty361.png",
    "size": "full",
    "margin": "md"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴄʀᴇᴀᴛᴏʀ",
        "size": "sm",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "https://line.me/ti/p/~aryopandelaki"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴏʀᴅᴇʀ",
        "size": "sm",
        "wrap": True,
        "weight": "bold",
        "color": "#FF00FF",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "Cannibal Killer",
        "size": "sm",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate4(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} Cannibal Killer".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xs",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#FFD700"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://h.top4top.io/p_1521hoe870.jpg",
    "size": "full",
    "margin": "md"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴄʀᴇᴀᴛᴏʀ",
        "size": "sm",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "https://line.me/ti/p/~aryopandelaki"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴏʀᴅᴇʀ",
        "size": "sm",
        "wrap": True,
        "weight": "bold",
        "color": "#FF00FF",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "Cannibal Killer",
        "size": "sm",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate5(to, text):
    data = {
            "type": "flex",
            "altText": "Canninal Killer",
            "contents": {
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#000000"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#00FFFF"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": " Cannibal Killer ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": " ᴍᴇɴᴜ ʙᴏᴛ ",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FF00FF",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate1(to, text):
    data = {
                "type": "template",
                "altText": "Cannibal Killer",
                "contents": {
                    "type": "bubble",
                    "size": "micro",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                               "text": text,
                               "size": "xs",
                               "margin": "none",
                               "color": "#8B008B",
                               "wrap": True,
                               "weight": "regular",
                               "type": "text"
                            }
                        ]
                    }
                }
            }
    cl.postTemplate(to, data)
    
def sendTextTemplate2(to, text):
    data = {
            "type": "flex",
            "altText": "Cannibal Killer",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000CD"
    }
  },
  "type": "bubble",
  "size": "micro",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate9(to, text):
    data = {
            "type": "flex",
            "altText": " ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴᴅᴀ ᴋᴇ ɢʀᴏᴜᴘ.",
            "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.top4top.io/p_1521lty361.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": text,
                    "size": "xxs",
                    "color": "#7CFC00",
                    "weight": "bold",
                    "flex": 1,
                    "align": "center",
                    "gravity": "top",
                    "wrap": True
                  }
                ],
                "spacing": "xs",
                "margin": "xs",
                "borderColor": "#000000"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler",
                    "flex": 1
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler",
                        "flex": 1
                      },
                      {
                        "type": "text",
                        "text": "Cannibal Killer",
                        "color": "#7CFC00",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "size": "sm",
                        "weight": "bold",
                        "align": "center",
                        "gravity": "top",
                        "wrap": True,
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "http://linecorp.com/"
                        }
                      },
                      {
                        "type": "filler",
                        "flex": 1
                      }
                    ],
                    "spacing": "xs",
                    "margin": "xs"
                  },
                  {
                    "type": "filler",
                    "flex": 1
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "xs",
                "borderColor": "#40E0D0",
                "margin": "md",
                "height": "40px",
                "flex": 2
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ʟɪᴋᴇ",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "align": "center",
                "gravity": "top",
                "wrap": True,
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
}
    cl.postTemplate(to, data)
    
def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "sm", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "https://line.me/ti/p/~aryopandelaki"
           }                                                
 }
]
                          }
                      }
    cl.postTemplate(to, data)

def musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+cl.getContact(mid).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': cl.getContact(mid).statusMessage if cl.getContact(mid).statusMessage != '' else 'http://line.me/ti/p/~dzul1991ji', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': cl.getContact(mid).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.cl.cl/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+mid,'MSG_SENDER_NAME':  cl.getContact(mid).displayName,}
    return cl.sendMessage(to, cl.getContact(mid).displayName, contentMetadata, 19)

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd

def help():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭─────────────\n"
    helpMessage += "│" + "「Menu Cannibal」\n"
    helpMessage += "├" + "─────────────\n"
    helpMessage += "│%i. " % num + key + "ᴍᴇ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴋᴇᴘᴏ @\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ANU\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "sᴘ\n"
    num = (num+1)   
    helpMessage += "│%i. " % num + key + "ᴘᴀsᴜᴋᴀɴ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ʀᴇsᴘᴏɴ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴄᴇᴋ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴛɪᴍᴇ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴀᴘᴀʟᴜ @\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ɢɪɴғᴏ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴏᴘᴇɴ\n"
    num = (num+1)    
    helpMessage += "│%i. " % num + key + "ᴄʟᴏsᴇ\n"
    num = (num+1)
    helpMessage += "│%i ." % num + key + "ᴄᴇᴋᴀᴅ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴘᴀʏᴍᴇɴᴛ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "sᴛᴀғғʟɪsᴛ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ʙᴏᴛʟɪsᴛ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ʜᴀᴘᴜsᴄʜᴀᴛ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "sɪᴅᴇʀ「on/oғғ」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴀʙɪᴍᴘ⁴\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "sᴛᴀʏ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ʙʀᴏᴀᴅᴄᴀsᴛ:「ᴘᴇsᴀɴ」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "sᴇᴛ sɴᴀᴍᴇ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴄɴ:「ᴄɴ」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ʀᴇsᴇᴛ sɴᴀᴍᴇ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ssɪᴅᴇʀ:「ᴘᴇsᴀɴ」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "sᴘᴇsᴀɴ:「ᴘᴇsᴀɴ」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "sᴡᴇʟᴄᴏᴍᴇ:「ᴘᴇsᴀɴ」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "sʀᴇsᴘᴏɴ:「ᴘᴇsᴀɴ」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ɢʀᴏᴜᴘʟɪsᴛ \n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴄᴇᴋᴘʀᴏ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴘɪɴᴀ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ʀᴇsᴘᴏɴ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ɢғ\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "sᴛɪᴄᴋᴇʀ「ᴘᴇsᴀɴ」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴜɴsᴇɴᴅ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴀᴜᴛᴏʙʟᴏᴄᴋ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│%i. " % num + key + "ᴡᴇʟᴄᴏᴍᴇ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "├────────────\n"
    helpMessage += "╰────────────\n"
    return helpMessage

def helpbot():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╭─────────────\n"
    helpMessage2 += "│" + "「Menu Cannibal」\n"
    helpMessage2 += "├" + "────────────\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴠᴄ @ \n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴍᴀɪɴᴋᴀɴ @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴄʙᴀɴ / ʙʟ @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ʙᴀɴ ᴀʟʟ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴜɴʙᴀɴ ᴀʟʟ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ʀᴇғʀᴇsʜ \n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴋɪʟʟʙᴀɴ \n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "sᴘᴀᴍɪɴᴠɪᴛᴇ ᴏɴ/ᴏғғ \n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ʙᴀɴʟɪsᴛ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ʙᴀɴ ᴀʟʟ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴄʙᴀɴ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴀᴅᴍɪɴᴇxᴘʟ:ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴀᴅᴍɪɴ:ᴏɴ @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴀᴅᴍɪɴ:ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴀᴅᴍɪɴᴇxᴘʟ:ᴏɴ @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴏᴡɴᴇʀ:ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "sᴛᴀғғ:ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "sᴛᴀғғ:ᴏɴ @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "sᴛᴀғғᴇxᴘʟ:ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "sᴛᴀғғᴇxᴘʟ:ᴏɴ @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ʙᴏᴛ:ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ʙᴏᴛ:ᴏɴ @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ʙᴏᴛᴇxᴘʟ:ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ʙᴏᴛᴇxᴘʟ:ᴏɴ @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ʙᴀɴ:ᴏɴ @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ʙᴀɴ:ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴜɴʙᴀɴ:ᴏɴ @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴜɴʙᴀɴ:ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│%i ." % num + key + "ᴛᴀʟᴋʙᴀɴ:on @\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴀʟʟᴘʀᴏ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴀᴜᴛᴏᴊᴏɪɴ oɴ/oғғ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ᴊs oɴ/oғғ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ɢs oɴ/oғғ\n"
    num = (num+1)
    helpMessage2 += "│%i. " % num + key + "ʟᴇᴀᴠᴇ oɴ/oғғ\n"
    num = (num+1)
    helpMessage2 += "├─────────────\n"
    helpMessage2 += "╰─────────────\n"
    return helpMessage2
    
def helpbot1():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "╭─────────────\n"
    helpMessage3 += "│" + "「Menu Cannibal」\n"
    helpMessage3 += "├" + "────────────\n"  
    helpMessage3 += "│%i. " % num + key + "sᴍᴜʟᴇ: ʟɪɴᴋ \n"
    num = (num+1)
    helpMessage3 += "│%i. " % num + key + "ᴘʀᴏғɪʟsᴍᴜʟᴇ: ɪᴅ \n"
    num = (num+1)
    helpMessage3 += "│%i. " % num + key + "ᴛᴀғsɪʀǫᴜʀᴀɴ ɴᴏ \n"
    num = (num+1)
    helpMessage3 += "│%i. " % num + key + "ʟɪʜᴀᴛ ɴᴏ\n"
    num = (num+1)
    helpMessage3 += "│%i. " % num + key + "ʟɪᴋᴇ @ \n"
    num = (num+1)
    helpMessage3 += "│%i. " % num + key + "ᴀᴅᴅɪᴍɢ ɴᴀᴍᴇ \n"
    num = (num+1)
    helpMessage3 += "│%i. " % num + key + "ᴅᴇʟʟɪᴍɢ ɴᴀᴍᴇ \n"
    num = (num+1)
    helpMessage3 += "│%i. " % num + key + "ʟɪsᴛɪᴍɢ ɴᴀᴍᴇ \n"
    num = (num+1)
    helpMessage3 += "├─────────────\n"
    helpMessage3 += "╰─────────────\n"
    return helpMessage3
    
def helpbot2():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = "╭─────────────\n"
    helpMessage4 += "│" + "「Menu Cannibal」\n"
    helpMessage4 += "├" + "─────────────\n"
    helpMessage4 += "│%i. " % num + key + "ʜᴇʟᴘ\n"
    num = (num+1)
    helpMessage4 += "│%i. " % num + key + "ʜᴇʟᴘ1\n"
    num = (num+1)
    helpMessage4 += "│%i. " % num + key + "ʜᴇʟᴘ2\n"
    num = (num+1)
    helpMessage4 += "│%i. " % num + key + "ʜᴇʟᴘ3\n"
    num = (num+1)
    helpMessage4 += "│%i. " % num + key + "sᴇᴛᴛɪɴɢs\n"
    helpMessage4 += "├─────────────\n"
    helpMessage4 += "╰─────────────\n"
    return helpMessage4


def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protect["pqr"]:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = cl.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)
                            cl.updateGroup(X)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ticket = ki.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                sw.leaveGroup(op.param1)
                                ki.updateGroup(X)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(X)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Ticket = kc.reissueGroupTicket(op.param1)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                        kc.updateGroup(X)
                            except:
                                try:
                                    if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            kb.reissueGroupTicket(op.param1)
                                            X = kb.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            kb.updateGroup(X)
                                except:
                                    try:
                                        if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                ke.reissueGroupTicket(op.param1)
                                                X = ke.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                Ticket = ke.reissueGroupTicket(op.param1)
                                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                ke.updateGroup(X)
                                    except:
                                        pass
#====================================================================                                                  
#====================================================================                            
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,"ᴍᴀᴀғ ᴀɴᴅᴀ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴛᴇᴀᴍ Cannibal\nsᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ᴋᴀᴡᴀɴ " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,"Im'coming " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,"🍁I'm coming " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,"🍁I'm coming " + str(ginfo.name))
#====================================================================                            
        if op.type == 13:
            if op.param1 in protect['pinv']:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        pass
  
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            cl.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            pass
                                                    
                return                                       
#====================================================================
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        ck.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                                                    
                return                                
#====================================================================                            
        if op.type == 19:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                                                    
                return                      
#======WELCOMEMEMBERS==============================================================                            
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                data = {
                        "type": "flex",
                        "altText": "{} Canibal Killer".format(cl.getProfile().displayName),
                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "xxl",
            "aspectRatio": "2:3",
            "gravity": "top",
            "backgroundColor": "#0000CD",
            "aspectMode": "fit"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": wait["welcome"],
                    "color": "#7CFC00",
                    "gravity": "top",
                    "flex": 0,
                    "size": "xs",
                    "weight": "bold",
                    "align": "center",
                    "wrap": True,
                    "margin": "xs"
                  }
                ],
                "spacing": "xs",
                "flex": 0,
                "margin": "xs"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "{}".format(cl.getContact(op.param2).displayName),
                        "color": "#7CFC00",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "http://linecorp.com/"
                        },
                        "size": "xs"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "xs",
                "borderColor": "#40E0D0",
                "margin": "sm",
                "height": "40px",
                "flex": 1
              }
            ],
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴡᴇʟᴄᴏᴍᴇ",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px",
                "gravity": "top"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px"
      },
      "styles": {
        "body": {
          "separatorColor": "#7CFC00",
          "separator": True,
          "backgroundColor": "#00008B"
        }
      }
    }
  ]
}
}
                cl.postTemplate(op.param1, data)
#=========LEAVEMEMBERS============================================
        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                data = {
                        "type": "flex",
                        "altText": "{} Cannibal Killer".format(cl.getProfile().displayName),
                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": wait["leave"],
                    "size": "sm",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center",
                    "gravity": "top",
                    "wrap": True
                  }
                ],
                "spacing": "xs"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "{}".format(cl.getContact(op.param2).displayName),
                        "color": "#7CFC00",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "http://linecorp.com/"
                        },
                        "size": "xs"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "xs",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ʟᴇᴀᴠᴇ",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px",
                "gravity": "top"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px"
      },
      "styles": {
        "body": {
          "separatorColor": "#7CFC00",
          "separator": True,
          "backgroundColor": "#00008B"
        }
      }
    }
  ]
}
}
                cl.postTemplate(op.param1, data)
#=======================================================             
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        sendTextTemplate8(op.param1, wait["message"])
                        
        if op.type == 5:
            if settings['autoBlock'] == True:
                try:
                    usr = cl.getContact(op.param2)
                    sendTextTemplate(op.param1, "ʜᴀʟʟᴏ {} ᴍᴀᴀғ ᴀᴜᴛᴏ ʙʟᴏᴄᴋ , ᴄᴏᴍᴍᴇɴ ᴅɪ ᴛʟ ᴅᴜʟᴜ ʏᴀ ᴋᴀᴋ, ɴᴛᴀʀ ʙᴀʀᴜ ʙᴜᴋᴀ ᴀᴜᴛᴏ ʙʟᴏᴄᴋ".format(usr.displayName))
                    cl.talk.blockContact(0, op.param1)
                    wait["Blacklist"][op.param2] = True
                except Exception as e:
                	print (e)
#=======================================================
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param3 in Bots:
                    if op.param2 not in Bots and op.param2 not in Team:
                        wait["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in wait["blacklist"]:
                                random.coice(ABC).findAndAddContactsByMid(op.param1,[op.param3])
                                random.coice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                random.coice(ABC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass

        if op.type == 32:
            if op.param3 in Bots:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  wait["blacklist"][op.param2] = True
                  try:
                      if op.param3 not in wait["blacklist"]:
                          cl.kickoutFromGroup(op.param1,[op.param2])
                          cl.inviteIntoGroup(op.param1,[op.param3])
             #             cl.sendMessage(op.param1, "ᴊᴀɴɢᴀɴ ᴅɪ ᴄᴀɴᴄᴇʟ ᴋɪᴋɪʟ sᴇᴛᴀɴ ")
                  except:
                      pass
              return
              
        if op.type == 32:
            if op.param3 in Bots:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  wait["blacklist"][op.param2] = True
                  try:
                      if op.param3 not in wait["blacklist"]:
                          cl.kickoutFromGroup(op.param1,[op.param2])
                          cl.inviteIntoGroup(op.param1,[op.param3])
               #           cl.sendMessage(op.param1, "ᴊᴀɴɢᴀɴ ᴅɪ ᴄᴀɴᴄᴇʟ sᴇᴛᴀɴ")
                  except:
                      pass
              return
#====================================================================                            
        if op.type == 19:
            if op.param1 in protect["proall"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                else:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param3 in wait["blacklist"]:
                        pass
                    else:
                        random.coice(ABC).findAndAddContactsByMid(op.param3)                       
                        wait["blacklist"][op.param2] = True

            if op.param1 in protect["protect"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                elif op.param2 in Bots:
                    pass
                else:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    
            if op.param1 in protect["antijs"]:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    elif op.param2 in Bots:
                        pass
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    else:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        bi.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid,Abi])
                        cl.inviteIntoGroup(op.param1,[admin])
            try:
                if op.param3 in owner:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in admin:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in staff:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in staff:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True              
            except:
                pass
  #===================================================================================================              
        if op.type == 25 or op.type == 26:
          if settings['SpamInvite'] == True:
            msg = op.message
            sender = msg._from
            receiver = msg.to
            if msg.contentType == 13:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            cl.sendMessage(msg.to, korban + " 🍁sᴜᴅᴀʜ ᴀᴅᴀ ᴅɪ ɢᴄ ɪɴɪ ʙᴏssᴋᴜ")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                        
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                    
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                        
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                    
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                        
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                    
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                        
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                    
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                        
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                    
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                        
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                    
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                        
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                    
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                        
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                    
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                        
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                    
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                        
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                    
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])
                                sendTextTemplate(msg.to, "🍁sᴘᴀᴍ ɪɴᴠɪᴛᴇ ᴋᴇ " + korban + "\n🍁sᴜᴄᴄᴇs..")
                                settings['SpamInvite'] = False
                            except:             
                                 sendTextTemplate(msg.to, '🍁Contact error')
                                 settings['SpamInvite'] = False
                                 break
#===================================================================================================        
        if op.type in [25, 26]:           
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != mid: to = sender
                else: to = receiver
                if receiver in temp_flood:
                    if temp_flood[receiver]["expire"] == True:
                        if cmd == "open" and sender == mid:
                            temp_flood[receiver]["expire"] = False
                            temp_flood[receiver]["time"] = time.time()
                            sendTextTemplate(to, "🍁ʙᴏᴛ ᴀᴋᴛɪғ")
                        return
                    elif time.time() - temp_flood[receiver]["time"] <= 1:
                        temp_flood[receiver]["flood"] += 1
                        if temp_flood[receiver]["flood"] >= 20:
                            temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["expire"] = True
                            ret_ = "sᴘᴀᴍ ᴛᴇʀᴅᴇᴛᴇᴋsɪ, ʙᴏᴛ ᴀᴋᴀɴ sɪʟᴇɴᴛ sᴇʟᴀᴍᴀ 30 ᴅᴇᴛɪᴋ ᴘᴀᴅᴀ ʀᴜᴀɴɢ ɪɴɪ ᴋᴇᴛɪᴋ {}ᴏᴘᴇɴ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴋᴇᴍʙᴀʟɪ.".format(setKey)
                            sendTextTemplate(to, str(ret_))
                    else:
                         temp_flood[receiver]["flood"] = 0
                         temp_flood[receiver]["time"] = time.time()
                else:
                    temp_flood[receiver] = {
    	                "time": time.time(),
    	                "flood": 0,
    	                "expire": False
                    }             
#===================================================================================================        
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        data = {
                                "type": "flex",
                                "altText": "Cannibal Killer",
                                "contents":{
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "  {}".format(cl.getContact(op.param2).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "ɴɢɪɴᴛɪᴘ² ɢᴀʙᴜɴɢ sɪɴɪ",
                    "color": "#ebebeb",
                    "size": "xxs",
                    "flex": 0
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "Cannibal Killer",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "0px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "filler"
                  }
                ],
               # "borderWidth": "1px",
                #"cornerRadius": "4px",
            #    "spacing": "xs",
             #   "borderColor": "#ffffff",
              #  "margin": "xs",
             #   "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "0px",
            "paddingTop": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "cctv",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "-3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "8px",
            "offsetTop": "3px",
            "backgroundColor": "#ff334b",
            "offsetStart": "5px",
            "height": "15px",
            "width": "38px"
          }
        ],
        "paddingAll": "0px"
    }
 }
}
                        cl.postTemplate(op.param1, data);
#===========================================================                                                                     
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == '🍁Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  " 🍁ғᴏᴛᴏ ᴅɪ ʜᴀᴘᴜs \n 🍁ᴘᴇɴɢɪʀɪᴍ : "
                                ret_ = " 🍁ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\n 🍁ᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  " 🍁ᴘᴇsᴀɴ ᴅɪ ʜᴀᴘᴜs \n"
                                ret_ += " 🍁ᴘᴇɴɢɪʀɪᴍ : {}".format(str(ryan.displayName))
                                ret_ += "\n 🍁ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\n 🍁ᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n 🍁ᴘᴇsᴀɴɴʏᴀ : {}".format(str(msg_dict[msg_id]["text"]))
                                sendTextTemplate(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  " 🍁sᴛɪᴄᴋᴇʀ ᴅɪ ʜᴀᴘᴜs \n"
                                ret_ += " 🍁ᴘᴇɴɢɪʀɪᴍ : {}".format(str(ryan.displayName))
                                ret_ += "\n 🍁ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\n 🍁ᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e) 
                    
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n🍁sᴛɪᴄᴋᴇʀ ɪɴғᴏ"
                   ret_ += "\n🍁sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(stk_id)
                   ret_ += "\n🍁sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(stk_ver)
                   ret_ += "\n🍁sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇ : {}".format(pkg_id)
                   ret_ += "\n🍁sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
#==================================================================================
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                   if msg._from in wait["blacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
#======Responpm==========================================                           
               if 'MENTION' in msg.contentMetadata.keys()!= None:
                   names = re.findall(r'@(\w+)', text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   lists = []
                   for mention in mentionees:
                       if mid in mention["M"]:
                           if wait["autoResponPm"] == True:
                            cl.sendChatChecked(msg._from,msg.id)
                            contact = cl.getContact(msg._from)
                            cl.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                            sendMention(sender, "ɪʏᴀ ʜᴀᴅɪʀ @!      ,\nᴀᴅᴀ ᴀᴘᴀ ᴋᴀɴɢᴇɴ ʏᴀ?", [sender])
                            ee = "" + random.choice(balas)
                           break                             
#=====AutoRespon1========================================================                                            
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   #contact = cl.getContact(msg._from)
                   #name = re.findall(r'@(\w+)', msg.text)
                   #image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sendTextTemplate4(msg.to, wait["Respontag"])
                           #cl.sendImageWithURL(msg.to,image)
                           break                              
#=====Autorespon2=========================================================      
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention1"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           saints = cl.getContact(msg._from)
                           cl.sendMessage(msg.to, wait["Respontag"])
                           rnd = ["🍁ɢᴀᴅɪs ᴅɪ ʟᴀʀᴀɴɢ ɴɢᴇᴛᴀɢ ʙᴀɪᴍ\n🍁ᴋᴀʟᴏ ᴊᴀɴᴅᴀ ʙᴜʀᴜᴀɴ ᴊᴀɴɢᴀɴ ʟᴀᴍᴀ-ʟᴀᴍᴀ 😂"]
                           p = random.choice(rnd)
                           lang = 'id'
                           image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                           cl.sendImageWithURL(op.param1, image)
                           tts = gTTS(text=p, lang=lang)
                           tts.save("hasil.mp3")
                           cl.sendAudio(msg.to,"hasil.mp3")
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                           break
#=====AutoResponKick=============================================                           
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["MentionKick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           cl.sendMessage(msg.to, "ᴅᴏɴᴇ ᴛᴀɢ ᴍᴇ !")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
#======================================================        
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"ᴄᴇᴋ ɪᴅ sᴛɪᴄᴋᴇʀ\nsᴛᴋɪᴅ : " + msg.contentMetadata["STKID"] + "\sᴛᴋᴘᴋɢɪᴅ : " + msg.contentMetadata["STKPKGID"] + "\nsᴛᴋᴠᴇʀ: " + msg.contentMetadata["STKVER"]+ "\n\nʟɪɴᴋ sᴛɪᴄᴋᴇʀ" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"🍁ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\n🍁ᴍɪᴅ : " + msg.contentMetadata["mid"] + "\n🍁sᴛᴀᴛᴜs ᴍsɢ : " + contact.statusMessage + "\n🍁ᴘɪᴄᴛᴜʀᴇ ᴜʀʟ : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#=======================================================================            
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 16:
                        url = msg.contentMetadata["postEndUrl"]
                        cl.likePost(url[25:58], url[66:], likeType=1004)
                        cl.createComment(url[25:58], url[66:], wait["comment"])
                        print ("Auto like done")
                        sendTextTemplate9(msg.to,"❂➤ʟɪᴋᴇ sᴜᴄᴄᴇss➤➤")
                        settings["likeOn"] = False  
#===========================================================       
        if op.type == 25 or op.type == 26:	     
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                if settings["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[class~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = " 🍁sᴛɪᴄᴋᴇʀ ɪɴғᴏ "
                            ret_ += "\n🍁sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(stk_id)
                            ret_ += "\n🍁sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇ ɪᴅ : {}".format(pkg_id)
                            ret_ += "\n🍁sᴛɪᴄᴋᴇғ ᴠᴇʀsɪᴏɴ : {}".format(stk_ver)
                            ret_ += "\n🍁sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
                        else:
                            ret_ = " 🍁sᴛɪᴄᴋᴇʀ ɪɴғᴏ"
                            ret_ += "\n🍁ᴘʀɪᴄᴇ: "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                            ret_ += "\n🍁ᴀᴜᴛʜᴏʀ : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\n🍁sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(str(stk_id))
                            ret_ += "\n🍁sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇ ɪᴅ : {}".format(str(pkg_id))
                            ret_ += "\n🍁sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(str(stk_ver))
                            ret_ += "\n🍁sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\n🍁ᴅᴇsᴄʀɪᴘᴛɪᴏɴ :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"  ᴄᴏɴᴛᴀᴄᴛ ɪɴғᴏ \n 🍁ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\n 🍁ᴍɪᴅ : " + msg.contentMetadata["mid"] + "\n 🍁sᴛᴀᴛᴜs ᴍsɢ : " + contact.statusMessage + "\n 🍁ᴘɪᴄᴛᴜʀᴇ ᴜʀʟ : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            cl.sendMessage(msg.to, "🍁sɪ sᴏᴍᴘʟᴀᴋ ᴋᴇ ʙʟ ʙᴏssᴋᴜ... ᴅᴇʟᴇᴛᴇ ʙᴀʀᴜ ᴊᴇᴘɪᴛ ʟᴀɢɪ ʙᴏssᴋᴜ")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  " 🍁sᴜᴋsᴇs ɪɴᴠɪᴛᴇ \n🍁ɴᴀᴍᴀ "
                                  ret_ = "🍁ᴋᴇᴛɪᴋ ɪɴᴠɪᴛᴇ ɪɴғᴏ ᴋᴀʟᴏ sᴜᴅᴀʜ ᴅᴏɴᴇ"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  sendTextTemplate(msg.to,"🍁ʟɪᴍɪᴛ ʙᴏssᴋᴜ...")
                                  wait["invite"] = False
                                  break
#ADD Bots&media
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["AddstickerTag"]["status"] == True:
                         settings["AddstickerTag"]["sid"] = msg.contentMetadata["STKID"]
                         settings["AddstickerTag"]["spkg"] = msg.contentMetadata["STKPKGID"]
                         sendTextTemplate(msg.to, "🍁sᴛɪᴄᴋᴇʀ ʀᴇsᴘᴏɴ ʜᴀsʙᴇᴇɴ ᴀᴋᴛɪғ")
                         settings["AddstickerTag"]["status"] = False
                         
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            sendTextTemplate(msg.to,"🍁sᴇɴᴅ ɢᴀᴍʙᴀʀɴʏᴀ...")
                            
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            sendTextTemplate(msg.to,"🍁ɢᴀɴᴛɪ ᴠɪᴅɪᴏ ᴘʀᴏғɪʟ ᴅᴏɴᴇ!!!")
                            
               if msg.contentType == 1:
                  if msg._from in mid:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate(msg.to, "🍁ᴅᴏɴᴇ ɴᴀᴍʙᴀʜ ғᴏᴛᴏ {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in mid:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate(msg.to, "🍁ᴅᴏɴᴇ ɴᴀᴍʙᴀʜ ᴠɪᴅɪᴏ {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate(msg.to, "🍁ᴅᴏɴᴇ ɴᴀᴍʙᴀʜ sᴛɪᴄᴋᴇʀ {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in mid:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate(msg.to, "🍁ᴅᴏɴᴇ ɴᴀᴍʙᴀʜ ᴍᴘ3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)                      
                      print ("Read")
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                          if msg._from in mid:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in mid:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in mid:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in mid:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sendTextTemplate(msg.to,"🍁sɪᴀᴘ ᴛᴇᴍᴘᴜʀ ʙᴏssᴋᴜ")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ᴀᴅᴅ ᴀʟʟ ʙᴏᴛ")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ᴅᴇʟᴇᴛᴇ ʙᴏᴛ")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate(msg.to,"🍁Nothing in bot")
#ADD STAFF
                 if msg._from in owner or msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ sᴛᴀғғʟɪsᴛ")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ᴀᴅᴅ sᴛᴀғғ")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ᴇxᴘᴇʟ sᴛᴀғғ")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        sendTextTemplate(msg.to,"🍁Nothing in staff")
#ADD ADMIN
                 if msg._from in owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ᴀᴅᴍɪɴ")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ᴀᴅᴅ ᴀᴅᴍɪɴ")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ᴇxᴘᴇʟ ᴀᴅᴍɪɴ")
                    else:
                        wait["delladmin"] = True
                        sendTextTemplate(msg.to,"🍁ᴄᴏɴᴛᴀᴄᴛ ɪᴛᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ")
#ADD BLACKLIST
                 if msg._from in owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ɪɴ ʙʟ")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ᴀᴅᴅ ʙʟ")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ᴅᴇʟᴇᴛᴇ ʙʟ")
                    else:
                        wait["dblacklist"] = True
                        sendTextTemplate(msg.to,"🍁ɴᴏᴛʜɪɴɢ ɪɴ ʙʟ")
#TALKBAN
                 if msg._from in owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ɪɴ ᴛʙ")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ᴀᴅᴅ ᴛʙ")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate(msg.to,"🍁ᴅᴏɴᴇ ᴅᴇʟᴇᴛᴇ ᴛʙ")
                    else:
                        wait["Talkdblacklist"] = True
                        sendTextTemplate(msg.to,"🍁ɴᴏᴛʜɪɴɢ ɪɴ ᴛʙ")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sendTextTemplate(msg.to, "🍁ᴅᴏɴᴇ ᴀᴅᴅ ᴘɪᴄᴛᴜʀᴇ")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     sendTextTemplate(msg.to, "🍁ᴅᴏɴᴇ ᴘɪᴄᴛᴜʀᴇ ᴘɪᴄᴋ ɢʀᴏᴜᴘ")
                     
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help1":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage = help()
                               sendTextTemplate8(msg.to, str(helpMessage))
                               
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage2 = helpbot()
                               sendTextTemplate8(msg.to, str(helpMessage2))
                               
                        elif cmd == "help3":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage3 = helpbot1()
                               sendTextTemplate8(msg.to, str(helpMessage3)) 
                              
                        elif cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage4 = helpbot2()
                               sendTextTemplate8(msg.to, str(helpMessage4)) 
                                                                                       
                        if cmd == "on":
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["selfbot"] = True
                                sendTextTemplate(msg.to, "🍁ʙᴏᴛ ᴀᴋᴛɪғ ᴋᴇᴍʙᴀʟɪ")
                                
                        elif cmd == "off":
                            if msg._from in owner or msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate(msg.to, "🍁ʙᴏᴛ ᴍᴀᴛɪ sᴇᴍᴇɴᴛᴀʀᴀ")
                                
                        elif cmd == 'vp':
                        	if msg._from in owner or msg._from in admin:
                                 me = cl.getContact(mid)
                                 cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")                                            
                                                
                        elif cmd == "settings":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭─────────────\n"
                                if wait["sticker"] == True: md+="│sᴛɪᴄᴋᴇʀ ⭕\n"
                                else: md+="│sᴛɪᴄᴋᴇʀ ⛔\n"
                                if wait["contact"] == True: md+="│ᴄᴏɴᴛᴀᴄᴛ ⭕\n"
                                else: md+="│ᴄᴏɴᴛᴀᴄᴛ ⛔\n"
                                if wait["detectMention"] == True: md+="│ʀᴇsᴘᴏɴ ⭕\n"
                                else: md+="│ʀᴇsᴘᴏɴ ⛔\n"
                                if wait["autoJoin"] == True: md+="│ᴀᴜᴛᴏᴊᴏɪɴ ⭕\n"
                                else: md+="│ᴀᴜᴛᴏᴊᴏɪɴ ⛔\n"
                                if settings["autoJoinTicket"] == True: md+="│ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ⭕\n"
                                else: md+="│ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ⛔\n"
                                if settings["unsendMessage"] == True: md+="│ᴜɴsᴇɴᴅ ⭕\n"
                                else: md+="│ᴜɴsᴇɴᴅ ⛔\n"
                                if wait["autoAdd"] == True: md+="│ᴀᴜᴛᴏᴀᴅᴅ ⭕\n"
                                else: md+="│ᴀᴜᴛᴏᴀᴅᴅ ⛔\n"
                                if msg.to in welcome: md+="│ᴡᴇʟᴄᴏᴍᴇ ⭕\n"
                                else: md+="│ᴡᴇʟᴄᴏᴍᴇ ⛔\n"
                                if wait["autoLeave"] == True: md+="│ᴀᴜᴛᴏʟᴇᴀᴠᴇ ⭕\n"
                                else: md+="│ᴀᴜᴛᴏʟᴇᴀᴠᴇ ⛔\n"
                                if msg.to in protect["pqr"]: md+="│ᴘʀᴏᴜʀʟ ⭕\n"
                                else: md+="│ᴘʀᴏᴜʀʟ ⛔\n"
                                if msg.to in protect["proall"]: md+="│ᴘʀᴏᴀʟʟ ⭕\n"
                                else: md+="│ᴘʀᴏᴀʟʟ ⛔\n"
                                if msg.to in protect["protect"]: md+="│ᴘʀᴏᴛᴇᴄᴛ ⭕\n"
                                else: md+="│ᴘʀᴏᴛᴇᴄᴛ ⛔\n"
                                if msg.to in protect["pinv"]: md+="│ʀᴏɪɴᴠ ⭕\n"
                                else: md+="│ᴘʀᴏɪɴᴠ ⛔\n"
                                if msg.to in protect["antijs"]: md+="│ᴊs ⭕\n"
                                else: md+="│ᴊs ⛔\n"
                                if msg.to in ghost: md+="│ɢʜᴏsᴛ ⭕\n"
                                else: md+="│ɢʜᴏsᴛ ⛔\n"
                                if msg.to in protectcancel: md+="│ᴘʀᴏᴄᴀɴᴄᴇʟ ⭕\n├─────────────\n"
                                else: md+="│ᴘʀᴏᴄᴀɴᴄᴇʟ ⛔\n├─────────────\n"
                                sendTextTemplate8(msg.to, md+"│ᴅᴀᴛᴇ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│ᴛɪᴍᴇ  "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╰────────────── ")                              
                                
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                cl.sendText(msg.to,"🍁ɪɴɪ ᴄʀᴇᴀᴛᴏʀ ᴋᴀᴍɪ, ᴍᴀɴɪs ᴋᴀɴ 😂")
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate(msg.to, "🍁ᴍʏ ᴄʀᴇᴀᴛᴏʀ")
                               sendTextTemplate4(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == ".me" or text.lower() == 'aku':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:                                           
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': msg._from}
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)
                         #       path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                          #      image = 'http://dl.profile.line.naver.jp'+path
                        #        cl.sendImageWithURL(msg.to, image)
                                
                        elif cmd == ".me":                       	
                    	    if msg._from in owner or msg._from in admin or msg._from in staff: 
                              contact = cl.getContact(sender)
                              image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                              cl.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(contact.displayName))
                              cl.sendMessage(msg.to, None,contentMetadata={'mid': sender}, contentType=13)
                              image = 'http://dl.profile.line.naver.jp'+path
                              cl.sendImageWithURL(msg.to, image)
                              
                        elif cmd == "me":
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                               	
                                data = {
                                        "type": "flex",
                                        "altText": "Cannibal Killer",
                                        "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(status.displayName),
            "weight": "bold",
            "size": "xs",
            "wrap": True
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(status.statusMessage),
                "size": "xs",
                "color": "#000000",
                "wrap": True
              }
            ]
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "spacing": "xs",
                "contents": [
                  {
                    "type": "text",
                    "text": "         Cannibal Killer",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "offsetTop": "0px"
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "xs",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://h.top4top.io/p_1556ubozy0.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "ᴄʀᴇᴀᴛᴏʀ ᴛᴇᴍᴘʟᴀᴛᴇ",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Cannibal",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "         Cannibal Killer",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://i.top4top.io/p_1521lty361.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "ᴄʀᴇᴀᴛᴏʀ ᴛᴇᴍᴘʟᴀᴛᴇ",
            "weight": "bold",
            "size": "sm"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Cannibal",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "         Cannibal Killer",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
}
}
                                cl.postTemplate(to, data)
                                                                       
                        elif text.lower() == "mid":
                              # cl.sendMessage(msg.to, msg._from)
                               sendTextTemplate2(msg.to, "ᴍᴀᴜ ɴɢᴀᴘᴀɪɴ ᴋᴋ,,,ᴍᴀᴜ ɴʏᴇᴘᴀᴍ ᴊᴀɴᴅᴀ ᴀᴘᴀ ᴍᴀᴜ ᴊs ɢᴄ ᴋᴋ,,")
                             #  cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'janda':
                               sendTextTemplate2(msg.to, "ᴇᴍᴀɴɢ ᴀᴋᴜ ᴊᴀɴᴅᴀ ᴋᴋ, ᴇᴀɴɢ ᴍᴀᴜ sᴀᴍᴀ ᴊᴀɴᴅᴀ ᴀɴᴀᴋ 3 ᴋᴋ, ᴛᴀᴘɪ sᴀʏᴀɴɢ ᴜᴅᴀʜ ᴀɴᴜ ᴘᴜɴʏᴀᴋᴜ ᴋᴋ 😂")
                             #  cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'sue':
                               sendTextTemplate2(msg.to, "ᴇᴍᴀɴɢ ᴜᴅᴀʜ sᴜᴇ ᴘᴜɴʏᴀ ᴋᴋ, ᴋᴀʟᴏ ɢᴀᴋ sᴜᴇ, ɢᴀᴋ ʙᴀᴋᴀʟᴀɴ ʙɪsᴀ ᴅɪ ᴛᴜsᴜᴋ ᴀɴᴜ ᴋᴋ😂")
                             #  cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'dudul':
                               sendTextTemplate2(msg.to, "sᴇsᴀᴍᴀ ᴅᴜᴅᴜʟ ᴊᴀɴɢᴀɴ sᴀʟɪɴɢ ʙᴜʟʟʏ ᴋᴋ😂, ᴅɪ ʙᴀᴡᴀʜ ᴍᴜ ᴊᴜɢᴀ ᴜᴅᴀʜ ɢᴜɴᴅᴜʟ ᴋᴋ 😜")
                              # cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'setan':
                               sendTextTemplate2(msg.to, "sᴇᴛᴀɴ sᴇᴛᴀɴ sᴇᴛᴀɴ, ᴇᴍᴀɴɢ ᴍᴜᴋᴀ ʟᴜ ᴋᴀʏᴀᴋ sᴇᴛᴀɴ ᴋᴋ😂")
                            #   cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'makan':
                               sendTextTemplate2(msg.to, "ᴜᴅᴀʜ ᴘᴀᴅᴀ ᴍᴀᴋᴀɴ ʙᴇʟᴏᴍ ᴋᴋ, ᴋᴀʟᴏ ʙᴇʟᴏᴍ sɪɴɪ ᴀᴋᴜ sᴜᴀᴘɪɴ ᴋᴋ")
                           #    cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'minum':
                               sendTextTemplate2(msg.to, "sɪɴɪ ᴋᴋ ᴍɪɴᴜᴍ ʙᴀʀᴇɴɢ ᴋɪᴛᴀ😛")
                            #   cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'susu':
                               sendTextTemplate2(msg.to, "sᴜsᴜ sᴜsᴜ sᴜsᴜ, ᴅᴀʀɪ ᴋᴇᴄɪʟ ʟᴜ sᴜᴅᴀʜ ᴅɪ ɴʏᴜsᴜɪɴ, ᴍᴀsᴀ ᴍɪɴᴛᴀ ɴʏᴜsᴜ sᴀᴍᴀ ʀᴏɴᴅᴏ ᴋᴋ😂")
                            #   cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'duda':
                               sendTextTemplate2(msg.to, "ᴇᴍᴀɴɢ ᴀᴋᴜ ᴅᴜᴅᴀ ᴋᴋ,,,ᴋʟᴏ ᴋᴋ ᴍᴀᴜ ᴀᴍᴀ ᴅᴜᴅᴀ, ᴀʏᴜᴋ ᴋɪᴛᴀ ᴊᴀᴅɪᴀɴ😂")
                             #  cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'ngopi':
                               sendTextTemplate2(msg.to, "ᴜᴅᴀʜ ᴘᴀᴅᴀ ɴɢᴏᴘɪ ʙᴇʟᴜᴍ ᴋᴋ, ᴋᴀʟᴏ ʙᴇʟᴜᴍ sɪɴɪ ᴋᴋ ɴɢᴏᴘɪ ʙᴀʀᴇɴɢ 😍")
                            #   cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'bot':
                               sendTextTemplate2(msg.to, "ʙᴀᴛ ʙᴏᴛ ʙᴀᴛ ʙᴏᴛ ᴍᴀᴛᴀᴍᴜ ɪᴛᴜ ʙᴏᴛ, ᴀᴋᴜ ᴍᴀʜ ʙᴜᴋᴀɴ ʙᴏᴛ, ᴛᴀᴘɪ ʙᴀᴘᴀᴋᴇ ʙᴏᴛ 😜")
                              # cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'siang':
                               sendTextTemplate2(msg.to, "sɪᴀɴɢ ᴊᴜɢᴀ ᴋᴋ ᴋᴜ sʏᴀɴᴛɪᴋ, ᴜᴅᴀʜ ᴅᴀᴘᴀᴛ ᴛɪᴋᴜɴɢᴀɴ ʙᴇʟᴜᴍ ᴋᴋ 😅")
                             #  cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'pagi':
                               sendTextTemplate2(msg.to, "ᴘᴀɢɪ ᴊᴜɢᴀ ᴋᴋ, ᴜᴅᴀʜ sᴀʀᴀᴘᴀɴ ʙᴇʟᴜᴍ 😘")
                             #  cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'sore':
                               sendTextTemplate2(msg.to, "sᴏʀᴇ ᴊᴜɢᴀ ᴋᴋ, ᴜᴅᴀʜ ᴍᴀɴᴅɪ ʙᴇʟᴜᴍ, ᴋᴀʟᴏ ʙᴇʟᴜᴍ sɪɴɪ ᴀᴋᴜ ᴛᴇᴍᴇɴɪ ᴋᴋ ᴍᴀɴᴅɪ 🤗")
                          #     cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'malam':
                               sendTextTemplate2(msg.to, "ᴍᴀʟᴀᴍ ᴊᴜɢᴀ ᴋᴋ, ᴡᴀᴋᴛᴜ ɴʏᴀ ɴɪᴋᴜɴɢ ᴇɴᴀᴋ ɴʏᴀ ᴍᴀʟᴀᴍ-ᴍᴀʟᴀᴍ ɢɪɴɪ ᴋᴋ 😛")
                             #  cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'kojom':
                               sendTextTemplate2(msg.to, "ɴᴀʜ ᴋᴀɴ,,,ɴɢᴀᴊᴀᴋɪɴ ᴋᴏᴊᴏᴍ,,,ɴᴛᴀʀ ʙᴏᴊᴏɴᴇ ᴍᴀʀᴀʜ ʙᴀʀᴜ ᴛᴀᴜ ʀᴀsᴀ ᴋᴋ 😜")
                            #   cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'nikung':
                               sendTextTemplate2(msg.to, "ᴀʏᴜᴋ ᴋᴋ ᴋɪᴛᴀ ɴɪᴋᴜɴɢ, ʟᴀɴɢsᴜɴɢ ᴘᴍ ᴀᴊᴀ ʏᴀ ᴋᴋ😂")
                            #   cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835583","STKPKGID":"7451","STKVER":"9"}, contentType=7)
                        elif text.lower() == 'salam':
                               sendTextTemplate2(msg.to, "ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ")
                           #    cl.sendMessage(msg.to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                        elif text.lower() == 'assalamualaikum':
                               sendTextTemplate2(msg.to, "ᴡᴀᴀʟᴀɪᴋᴜᴍsᴀʟᴀᴍ")
                             #  cl.sendMessage(msg.to, "ُوَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")
                        elif cmd == "jandeee":
                          if wait["selfbot"] == True:                            
                               cl.sendMessage(msg.to, "nyaman nyaman nyaman nyaman nyaman nyaman    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿 ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.")
                        
                        elif ("Get id " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "🍁ɴᴀᴍᴀ : "+str(mi.displayName)+"\n🍁ᴍɪᴅ : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Kepo " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "🍁ɴᴀᴍᴀ : "+str(mi.displayName)+"\n🍁ᴍɪᴅ : " +key1+"\n🍁Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                                             
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)                                      
                                  sendTextTemplate(to, "🍁sᴜᴄᴄᴇs ʀᴇᴊᴇᴄᴛ {} ".format(str(len(ginvited))))                                  
                              else:
                                  sendTextTemplate(to, "🍁sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")                 

                        elif "autoreject " in msg.text.lower():
                            xpesan = msg.text.lower()
                            xres = xpesan.replace("autoreject ","")
                            if xres == "off":
                                settings['autorejc'] = False
                                sendTextTemplate(msg.to,"🍁Auto Reject already Off")
                            elif xres == "on":
                                settings['autorejc'] = True
                                sendTextTemplate(msg.to,"🍁Auto Reject already Onn")                 

                        elif text.lower() == "hapuschat":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               try:
                                   cl.removeAllMessages(op.param2)                                                                     
                                   sendTextTemplate(msg.to,"🍁sᴜᴅᴀʜ ᴅɪ ʙᴇʀsɪʜᴋᴀɴ ʙᴏssᴋᴜ...👍")                                   
                               except:
                                   pass
                                
                        elif cmd.startswith("bcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   sendTextTemplate4(group,"🔰ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴋ🔰 \n\n" + str(pesan))
                                   
                        elif cmd.startswith("broadcast: "):
                           if msg._from in admin:
                             sep = text.split(" ")
                             bc = text.replace(sep[0] + " ","")
                             saya = cl.getGroupIdsJoined()
                             for group in saya:
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  " [ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴋ] \n🍁ʙʀᴏᴀᴅᴄᴀsᴛ ʙʏᴇ "
                                ret_ = "{}".format(str(bc))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                sendTextTemplate4(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif "hah" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-W_bn2qqdYXE/Wyhbjj2wqKI/AAAAAAANIz4/KQVsbq-aXm0kZNfFOS5SN8fqCvQ18xnUACLcBGAs/s1600/AW1238502_03.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~aryopandelaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    #cl.postTemplate(to, data)
                        elif "sedih" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-OfIz4mSIumw/WbLEZw7l6nI/AAAAAAARd6Y/Dxzos1SA_5MU32bXFTKToLDndM7YpV7WACLcBGAs/s1600/AW529310_04.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~aryopandelaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    #cl.postTemplate(to, data) 
                        elif "hadeh" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/pPz524G/Benjol.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~aryopandelaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    #cl.postTemplate(to, data)
                                    
                        elif "sue" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/pPz524G/tai-line.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~aryopandelaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    #cl.postTemplate(to, data)
                                    
                        elif "wkwk" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://thumbs.gfycat.com/QuaintScornfulAmericanlobster-small.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~aryopandelaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    #cl.postTemplate(to, data)
                                    
                        elif "cium" in msg.text.lower():                     	
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/pPz524G/7c8ab257ee3b7e1ef283b7c0a35d9d2c.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~aryopandelaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                 #   cl.postTemplate(to, data)
           
                        elif "gombal" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://thumbs.gfycat.com/KlutzyUglyGelding-small.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~aryopandelaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    #cl.postTemplate(to, data)
                                    
                        elif "diam" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://thumbs.gfycat.com/BigIdealAsianelephant-small.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~aryopandelaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    #cl.postTemplate(to, data)
                                    
                        elif "sepi" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/pPz524G/AW316819-05.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~aryopandelaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    #cl.postTemplate(to, data)

                        elif text.lower() == "sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate2(msg.to, "🍁sɴᴀᴍᴇ \n\n" + str(Setmain["keyCommand"]) + " ")
                               
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate2(msg.to, " 🍁sᴛᴀᴛᴜs ᴋᴇʏ \n🍁sᴇᴛᴋᴇʏ sᴀᴀᴛ ɪɴɪ " + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendTextTemplate2(msg.to, "🍁ɢᴀɢᴀʟ ɢᴀɴᴛɪ ᴋᴇʏ")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sendTextTemplate2(msg.to, " 🍁ɢᴀɴᴛɪ sᴇᴛᴋᴇʏ \n🍁sᴇᴛᴋᴇʏ ᴊᴀᴅɪ{}".format(str(key).lower()))
                                   
                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               sendTextTemplate2(msg.to, " 🍁ʀᴇsᴇᴛ ᴋᴇʏ \n🍁sᴇᴛᴋᴇʏ ᴛᴇʟᴀʜ ᴅɪ ʀᴇsᴇᴛ")
                               
                        elif cmd.startswith("setsname "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendTextTemplate2(msg.to, "🍁ᴅᴏɴᴇ ɢᴀɴᴛɪ sɴᴀᴍᴇ")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sendTextTemplate2(msg.to, "🍁sɴᴀᴍᴇ ɢᴀɴᴛɪ \n\nsɴᴀᴍᴇ ᴅᴏɴᴇ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ {}".format(str(key).lower()))

                        elif text.lower() == "reset sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               Setmain["keyCommand"] = ""
                               sentTextTemplate2(msg.to, "🍁ᴅᴏɴᴇ ʀᴇsᴇᴛ sɴᴀᴍᴇ")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sendTextTemplate(msg.to, "🍁ᴡᴀɪᴛ...")
                               sendTextTemplate(msg.to, "🍁ᴅᴏɴᴇ...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               sendTextTemplate(msg.to, "🍁ᴅᴏɴᴇ...")
                            
                        elif cmd == "time":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "ᴀᴋᴛɪғ " +waktu(eltime)
                               sendTextTemplate2(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "🍁ᴛᴇʀᴛᴜᴛᴜᴘ"
                                    gTicket = "🍁ᴛɪᴅᴀᴋ ᴀᴅᴀ"
                                else:
                                    gQr = "🍁Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate3(msg.to, "🍁ɢʀᴏᴜᴘ ɪɴғᴏ\n\n🍁ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(G.name)+ "\n🍁ɪᴅ ɢʀᴏᴜᴘ : {}".format(G.id)+ "\n🍁ᴄʀᴇᴀᴛᴏʀ ɢʀᴏᴜᴘ : {}".format(G.creator.displayName)+ "\n🍁ᴡᴀᴋᴛᴜ ᴅɪʙᴜᴀᴛ : {}".format(str(timeCreated))+ "\n🍁ᴊᴜᴍʟᴀʜ ᴀɴɢɢᴏᴛᴀ : {}".format(str(len(G.members)))+ "\n🍁ᴊᴜᴍʟᴀʜ ᴘᴇɴᴅɪɴɢɢᴀɴ : {}".format(gPending)+ "\n🍁ɢʀᴏᴜᴘ ǫʀ : {}".format(gQr)+ "\n🍁ɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ: {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                sendTextTemplate(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in owner or msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "🍁ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += " ɪɴғᴏ ɢʀᴏᴜᴘ\n"
                                ret_ += "\n🍁ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(G.name)
                                ret_ += "\n🍁ɪᴅ ɢʀᴏᴜᴘ : {}".format(G.id)
                                ret_ += "\n🍁ᴘᴇᴍʙᴜᴀᴛ : {}".format(gCreator)
                                ret_ += "\n🍁ᴡᴀᴋᴛᴜ ᴅɪʙᴜᴀᴛ : {}".format(str(timeCreated))
                                ret_ += "\n🍁ᴊᴜᴍʟᴀʜ ᴀɴɢɢᴏᴛᴀ : {}".format(str(len(G.members)))
                                ret_ += "\n🍁ᴊᴜᴍʟᴀʜ ᴘᴇɴᴅɪɴɢɢᴀɴ : {}".format(gPending)
                                ret_ += "\n🍁ɢʀᴏᴜᴘ ǫʀ : {}".format(gQr)
                                ret_ += "\n🍁ɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ : {}".format(gTicket)
                                ret_ += ""
                                sendTextTemplate4(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"🍁ɢʀᴏᴜᴘ ɴᴀᴍᴇ : " + str(G.name) + " \n\n🍁ᴍᴇᴍʙᴇʀ ʟɪsᴛ \n" + ret_ + "\n\n🍁ᴛᴏᴛᴀʟ %i ᴍᴇᴍʙᴇʀ" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leavegrup "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    ginfo = cl.getGroup(group)
                                    gCreator = ginfo.creator.mid
                                    recky = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '🍁ᴍᴀᴀғ ɴɪᴋᴜɴɢ ᴅᴜʟᴜ ʏᴀ'
                                    reck = str(recky.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':recky.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan+zxc + "🍁ʟᴀɪɴ ᴋᴀʟɪ ᴍᴀᴍᴘɪʀ ʟᴀɢɪ, ʏɢ ᴘᴇɴᴛɪɴɢ ᴀᴅᴀ ᴍᴀᴋ ᴊᴀɴᴅᴀ ɴʏᴀ 😂" 
                                    cl.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    cl.sendImageWithURL(group,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=u48c350911cde6604da051d9da06c5db7&oid=faadb1b4f3991376bdccbd5700545da6")
                                    cl.leaveGroup(group)
                                except:
                                    cl.sendMessage(msg.to, "")
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ginfo = cl.getGroup(group)
                                gCreator = ginfo.creator.mid
                                reck = cl.getContact(gCreator)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = ' 🍁ᴅᴏɴᴇ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ \n 🍁ᴄʀᴇᴀᴛᴏʀ :  '
                                recky = str(reck.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':reck.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                ret_ += xpesan +zxc
                                ret_ += " 🍁ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(G.name)
                                ret_ += "\n 🍁ᴘᴇɴᴅɪɴɢɢᴀɴ : {}".format(gPending)
                                ret_ += "\n 🍁ᴊᴜᴍʟᴀʜ ᴀɴɢɢᴏᴛᴀ : {}".format(str(len(G.members)))
                                sendTextTemplate4(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as e:
                                sendTextTemplate(to, str(e))
								
                        elif 'leaveto ' in text.lower():
                            if msg._from in owner:		   
                                gids = msg.text.replace('leaveto ',"")
                                gid = cl.getGroup(gids)
                                try:
                                    sendTextTemplate(gids, "🍁ᴍᴀᴀғ ʏᴀ")							
                                    cl.leaveGroup(gids)
                                except:
                                    sendTextTemplate(to,"🍁ᴅᴏɴᴇ ʟᴇᴀᴠᴇ ᴛᴏ ɢʀᴏᴜᴘ " + gids.name)
                                    
                        elif cmd.startswith("leaveall "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    cl.sendText(group,"🍁ᴍᴀᴀғ  ᴏᴛᴡ ᴅᴜʟᴜ\n🍁ᴋᴇᴛᴇᴍᴜ ʟᴀɪɴ ᴡᴀᴋᴛᴜ ʏᴀ")
                                    cl.leaveGroup(group)
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = ' 🍁ᴅᴏɴᴇ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ \nᴄʀᴇᴀᴛᴏʀ :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    cl.sendText(msg.to, "")
                                    gCreator = "🍁ᴛɪᴅᴀᴋ ᴅɪ ᴛᴇᴍᴜᴋᴀɴ"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += " 🍁ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(G.name)
                                ret_ += "\n 🍁ᴘᴇɴᴅɪɴɢᴀɴ : {}".format(gPending)
                                ret_ += "\n 🍁ᴊᴜᴍʟᴀʜ ᴀɴɢɢᴏᴛᴀ : {}".format(str(len(G.members)))
                                sendTextTemplate4(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as e:
                                sendTextTemplate(to, str(e))           
                        

                        elif cmd == "flist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate3(msg.to,"🍁ғʀɪᴇɴᴅ ʟɪsᴛ\n\n"+ma+"\n🍁ᴛᴏᴛᴀʟ"+str(len(gid))+"ғʀɪᴇɴᴅ")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "│ " + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate3(msg.to,"╭──[ ʟɪsᴛ ɢʀᴏᴜᴘ ]\n│\n"+ma+"│\n╰──[ ᴛᴏᴛᴀʟ「"+str(len(gid))+"」ɢʀᴏᴜᴘ ]")

                        elif cmd == "curl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendTextTemplate(msg.to, "🍁ᴜʀʟ ᴄʟᴏsᴇᴅ")

                        elif cmd == "ourl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "🍁ɴᴀᴍᴀ : "+str(x.name)+ "\n🍁ᴜʀʟ ɢʀᴏᴜᴘ : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE FROFILE============#
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate(msg.to,"🍁sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                                
                        elif cmd == "cp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["OKfoto"][mid] = True
                                sendTextTemplate(msg.to,"🍁sᴇɴᴅ ғᴏᴛᴏ")
                                
#================BOT UPDATE NAME============#
                        elif cmd.startswith("cn: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                sendTextTemplate(msg.to,"🍁ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")

#===========BOT UPDATE============#                                                          
                        elif cmd == "mentionall" or text.lower() == 'nah':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                cl.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)  
                                
                        elif cmd == "botlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"🍁ʙᴏᴛʟɪsᴛ\n\n\n"+ma+"\n%s ʙᴏᴛs" %(str(len(Bots))))

                        elif cmd == "adminlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                sentTextTemplate3(msg.to,"🔰ᴀᴅᴍɪɴ🔰\n\n🍁ᴏᴡɴᴇʀ\n"+ma+"\n🍁ᴀᴅᴍɪɴ\n"+mb+"\n🍁sᴛᴀғғ:\n"+mc+"\n%s ᴀᴅᴍɪɴ" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "cekpro":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                mg = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0
                                g = 0
                                gid = protect["pqr"]
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["pinv"]
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["antijs"]
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["protect"]
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["proall"]
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +cl.getGroup(group).name + "\n"
                                gid = ghost
                                for group in gid:
                                    g = g + 1
                                    end = '\n'
                                    mg += str(g) + ". " +cl.getGroup(group).name + "\n"
                                sendTextTemplate3(msg.to,"🛡sᴇᴛ ᴘʀᴏ🛡\n\n🍁ᴘʀᴏ ǫʀ :\n"+ma+"\n🍁ᴘʀᴏ ɪɴᴠɪ:\n"+mb+"\n🍁ᴘʀᴏ ᴀᴊs:\n"+mc+"\n🍁ᴘʀᴏ ᴄᴀɴᴄᴇʟ:\n"+md+"\n🍁ᴘʀᴏ:\n"+me+"\n🍁ᴘʀᴏ ᴀʟʟ:\n"+mf+"\n🍁ɢʜᴏsᴛ:\n"+mg+"\n\n🍁ᴘʀᴏʟɪsᴛ %s ɢʀᴏᴜᴘ ᴘʀᴏ" %(str(len(protect["pqr"])+len(protect["pinv"])+len(protect["antijs"])+len(protectcancel)+len(protect["protect"])+len(protect["proall"])+len(ghost))))
#====================================================================                            
                              
                        elif cmd.startswith("bots_in "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(group)
                                cl.acceptGroupInvitationByTicket(group,Ticket)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = ' 🍁ᴅᴏɴᴇ ᴍᴀsᴜᴋ ɢʀᴏᴜᴘ \n 🍁ᴄʀᴇᴀᴛᴏʀ :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = ""
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = ""
                                    gTicket = "Error"
                                else:
                                    gQr = ""
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += " 🍁ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(G.name)
                                ret_ += "\n 🍁ɢʀᴏᴜᴘ ǫʀ : {}".format(gQr)
                                ret_ += "\n 🍁ᴘᴇɴᴅɪɴɢɢᴀɴ : {}".format(gPending)
                                ret_ += "\n 🍁ɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ : {}".format(gTicket)
                                ret_ += ""
                                sendTextTemplate4(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass
                                
                        elif cmd == "mulih":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sendTextTemplate(msg.to, "🍁ᴍᴀᴋᴀsɪ sᴜᴅᴀʜ ᴊᴇᴘɪᴛ\nᴋᴇᴛᴇᴍᴜ ʟᴀɪɴ ᴡᴀᴋᴛᴜ ʏᴀ ᴋᴀᴡᴀɴ... "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin or msg._from in owner:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        sendTextTemplate(i, " 🍁sɪʟᴀʜᴋᴀɴ ᴀᴅᴅ ᴏᴡɴᴇʀ ᴋᴀᴍɪ ")
                                        cl.leaveGroup(i)
                                        sendTextTemplate(to,"🍁ᴅᴏɴᴇ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ " +h)
#====================================================================                            
                        elif cmd == "timerespon":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                sendTextTemplate4(msg.to, "🍁ᴛɪᴍᴇ ʀᴇsᴘᴏɴ\n\n 🍁ɢᴇᴛ ᴘʀᴏғɪʟᴇ\n   %.10f\n 🍁ɢᴇᴛ ᴄᴏɴᴛᴀᴄᴛ\n   %.10f\n 🍁ɢᴇᴛ ɢʀᴏᴜᴘ\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:                              
                               sendMention1(msg.to, sender, "⇨sᴘᴇᴇᴅ ᴜᴘ\nᴜsᴇʀ:","")
                               start = time.time() / 3 
                               time.sleep(0.002)  
                               elapsed_time = time.time() / 3 - start
                               cl.sendMessage(msg.to,format(str(elapsed_time/3)))
                               
                               
                        elif cmd == "lurk:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 sendTextTemplate(msg.to, "🍁ʟᴜʀᴋɪɴɢ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ\n\nᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurk:off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 sendTextTemplate(msg.to, "🍁ʟᴜʀᴋɪɴɢ ʙᴇʀʜᴀsɪʟ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ\n\nᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ ʀᴇsᴜʟᴛ {} ᴍᴇᴍʙᴇʀ ]    \n\n  [ ʟᴜᴋᴇʀs ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['OKreadPoint'][msg.to]
                                        del Setmain['OKreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['OKreadPoint'][msg.to] = msg.id
                                    Setmain['OKreadMember'][msg.to] = {}
                                else:
                                    sendTextTemplate(msg.to, "🍁ᴜsᴇʀ ᴋᴏsᴏɴɢ...")
                            else:
                                sendTextTemplate(msg.to, "🍁ᴋᴇᴛɪᴋ ʟᴜʀᴋɪɴɢ ᴅᴜʟᴜ")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate(msg.to, "╭──────────────\n│sɪᴅᴇʀ ᴏɴ\n├──────────────\n│ᴅᴀᴛᴇ "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│ᴛɪᴍᴇ  "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╰────────────── ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(msg.to, "╭──────────────\n│sɪᴅᴇʀ ᴏғғ\n├──────────────\n│ᴅᴀᴛᴇ "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│ᴛɪᴍᴇ  "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╰────────────── ")
                              else:
                                  sendTextTemplate(msg.to, "🍁sᴜᴅᴀʜ ᴀᴋᴛɪғ")

#===========add img============# 
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate(msg.to,"🍁sᴇɴᴅ ʏᴏᴜʀ ɪᴍᴀɢᴇ.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                sendTextTemplate(msg.to,"🍁sᴇɴᴅ ʏᴏᴜʀ ɪᴍᴀɢᴇ.....")
                                              
                        elif cmd == "gf":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["ChangeVideoProfilevid"][msg._from] = True
                                sendTextTemplate(msg.to,"🍁sᴇɴᴅ ᴠɪᴅɪᴏ ɴʏᴀ...")
                                
                        elif cmd.startswith("changedualurl: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ","")                            
                                cl.downloadFileURL(url,'path','video.mp4')
                                settings["ChangeVideoProfilePicture"][msg._from] = True
                                sendTextTemplate(msg.to, "🍁sᴇɴᴅ ɢᴀᴍʙᴀʀ ɴʏᴀ.....")
                                
                        elif cmd.startswith("addimg"):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addimage"]["status"] = True
                                    settings["Addimage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "🍁sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ...")
                                else:
                                    sendTextTemplate(to, "🍁ғᴏᴛᴏ ɪᴛᴜ sᴜᴅᴀʜ ᴅᴀʟᴀᴍ ʟɪsᴛ")
                        elif cmd.startswith("dellimg "):
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("image.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate(to, "🍁ғᴏᴛᴏ ɪᴛᴜ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ʟɪsᴛ")

                        elif cmd == "listimage":
                                no = 0
                                ret_ = "🔰ᴅᴀғᴛᴀʀ ɪᴍᴀɢᴇ🔰\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + image.title() + "\n"
                                ret_ += "\n🍁ᴛᴏᴛᴀʟ {} ɪᴍᴀɢᴇ".format(str(len(images)))
                                sendTextTemplate(to, ret_)
#==============add video==========================================================================
                        elif cmd.startswith("addvideo"):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addvideo"]["status"] = True
                                    settings["Addvideo"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "🍁sɪʟᴀʜᴋᴀɴɴᴋɪʀɪᴍ ᴠɪᴅɪᴏ ɴʏᴀ...")
                                else:
                                    sendTextTemplate(to, "🍁ᴠɪᴅɪᴏ ɪᴛᴜ sᴜᴅᴀʜ ᴅᴀʟᴀᴍ ʟɪsᴛ")
                        elif cmd.startswith("dellvideo "):
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("video.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate(to, "🍁ᴠɪᴅɪᴏ ɪᴛᴜ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ʟɪsᴛ")

                        elif cmd == "listvideo":
                                no = 0
                                ret_ = "🔰ᴅᴀғᴛᴀʀ ᴠɪᴅɪᴏ🔰\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + image.title() + "\n"
                                ret_ += "\n🍁ᴛᴏᴛᴀʟ {} ᴠɪᴅɪᴏ".format(str(len(images)))
                                sendTextTemplate(to, ret_)
#=========== [ Add Audio] ============#
                        elif cmd.startswith("addmp3 "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["status"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "🍁sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ ᴍᴘ3ɴʏᴀ...") 
                                else:
                                    sendTextTemplate(to, "🍁ᴍᴘ3 ɪᴛᴜ sᴜᴅᴀʜ ᴅᴀʟᴀᴍ ʟɪsᴛ") 
                                
                        elif cmd.startswith("dellmp3 "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    cl.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘsᴜ ᴍᴘ3 {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate(to, "🍁ᴍᴘ3 ɪᴛᴜ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ʟɪsᴛ") 
                                 
                        elif cmd == "listmp3":
                                no = 0
                                ret_ = "🔰ᴅᴀғᴛᴀʀ ʟᴀɢᴜ🔰\n\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str(no) + ". " + audio.title() + "\n"
                                ret_ += "\n🍁ᴛᴏᴛᴀʟ {} ʟᴀɢᴜ".format(str(len(audios)))
                                sendTextTemplate(to, ret_)
 #=========== [ Add sticker] ============#                   
                        elif cmd.startswith("addsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["Addsticker"]["status"] = True
                                    settings["Addsticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "🍁sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ sᴛɪᴄᴋᴇʀɴʏᴀ...") 
                                else:
                                    sendTextTemplate(to, "🍁sᴛɪᴄᴋᴇʀ ɪᴛᴜ sᴜғᴀʜ ᴅᴀʟᴀᴍ ʟɪsᴛ") 
                                
                        elif cmd.startswith("dellsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs sᴛɪᴄᴋᴇʀ {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate(to, "🍁sᴛɪᴄᴋᴇʀ ɪᴛᴜ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ʟɪsᴛ") 
                                                   
                        elif cmd == "liststicker":
                                no = 0
                                ret_ = " 🔰ᴅᴀғᴛᴀʀ sᴛɪᴄᴋᴇʀ🔰 \n\n"
                                for sticker in stickers:
                                    no += 1
                                    ret_ += str(no) + ". " + sticker.title() + "\n"
                                ret_ += "\n🍁ᴛᴏᴛᴀʟ {} sᴛɪᴄᴋᴇʀs".format(str(len(stickers)))
                                sendTextTemplate(to, ret_)
#====================================================================   
                        elif 'like ' in text.lower():
                           if msg._from in admin:
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).mid
                                    s = cl.getContact(u).displayName
                                    hasil = cl.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        cl.likePost(str(msg.to), str(result), likeType=random.choice(typel))
                                        cl.createComment(str(msg.to), str(result), wait["comment"])
                                    sendTextTemplate(msg.to, '🍁ᴅᴏɴᴇ ʟɪᴋᴇ+ᴄᴏᴍᴍᴇɴᴛ '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    sendTextTemplate(msg.to, str(e))
                                 
                        elif cmd.startswith("tafsirquran "):
                          if msg._from in admin:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","+")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://tafsirq.com/topik/{}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.findAll('div', attrs={'class':'col-md-12'})
                                    tit = soup.findAll('h1')[0].text
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = tit+"\n"
                                        for get in data:
                                            num += 1
                                            tip = get.find('span').text
                                            isi = tip+': '+get.find('a').text
                                            link = get.find('a')['href']
                                            ret_ += "\n {}. {}".format(str(num), str(isi))
                                        ret_ += "\n\n 🍁ᴛᴏᴛᴀʟ {} ʀᴇsᴜʟᴛ".format(str(len(data)))
                                        cl.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data):
                                            get = data[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get(get.find('a')['href'])
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                data = soup.findAll('div', attrs={'class':'panel-body'})[0]
                                                try:
                                                    ret = get.find('a').text+"\n"
                                                    ret += data.findAll('p')[0].text
                                                    ret += "\n\n"+data.findAll('p')[1].text
                                                    sendTextTemplate4(to, str(ret))
                                                except:
                                                    sendTextTemplate(to, "🍁ɢᴀɢᴀʟ ᴍᴇɴɢɢᴀᴍʙɪʟ ᴅᴀᴛᴀ")                                                       
                                                                                               
                        elif text.lower().startswith("music "):
                            try:
                                search = text.lower().replace("musik","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 ʜᴀsɪʟ ᴍᴜsɪᴄ 」\n"
                                hasil += "\n🍁ᴘᴇɴʏᴀɴʏɪ : {}".format(str(info["penyanyi"]))
                                hasil += "\n🍁ᴊᴜᴅᴜʟ : {}".format(str(info["judul"]))
                                hasil += "\n🍁ᴀʟʙᴜᴍ : {}".format(str(info["album"]))
                                hasil += "\n\n🍁ʟɪɴᴋ : \n1. ɪᴍᴀɢᴇ : {}".format(str(data["gambar"]))
                                hasil += "\n\n🍁ʟɪɴᴋ : \n2. ᴍᴘ3 : {}".format(str(audio["mp3"]))
                                cl.sendImageWithURL(msg.to, str(data["gambar"]))
                                cl.sendMessage(msg.to, str(hasil))
                                cl.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                sendTextTemplate7(msg.to, "🍁sᴇᴀʀᴇᴢ ᴍᴘ3 sᴜᴋsᴇs..")
                            except Exception as error:
                            	sendTextTemplate(msg.to, "「 ʀᴇsᴜʟᴛ ᴇʀʀᴏʀ」\n" + str(error))
                        
                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                cl.sendMessage(msg.to, "🍁sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ...")
                                time.sleep(2)
                                sendTextTemplate(msg.to, "🍁ɪᴅ sᴍᴜʟᴇ : "+smule+"\n🍁ʟɪɴᴋ : "+links)
                                cl.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass
                                
                          
                        elif msg.text.lower().startswith("smule: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            channel = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0"
                                r = web.get("https://citldesign.herokuapp.com/downloadsmule={}".format(urllib.parse.quote(channel)))
                                data = r.text
                                data = json.loads(data)
                                for design in data["result"]:
                                    image = design["image"]
                                    url = design["url"]
                                cl.sendImageWithURL(msg.to, image)
                                cl.sendAudioWithURL(msg.to, url)
                                cl.sendVideoWithURL(msg.to, url)
                                
                        elif cmd.startswith("abi"):
                          if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            cl.sendImageWithURL(msg.to, image)                            
                                                                
                        elif cmd.startswith("getabi"):
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ","")
                                count = keyword.split("|")
                                search = str(count[0])
                                r = requests.get("http://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "ᴀʙɪ ɪᴍᴀɢᴇ ʟɪsᴛ\n"
                                    for aa in data["data"]["memes"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                    hasil += " "
                                    cl.sendMessage(msg.to,hasil)
                                    sendTextTemplate(msg.to,"🍁sɪʟᴀʜᴋᴀɴ ᴘɪʟɪʜ ᴋᴇɪɴɢɪɴᴀɴ:\n\n[ᴄᴇᴋ ᴀʙɪ]\nɢᴇᴛᴀʙɪ | ᴜʀᴜᴛᴀɴ\n\n[ᴄʀᴇᴀᴛᴇ ᴀʙɪ]\nᴀʙɪ ᴛᴇᴋs1|ᴛᴇᴋs2|ᴜʀᴜᴛᴀɴ")
                                if len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        gambar = data["data"]["memes"][num - 1]
                                        hasil = "{}".format(str(gambar["name"]))
                                        sendMention(msg.to, sender,"","\n🍁ғᴏᴛᴏ sᴇᴅᴀɴɢ ᴅɪ ᴘʀᴏssᴇs...")
                                        cl.sendMessage(msg.to,hasil)
                                        cl.sendImageWithURL(msg.to,gambar["url"])
                                    except Exception as e:
                                        sendTextTemplate(msg.to," "+str(e))
                        elif "meme" in text.lower():
          #                 if msg._from admin:
                                proses = text.split(" ")
                                keyword = text.replace(proses[0]+" ","")
                                query = keyword.split("|")
                                atas = query[0]
                                bawah = query[1]
                                r = requests.get("https://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                try:
                                    num = int(query[2])
                                    namamem = data["data"]["memes"][num - 1]
                                    meme = int(namamem["id"])
                                    api = pyimgflip.Imgflip(username='andyihsan', password='ihsan848')
                                    result = api.caption_image(meme, atas,bawah)
                                    sendTextTemplate4(msg.to, "🍁ғᴏᴛᴏ sᴇᴅᴀɴɢ ᴅɪᴘʀᴏssᴇs...")
                                    cl.sendImageWithURL(msg.to,result["url"])
                                except Exception as e:
                                    sendTextTemplate(msg.to," "+str(e)) 
                                        
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "🍁ɴᴀᴍᴇ: " + text[-2] + "\n"
                                user1 = "🍁ᴜsᴇʀɴᴀᴍᴇ: " + text[-1] + "\n"
                                followers = "🍁ғᴏʟʟᴏᴡᴇʀs: " + text[0] + "\n"
                                following = "🍁ғᴏʟʟᴏᴡɪɴɢ: " + text[2] + "\n"
                                post = "🍁ᴘᴏsᴛ: " + text[4] + "\n"
                                link = "🍁ʟɪɴᴋ: " + "https://www.instagram.com/" + instagram
                                detail = "========ɪɢ ɪɴғᴏ ========\n"
                                details = "\n========ɪɢ ɪɴғᴏ ========"
                                sendTextTemplate4(msg.to, detail + user + user1 + followers + following + post + link + details)
                                cl.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                sendTextTemplate(msg.to, str(njer))
                                
                        elif cmd.startswith("lihat "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            cct = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                try:
                                    ret_ = "「 ɪɴғᴏʀᴍᴀsɪ ᴄᴄᴛᴠ 」\n🍁ᴅᴀᴇʀᴀʜ "
                                    ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                    ret_ += "\n🍁ᴄᴄᴛᴠ ᴜᴘᴅᴀᴛᴇ ᴘᴇʀ 5 ᴍᴇɴɪᴛ"
                                    vid = soup.find('source')['src']
                                    ret = "🍁ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴡɪʟɪʏᴀʜ ʟᴀɪɴɴʏᴀ, ᴋᴇᴛɪᴋ ᴋᴏᴅᴇ ᴡɪʟᴀʏᴀʜ"
                                    sendTextTemplate7(to, ret_)
                                    cl.sendVideoWithURL(to, vid)
                                    sendTextTemplate7(to, ret)
                                except:
                                    sendTextTemplate(to, "🍁ᴅᴀᴛᴀ ᴄᴄᴛᴠ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!")
                                    
                        elif cmd.startswith("get-apk "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split("|")
                            search = str(cond[0])
                            with requests.session() as s:
                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                r = s.get("https://apkpure.com/id/search?q={}".format(str(search)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                data = soup.findAll('dl', attrs={'class':'search-dl'})
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "「 ᴘᴇɴᴄᴀʀɪᴀɴ ᴀᴘʟɪᴋᴀsɪ 」\n"
                                    for apk in data:
                                        num += 1
                                        link = "https://apkpure.com"+apk.find('a')['href']
                                        title = apk.find('a')['title']
                                        ret_ += "\n {}. {}".format(str(num), str(title))
                                    ret_ += "\n\n ᴛᴏᴛᴀʟ {} ʀᴇsᴜʟᴛ".format(str(len(data)))
                                    ret = "🍁sᴇʟᴀɴᴊᴜᴛɴʏᴀ ᴋᴇᴛɪᴋ:\n🍁ɢᴇᴛ-ᴀᴘᴋ {} | ᴀɴɢᴋᴀ".format(str(search))
                                    cl.sendMessage(to, str(ret_))
                                    cl.sendMessage(to, str(ret))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        apk = data[num - 1]
                                        with requests.session() as s:
                                            s.headers['user-agent'] = random.choice(settings["userAgent"])
                                            r = s.get("https://apkpure.com{}/download?from=details".format(str(apk.find('a')['href'])))
                                            soup = BeautifulSoup(r.content, 'html5lib')
                                            data = soup.findAll('div', attrs={'class':'fast-download-box'})
                                            for down in data:
                                                load = down.select("a[href*=https://download.apkpure.com/]")[0]
                                                file = load['href']
                                                ret_ = "🍁ғɪʟᴇ ɪɴғᴏ :\n"+down.find('span', attrs={'class':'file'}).text
                                                with requests.session() as web:
                                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                    r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(urllib.parse.quote(file)))
                                                    data = r.text
                                                    data = json.loads(data)
                                                    ret_ += "\n🍁ʟɪɴᴋ ᴅᴏᴇɴʟᴏᴀᴅ :\n"+data["data"]["url"]
                                                sendTextTemplate7(to, str(ret_))
                                                
                        elif cmd.startswith("get-mimpi "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            mimpi = msg.text.replace(sep[0] + " ","")  
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for anu in soup.find_all('i'):
                                    ret_ = anu.get_text()
                                    sendTextTemplate4(msg.to,ret_)
                                    
                        elif text.lower() == 'top kaskus':
                           if msg._from in admin:
                               r = requests.get("https://api.bayyu.net/kaskus-hotthread/?apikey=c28c944199384f191335f1f8924414fa839350d&page=2")
                               data=r.text
                               data=json.loads(data)                                                                                                      
                               if data["hot_threads"] != []:
                                   no = 0
                                   hasil = "「 ᴋᴀsᴋᴜs sᴇᴀʀᴄʜ」\n"
                                   for news in data["hot_threads"]:
                                        no += 1                  
                                        hasil += "\n" + str(no) + ". 🍁ᴊᴜᴅᴜʟ : " + str(news["title"]) + "\n 🍁ᴅᴇsᴋʀɪᴘsɪ : " + str(news["detail"]) + "\n 🍁ʟɪɴᴋ: " + str(news["link"]) + "\n"
                                        hasil += "\n"
                                   sendTextTemplate4(msg.to, str(hasil))
                                                           
                                                                                    
                        elif cmd.startswith("abimp4: "):
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "🍁ᴊᴜᴅᴜʟ [ " + vid.title + " ]"
                                    author = '\n\n🍁ᴀᴜᴛʜᴏʀ : ' + str(vid.author)
                                    durasi = '\n🍁ᴅᴜʀᴀᴛɪᴏɴ : ' + str(vid.duration)
                                    suka = '\n🍁ʟɪᴋᴇs : ' + str(vid.likes)
                                    rating = '\n🍁ʀᴀᴛɪɴɢ : ' + str(vid.rating)
                                    deskripsi = '\n🍁ᴅᴇsᴋʀɪᴘsɪ : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                sendTextTemplate7(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                sendTextTemplate(msg.to,str(e))
                                
                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        cl.sendImageWithURL(msg.to, str(food["url"]))
                        
                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            sendTextTemplate4(msg.to,"🍁ɪɴғᴏʀᴍᴀsɪ™\n\n"+"🍁ᴅᴀᴛᴇ ᴏғ ʙɪʀᴛ : "+lahir+"\n🍁ᴀɢᴇ : "+usia+"\n🍁ᴜʟᴛᴀʜ : "+ultah+"\n🍁ᴢᴏᴅɪᴀᴋ : "+zodiak)
                            
                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    abi = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 ᴄʟᴏɴᴇ ᴘʀᴏғɪʟ 」\n🍁ᴛᴀʀɢᴇᴛ ɴʏᴀ "
                                    ret_ = "🍁ᴅᴏɴᴇ ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ"
                                    ry = str(abi.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':abi.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    sendTextTemplate(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    sendTextTemplate(msg.to, "🍁ɢᴀɢᴀʟ ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ")
                            
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  lineProfile.displayName = str(myProfile["displayName"])
                                  lineProfile.statusMessage = str(myProfile["statusMessage"])
                                  lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                  cl.updateProfile(lineProfile)
                                  sendTextTemplate(msg.to, sender, "「 ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟ 」 \n🍁ʙᴇʀʜᴀsɪʟ ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟ")
                              except:
                                  sendTextTemplate(msg.to, "🍁ɢᴀɢᴀʟ ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟ")
                                  
                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate(msg.to,"🍁sᴘᴀᴍᴛᴀɢ ᴄʜᴀɴɢɢᴇ ᴛᴏ " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate(msg.to,"🍁ᴛᴏᴛᴀʟ sᴘᴀᴍᴄᴀʟʟ ᴅɪ ʀᴜʙᴀʜ ᴊᴀᴅɪ " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        sendTextTemplate(msg.to,"🍁ᴊᴜᴍʟᴀʜ ᴍᴇʟᴇʙɪʜɪ 1000")
                        
                        elif cmd == "vcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                sendTextTemplate(msg.to, "🍁ʙᴇʀʜᴀsɪʟ ɴᴀɪᴋɪɴ {} ᴜɴᴅᴀɴɢᴀɴ ᴠɪᴅɪᴏ ɢʀᴏᴜᴘ".format(str(wait["limit"])))
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                        
                        elif cmd == "rcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                sentTextTemplate(msg.to, "🍁ʙᴇʀʜᴀsɪʟ ɴᴀɪᴋɪɴ {} ᴜɴᴅᴀɴɢᴀɴ ᴄᴀʟʟ ɢʀᴏᴜᴘ".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    sendTextTemplate(msg.to,"🍁ᴊᴜᴍʟᴀʜ ᴍᴇʟᴇʙɪʜɪ ʙᴀᴛᴀs")
                                    
                        elif cmd.startswith("spaminvid"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    dan = text.split("|")
                                    userid = dan[1]
                                    namagrup = dan[2]
                                    jumlah = int(dan[3])
                                    grups = cl.groups
                                    tgb = cl.findContactsByUserid(userid)
                                    cl.findAndAddContactsByUserid(userid)
                                    if jumlah <= 1000:
                                        for var in range(0,jumlah):
                                            try:
                                                cl.createGroup(str(namagrup), [tgb.mid])
                                                for i in grups:
                                                	grup = cl.getGroup(i)
                                                	if grup.name == namagrup:
                                                	    cl.inviteIntoGroup(grup.id, [tgb.mid])
                                                	    cl.leaveGroup(grup.id)
                                                	    sendTextTemplate7(to,"@! ᴅᴏɴᴇ sᴘᴀᴍ ɢʀᴏᴜᴘ!\n\n🍁ᴋᴏʀʙᴀɴ: @!\n🍁ᴊᴜᴍʟᴀʜ: {}\n🍁ɴᴀᴍᴀ ɢʀᴏᴜᴘ: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      sendTextTemplate(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      sendTextTemplate(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  sendTextTemplate(msg.to, "http://line.me/ti/p/~" + msgs)
                                  sendTextTemplate(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "🍁ᴡᴇʟᴄᴏᴍᴇ ᴏɴ"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "🍁ᴡᴇʟᴄᴏᴍᴇ ᴏɴ\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "「ᴅɪᴀᴋᴛɪғᴋᴀɴ」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🍁ᴡᴇʟᴄᴏᴍᴇ ᴏғғ\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "🍁ᴡᴇʟᴄᴏᴍᴇ ᴏғғ"
                                    sendTextTemplate(msg.to, "「ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ」\n" + msgs)

                        elif 'Leave ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Leave ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "🍁Leave ᴏɴ"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "🍁Leave ᴏɴ\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "「ᴅɪᴀᴋᴛɪғᴋᴀɴ」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🍁Leave ᴏғғ\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "🍁Leave ᴏғғ"
                                    sendTextTemplate(msg.to, "「ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ」\n" + msgs)

                        elif 'Pqr ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Pqr ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = "🍁ᴘʀᴏᴜʀʟ ʜᴀs ʙᴇᴇɴ ᴀᴋᴛɪғ"
                                  else:
                                       protect["pqr"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "🍁ᴘʀᴏᴜʀʟ ʜᴀs ʙᴇᴇɴ ᴀᴋᴛɪғ\n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "ᴀᴋᴛɪғ\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🍁ᴘʀᴏᴜʀʟ ʜᴀs ʙᴇᴇɴ ɴᴏɴᴀᴋᴛɪғ\n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "🍁ᴘʀᴏᴜʀʟ ʜᴀs ʙᴇᴇɴ ɴᴏɴᴀᴋᴛɪғ"
                                    sendTextTemplate(msg.to, "ɴᴏɴᴀᴋᴛɪғ\n\n" + msgs)

                        elif 'Protect ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in protect["protect"]:
                                       msgs = "🍁ᴘʀᴏ ʜᴀs ʙᴇᴇɴ ᴀᴋᴛɪғ"
                                  else:
                                       protect["protect"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "🍁ᴘʀᴏ ᴀᴋᴛɪғ\n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "ᴀᴋᴛɪғ\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🍁ᴘʀᴏ ʜᴀs ʙᴇᴇɴ ɴᴏɴᴀᴋᴛɪғ\n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "🍁ᴘʀᴏ ʜᴀs ʙᴇᴇɴ ɴᴏɴᴀᴋᴛɪғ"
                                    sendTextTemplate(msg.to, "ɴᴏɴᴀᴋᴛɪғ\n\n" + msgs)

                        elif 'Proall ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Proall ','')
                              if spl == 'on':
                                  if msg.to in protect["proall"]:
                                       msgs = "🍁ᴘʀᴏᴛᴇᴄᴛ sᴜᴅᴀʜ ᴀᴋᴛɪғ sᴇᴍᴜᴀ"
                                  else:
                                       protect["proall"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "🍁ᴘʀᴏᴛᴇᴄᴛ sᴜᴅᴀʜ ᴀᴋᴛɪғ sᴇᴍᴜᴀ\n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "ᴀᴋᴛɪғ \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🍁ᴘʀᴏᴛᴇᴄᴛ ᴅɪ ᴏғғ ɪɴ sᴇᴍᴜᴀ\n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "🍁ᴘʀᴏᴛᴇᴄᴛ sᴜᴅᴀʜ  ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ sᴅᴍᴜᴀ"
                                    sendTextTemplate(msg.to, "ɴᴏɴᴀᴋᴛɪғ\n\n" + msgs)

                        elif 'Pcancel ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Pcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "🍁ᴘʀᴏᴄᴀɴ ʜᴀs ʙᴇᴇɴ ᴀᴋᴛɪғ "
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "🍁ᴘʀᴏᴄᴀɴ ʜᴀs ʙᴇᴇɴ ᴀᴋᴛɪғ\n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🍁ᴘʀᴏᴄᴀɴ ʜᴀs ʙᴇᴇɴ ɴᴏɴᴀᴋᴛɪғ\n\n🍁ᴅɪ ɢʀᴏᴜᴘ: " +str(ginfo.name)
                                    else:
                                         msgs = "🍁ᴘʀᴏᴄᴀɴ ʜᴀs ʙᴇᴇɴ ɴᴏɴᴀᴋᴛɪғ"
                                    sendTextTemplate(msg.to, "ɴᴏɴᴀᴋᴛɪғ\n\n" + msgs)

                        elif 'Pinvite ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Pinvite ','')
                              if spl == 'on':
                                  if msg.to in protect["pinv"]:
                                       msgs = "🍁ᴘʀᴏɪɴᴠ ʜᴀs ʙᴇᴇɴ ᴀᴋᴛɪғ"
                                  else:
                                       protect["pinv"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "🍁ᴘʀᴏɪɴᴠ ᴀᴋᴛɪғ\n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "ᴀᴋᴛɪғ \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🍁ᴘʀᴏɪɴᴠ ɴᴏɴᴀᴋᴛɪғ\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "🍁ᴘʀᴏɪɴᴠ ʜᴀs ʙᴇᴇɴ ɴᴏɴᴀᴋᴛɪғ"
                                    sendTextTemplate(msg.to, "ɴᴏɴᴀᴋᴛɪғ\n\n" + msgs)

                        elif 'Js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protect["antijs"]:
                                       msgs = "🍁ᴊs ʜᴀs ʙᴇᴇɴ ᴀᴋᴛɪғ"
                                  else:
                                       protect["antijs"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "🍁ᴊs ᴏɴ \n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "ᴀᴋᴛɪғ\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🍁ᴊs ᴏғғ\n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "🍁ᴊs ᴏғғ "
                                    sendTextTemplate(msg.to, "ɴᴏɴᴀᴋᴛɪғ\n" + msgs)
                                    
                        elif 'Ghost ' in msg.text:
                          if msg._from in admin:
                             spl = msg.text.replace('Ghost ','')
                             if spl == 'on':
                                 if msg.to in ghost:
                                      msgs = "🍁ɢʜᴏsᴛ ᴏɴ"
                                 else:
                                        ghost.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "🍁ɢʜᴏsᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                 sendTextTemplate(msg.to, "sᴛᴀᴛᴜs:\n" + msgs)
                             elif spl == 'off':
                                   if msg.to in ghost:
                                        ghost.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "🍁ɢʜᴏsᴛ ᴅɪ ᴍᴀᴛɪᴋᴀɴ\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                   else:
                                        msgs = "🍁ɢʜᴏsᴛ sᴜᴅᴀʜ ᴍᴀᴛɪ sᴇᴍᴜᴀ"
                                   sendTextTemplate(msg.to, "sᴛᴀᴛᴜs:\n" + msgs)

                        elif 'Allpro ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = ""
                                  else:
                                       protect["pqr"].append(msg.to)
                                  if msg.to in protect["protect"]:
                                      msgs = ""
                                  else:
                                      protect["protect"].append(msg.to)
                                  if msg.to in protect["pinv"]:
                                      msgs = ""
                                  else:
                                      protect["pinv"].append(msg.to)
                                  if msg.to in protect["antijs"]:
                                      msgs = ""
                                  else:
                                      protect["antijs"].append(msg.to)
                                  if msg.to in ghost:
                                      msgs = ""
                                  else:
                                      ghost.append(msg.to)
                                  if msg.to in protect["proall"]:
                                      msgs = ""
                                  else:
                                      protect["proall"].append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "🍁sᴇᴍᴜᴀ ᴘʀᴏᴛᴇᴄᴛ ᴏɴ \n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "🍁sᴜᴄᴄᴇs\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "ᴀᴋᴛɪғ\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🍁sᴇᴍᴜᴀ ᴘʀᴏᴛᴇᴄᴛ ᴏғғ\n\n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🍁sᴇᴍᴜᴀ ᴘʀᴏᴛᴇᴄᴛ ᴅɪ ᴍᴀᴛɪᴋᴀɴ \n🍁ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    sendTextTemplate(msg.to, "ɴᴏɴᴀᴋᴛɪғ\n" + msgs)

#===========KICKOUT============#       
                        elif ("apalu " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Vc " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass
                                           
                        elif ("!Bubar" in msg.text):
                            if msg._from in admin:
                             if msg.toType == 2:
                                 print ("[ 19 ] KICK ALL MEMBER")
                                 _name = msg.text.replace("!Bubar","")                                 
                                 gs = cl.getGroup(msg.to)
                                 gs = kk.getGroup(msg.to)
                                 gs = kc.getGroup(msg.to)
                                 gs = kb.getGroup(msg.to)
                                 gs = ke.getGroup(msg.to)
                                 gs = sw.getGroup(msg.to)
                                 gs = bi.getGroup(msg.to)
                                 cl.sendMessage(msg.to,"「 Papay Sayang 😚😚😚」")
                                 cl.sendMessage(msg.to,"「 sᴏʀʀʏ ʀᴏᴏᴍ ᴋᴀᴍɪ sɪᴛᴀ ʙʏᴇ ᴛᴇᴀᴍ Cannibal ᴋɪʟʟᴇʀ」")
                                 targets = []
                                 for g in gs.members:
                                     if _name in g.displayName:
                                         targets.append(g.mid)
                                 if targets == []:
                                     sendTextTemplate(msg.to,"🍁ʟɪᴍɪᴛ ʙᴏss")
                                 else:
                                     for target in targets:
                                       if not target in Bots:
                                          if not target in admin:
                                             if not target in staff:
                                               try:
                                                   abi= [cl]
                                                   kicker=random.choice(abi)
                                                   kicker.kickoutFromGroup(msg.to,[target])
                                                   print (msg.to,[g.mid])
                                               except Exception as error:
                                                   cl.sendMessage(msg.to, str(error))

                        elif text.lower() == '!bajingan':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                           	if msg.toType == 2:
                                  ginfo = cl.getGroup(msg.to)
                              #    cl.sendMessage(msg.to, "ᴘʀᴏsᴇs ᴄʟᴇᴀɴsᴇ....")
                              #    cl.sendMessage(msg.to, "「 ᴏʟᴇɴɢ 」\nᴍᴇᴍʙᴇʀ : " +str(len(ginfo.members)) + " \nғᴜᴄᴋ ʏᴏᴜ...")
                                  G = cl.getGroup(msg.to)
                                  G.preventedJoinByTicket = False
                                  cl.updateGroup(G)
                                  Ticket = cl.reissueGroupTicket(msg.to)
                                  ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  bi.acceptGroupInvitationByTicket(msg.to,Ticket)                                 
                                  _name = text.lower().replace('ᴏʟᴇɴɢ','')
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
                                  gs = kc.getGroup(msg.to)
                                  gs = kb.getGroup(msg.to)
                                  gs = ke.getGroup(msg.to)
                                  gs = sw.getGroup(msg.to)
                                  gs = bi.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                  	if _name in g.displayName:
                                  	   targets.append(g.mid)
                                  if targets == []:
                                  	sendTextTemplate(msg.to, "🍁ɴᴏᴛʜɪɴɢ ᴍᴇᴍʙᴇʀ")
                                  else:
                                       for target in targets:
                                        if not target in Bots:
                                           if not target in admin:
                                              if not target in staff:
                                                 try:
                                                      random.choice(Bots).kickoutFromGroup(msg.to, [target])
                                                      G = cl.getGroup(msg.to)
                                                      G.preventedJoinByTicket = True
                                                      cl.updateGroup(G)
                                                      G.preventedJoinByTicket(G)
                                                      cl.updateGroup(G)
                                                 except:
                                                      pass
                                                      
                        elif text.lower() == '.killban':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              gid = cl.getGroupIdsJoined()
                              group = cl.getGroup(to)
                              gMembMids = [contact.mid for contact in group.members]
                              ban_list = []
                              for tag in wait["blacklist"]:
                                    ban_list += filter(lambda str: str == tag, gMembMids)
                              if ban_list == []:
                                    sendTextTemplate(to, "🍁ʟɪᴍɪᴛ ʙᴏss")
                                    return
                              else:
                                    for i in gid:
                                    	for jj in ban_list:
                                         if jj in admin:
                                                pass
                                         elif jj in staff:
                                                pass
                                         elif jj in Bots:
                                                pass
                                         else:
                                                cl.kickoutFromGroup(i, [jj])
                                      
                           elif "Invite " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass 
#===========ADMIN ADD============
                        elif ("Staff:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.append(target)
                                           sendTextTemplate(msg.to,"🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴛᴀғғ")
                                       except:
                                           pass

                        elif ("Bot:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.append(target)
                                           sendTextTemplate(msg.to,"🍁sᴜᴄᴄᴇs ᴀᴅᴅʙᴏᴛ")
                                       except:
                                           pass

                        elif ("Adminexpl:on " in msg.text):
                            if msg._from in owner or msg_from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.remove(target)
                                           sendTextTemplate(msg.to,"🍁sᴜᴄᴄᴇs ᴇxᴘᴇʟ ᴀᴅᴍɪɴ")
                                       except:
                                           pass

                        elif ("Staffexpl:on " in msg.text):
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.remove(target)
                                           sendTextTemplate(msg.to,"🍁sᴜᴄᴄᴇs ᴇxᴘᴇʟ sᴛᴀғғ")
                                       except:
                                           pass

                        elif ("Botexpl:on " in msg.text):
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           sendTextTemplate(msg.to,"🍁sᴜᴄᴄᴇs ᴇxᴘᴇʟ ʙᴏᴛs")
                                       except:
                                           pass

#==================================#
                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in owner:
                                wait["addadmin"] = True
                                sendTextTemplate(msg.to,"🍁sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛɴʏᴀ...")

                        elif cmd == "adminexpl:on" or text.lower() == 'adminexpl:on':
                            if msg._from in owner:
                                wait["delladmin"] = True
                                sendTextTemplate(msg.to,"🍁sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛɴʏᴀ...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addstaff"] = True
                                sendTextTemplate(msg.to,"🍁sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛɴʏᴀ...")

                        elif cmd == "staffexpl:on" or text.lower() == 'staffexpl:on':
                            if msg._from in owner or msg._from in admin:
                                wait["dellstaff"] = True
                                sendTextTemplate(msg.to,"🍁sᴇɴᴅ ᴄᴏɴᴛᴀᴄʏɴʏᴀ...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addbots"] = True
                                sendTextTemplate(msg.to,"🍁sᴇɴᴅ ᴋᴏɴᴛᴀᴋɴʏᴀ...")

                        elif cmd == "botexpl:on" or text.lower() == 'botexpl:on':
                            if msg._from in owner:
                                wait["dellbots"] = True
                                sendTextTemplate(msg.to,"🍁ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛɴʏᴀ...")

                        elif cmd == "fresh" or text.lower() == 'refresh':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                sendTextTemplate(msg.to,"🍁ᴡᴀɪᴛ...")
                                sendTextTemplate(msg.to,"🍁ʀᴇғʀᴇsʜ ᴅᴏɴᴇ...")

                        elif cmd == "admin" or text.lower() == 'contact admin':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    sendTextTemplate(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "staff" or text.lower() == 'contact staff':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    sendTextTemplate(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                     
                        elif cmd == "spaminvite on" or text.lower == 'spaminvite on':
                            if msg._from in admin:
                                settings["SpamInvite"] = True
                                sendTextTemplate(msg.to, "🍁sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ɢʀᴏᴜᴘ..")
                                
                        elif cmd == "spaminvite off" or text.lower() == 'spaminvite off':
                            if msg._from in admin:
                                settings["Spaminvite"] = False
                                sendTextTemplate(msg.to, "🍁sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ɢʀᴏᴜᴘ ᴏғғ..")
                                
#===========COMMAND ON OFF============#                                         
                        elif cmd == "autojoin on":
                            if msg._from in owner:
                                wait["autoJoin"] = True
                                sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀᴜᴛᴏ ᴊᴏɪɴ")
                        elif cmd == "autojoin off":
                            if msg._from in owner:	
                                wait["autoJoin"] = False
                                sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴀᴜᴛᴏ ᴊᴏɪɴ")
                                
                        elif cmd == "autoblock on":
                           if msg._from in owner:
                                settings["autoBlock"] = True
                                sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀᴜᴛᴏ ʙʟᴏᴄᴋ")
                        elif cmd == "autoblock off":    
                            if msg._from in owner: 	
                                settings["autoBlock"] = False
                                sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴀᴜᴛᴏ ʙʟᴏᴄᴋ")
                                
                        elif cmd == "autoleave on":
                            if msg._from in owner:	
                                wait["autoLeave"] = True
                                sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ")
                        elif cmd == "autoleave off":
                            if msg._from in owner:
                                wait["autoLeave"] = False
                                sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ")
                                
                        elif cmd == "autojointicket on":
                        	if msg._from in owner:
                                 wait["autoJoinTicket"] = True
                                 sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀᴜᴛᴏ ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ")
                        elif cmd == "autojointicket off":
                           if msg._from in owner:
                                 wait["autoJoinTicket"] = False
                                 sendTextTemplate(to, "🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴀᴜᴛᴏ ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ")
                                 
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = True
                                sendTextTemplate(msg.to,"🍁ɴᴏᴛᴀɢ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["MentionKick"] = False
                                sendTextTemplate(msg.to,"🍁ɴᴏᴛᴀɢ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = True
                                sendTextTemplate(msg.to,"🍁ᴅᴇᴛᴇᴋsɪ ᴄᴏɴᴛᴀᴄᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = False
                                sendTextTemplate(msg.to,"🍁ᴅᴇᴛᴇᴋsɪ ᴄᴏɴᴛᴀᴄᴛ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = True
                                sendTextTemplate(msg.to,"🍁ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = False
                                sendTextTemplate(msg.to,"🍁ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "responpm on" or text.lower() == 'responpm on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoResponPm"] = True
                                sendTextTemplate(msg.to,"🍁ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴍ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
                        elif cmd == "responpm off" or text.lower() == 'responpm off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoResponPm"] = False
                                sendTextTemplate(msg.to,"🍁ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴍ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = True
                                sendTextTemplate(msg.to,"🍁ᴀᴜᴛᴏ ᴀᴅᴅ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = False
                                sendTextTemplate(msg.to,"🍁ᴀᴜᴛᴏ ᴀᴅᴅ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "autoread on" or text.lower() == 'autoread on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["autoRead"] = True
                                sendTextTemplate(msg.to,"🍁ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
                        elif cmd == "autoread off" or text.lower() == 'autoread off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["autoRead"] = False
                                sendTextTemplate(msg.to,"🍁ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = True
                                sendTextTemplate(msg.to,"🍁ᴅᴇᴛᴇᴋsɪ sᴛɪᴄᴋᴇʀ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = False
                                sendTextTemplate(msg.to,"🍁ᴅᴇᴛᴇᴋsɪ sᴛɪᴄᴋᴇʀ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
                                
                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if settings["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["unsendMessage"] = True
                                sendTextTemplate(msg.to,"🍁ᴅᴇᴛᴇᴄᴛ ᴜɴsᴇɴᴅ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if settings["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["unsendMessage"] = False
                                sendTextTemplate(msg.to,"🍁ᴅᴇᴛᴇᴄᴛ ᴜɴsᴇɴᴅ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
                                
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendTextTemplate(msg.to, "「 sᴛᴀᴛᴜs ɪɴᴠɪᴛᴇ 」\n🍁sᴇɴᴅ ᴀ ᴄᴏɴᴛᴀᴄᴛ ɪɴᴠɪᴛᴇ,\nʟғ ᴅᴏɴᴇ -> ɪɴᴠɪᴛᴇ ᴏғғ")
                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendTextTemplate(msg.to, "「 sᴛᴀᴛᴜs ɪɴᴠɪᴛᴇ 」 \n🍁ɪɴᴠɪᴛᴇ ʜᴀs ʙᴀɴ ᴅɪsᴀʙʟᴇᴅ")
                                
                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["Timeline"] = True
                                sendTextTemplate(msg.to, "「 sᴛᴀᴛᴜs ᴛɪᴍᴇʟɪɴᴇ 」\n🍁sᴇɴᴅ ᴀ ᴘᴏsᴛ,\nʟғ ᴅᴏɴᴇ -> ᴛɪᴍᴇʟɪɴᴇ ᴏғғ")
                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["Timeline"] = False
                                sendTextTemplate(msg.to, "「 sᴛᴀᴛᴜs ᴛɪᴍᴇʟɪɴᴇ 」 \n🍁ᴅᴇᴛᴇᴋsɪ ᴛɪᴍᴇʟɪɴᴇ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

#===========COMMAND BLACKLIST============#
                        elif cmd == "ban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    sendTextTemplate2(msg.to,"🍁ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴏʀᴀɴɢ")
                                else:
                                    for target in targets:
                                         if target not in wait["selfbot"] or target not in Bots:
                                            try:
                                                wait["blacklist"][target] = True
                                                sendTextTemplate2(msg.to,"🍁ᴀɴᴅᴀ ʙᴜʀᴏɴᴀɴ")
                                            except:
                                                pass
                                                
                        elif cmd == "unban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    sendTextTemplate2(msg.to,"🍁ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴏʀᴀɴɢ")
                                else:
                                    for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                sendTextTemplate2(msg.to,"🍁ᴀɴᴅᴀ ʙᴜʀᴏɴᴀɴ")
                                            except:
                                                pass
                        elif ("Talkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           sendTextTemplate2(msg.to,"🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜ ʙʟᴀᴄᴋʟɪsᴛ")
                                       except:
                                           pass

                        elif ("Untalkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           sendTextTemplate2(msg.to,"🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs ʙʟᴀᴄᴋʟɪsᴛ")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkwblacklist"] = True
                                sendTextTemplate2(msg.to,"🍁sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkdblacklist"] = True
                                sendTextTemplate2(msg.to,"🍁sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["blacklist"][target] = True
                                           sendTextTemplate2(msg.to,"🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜ ʙʟᴀᴄᴋʟɪsᴛ")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sendTextTemplate2(msg.to,"🍁ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs ʙʟᴀᴄᴋʟɪsᴛ")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["wblacklist"] = True
                                sendTextTemplate2(msg.to,"🍁sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["dblacklist"] = True
                                sendTextTemplate2(msg.to,"🍁sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate2(msg.to,"🍁 ɴᴏᴛʜɪɴɢ ʙʟᴀᴄᴋʟɪsᴛ")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate2(msg.to,"ʙʟᴀᴄᴋʟɪsᴛ\n\n"+ma+"\n %s ᴜsᴇʀ" %(str(len(wait["blacklist"]))))
                                

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["Talkblacklist"] == {}:
                                sendTextTemplate2(msg.to,"ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴛᴀʟᴋʙᴀɴʟɪsᴛ ᴜsᴇʀ")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate2(msg.to," ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ\n\n"+ma+"\nᴛᴏᴛᴀʟ「%s」ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "bl" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["blacklist"] == {}:
                                    sendTextTemplate2(msg.to,"🍁 ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʟᴀᴄᴋʟɪsᴛ")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        sendTextTemplate2(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif text.lower() == 'cban':
                            if msg._from in owner or msg._from in admin:
                                wait["blacklist"] = {}
                                ragets = cl.getContacts(wait["blacklist"])
                                mc = "「%i」" % len(ragets)
                                sendTextTemplate2(msg.to,"🍁 ᴅᴏɴᴇ ᴅᴇʟᴇᴛᴇ ʙᴜʀᴏɴᴀɴ " +mc)
                                
                     #   elif text.lower() == 'payment':
                      #         cl.sendMessage(msg.to, "ᴘᴀʏᴍᴇɴᴛ ᴠɪᴀ ʙᴀɴᴋ\nɴᴏ ʀᴇᴋ : 481901020711531\nᴀᴛᴀs ɴᴀᴍᴀ : muhazir\nʙᴀɴᴋ ʙʀɪ\n\nᴠɪᴀ ᴘᴜʟsᴀ\n08992906209")
#===========COMMAND SET============#
                        elif msg.contentType == 16:
                           if wait["Timeline"] == True:
                              msg.contentType = 0
                              msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                              sendTextTemplate(msg.to, "ʟɪᴋᴇ sᴜᴄᴄᴇs...")
                              
                        elif 'Spesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Spesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "ɢᴀɢᴀʟ ᴍᴇɴɢɢᴀɴᴛɪ ᴘᴇsᴀɴ ᴍsɢ")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate(msg.to, "「ᴘᴇsᴀɴ ᴍsɢ」\nᴘᴇsᴀɴ ᴍsɢ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ :\n\n「{}」".format(str(spl)))

                        elif 'Swelcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Swelcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "ɢᴀɢᴀʟ ᴍᴇɴɢɢᴀɴᴛɪ ᴡᴇʟᴄᴏᴍᴇ ᴍsɢ")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate(msg.to, "「ᴡᴇʟᴄᴏɴᴇ ᴍsɢ」\nᴡᴇʟᴄᴏᴍᴇ ᴍsɢ ᴅɪɢᴀɴᴛɪ ᴊᴀᴅɪ :\n\n「{}」".format(str(spl)))

                        elif 'Srespon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Srespon: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "ɢᴀɢᴀʟ ᴍᴇɴɢɢᴀɴᴛɪ ʀᴇsᴘᴏɴ ᴍsɢ")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate(msg.to, "「ʀᴇsᴘᴏɴ ᴍsɢ」\nʀᴇsᴘᴏɴ ᴍsɢ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ :\n\n「{}」".format(str(spl)))

                        elif 'Sspam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Sspam: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "ɢᴀɢᴀʟ ᴍᴇɴɢɢᴀɴᴛɪ sᴘᴀᴍ ᴍsɢ")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  sendTextTemplate(msg.to, "「sᴘᴀᴍ ᴍsɢ」\nsᴘᴀᴍ ᴍsɢ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ :\n\n「{}」".format(str(spl)))

                        elif 'Ssider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ssider: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "ɢᴀɢᴀʟ ᴍᴇɴɢɢᴀɴᴛɪ sɪᴅᴇʀ ᴍsɢ")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate(msg.to, "「sɪᴅᴇʀ ᴍsɢ」\nsɪᴅᴇʀ ᴍsɢ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cpesan":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「ᴘᴇsᴀɴ ᴍsɢ」\nᴘᴇᴅᴀɴ ᴍsɢ ᴍᴜ :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cwelcome":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「ᴡᴇʟᴄᴏᴍᴇ ᴍsɢ」\nᴡᴇʟᴄᴏᴍᴇ ᴍsɢ ᴍᴜ :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "crespon":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「ʀᴇsᴘᴏɴ ᴍsɢ」\nʀᴇsᴘᴏɴ ᴍsɢ ᴍᴜ :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cspam":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「sᴘᴀᴍ ᴍsɢ」\nsᴘᴀᴍ ᴍsɢ ᴍᴜ :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "csider":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「sɪᴅᴇʀ ᴍsɢ」\nsɪᴅᴇʀ ᴍsɢ ᴍᴜ :\n\n「 " + str(wait["mention"]) + " 」")
#=================================[ STAMINA BOT ]================================================                               
                        elif cmd == "cek":
                            if msg._from in admin or msg._from in owner:
                               try:cl.inviteIntoGroup(to, [mid]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, [mid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               sendTextTemplate(to, "🍁 sᴛᴀᴛᴜs 🍁:\n\n⏩ ᴋɪᴄᴋ : {} \n⏩ ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                                                                    
#=============================[ JOIN TICKET ]============+=============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     sendTextTemplate(msg.to, " 🍁 ʟᴇsᴛ ɢᴏ : %s" % str(group.name))
                                     group1 = cl.findGroupByTicket(ticket_id)
                                                                        
    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
