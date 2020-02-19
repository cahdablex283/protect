#CANNIBAL===Version SB
# sᴄʀɪᴘᴇ CANNIBAL KILLER ᴜᴘᴅᴀᴛᴇ 2-11-2019
# ᴛᴇᴀᴍ CANNIBAL KILLER
#ᴊᴀɴɢᴀɴ sᴏᴋ ʙɪsᴀ ɴɢᴇᴅɪᴛ ᴋʟᴏ ɢᴋ ʙɪsᴀ ɴɢᴇᴅɪᴛ
#ᴄʀᴇᴀᴛᴏʀ ʙʏᴇ CANNIBAL
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
from zalgo_text import zalgo
from threading import Thread,Event
#import requests,uvloop
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
#loop = uvloop.new_event_loop()
#==============================================================================#
botStart = time.time()
msg_dict = {}
msg_dict1 = {}
#==============[ token 1 ]==============#
cl = LINE("")
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))

ki = LINE("@gmail.com","password")
ki.log("Auth Token : " + str(ki.authToken))
ki.log("Timeline Token : " + str(ki.tl.channelAccessToken))

kk = LINE("@gmail.com","password")
kk.log("Auth Token : " + str(kk.authToken))
kk.log("Timeline Token : " + str(kk.tl.channelAccessToken))

kc = LINE("@gmail.com","password")
kc.log("Auth Token : " + str(kc.authToken))
kc.log("Timeline Token : " + str(kc.tl.channelAccessToken))

ko = LINE("@gmail.com","password")
ko.log("Auth Token : " + str(ko.authToken))
ko.log("Timeline Token : " + str(ko.tl.channelAccessToken))

jk = LINE("@gmail.com","password")
jk.log("Auth Token : " + str(jk.authToken))
jk.log("Timeline Token : " + str(jk.tl.channelAccessToken))

sw = LINE("@gmail.com","password")
sw.log("Auth Token : " + str(sw.authToken))
sw.log("Timeline Token : " + str(sw.tl.channelAccessToken))
#==============[●●●●●●]==============#
print ("=========== ʟᴏɢɪɴ sᴜᴄᴄᴇs ==========")

oepoll = OEPoll(cl)

mid = cl.profile.mid
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ko.getProfile().mid
Emid = jk.getProfile().mid
Zmid = sw.getProfile().mid
#===========================================================================================
KAC = [cl,ki,kk,kc,ko,jk]
ABC = [cl,ki,kk,kc,ko,jk]
GHOST = [sw]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid]
creator = ["ucc10b6f6bc11284e0aa9b2a2fb16b70c"]
owner = ["ucc10b6f6bc11284e0aa9b2a2fb16b70c"]
admin = ["ucc10b6f6bc11284e0aa9b2a2fb16b70c"]
staff = ["ucc10b6f6bc11284e0aa9b2a2fb16b70c"]
Oleng = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = ko.getProfile().displayName
responsename5 = jk.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "comment":"╭──────────────────╮\n├🔹ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴀᴋᴀᴋ  \n╰──────────────────╯\n╭──────────────────\n├🔹ʀᴇᴀᴅʏ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n├🔹ʀᴏᴏᴍ sᴍᴜʟᴇ / ᴇᴠᴇɴᴛ \n├🔹ʀᴇᴀᴅʏ sʙ ᴏɴʟʏ \n├🔹sʙ ᴏɴʟʏ + ᴀᴊs \n├🔹sʙ + ᴀssɪsᴛ + ᴀᴊs \n├🔹ʟᴏɢɪɴ ᴊs / ʙʏᴘᴀs\n├🔹ɴᴇᴡ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴄ ʙᴏᴛ \n├🔹ɴᴇᴡ ʙᴇʟᴀᴊᴀʀ ʙᴏᴛ \n├🔹ᴘᴇᴍᴀsᴀɴɢ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ\n├🔹ʀᴇᴀᴅʏ ᴀᴋᴜɴ ᴄᴏɪɴ\n├🔹ʀᴇᴀᴅʏ ᴄᴏɪɴ ɢɪғᴛ \n╰────────────────── \n╭─────────────────\n├ line.me/ti/p/~4rman3\n╰─────────────────",
    "autoJoinTicket":False,
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
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
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
    'autoJoin':True,
    'autoAdd':True,
    'left':False,
    'leaveMsg':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":True,
    "sticker":False,
    "selfbot":True,
    "likeOn":False,
    'autoBlock':False,
    "unsend":True,
    "arespon":True,
    "mention":"╭──────────────────╮\n├🔹ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴀᴋᴀᴋ  \n╰──────────────────╯\n╭──────────────────\n├🔹ʀᴇᴀᴅʏ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n├🔹ʀᴏᴏᴍ sᴍᴜʟᴇ / ᴇᴠᴇɴᴛ \n├🔹ʀᴇᴀᴅʏ sʙ ᴏɴʟʏ \n├🔹sʙ ᴏɴʟʏ + ᴀᴊs \n├🔹sʙ + ᴀssɪsᴛ + ᴀᴊs \n├🔹ʟᴏɢɪɴ ᴊs / ʙʏᴘᴀs / ɴɪɴᴊᴀ\n├🔹ɴᴇᴡ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴄ ʙᴏᴛ \n├🔹ɴᴇᴡ ʙᴇʟᴀᴊᴀʀ ʙᴏᴛ \n├🔹ᴘᴇᴍᴀsᴀɴɢ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ\n├🔹ʀᴇᴀᴅʏ ᴀᴋᴜɴ ᴄᴏɪɴ\n├🔹ʀᴇᴀᴅʏ ᴄᴏɪɴ ɢɪғᴛ \n╰────────────────── \n╭─────────────────\n├ line.me/ti/p/~4rman3\n╰─────────────────",
    "Respontag":"Sekali lagi lu tag,gua tampol lu",
    "welcome":"Selamat datang & semoga betah n bahagia",
    "message":"╭──────────────────╮\n├🔹ᴛᴇʀɪᴍᴀ ᴋᴀsɪʜ sᴜᴅᴀʜ ᴀᴅᴅ  \n╰──────────────────╯\n╭──────────────────\n├🔹ʀᴇᴀᴅʏ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n├🔹ʀᴏᴏᴍ sᴍᴜʟᴇ / ᴇᴠᴇɴᴛ \n├🔹ʀᴇᴀᴅʏ sʙ ᴏɴʟʏ \n├🔹sʙ ᴏɴʟʏ + ᴀᴊs \n├🔹sʙ + ᴀssɪsᴛ + ᴀᴊs \n├🔹ʟᴏɢɪɴ ᴊs / ʙʏᴘᴀs\n├🔹ɴᴇᴡ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴄ ʙᴏᴛ \n├🔹ɴᴇᴡ ʙᴇʟᴀᴊᴀʀ ʙᴏᴛ \n├🔹ᴘᴇᴍᴀsᴀɴɢ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ\n├🔹ʀᴇᴀᴅʏ ᴀᴋᴜɴ ᴄᴏɪɴ\n├🔹ʀᴇᴀᴅʏ ᴄᴏɪɴ ɢɪғᴛ \n╰────────────────── \n╭─────────────────\n├ line.me/ti/p/~4rman3\n╰─────────────────",
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

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

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

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╭──[DAFTAR JONES {}]──\n├ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "├ "
            else:
                try:
                    textx += "╰──[CANNIBAL KILLER]──".format(str(cl.getGroup(to).name))
                except:
                    pass
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ ɪɴғᴏ ] ᴇʀᴏʀ :\n" + str(error))

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
            textx += settings["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to,"sɪ ᴊᴏɴᴇs")

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
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
            textx += "welcome"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
      #  client.sendMessage(to, textx)
    except Exception as error:
        cl.sendMessage(to)
        
def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd.startswith('ex\n'):
      if sender in clientMid:
        try:
            sep = text.split('\n')
            ryn = text.replace(sep[0] + '\n','')
            f = open('exec.txt', 'w')
            sys.stdout = f
            print(' ')
            exec(ryn)
            print('\n%s' % str(datetime.now()))
            f.close()
            sys.stdout = sys.__stdout__
            with open('exec.txt','r') as r:
                txt = r.read()
            cl.sendMessage(to, txt)
        except Exception as e:
            pass
      else:
        cl.sendMessage(to, 'ᴀᴘᴀʟᴜ !')
    elif cmd.startswith('exc\n'):
      if sender in clientMid:
        sep = text.split('\n')
        ryn = text.replace(sep[0] + '\n','')
        if 'print' in ryn:
        	ryn = ryn.replace('print(','cl.sendExecMessage(to,')
        	exec(ryn)
        else:
        	exec(ryn)
      else:
        cl.sendMessage(to, 'ᴀᴘᴀʟᴜ !')        

def logError(text):
    cl.log("[ CANNIBAL KILLER ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
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
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))
        
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
            "altText": "CANNIBAL KILLER",
            "contents":{
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text":  text,
            "size": "xs",
            "wrap": True,
            "weight": "regular",
            "offsetStart": "3px"
          }
        ],
        "margin": "xs",
        "spacing": "md",
        "backgroundColor": "#ffffff"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "CANNIBAL KILLER",
            "align": "center",
            "size": "xs"
          }
        ],
        "paddingAll": "2px",
        "backgroundColor": "#000000",
        "margin": "xs"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "2px",
    "borderColor": "#FF0000",
    "cornerRadius": "10px",
    "spacing": "xs"
  },
  "styles": {
    "body": {
      "backgroundColor": "#ffff00"
    }
  }
}
}
    cl.postTemplate(to, data)
 
def sendTextTemplate8(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
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
            "size": "md",
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
      "backgroundColor": "#000000"
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
    "url": "https://media.tenor.com/images/842c542426869f999afaeb7d8c7940b3/tenor.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏᴡɴᴇʀ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~4rman3"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴘᴇsᴀɴ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
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
        "text": "CANNIBAL KILLER",
        "size": "xl",
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
    
def sendTextTemplate7(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
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
            "size": "md",
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
      "backgroundColor": "#000000"
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
    "url": "https://media.giphy.com/media/NTj6PZtxqt6U91ksRZ/giphy.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏᴡɴᴇʀ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~4rman3"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴘᴇsᴀɴ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~4rman3"
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
        "text": "CANNIBAL KILLER",
        "size": "xl",
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
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
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
            "size": "md",
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
      "backgroundColor": "#000000"
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
    "url": "https://media.giphy.com/media/nbBbfmBVnuIYZ5itAc/giphy.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏᴡɴᴇʀ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~4rman3"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴘᴇsᴀɴ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~4rman3"
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
        "text": "CANNIBAL",
        "size": "xl",
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
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
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
            "size": "md",
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
      "backgroundColor": "#000000"
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
    "url": "https://media0.giphy.com/media/xVxio2tNLAM5q/200w.webp?cid=19f5b51a5c44951d4b47664273e6c074",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏᴡɴᴇʀ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~4rman3"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴘᴇsᴀɴ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~4rman3"
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
        "text": "CANNIBAL KILLER",
        "size": "xl",
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
            "altText": "CANNIBAL KILLER",
            "contents": {
  "type": "bubble",
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
            "color": "#F0F8FF"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
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
        "text": "sᴇᴇ ʏᴏᴜ",
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
        "text": "sᴏᴜɴᴅᴄʟᴏᴜᴅ",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
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
                "altText": "CANNIBAL KILLER",
                "contents": {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                               "text": text,
                               "size": "sm",
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
            "altText": "CANNIBAL KILLER",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000CD"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
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
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate3(to, text):
    data = {
            "type": "flex",
            "altText": "CANNIBAL KILLER",
            "contents": {
  "type": "bubble",
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
            "color": "#00FF00"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FFFF"
    },
    "header": {
      "backgroundColor": "#00FFFF"
    }
    },  
     "hero": {
     "type": "image",
     "aspectRatio": "20:13",
     "aspectMode": "cover",
     "url": "https://media.giphy.com/media/67pVlH3LSLDjTBikzf/giphy.gif",
     "size": "full",
     "margin": "xl"
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏᴡɴᴇʀ",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~4rman3"
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
        "text": "CANNIBAL",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
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
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~4rman3"
           }                                                
 }
]
                          }
                      }
    
def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(client.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~4rman3"
           }                                                
 }
]
                          }
                      }
    cl.postTemplate(to, data)    
    
def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output oleng.mp3 {}'.format(link))
    try:
        cl.sendAudio(to, 'cannibal.mp3')
        time.sleep(2)
        os.remove('cannibal.mp3')
    except Exception as e:
        cl.sendMessage(to, 'CANNIBAL KILLER\nʟɪɴᴋ ᴀɴᴅᴀ sᴀʟᴀʜ')
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output cannibal.mp4 {}'.format(link))
    try:
        cl.sendVideo(to, "cannibal.mp4")
        time.sleep(2)
        os.remove('cannibal.mp4')
    except Exception as e:
        cl.sendMessage(to, ' ᴇʀʀᴏʀ\nʟɪɴᴋ ᴀɴᴅᴀ sᴀʟᴀʜ', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+client.getContact(clientMid).pictureStatus, 'AGENT_NAME': 'ᴇʀʀᴏʀ', 'AGENT_LINK': 'https://line.me/ti/p/~4rman3'})

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "ʙᴏᴛ ᴀᴋᴛɪғ ʙᴏssᴋᴜ"
                        cl.sendMessage(tmp, veza, {'AGENT_LINK': "https://line.me/ti/p/~4rman3", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)

def delExpirev2():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "ʙᴏᴛ ᴀᴋᴛɪғ ʙᴏssᴋᴜ"
                        cl.sendMessage(tmp, veza, {'AGENT_LINK': "https://line.me/ti/p/~4rman3", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)    

def musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+cl.getContact(mid).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': cl.getContact(mid).statusMessage if cl.getContact(mid).statusMessage != '' else 'http://line.me/ti/p/~4rman3', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': cl.getContact(mid).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.cl.cl/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+mid,'MSG_SENDER_NAME':  cl.getContact(mid).displayName,}
    return cl.sendMessage(to, cl.getContact(mid).displayName, contentMetadata, 19)

def sendMention2(to, mid, firstmessage, lastmessage):
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
        cl.sendImageWithURL(msg.to,image)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
    
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭───────────────────╮" + "\n" + \
                  "├  🔹CANNIBAL KILLER🔹 │" + "\n" + \
                  "╰───────────────────╯" + "\n" + \
                  "╭────────────╮" + "\n" + \
                  "├🔹" + key + "ᴍᴇ\n" + \
                  "├🔹" + key + "ᴍɪᴅ「@」\n" + \
                  "├🔹" + key + "ɪɴғᴏ「@」\n" + \
                  "├🔹" + key + "ʀᴇsᴛᴀʀᴛ\n" + \
                  "├🔹" + key + "ʀᴜɴᴛɪᴍᴇ\n" + \
                  "├🔹" + key + "ʙᴀʙᴀᴛ「@」\n" + \
                  "├🔹" + key + "sᴘ\n" + \
                  "├🔹" + key + "ᴡᴏʏ / ᴄᴏʟᴏᴋ\n" + \
                  "├🔹" + key + "ᴊᴏɪɴ\n" + \
                  "├🔹" + key + "ᴏᴜᴛ\n" + \
                  "├🔹" + key + "ᴀs¹-⁴\n" + \
                  "├🔹" + key + "ᴊs sᴛᴀʏ\n" + \
                  "├🔹" + key + "ᴊs ɪɴ\n" + \
                  "├🔹" + key + "ʙʏᴇᴍᴇ\n" + \
                  "├🔹" + key + "ʟᴇᴀᴠᴇ「ɴᴀᴍᴇ ɢʀᴏᴜᴘ」\n" + \
                  "├🔹" + key + "ɢɪɴғᴏ\n" + \
                  "├🔹" + key + "sᴇʟғ ᴏɴ「@」\n" + \
                  "├🔹" + key + "ᴏᴘᴇɴ\n" + \
                  "├🔹" + key + "ᴄʟᴏsᴇ\n" + \
                  "├🔹" + key + "ᴜʀʟɢʀᴜᴘ\n" + \
                  "├🔹" + key + "ɪɴғᴏɢʀᴜᴘ「ɴᴏ」\n" + \
                  "├🔹" + key + "ɪɴғᴏᴍᴇᴍ「ɴᴏ」\n" + \
                  "├🔹" + key + "ᴀʟʟ ᴄʟᴇᴀʀ\n" + \
                  "├🔹" + key + "ʜᴀᴘᴜsᴄʜᴀᴛ\n" + \
                  "├🔹" + key + "ғʀɪᴇɴᴅʟɪsᴛ\n" + \
                  "├🔹" + key + "ɢʀᴏᴜᴘʟɪsᴛ\n" + \
                  "├🔹" + key + "ᴜᴘᴅᴀᴛᴇғᴏᴛᴏ\n" + \
                  "├🔹" + key + "ᴜᴘᴅᴀᴛᴇɢʀᴜᴘ\n" + \
                  "├🔹" + key + "ᴜᴘᴅᴀᴛᴇʙᴏᴛ\n" + \
                  "├🔹" + key + "sᴇᴛᴋᴇʏ「ɴᴇᴡᴋᴇʏ」\n" + \
                  "├🔹" + key + "ᴍʏᴋᴇʏ\n" + \
                  "├🔹" + key + "sᴇʟғ 「ᴏɴ/ᴏғғ」\n" + \
                  "├🔹" + key + "ᴋᴇᴛɪᴋ「 ʀᴇғʀᴇsʜ 」\n" + \
                  "╰───────────────╯"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╭───────────────────╮" + "\n" + \
                  "├  🔹CANNIBAL KILLER🔹 │" + "\n" + \
                  "╰───────────────────╯" + "\n" + \
                  "╭────────────╮" + "\n" + \
                  "├🔹" + key + "ʙʟᴄ\n" + \
                  "├🔹" + key + "ʙᴀɴ:ᴏɴ\n" + \
                  "├🔹" + key + "ᴜɴʙᴀɴ:ᴏɴ\n" + \
                  "├🔹" + key + "ʙᴀɴ「@」\n" + \
                  "├🔹" + key + "ᴜɴʙᴀɴ「@」\n" + \
                  "├🔹" + key + "ᴛᴀʟᴋʙᴀɴ「@」\n" + \
                  "├🔹" + key + "ᴜɴᴛᴀʟᴋʙᴀɴ「@」\n" + \
                  "├🔹" + key + "ᴛᴀʟᴋʙᴀɴ:ᴏɴ\n" + \
                  "├🔹" + key + "ᴜɴᴛᴀʟᴋʙᴀɴ:ᴏɴ\n" + \
                  "├🔹" + key + "ʙᴀɴʟɪsᴛ\n" + \
                  "├🔹" + key + "ᴛᴀʟᴋʙᴀɴʟɪsᴛ\n" + \
                  "├🔹" + key + "ᴄʟᴇᴀʀʙᴀɴ\n" + \
                  "├🔹" + key + "ʀᴇғʀᴇsʜ\n" + \
                  "├🔹CANNIBAL KILLER🔹\n" + \
                  "├🔹" + key + "ᴄᴇᴋ sɪᴅᴇʀ\n" + \
                  "├🔹" + key + "ᴄᴇᴋ sᴘᴀᴍ\n" + \
                  "├🔹" + key + "ᴄᴇᴋ ᴘᴇsᴀɴ \n" + \
                  "├🔹" + key + "ᴄᴇᴋ ʀᴇsᴘᴏɴ \n" + \
                  "├🔹" + key + "ᴄᴇᴋ ᴡᴇʟᴄᴏᴍᴇ\n" + \
                  "├🔹" + key + "sᴇᴛ sɪᴅᴇʀ: (ᴛᴇxᴛ)\n" + \
                  "├🔹" + key + "sᴇᴛ sᴘᴀᴍ: (ᴛᴇxᴛ)\n" + \
                  "├🔹" + key + "sᴇᴛ ᴘᴇsᴀɴ: (ᴛᴇxᴛ)\n" + \
                  "├🔹" + key + "sᴇᴛ ʀᴇsᴘᴏɴ: (ᴛᴇxᴛ)\n" + \
                  "├🔹" + key + "sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ: (ᴛᴇxᴛ)\n" + \
                  "├🔹" + key + "ᴍʏɴᴀᴍᴇ:「ɴᴀᴍᴀ」\n" + \
                  "├🔹" + key + "ɢɪғᴛ:「ᴍɪᴅ 」「ᴊᴜᴍʟᴀʜ」\n" + \
                  "├🔹" + key + "sᴘᴀᴍ:「ᴍɪᴅ」「ᴊᴜᴍʟᴀʜ」\n" + \
                  "╰──────────────────╯" + "\n" + \
                  "╭─🔹ᴄʀᴇᴀᴛᴏʀ ʙʏᴇ🔹─╮\n            cannibal team\n╰─🔹CANNIBAL KILLER🔹─╯"
                  
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:   
    	#if op.type == 0:
            #return
            
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = cl.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.cancelGroupInvitation(op.param1,[op.param2])
                            cl.updateGroup(X)                           
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ticket = ki.reissueGroupTicket(op.param1)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.cancelGroupInvitation(op.param1,[op.param2])
                                ki.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.cancelGroupInvitation(op.param1,[op.param2])
                                    kk.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Ticket = kc.reissueGroupTicket(op.param1)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.cancelGroupInvitation(op.param1,[op.param2])
                                        kc.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if ko.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            ko.reissueGroupTicket(op.param1)
                                            X = ko.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            Ticket = ko.reissueGroupTicket(op.param1)
                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ko.kickoutFromGroup(op.param1,[op.param2])
                                            ko.cancelGroupInvitation(op.param1,[op.param2])
                                            ko.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)                                        
                                except:
                                    try:
                                        if jk.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                cl.reissueGroupTicket(op.param1)
                                                X = jk.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                Ticket = jk.reissueGroupTicket(op.param1)
                                                jk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                jk.kickoutFromGroup(op.param1,[op.param2])
                                                jk.cancelGroupInvitation(op.param1,[op.param2])
                                                jk.updateGroup(X)
                                                jk.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if cl.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    cl.reissueGroupTicket(op.param1)
                                                    X = cl.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    Ticket = cl.reissueGroupTicket(op.param1)
                                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                                    sw.cancelGroupInvitation(op.param1,[op.param2])
                                                    sw.leaveGroup(op.param1)
                                                    cl.updateGroup(X)
                                                    cl.inviteIntoGroup(op.param1,[Zmid])
                                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                        except:
                                            pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,"ᴘᴀᴘᴀʏ ᴄᴀʏᴀɴᴋ...\n ɢʀᴏᴜᴘ " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,"ᴛᴀɴᴋs ᴜᴅᴀʜ ᴊᴇᴘɪᴛ... " + str(ginfo.name))
                  
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,"ʜᴀʏ sᴇᴍᴜᴀ\nᴀʙɪ ᴅᴀᴛᴀɴɢ\nᴅɪ ɢʀᴏᴜᴘ " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,"ʜᴀʏ sᴇᴍᴜᴀ\nᴀʙɪ ᴅᴀᴛᴀɴɢ\nᴅɪ ɢʀᴏᴜᴘ " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ko.acceptGroupInvitation(op.param1)
                        ginfo = ko.getGroup(op.param1)
                        ko.leaveGroup(op.param1)
                    else:
                        ko.acceptGroupInvitation(op.param1)
                        ginfo = ko.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        jk.acceptGroupInvitation(op.param1)
                        ginfo = jk.getGroup(op.param1)
                        jk.leaveGroup(op.param1)
                    else:
                        jk.acceptGroupInvitation(op.param1)
                        ginfo = jk.getGroup(op.param1)
                        
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        jk.findAndAddContactsByMid(op.param3)
                        jk.kickoutFromGroup(op.param1,[op.param2])
                        jk.cancelGroupInvitation(op.param1,[op.param2])
                        jk.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            ki.findAndAddContactsByMid(op.param3)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kk.findAndAddContactsByMid(op.param3)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])    
                                except:
                                    try:
                                        ko.findAndAddContactsByMid(op.param3)
                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                        ko.cancelGroupInvitation(op.param1,[op.param2])
                                        ko.inviteIntoGroup(op.param1,[op.param3])        
                                    except:
                                        try:
                                            random.choice(ABC).findAndAddContactsByMid(op.param3)
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(ABC).cancelGroupInvitation(op.param1,[op.param2])
                                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass                
                        

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(ABC).cancelGroupInvitation(op.param1,[op.param2])
            else:
                pass

        if op.type == 15:
            if wait["leaveMsg"] == True:
                ginfo = cl.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])
                contact = cl.getContact(op.param2)
                data = {
                        "type": "flex",
                        "altText": "CANNIBAL KILLER",
                        "contents": {
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
                    "size": "xs",
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
                    "text": "🔹ʙᴀᴘᴇʀ ᴋᴀɴ ᴅɪᴀ ʟᴇғᴛ",
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
                        "text": "CANNIBAL KILLER",
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
                "text": "ʟᴇғᴛ",
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
                cl.postTemplate(op.param1, data)
              
        if op.type == 17:
            if wait["welcomeOn"] == True:
                ginfo = cl.getGroup(op.param1)
                welcomeMembers(op.param1, [op.param2])
                contact = cl.getContact(op.param2)
                data = {
                        "type": "flex",
                        "altText": "CANNIBAL KILLER",
                        "contents": {
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
                    "size": "xs",
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
                    "text": "🔹sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ",
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
                        "text": "CANNIBAL KILLER",
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
                "text": "ᴡʟᴄᴍ",
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
                cl.postTemplate(op.param1, data)
        if op.type == 5:
            print ("[ 5 ] ɴᴏᴛɪғɪᴇᴅ ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ")
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1, wait["ᴍᴀᴀғ ᴀɪᴍ ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴀɪᴍ ᴀᴋᴛɪғ"])
                
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'ɢᴀᴍʙᴀʀɴʏᴀ ᴅɪ ʙᴀᴡᴀʜ':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 ɢᴀᴍʙᴀʀ ᴅɪ ʜᴀᴘᴜs 」\nᴘᴇɴɢɪʀɪᴍ : "
                                ret_ = "ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\nᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
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
                                ret_ =  "ᴘᴇsᴀɴ ᴅɪ ʜᴀᴘᴜs\n"
                                ret_ += "ᴘᴇɴɢɪʀɪᴍ : {}".format(str(ryan.displayName))
                                ret_ += "\n°ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\nᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\nᴘᴇsᴀɴ ɴʏᴀ : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "sᴛɪᴄᴋᴇʀ ᴅɪ ʜᴀᴘᴜs\n"
                                ret_ += "ᴘᴇɴɢɪʀɪᴍ : {}".format(str(ryan.displayName))
                                ret_ += "\nɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\nᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
                
        if op.type == 19:
            if mid in op.param3:
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
                        sw.acceptGroupInvitation(op.param1)
                        sw.findAndAddContactsByMid(op.param3)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        x = sw.getGroup(op.param1)
                        x.preventedJoinByTicket = False
                        sw.updateGroup(x)
                        invsend = 0
                        Ti = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        ko.acceptGroupInvitationByTicket(op.param1,Ti)
                        jk.acceptGroupInvitationByTicket(op.param1,Ti)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        sw.leaveGroup(op.param1)
                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                    except:
                        random.choice(ABC).findAndAddContactsByMid(op.param3)
                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])        
            
        if op.type == 19:
            if mid in op.param3:
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
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = ki.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    ki.updateGroup(x)
                                    invsend = 0
                                    Ti = ki.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(KAC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)    
                                            except:
                                                pass
                return

            if Amid in op.param3:
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
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                jk.kickoutFromGroup(op.param1,[op.param2])
                                jk.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = kk.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    kk.updateGroup(x)
                                    invsend = 0
                                    Ti = kk.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)        
                                            except:
                                                pass
                return

            if Bmid in op.param3:
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
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            jk.kickoutFromGroup(op.param1,[op.param2])
                            jk.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = kc.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    kc.updateGroup(x)
                                    invsend = 0
                                    Ti = kc.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)            
                                            except:
                                                pass
                return
                    
            if Cmid in op.param3:
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
                        jk.kickoutFromGroup(op.param1,[op.param2])
                        jk.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = ko.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    ko.updateGroup(x)
                                    invsend = 0
                                    Ti = ko.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)                
                                            except:
                                                pass
                return

            if Dmid in op.param3:
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
                        jk.kickoutFromGroup(op.param1,[op.param2])
                        jk.inviteIntoGroup(op.param1,[op.param3])
                        ko.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ko.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                ko.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = cl.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    invsend = 0
                                    Ti = cl.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        ko.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            ko.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                ko.acceptGroupInvitation(op.param1)                    
                                            except:
                                                pass
                return
                
            if Emid in op.param3:
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
                        ko.kickoutFromGroup(op.param1,[op.param2])
                        ko.inviteIntoGroup(op.param1,[op.param3])
                        jk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            jk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                jk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = cl.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    invsend = 0
                                    Ti = cl.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        jk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            jk.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                jk.acceptGroupInvitation(op.param1)                    
                                            except:
                                                pass
                return    
                
            if Zmid in op.param3:
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
                        jk.findAndAddContactsByMid(op.param3)
                        jk.kickoutFromGroup(op.param1,[op.param2])
                        jk.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            ki.findAndAddContactsByMid(op.param3)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kk.findAndAddContactsByMid(op.param3)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])    
                                except:
                                    try:
                                        ko.findAndAddContactsByMid(op.param3)
                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                        ko.inviteIntoGroup(op.param1,[op.param3])        
                                    except:
                                        try:
                                            random.choice(ABC).findAndAddContactsByMid(op.param3)
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass
                return    
                
            if admin in op.param3:
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
                        jk.kickoutFromGroup(op.param1,[op.param2])
                        jk.findAndAddContactsByMid(op.param1,admin)
                        jk.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])    
                                except:
                                    try:
                                        ko.findAndAddContactsByMid(op.param3)
                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                        ko.inviteIntoGroup(op.param1,[op.param3])        
                                    except:
                                        try:
                                            random.choice(ABC).findAndAddContactsByMid(op.param3)
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])    
                                        except:
                                            pass

                return

            if staff in op.param3:
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
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    ko.findAndAddContactsByMid(op.param3)
                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                    ko.inviteIntoGroup(op.param1,[op.param3])        
                                except:
                                    try:
                                        random.choice(ABC).findAndAddContactsByMid(op.param3)
                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])        
                                    except:
                                        pass

                return
              
        if op.type == 13:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                      
        if op.type == 13:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        group = jk.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            jk.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = ko.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            ko.cancelGroupInvitation(op.param1,[_mid])        
                                    except:
                                        pass
        
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                jk.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                          
        if op.type == 32:
            if Zmid in op.param3:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[Zmid])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[Zmid])
                            except:
                                try:
                                    ko.inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        jk.inviteIntoGroup(op.param1,[Zmid])
                                    except:
                                        try:
                                            random.choice(ABC).inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Zmid])
                                        except:
                                            pass
            return
        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        
        if op.type == 55:
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
                                "altText": "CANNIBAL KILLER",
                                "contents": {
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
                    "text": "🔹ɴɢɪɴᴛɪᴘ² ɢᴀʙᴜɴɢ sɪɴɪ",
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
                        "text": "CANNIBAL KILLER",
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
                "text": "sᴄᴛᴠ",
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
                        cl.postTemplate(op.param1, data)
                
        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
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
                                        
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sendTextTemplate(msg.to, wait["Respontag"])
                           break
                           
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "ᴊᴀɴɢᴀɴ ᴛᴀǫ ᴀʙɪ....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
                           
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["arespon"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   lists = []
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           contact = cl.getContact(msg._from)
                           cl.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                           sendMention1(sender, "╭──────────────────╮\n├🔹ᴛᴇʀɪᴍᴀ ᴋᴀsɪʜ sᴜᴅᴀʜ ᴀᴅᴅ  │\n╰──────────────────╯\n╭──────────────────\n├🔹ʀᴇᴀᴅʏ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n├🔹ʀᴏᴏᴍ sᴍᴜʟᴇ / ᴇᴠᴇɴᴛ \n├🔹ʀᴇᴀᴅʏ sʙ ᴏɴʟʏ \n├🔹sʙ ᴏɴʟʏ + ᴀᴊs \n├🔹sʙ + ᴀssɪsᴛ + ᴀᴊs \n├🔹ʟᴏɢɪɴ ᴊs / ʙʏᴘᴀs / ɴɪɴᴊᴀ\n├🔹ɴᴇᴡ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴄ ʙᴏᴛ \n├🔹ɴᴇᴡ ʙᴇʟᴀᴊᴀʀ ʙᴏᴛ \n├🔹ᴘᴇᴍᴀsᴀɴɢ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ\n├🔹ʀᴇᴀᴅʏ ᴀᴋᴜɴ ᴄᴏɪɴ\n├🔹ʀᴇᴀᴅʏ ᴄᴏɪɴ ɢɪғᴛ \n╰────────────────── \n╭─────────────────\n├ line.me/ti/p/~4rman3\n╰─────────────────", [sender])
                           break
                           
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「ᴄᴇᴋ ɪᴅ sᴛɪᴄᴋᴇʀ」\nsᴛᴋɪᴅ : " + msg.contentMetadata["STKID"] + "\nsᴛᴋᴘᴋɢɪᴅ : " + msg.contentMetadata["STKPKGID"] + "\nsᴛᴋᴠᴇʀ : " + msg.contentMetadata["STKVER"]+ "\n\n「ʟɪɴᴋ sᴛɪᴄᴋᴇʀ」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\nᴍɪᴅ : " + msg.contentMetadata["mid"] + "\nsᴛᴀᴛᴜs ᴍsɢ : " + contact.statusMessage + "\nᴘɪᴄᴛᴜʀᴇ ᴜʀʟ : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
                        
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 16:
                        url = msg.contentMetadata["postEndUrl"]
                        cl.likePost(url[25:58], url[66:], likeType=1004)
                        cl.createComment(url[25:58], url[66:], settings["comment"])
                        print ("ᴀᴜᴛᴏ ʟɪᴋᴇ ᴅᴏɴᴇ")
                        sendTextTemplate(msg.to,"👍 AUTO LIKE BY CANNIBAL")
                        settings["likeOn"] = False
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
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    sendTextTemplate(msg.to,"sᴛᴋɪᴅ : " + msg.contentMetadata["STKID"] + "\nsᴛᴋᴘᴋɢɪᴅ : " + msg.contentMetadata["STKPKGID"] + "\nsᴛᴋᴠᴇʀ : " + msg.contentMetadata["STKVER"]+ "\n\n「ʟɪɴᴋ sᴛɪᴄᴋᴇʀ」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sendTextTemplate(msg.to,"ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\nᴍɪᴅ : " + msg.contentMetadata["mid"] + "\nsᴛᴀᴛᴜs ᴍsɢ : " + contact.statusMessage + "\nᴘɪᴄᴛᴜʀᴇ ᴜʀʟ: http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#===================================[ ] ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sendTextTemplate(msg.to,"🔹sᴜᴅᴀʜ ᴊᴀᴅɪ ʙᴏᴛ")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate(msg.to,"🔹ɪᴛᴜ ʙᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")
                        
#===================================[ ]  ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"🔹sᴜᴅᴀʜ ᴊᴀᴅɪ sᴛᴀғғ")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴛᴀғғ")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs sᴛᴀғғ")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        sendTextTemplate(msg.to,"🔹ɪᴛᴜ ʙᴜᴋᴀɴ sᴛᴀғғ")
#===================================[ ]  ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sendTextTemplate(msg.to,"🔹ɪᴛᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ᴀᴅᴍɪɴ")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀᴅᴍɪɴ")
                    else:
                        wait["delladmin"] = True
                        sendTextTemplate(msg.to,"🔹ɪᴛᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ")
#===================================[ ]  ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sendTextTemplate(msg.to,"🔹sᴜᴅᴀʜ ᴀᴅᴀ ᴅɪ ʙʟᴀᴄᴋʟɪsᴛ")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ")
                    else:
                        wait["dblacklist"] = True
                        sendTextTemplate(msg.to,"🔹ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʟᴀᴄᴋʟɪsᴛ")
#===================================[ ] TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sendTextTemplate(msg.to,"🔹sᴜᴅᴀʜ ᴀᴅᴀ ᴅɪ ᴛᴀʟᴋʙᴀɴ")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                         sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ")
                    else:
                        wait["Talkdblacklist"] = True
                        sendTextTemplate(msg.to,"🔹ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅɪ ᴛᴀʟᴋʙᴀɴ")
#===================================[ ] UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sendTextTemplate(msg.to, "🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ɢᴀᴍʙᴀʀ")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     sendTextTemplate(msg.to, "🔹ᴅᴏɴᴇ ᴍᴇɴɢᴜʙᴀʜ ғᴏᴛᴏ ɢʀᴏᴜᴘ")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            cl.updateProfilePicture(path)
                            sendTextTemplate(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["RAfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                        elif Bmid in Setmain["RAfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                        elif Cmid in Setmain["RAfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                        elif Dmid in Setmain["RAfoto"]:
                            path = ko.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Dmid]
                            ko.updateProfilePicture(path)
                            ko.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                        elif Bmid in Setmain["RAfoto"]:
                            path = jk.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Emid]
                            jk.updateProfilePicture(path)
                            jk.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                        elif Cmid in Setmain["RAfoto"]:
                            path = bu.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Fmid]
                            bu.updateProfilePicture(path)
                            bu.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                        elif Dmid in Setmain["RAfoto"]:
                            path = bi.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Gmid]
                            bi.updateProfilePicture(path)
                            bi.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                        elif Cmid in Setmain["RAfoto"]:
                            path = bo.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Hmid]
                            bo.updateProfilePicture(path)
                            bo.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                        elif Dmid in Setmain["RAfoto"]:
                            path = be.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Imid]
                            be.updateProfilePicture(path)
                            be.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                        elif Dmid in Setmain["RAfoto"]:
                            path = by.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Jmid]
                            by.updateProfilePicture(path)
                            by.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                            
                        elif Zmid in Setmain["RAfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = ko.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "🔹ғᴏᴛᴏ ʙᴏᴛ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "🔹ғᴏᴛᴏ ʙᴏᴛ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "🔹ғᴏᴛᴏ ʙᴏᴛ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                     ko.updateProfilePicture(path4)
                     ko.sendMessage(msg.to, "🔹ғᴏᴛᴏ ʙᴏᴛ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "menu":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               sendTextTemplate(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sendTextTemplate(msg.to, "🔹ᴛᴇᴍᴘʟᴀᴛᴇ ᴀᴋᴛɪғ ʙᴏssᴋᴜ")
                           
                        elif cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate(msg.to, "╭─────╮\n├🔹ʜᴇʟᴘ\n├🔹ᴍᴇɴᴜ\n├🔹ʜᴇʟᴘ¹\n├🔹ʜᴇʟᴘ²\n├🔹ʜᴇʟᴘ³\n├🔹ʜᴇʟᴘ⁴\n├🔹ʜᴇʟᴘ⅝\n├🔹ᴍʏsᴇᴛ\n├🔹ᴊᴏᴏx-ᴊᴜᴅᴜʟ\n├🔹ɢs ᴛᴀɢ\n├🔹ᴋᴄ ᴛᴀɢ\n├🔹ʜᴇʀᴇ\n├🔹ᴏᴜᴛ\n├🔹ʀs\n├🔹ʙᴄ¹:\n├🔹ʙʀᴏᴀᴅᴄᴀsᴛ:\n├🔹ᴀʙᴏᴜᴛ\n╰──────╯\n\n╭───────────────────────\n├🔹ᴄʀᴇᴀᴛᴏʀ ᴛᴇᴍᴘʟᴀᴛᴇ ʙʏᴇ : CANNIBAL\n╰───────────────────────")
 
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate(msg.to, "ᴛᴇᴍᴘʟᴀᴛᴇ ᴏғғ ʙᴏssᴋᴜ")
                          
                        elif cmd == "help1":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate(msg.to, "╭───────────╮\n├🔹ɴᴏᴛᴀɢ ᴏɴ|ᴏғғ\n├🔹ᴀʟʟᴘʀᴏ ᴏɴ|ᴏғғ\n├🔹ᴘʀᴏᴛᴇᴄᴛᴜʀʟ ᴏɴ|ᴏғғ\n├🔹ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ ᴏɴ|ᴏғғ\n├🔹ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ ᴏɴ|ᴏғғ\n├🔹ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ ᴏɴ|ᴏғғ\n╰───────────────╯\n\n╭───────────────────────\n├🔹ᴄʀᴇᴀᴛᴏʀ ᴛᴇᴍᴘʟᴀᴛᴇ ʙʏᴇ : CANNIBAL\n╰───────────────────────")                 
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               sendTextTemplate(msg.to, str(helpMessage1))
                        elif cmd == "help3":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate(msg.to, "╭───────╮\n├🔹ʜᴀʜ\n├🔹sᴜᴇ\n├🔹ᴡᴏʏ/ᴄᴏʟᴏᴋ\n├🔹sᴇᴅɪʜ\n├🔹sᴇᴘɪ\n├🔹ʜᴀᴅᴇʜ\n├🔹ᴊᴜᴍʟᴀʜ:\n├🔹sᴛᴀɢ ᴛᴀɢ\n├🔹sᴘᴀᴍᴄᴀʟʟ: ᴊᴜᴍʟᴀʜ\n├🔹sᴘᴀᴍᴄᴀʟʟ\n╰──────────╯\n\n╭───────────────────────\n├🔹ᴄʀᴇᴀᴛᴏʀ ᴛᴇᴍᴘʟᴀᴛᴇ ʙʏᴇ : CANNIBAL\n╰───────────────────────")
                        elif cmd == "help4":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate(msg.to, "╭───────────╮\n├🔹ʀᴇsᴘᴏɴ ᴏɴ|ᴏғғ\n├🔹ᴄᴏɴᴛᴀᴄᴛ ᴏɴ|ᴏғғ\n├🔹ᴀᴜᴛᴏᴊᴏɪɴ ᴏɴ|ᴏғғ\n├🔹ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ|ᴏғғ\n├🔹ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴏɴ|ᴏғғ\n├🔹ᴡᴇʟᴄᴏᴍᴇ ᴏɴ|ᴏғғ\n├??ᴊᴀɴᴅᴀ ᴏɴ|ᴏғғ\n╰───────────╯\n\n╭───────────────────────\n├🔹ᴄʀᴇᴀᴛᴏʀ ᴛᴇᴍᴘʟᴀᴛᴇ ʙʏᴇ : CANNIBAL\n╰───────────────────────")
                        elif cmd == "help5":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate(msg.to, "╭─────────╮\n├🔹ᴀᴅᴍɪɴ:ᴏɴ\n├🔹ᴀᴅᴍɪɴ:ʀᴇᴘᴇᴀᴛ\n├🔹sᴛᴀғғ:ᴏɴ\n├🔹sᴛᴀғғ:ʀᴇᴘᴇᴀᴛ\n├🔹ᴀᴅᴍɪɴᴀᴅᴅ ᴛᴀɢ\n├🔹ᴀ ᴛᴀɢ\n├🔹s ᴛᴀɢ\n├🔹s ᴛᴀɢ\n├🔹ʙᴏᴛᴀᴅᴅ ᴛᴀɢ\n├🔹ʙᴏᴛᴅᴇʟʟ ᴛᴀɢ\n├🔹ʀᴇғʀᴇsʜ\n├🔹ʟɪsᴛʙᴏᴛ\n├🔹ʟɪsᴛᴀᴅᴍɪɴ\n├🔹ʟɪsᴛᴘʀᴏᴛᴇᴄᴛ\n├🔹sᴇʟғ ᴏɴ|ᴏғғ\n╰─────────╯\n\n╭───────────────────────\n├🔹ᴄʀᴇᴀᴛᴏʀ ᴛᴇᴍᴘʟᴀᴛᴇ ʙʏᴇ : CANNIBAL\n╰───────────────────────")
                        
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
                                xpesan =  " [ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴋ] \nʙʀᴏᴀᴅᴄᴀsᴛ ʙʏᴇ "
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
                                cl.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        
                        elif cmd == "promo1":
                            if msg._from in admin:
                                saya = cl.getGroupIdsJoined()
                                for groups in saya:
                                    data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media0.giphy.com/media/xVxio2tNLAM5q/200w.webp?cid=19f5b51a5c44951d4b47664273e6c074",
        "action": {
          "uri": "http://line.me/ti/p/~4rman3",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#C0FF03"
        },
        "header": {
          "backgroundColor": "#C0FF03"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "CANNIBAL KILLER TEMPLATE",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media3.giphy.com/media/jLDTcbU89ZOW4/200.webp?cid=19f5b51a5c449c5e414637706ff581fb"
                  },
                  {
                    "text": "ᴘᴇᴍᴀsᴀɴɢᴀɴ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          
          {
            "text": "160K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#000000",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media3.giphy.com/media/jLDTcbU89ZOW4/200.webp?cid=19f5b51a5c449c5e414637706ff581fb"
                  },
                  {
                    "text": "sʙ ᴏɴʟʏ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "200K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#000000",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media3.giphy.com/media/jLDTcbU89ZOW4/200.webp?cid=19f5b51a5c449c5e414637706ff581fb"
                  },
                  {
                    "text": "sʙ 3 ᴀssɪsᴛ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "250k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#000000",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media3.giphy.com/media/jLDTcbU89ZOW4/200.webp?cid=19f5b51a5c449c5e414637706ff581fb"
                  },
                  {
                    "text": "sʙ 6 ᴀssɪsᴛ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "500k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#000000",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ᴏᴡɴᴇʀ",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#000000",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~4rman3"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ᴋᴇᴘᴏɪɴ sᴇᴋᴀʀᴀɴɢ\nhttp://line.me/ti/p/~4rman3",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#000000",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~4rman3"
            },
            "align": "center"                            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}

                                    cl.postFlex(groups, data)     
                        elif cmd == "me":
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                               	
                                data = {
                                        "type": "flex",
                                        "altText": "CANNIBAL",
                                        "contents": {
"type": "bubble",
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
            "flex": 2,
            "text": "{}".format(status.displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#657383"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "text",
            "text": "sᴛᴀᴛᴜs ᴘʀᴏғɪʟᴇ:",
            "size": "xs",
            "weight": "bold",
            "wrap": True,
            "color": "#657383"
          },
          {
            "type": "text",
            "text": "{}".format(status.statusMessage),
            "size": "xs",
            "color": "#657383",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#FFF5EE"
    },
    "footer": {
      "backgroundColor": "#00BFFF"
    }
  },
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴀʙᴏᴜᴛ",
        "size": "xs",
        "wrap": True,
        "weight": "bold",
        "color": "#E5E4E2",
        "action": {
          "type": "uri",
          "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=about"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴏᴡɴᴇʀ",
        "size": "xs",
        "wrap": True,
        "weight": "bold",
        "color": "#E5E4E2",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~4rman3"
        },
        "align": "center"
      }
    ]
  }
}
}
                                cl.postTemplate(to, data)
                            
                        elif cmd.startswith("joox"):
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "ᴘᴇɴʏᴀɴʏɪ: "+str(d)
                                hasil += "\nᴊᴜᴅᴜʟ : "+str(c)
                                data = {
                                        "type": "flex",
                                        "altText": "ᴍᴜsɪᴋ",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#9932CC"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": g,
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "CANNIBAL KILLER\n\nᴍᴘ³",
            "size": "sm",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": hasil,
                "size": "xs",
                "margin": "none",
                "color": "#FF6347",
                "wrap": True,
                "weight": "regular",
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
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "ᴘʟᴀʏ ᴅɪʙᴀᴡᴀʜ",
                "size": "xxl",
                "weight": "bold",
                "action": {
                  "uri": e,
                  "type": "uri",
                  "label": "Audio"
                },
                "margin": "xl",
                "align": "start",
                "color": "#FFD700",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(to, data)
                                cl.sendAudioWithURL(to,e)
                            except Exception as error:
                                sendTextTemplate(to, "error\n" + str(error))
                                logError(error)
 
                        elif cmd == "myset":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭──CANNIBAL KILLER──\n"
                                if wait["sticker"] == True: md+="├🔹sᴛɪᴄᴋᴇʀ ᴏɴ\n"
                                else: md+="├🔹sᴛɪᴄᴋᴇʀ ᴏғғ\n"
                                if wait["left"] == True: md+="├🔹ʟᴇғᴛ ᴏɴ\n"
                                else: md+="├🔹ʟᴇғᴛ ᴏғғ\n"                        
                                if wait["contact"] == True: md+="├🔹ᴄᴏɴᴛᴀᴄᴛ ᴏɴ\n"
                                else: md+="├🔹ᴄᴏɴᴛᴀᴄᴛ ᴏғғ\n"
                                if wait["talkban"] == True: md+="├🔹ᴛᴀʟᴋʙᴀɴ ᴏɴ\n"
                                else: md+="├🔹ᴛᴀʟᴋʙᴀɴ ᴏғғ\n"
                                if wait["unsend"] == True: md+="├🔹ᴜɴsᴇɴᴅ ᴏɴ\n"
                                else: md+="├🔹ᴜɴsᴇɴᴅ ᴏғғ\n"
                                if wait["Mentionkick"] == True: md+="├🔹ɴᴏᴛᴀɢ ᴏɴ\n"
                                else: md+="├🔹ɴᴏᴛᴀɢ ᴏɴ\n"
                                if wait["detectMention"] == True: md+="├🔹ʀᴇsᴘᴏɴ ᴏɴ\n"
                                else: md+="├🔹ʀᴇsᴘᴏɴ ᴏɴ\n"
                                if wait["autoJoin"] == True: md+="├🔹ᴀᴜᴛᴏᴊᴏɪɴ ᴏɴ\n"
                                else: md+="├🔹ᴀᴜᴛᴏᴊᴏɪɴ ᴏғғ\n"
                                if wait["autoAdd"] == True: md+="├🔹ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ\n"
                                else: md+="├🔹ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ\n"
                                if msg.to in welcome: md+="├🔹ᴡᴇʟᴄᴏᴍᴇ ᴏɴ\n"
                                else: md+="├🔹ᴡᴇʟᴄᴏᴍᴇ ᴏғғ\n"
                                if wait["autoLeave"] == True: md+="├🔹ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴏɴ\n"
                                else: md+="├🔹ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴏғғ\n"
                                if msg.to in protectqr: md+="├🔹ᴘʀᴏᴛᴇᴄᴛᴜʀʟ ᴏɴ\n"
                                else: md+="├🔹ᴘʀᴏᴛᴇᴄᴛᴜʀʟ ᴏғғ\n"
                                if msg.to in protectjoin: md+="├🔹ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ ᴏɴ\n"
                                else: md+="├🔹ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ ᴏғғ\n"
                                if msg.to in protectkick: md+="├🔹 ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ ᴏɴ\n"
                                else: md+="├🔹ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ ᴏғғ\n"
                                if msg.to in protectcancel: md+="├🔹ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ ᴏɴ\n"
                                else: md+="├🔹ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ ᴏғғ\n╰──────────────╯\n"
                                sendTextTemplate(msg.to, md+"\nᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "owner" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendMessage(msg.to, "ucc10b6f6bc11284e0aa9b2a2fb16b70c") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'ucc10b6f6bc11284e0aa9b2a2fb16b70c': i}, contentType=13)
                                    cl.sendMessage(msg.to, None, contentMetadata={"STKID":"16083749","STKPKGID":"1419343","STKVER":"1"}, contentType=7)

                        elif cmd == "asem" or text.lower() == 'asemmm' or text.lower() == 'sem' or text.lower() == 'semm':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴋᴇᴛᴀʜᴜᴀɴ ʟᴜ ᴋᴀᴋ ʙᴇʟᴜᴍ ᴍᴀɴᴅɪ ᴘᴀɴᴛᴇsᴀɴ ʙᴀᴜ ᴀssᴇᴇᴇᴍᴍ😂")

                        elif cmd == "pekok" or text.lower() == 'pekokkk':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴇsᴀᴍᴀ ᴘᴇᴋᴏᴋ ᴅɪ ʟᴀʀɪɴɢ ᴄᴏʟʟʏ😃😃")

                        elif cmd == "sue":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴇᴍᴀɴɢ ᴜᴅᴀʜ sᴜᴇ ᴘᴜɴʏᴀ ᴋᴋ, ᴋᴀʟᴏ ɢᴀᴋ sᴜᴇ, ɢᴀᴋ ʙᴀᴋᴀʟᴀɴ ʙɪsᴀ ᴅɪ ᴛᴜsᴜᴋ ᴀɴᴜ ᴋᴋ😂")
                             
                        elif cmd == "dudul" or text.lower() == 'pea':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴇsᴀᴍᴀ ᴅᴜᴅᴜʟ ᴊᴀɴɢᴀɴ sᴀʟɪɴɢ ʙᴜʟʟʏ ᴋᴋ😂, ᴅɪ ʙᴀᴡᴀʜ ᴍᴜ ᴊᴜɢᴀ ᴜᴅᴀʜ ɢᴜɴᴅᴜʟ ᴋᴋ 😜")
                        
                        elif cmd == "typo" or text.lower() == 'typo':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴛʏᴘᴏ ᴍᴜʟᴜ sɪʜ, ᴊᴀʀɪ ᴊᴇᴍᴘᴏʟ sᴇᴍᴜᴀ sᴏᴀʟ ɴʏᴀ😂")
                        
                        elif cmd == "aduh" or text.lower() == 'waduh':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴡᴀᴅᴜʜ ᴋᴇɴᴀᴘᴀ ᴋᴋ\nᴋᴇᴊᴇᴅᴏᴛ ᴘɪɴᴛᴜ ʏᴀ. ᴇᴍᴀɴɢ ᴇɴᴀᴋ😂")
                               
                        elif cmd == "hus" or text.lower() == 'huss':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴅɪ ʟᴀʀᴀɴɢ ʙʀɪsɪᴋ ᴅɪ ʀᴏᴏᴍ ɪɴɪ ʙᴀɴʏᴀᴋ ʏᴀɴɢ ᴏʟᴇɴɢ😂")
                               
                        elif cmd == "pm":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴏʀʀʏ ᴀᴋᴜ ᴛɪᴅᴀᴋ ɴᴇʀɪᴍᴀ ᴘᴍ ᴏʀᴀɴɢ ᴊᴏᴍʙʟᴏ ɴɢᴇɴᴇs😜")

                        elif text.lower() == "midku":
                          if wait["selfbot"] == True:
                               sendTextTemplate(msg.to, msg._from)
                               
                        elif cmd == "ngopi" or text.lower() == 'ngopi susu guys':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴜᴅᴀʜ ᴘᴀᴅᴀ ɴɢᴏᴘɪ ʙᴇʟᴜᴍ ᴋᴋ, ᴋᴀʟᴏ ʙᴇʟᴜᴍ sɪɴɪ ᴋᴋ ɴʏᴜsᴜ ʙᴀʀᴇɴɢ 😜")
                               
                        elif cmd == "nah" or text.lower() == 'nahhh':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ɴᴀʜ ɴᴏʜ ɴᴀʜ ɴᴏʜ\nᴘᴀʟᴀᴋ ᴋᴜ ᴍᴜᴍᴇᴛ\nᴋʟᴏ ʟᴜ ʙɪʟᴀɴɢ ɴᴀʜ ɴᴏʜ😂")
                               
                        elif cmd == "salken":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴀʟᴋᴇɴᴊᴜ ᴋᴋ\nsᴇᴍᴏɢᴀ ᴀᴡᴀʟ ᴋɪᴛᴀ ᴋᴇɴᴀʟ\nʙɪsᴀ ᴊᴀᴅɪ ᴊᴏᴅᴏʜ ʏᴀ ᴋᴋ😍")
                               
                        elif cmd == "bomat":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴀᴋᴜ ᴍᴀʜ ʙᴏᴅᴏʜ ᴀᴍᴀᴛ\nᴇᴍᴀɴɢ ɴʏᴀ ʟᴜ sɪᴀᴘᴀ😂")
                               
                        elif cmd == "cipok":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴄɪᴘᴏᴋ ᴄɪᴘᴏᴋ ᴄɪᴘᴏᴋ\nᴋᴇɴᴄɪɴɢ ʟᴜ ᴀᴊᴀ ᴍᴀsɪʜ ɢᴋ ʟᴜʀᴜs\nᴍᴀᴜ ᴄɪᴘᴏᴋ ᴏʀᴀɴɢ😜")

                        elif cmd == "janda":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴇᴍᴀɴɢ ᴋᴀᴜ ᴊᴀɴᴅᴀ ᴋᴋ\nᴇᴍᴀɴɢ ᴍᴀᴜ sᴀᴍᴀ ᴊᴀɴᴅᴀ ᴀɴᴀᴋ 3 ᴋᴋ\nᴛᴀᴘɪ sᴀʏᴀɴɢ ᴜᴅᴀʜ ᴀɴᴜ ᴘᴜɴʏᴀ ᴋᴋ 😂")

                        elif cmd == "duda":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴇᴍᴀɴɢ ᴀᴋᴜ ᴅᴜᴅᴀ ᴋᴋ,,,\nᴋʟᴏ ᴋᴋ ᴍᴀᴜ ᴀᴍᴀ ᴅᴜᴅᴀ\nᴀʏᴜᴋ ᴋɪᴛᴀ ᴊᴀᴅɪᴀɴ😂")

                        elif cmd == "salam":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")

                        elif cmd == "bot":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ʙᴀᴛ ʙᴏᴛ ʙᴀᴛ ʙᴏᴛ ᴍᴀᴛᴀᴍᴜ ɪᴛᴜ ʙᴏᴛ\nᴀᴋᴜ ᴍᴀʜ ʙᴜᴋᴀɴ ʙᴏᴛ\nᴛᴀᴘɪ ʙᴀᴘᴀᴋᴇ ʙᴏᴛ 😜")

                        elif cmd == "siang":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sɪᴀɴɢ ᴊᴜɢᴀ ᴋᴋ ᴋᴜ sʏᴀɴᴛɪᴋ, ᴜᴅᴀʜ ᴅᴀᴘᴀᴛ ᴛɪᴋᴜɴɢᴀɴ ʙᴇʟᴜᴍ ᴋᴋ 😅")

                        elif cmd == "pagi":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴘᴀɢɪ ᴊᴜɢᴀ ᴋᴋ, ᴜᴅᴀʜ sᴀʀᴀᴘᴀɴ ʙᴇʟᴜᴍ 😘")

                        elif cmd == "sore":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴏʀᴇ ᴊᴜɢᴀ ᴋᴋ, ᴜᴅᴀʜ ᴍᴀɴᴅɪ ʙᴇʟᴜᴍ, ᴋᴀʟᴏ ʙᴇʟᴜᴍ sɪɴɪ ᴀᴋᴜ ᴛᴇᴍᴇɴɪ ᴋᴋ ᴍᴀɴᴅɪ 🤗هُ")

                        elif cmd == "malam":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴍᴀʟᴀᴍ ᴊᴜɢᴀ ᴋᴋ, ᴡᴀᴋᴛᴜ ɴʏᴀ ɴɪᴋᴜɴɢ ᴇɴᴀᴋ ɴʏᴀ ᴍᴀʟᴀᴍ-ᴍᴀʟᴀᴍ ɢɪɴɪ ᴋᴋ 😛")

                        elif cmd == "kojom":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ɴᴀʜ ᴋᴀɴ,,,ɴɢᴀᴊᴀᴋɪɴ ᴋᴏᴊᴏᴍ,,,ɴᴛᴀʀ ʙᴏᴊᴏɴᴇ ᴍᴀʀᴀʜ ʙᴀʀᴜ ᴛᴀᴜ ʀᴀsᴀ ᴋᴋ 😜هُ")

                        elif cmd == "nikung":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴀʏᴜᴋ ᴋᴋ ᴋɪᴛᴀ ɴɪᴋᴜɴɢ, ʟᴀɴɢsᴜɴɢ ᴘᴍ ᴀᴊᴀ ʏᴀ ᴋᴋ😂")

                        elif cmd == "assalamualaikum" or text.lower() == 'asalamualaikum':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")

                        elif cmd == "susu" or text.lower() == 'nyusu':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴜsᴜ sᴜsᴜ sᴜsᴜ, ᴅᴀʀɪ ᴋᴇᴄɪʟ ʟᴜ sᴜᴅᴀʜ ᴅɪ ɴʏᴜsᴜɪɴ, ᴍᴀsᴀ ᴍɪɴᴛᴀ ɴʏᴜsᴜ sᴀᴍᴀ ʀᴏɴᴅᴏ ᴋᴋ😂")

                        elif cmd == "setan":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴇᴛᴀɴ sᴇᴛᴀɴ sᴇᴛᴀɴ, ᴇᴍᴀɴɢ ᴍᴜᴋᴀ ʟᴜ ᴋᴀʏᴀᴋ sᴇᴛᴀɴ ᴋᴋ😂")

                        elif cmd == "makan":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴜᴅᴀʜ ᴘᴀᴅᴀ ᴍᴀᴋᴀɴ ʙᴇʟᴏᴍ ᴋᴋ, ᴋᴀʟᴏ ʙᴇʟᴏᴍ sɪɴɪ ᴀᴋᴜ sᴜᴀᴘɪɴ ᴋᴋ")

                        elif cmd == "minum":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sɪɴɪ ᴋᴋ ᴍɪɴᴜᴍ ʙᴀʀᴇɴɢ ᴋɪᴛᴀ😛")

                        elif cmd == "paymment":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴘᴀʏᴍᴇɴᴛ ᴠɪᴀ ʙᴀɴᴋ\nɴᴏ ʀᴇᴋ : 481901020711531\nᴀᴛᴀs ɴᴀᴍᴀ : muhazir\nʙᴀɴᴋ ʙʀɪ\n\nᴠɪᴀ ᴘᴜʟsᴀ\n085753228919\n08992906209 \n082358521114")

                        elif cmd == "wa'alaikumsalam" or text.lower() == 'waalaikumsalam':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ɴᴀʜ ɢɪᴛᴜ ᴊᴀᴡᴀʙ sᴀʟᴀᴍ sᴇsᴀᴍᴀ ᴍᴜsʟɪᴍ😘😍")


                        elif cmd == "about":
                                groups = cl.getGroupIdsJoined()
                                contacts = cl.getAllContactIds()
                                blockeds = cl.getBlockedContactIds()
                                crt = "u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540"
                                supp = "u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540"
                                suplist = []
                                lists = []
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nâ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "ᴀʙᴏᴜᴛ",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "size": "micro",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "CANNIBAL\nKILLER\nTEAM\nSELFBOT",
            "size": "xs",
            "color": "#FFFF00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": " {}".format(cl.getProfile().displayName),
                "size": "xs",
                "margin": "none",
                "color": "#ADFF2F",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "text": "ɢʀᴏᴜᴘ: {}".format(str(len(groups))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "ғʀɪᴇɴᴅ: {}".format(str(len(contacts))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "ʙʟᴏᴄᴋ: {}".format(str(len(blockeds))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
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
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CANNIBAL",
        "size": "xs",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~4rman3"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text",
        "text": "ᴋɪʟʟᴇʀ",
        "size": "xs",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~4rman3"
        },
        "align": "center"
      }
    ]
  }
}
}
                                cl.postTemplate(to, data)

                        elif cmd == "aim":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                  musik(to)
                                  
                        elif cmd == ".me" or text.lower() == 'gue':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': mid}
                                cl.sendContact(to, mid)

                        elif "autoreject " in msg.text.lower():
                            xpesan = msg.text.lower()
                            xres = xpesan.replace("autoreject ","")
                            if xres == "off":
                                settings['autorejc'] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʀᴇᴊᴇᴄᴛ ᴏғғ ɢᴀᴋ ᴀᴍᴀɴ ᴅᴀᴅɪ sᴘᴀᴍ")
                            elif xres == "on":
                                settings['autorejc'] = True
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʀᴇᴊᴇᴄᴛ ᴏɴ ᴀᴍᴀɴ ᴅᴀʀɪ sᴘᴀᴍ")
                        
                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)
                        elif text.lower() == "mymid":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(mi.displayName)+"\nᴍɪᴅ : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'u03addfbbbdb20585381383e5d173d28d': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate8(msg.to, "ɴᴀᴍᴀ : "+str(mi.displayName)+"\nᴍɪᴅ : " +key1+"\nsᴛᴀᴛᴜs ᴍsɢ"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in creator:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13 
                               msg.contentMetadata = {'mid': Fmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Jmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13 
                               msg.contentMetadata = {'mid': Zmid}
                               cl.sendMessage1(msg)

                        elif text.lower() == "hapuschat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   sendTextTemplate(msg.to,"🔹ʜᴀᴘᴜs ᴄʜᴀᴛ ᴅᴏɴᴇ")
                               except:
                                   pass

                        elif text.lower() == "all clear":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   ki.sendMessage(msg.to,"🔹ʜᴀᴘᴜs ᴄʜᴀᴛ ʙᴏᴛ ᴅᴏɴᴇ")
                                   kk.removeAllMessages(op.param2)
                                   kk.sendMessage(msg.to,"🔹ʜᴀᴘᴜs ᴄʜᴀᴛ ʙᴏᴛ ᴅᴏɴᴇ")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to,"🔹ʜᴀᴘᴜs ᴄʜᴀᴛ ʙᴏᴛ ᴅᴏɴᴇ")                              
                                   sendTextTemplate(msg.to,"🔹ʜᴀᴘᴜs ᴄʜᴀᴛ ʙᴏᴛ ᴅᴏɴᴇ")
                               except:
                                   pass
                        
                        elif cmd.startswith("bs1: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media1.giphy.com/media/fnKtAO0GLeiD6/200w.webp?cid=19f5b51a5c454d542f704f7a6395da37",
        "action": {
          "uri": "http://line.me/ti/p/~4rman3",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "color": "#FF0000",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ᴘʀᴏᴍᴏ",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~4rman3"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "CANNIBAL BOT",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   #cl.postFlex(group, data)
                              #     
                       # elif cmd.startswith("broadcast: "):
                      #    if wait["selfbot"] == True:
                    #        if msg._from in admin:
                   #            sep = text.split(" ")
                   #            pesan = text.replace(sep[0] + " ","")
                #               saya = cl.getGroupIdsJoined()
                  #             for group in saya:
                #                   sendTextTemplate8(group,"[ ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ᴋᴋ ]\n" + str(pesan))
#
                #        elif "hah" in msg.text.lower():
                 #                   url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                #                    to = msg.to
                   #                 data = {
                     #                           "type": "template",
                   #                             "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                    #                            "template": {
                      #                             "type": "image_carousel",
                       #                            "columns": [
                         #                           {
                              #                          "imageUrl": "https://4.bp.blogspot.com/-W_bn2qqdYXE/Wyhbjj2wqKI/AAAAAAANIz4/KQVsbq-aXm0kZNfFOS5SN8fqCvQ18xnUACLcBGAs/s1600/AW1238502_03.gif",
                                    #                    "size": "full", 
                                 #                       "action": {
                                    #                        "type": "uri",
                                  #                          "uri": "http://line.me/ti/p/~muhajir_alwi"
               #                  }                                                
              #         }
               #       ]
                                #                }
                      #                      }
                           #         cl.postTemplate(to, data)
                             #       
                  #      elif "sedih" in msg.text.lower():
                      #              url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                   #                 to = msg.to
                      #              data = {
                          #                      "type": "template",
                         #                       "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                         #                       "template": {
                         #                          "type": "image_carousel",
                          #                         "columns": [
                          #                          {
                           #                             "imageUrl": "https://3.bp.blogspot.com/-OfIz4mSIumw/WbLEZw7l6nI/AAAAAAARd6Y/Dxzos1SA_5MU32bXFTKToLDndM7YpV7WACLcBGAs/s1600/AW529310_04.gif",
                         #                               "size": "full", 
                             #                           "action": {
                              #                              "type": "uri",
                             #                               "uri": "http://line.me/ti/p/~muhajir_alwi"
              #                   }                                                
               #        }
                  #    ]
                         #                       }
                          #                  }
                      #              cl.postTemplate(to, data) 
                                  #  
                      #  elif "hadeh" in msg.text.lower():
                        #            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                       #             to = msg.to
                        #            data = {
                       #                         "type": "template",
                        #                        "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                               #                 "template": {
                         #                          "type": "image_carousel",
                       #                            "columns": [
                         #                           {
                          #                              "imageUrl": "https://i.ibb.co/dJ1H13M/Benjol.gif",
                            #                            "size": "full", 
                             #                           "action": {
                             #                               "type": "uri",
                              #                              "uri": "http://line.me/ti/p/~muhajir_alwi"
                          #       }                                                
            #           }
           #           ]
                #                                }
                   #                         }
                    #                cl.postTemplate(to, data)
                       #
                #        elif "bomat" in msg.text.lower():
                 #                   url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                    #                to = msg.to
                  #                  data = {
                    #                            "type": "template",
                 #                               "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                      #                          "template": {
                          #                         "type": "image_carousel",
                          #                         "columns": [
                          #                          {
                            #                            "imageUrl": "https://lh3.googleusercontent.com/-xNJ4AMTRxv4/Wx92ZYSEflI/AAAAAAACsvA/KK44SSrO6dYlR7Xig15WXDN7oCcUS6fPwCJoC/w480-h480-n/gplus-1561983519.gif",
                           #                             "size": "full", 
                         #                               "action": {
                        #                                    "type": "uri",
                        #                                    "uri": "http://line.me/ti/p/~muhajir_alwi"
                      #           }                                                
                #       }
             #         ]
                    #                            }
                   #                         }
                   #                 cl.postTemplate(to, data)
              #                      
                  #      elif "asem" in msg.text.lower():
                #                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
              #                      to = msg.to
                 #                   data = {
                     #                           "type": "template",
                  #                              "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                     #                           "template": {
                    #                               "type": "image_carousel",
                      #                             "columns": [
                   #                                 {
                       #                                 "imageUrl": "https://1.bp.blogspot.com/-j51nCknouj8/WDwHtTJUqKI/AAAAAAALmo8/qax6OG7QAmQs6aICNGwSP0CkebJzAbOSgCLcB/s1600/AS001874_19.gif",
                         #                               "size": "full", 
                       #                                 "action": {
                       #                                     "type": "uri",
                        #                                    "uri": "http://line.me/ti/p/~muhajir_alwi"
                      #           }                                                
                #       }
                #      ]
                     #                           }
                      #                      }
                                  #  cl.postTemplate(to, data)
                          #          
                        #elif "biarin" in msg.text.lower():
                      #              url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                       #             to = msg.to
                       #             data = {
                             #                   "type": "template",
                              #                  "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                              #                  "template": {
                             #                      "type": "image_carousel",
                               #                    "columns": [
                              #                      {
                               #                         "imageUrl": "https://2.bp.blogspot.com/-ZlkxlajQM4k/WMlfThHb6eI/AAAAAAAOBf4/BNwKEazXVbc2xK2acnDck8MLJZ21lCeJwCLcB/s1600/AW392405_04.gif",
                                #                        "size": "full", 
                                 #                       "action": {
                                  #                          "type": "uri",
                              #                              "uri": "http://line.me/ti/p/~muhajir_alwi"
                           #      }                                                
                  #     }
                 #     ]
                            #                    }
                           #                 }
                            #        cl.postTemplate(to, data)                                                         
                        #            
                      #  elif "otw" in msg.text.lower():
                       #             url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                        #            to = msg.to
                         #           data = {
                         #                       "type": "template",
                           #                     "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                             #                   "template": {
                              #                     "type": "image_carousel",
                                #                   "columns": [
                               #                     {
                               #                         "imageUrl": "https://1.bp.blogspot.com/-CSIjz01zHi0/WMlfTS0Qw2I/AAAAAAAOBf0/7gw5JrbNbkQe-rdMqaNGuhhVBpE4snhWACLcB/s1600/AW392405_03.gif",
                              #                          "size": "full", 
                               #                         "action": {
                               #                             "type": "uri",
                              #                              "uri": "http://line.me/ti/p/~muhajir_alwi"
                            #     }                                                
                    #   }
                 #     ]
                         #                       }
                            #                }
                                 #   cl.postTemplate(to, data)
   
                    #    elif "oke" in msg.text.lower():
                       #             url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                     #               to = msg.to
                   #                 data = {
                    #                            "type": "template",
                     #                           "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                     #                           "template": {
                    #                               "type": "image_carousel",
                    #                               "columns": [
                     #                               {
                      #                                  "imageUrl": "https://3.bp.blogspot.com/-_ZZg6eH89Gc/WE95b91DwsI/AAAAAAAEpnI/tWy69rJIAmsPx7clwzBhVXiSOdpZSp4NACLcB/s1600/AW305486_05.gif",
                      #                                  "size": "full", 
                    #                                    "action": {
                        #                                    "type": "uri",
                        #                                    "uri": "http://line.me/ti/p/~muhajir_alwi"
                       #          }                                                
                   #    }
               #       ]
                    #                            }
                #                            }
                   #                 cl.postTemplate(to, data)
                   #                 
                #        elif "sue" in msg.text.lower():
                  #                  url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                  #                  to = msg.to
                #                    data = {
                 #                               "type": "template",
                 #                               "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                   #                             "template": {
                 #                                  "type": "image_carousel",
                      #                             "columns": [
                 #                                   {
                    #                                    "imageUrl": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                     #                                   "size": "full", 
                      #                                  "action": {
                        #                                    "type": "uri",
                        #                                    "uri": "http://line.me/ti/p/~muhajir_alwi"
                       #          }                                                
               #        }
               #       ]
                   #                             }
                   #                         }
                #                    cl.postTemplate(to, data)
                #                    
               #         elif "wkwk" in msg.text.lower():
                       #             url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                         #           to = msg.to
                           #         data = {
                              #                  "type": "template",
                              #                  "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                              #                  "template": {
                                #                   "type": "image_carousel",
                                 #                  "columns": [
                                  #                  {
                                  #                      "imageUrl": "https://thumbs.gfycat.com/QuaintScornfulAmericanlobster-small.gif",
                                  #                      "size": "full", 
                                  #                      "action": {
                                     #                       "type": "uri",
                                    #                        "uri": "http://line.me/ti/p/~muhajir_alwi"
                      #           }                                                
                  #     }
                  #    ]
                         #                       }
                            #                }
                          #          cl.postTemplate(to, data)
                      #           
                    #    elif "coba" in msg.text.lower():                     	
                       #             url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                         #           to = msg.to
                          #          data = {
                             #                   "type": "template",
                            #                    "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                              #                  "template": {
                             #                      "type": "image_carousel",
                                 #                  "columns": [
                                 #                   {
                               #                         "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/32128231/IOS/sticker_animation@2x.png",
                              #                          "size": "full", 
                              #                          "action": {
                             #                               "type": "uri",
                              #                              "uri": "http://line.me/ti/p/~muhajir_alwi"
                  #               }                                                
               #        }
              #        ]
                #                                }
                    #                        }
                           #         cl.postTemplate(to, data)
         #
                  #      elif "wah" in msg.text.lower():                     	
                         #           url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                          #          to = msg.to
                              #      data = {
                                #                "type": "template",
                               #                 "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                 #               "template": {
                                  #                 "type": "image_carousel",
                               #                    "columns": [
                              #                      {
                                #                        "imageUrl": "https://appstickers-cdn.appadvice.com/1161475669/819158103/5950933cc2b8a0948941fc446c3e1938-5.gif",
                                  #                      "size": "full", 
                                    #                    "action": {
                              #                              "type": "uri",
                               #                             "uri": "http://line.me/ti/p/~muhajir_alwi"
                 #                }                                                
                #       }
               #       ]
                     #                           }
                     #                       }
                          #          cl.postTemplate(to, data)
                         #           
                    #    elif "cium" in msg.text.lower():                     	
                          #          url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            #        to = msg.to
                               #     data = {
                               #                 "type": "template",
                                #                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                               #                 "template": {
                                #                   "type": "image_carousel",
                              #                     "columns": [
                              #                      {
                                #                        "imageUrl": "https://i.ibb.co/CVMQ40k/7c8ab257ee3b7e1ef283b7c0a35d9d2c.gif",
                               #                         "size": "full", 
                              #                          "action": {
                                     #                       "type": "uri",
                            #                                "uri": "http://line.me/ti/p/~muhajir_alwi"
                         #        }                                                
                   #    }
                    #  ]
                        #                        }
                             #               }
                                 #   cl.postTemplate(to, data)
           #
                      #  elif "gombal" in msg.text.lower():
                           #         url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                          #          to = msg.to
                               #     data = {
                              #                  "type": "template",
                                 #               "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                 #               "template": {
                                   #                "type": "image_carousel",
                                    #               "columns": [
                                    #                {
                                  #                      "imageUrl": "https://thumbs.gfycat.com/KlutzyUglyGelding-small.gif",
                               #                         "size": "full", 
                                   #                     "action": {
                                   #                         "type": "uri",
                                      #                      "uri": "http://line.me/ti/p/~muhajir_alwi"
                          #       }                                                
                 #      }
                  #    ]
                       #                         }
                         #                   }
                          #          cl.postTemplate(to, data)
                        #            
                      #  elif "diam" in msg.text.lower():
                           #         url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                             #       to = msg.to
                              #      data = {
                                 #               "type": "template",
                               #                 "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                      #          "template": {
                                     #              "type": "image_carousel",
                                         #          "columns": [
                                    #                {
                                         #               "imageUrl": "https://thumbs.gfycat.com/BigIdealAsianelephant-small.gif",
                                        #                "size": "full", 
                                    #                    "action": {
                                     #                       "type": "uri",
                                            #                "uri": "http://line.me/ti/p/~muhajir_alwi"
                    #             }                                                
             #          }
                 #     ]
               #                                 }
                      #                      }
                        #            cl.postTemplate(to, data)
                           #         
                    #    elif "sepi" in msg.text.lower():
                       #             url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                           #         to = msg.to
                          #          data = {
                            #                    "type": "template",
                                   #             "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                            #                    "template": {
                                     #              "type": "image_carousel",
                           #                        "columns": [
                                      #              {
                              #                          "imageUrl": "https://i.ibb.co/hHG5Mwb/AW316819-05.gif",
                                    #                    "size": "full", 
                                              #          "action": {
                                     #                       "type": "uri",
                                  #                          "uri": "http://line.me/ti/p/~muhajir_alwi"
                               #  }                                                
                #       }
                   #   ]
                            #                    }
                                       #     }
                                 #   cl.postTemplate(to, data)
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendTextTemplate(msg.to, "🔹ɢᴀɢᴀʟ ᴍᴇɴɢɢᴀɴᴛɪ ᴋᴇʏ")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sendTextTemplate(msg.to, "🔹sᴇᴛᴋᴇʏ\n🔹ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               sendTextTemplate(msg.to, "🔹sᴇᴛᴋᴇʏ\n🔹ᴋᴇᴍʙᴀʟɪ ᴋᴇ ᴀᴡᴀʟ")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔹ᴡᴀɪᴛ....")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               sendTextTemplate(msg.to, "🔹ᴅᴏɴᴇ ʀᴇsᴛᴀʀᴛ...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "🔹ʙᴏᴛ ᴀᴋᴛɪғ sᴇʟᴀᴍᴀ🔹\n" +waktu(eltime)
                               sendTextTemplate(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "🔹ᴛᴇʀᴛᴜᴛᴜᴘ"
                                    gTicket = "♦️ᴛɪᴅᴀᴋ ᴀᴅᴀ"
                                else:
                                    gQr = "🔹ᴛᴇʀʙᴜᴋᴀ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate(msg.to, "🔹CANNIBAL KILLER🔹ɢʀᴜᴘ ɪɴғᴏ\n\n🔹ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(G.name)+ "\n🔹ɪᴅ ɢʀᴜᴘ : {}".format(G.id)+ "\n🔹ᴘᴇᴍʙᴜᴀᴛ : {}".format(G.creator.displayName)+ "\n🔹ᴡᴀᴋᴛᴜ ᴅɪ ʙᴜᴀᴛ : {}".format(str(timeCreated))+ "\n🔹ᴊᴜᴍʟᴀʜ ᴀɴɢɢᴏᴛᴀ : {}".format(str(len(G.members)))+ "\n🔹ᴊᴜᴍʟᴀʜ ᴘᴇɴᴅɪɴɢᴀɴ : {}".format(gPending)+ "\n🔹ɢʀᴜᴘ ǫʀ : {}".format(gQr)+ "\n🔹ɢʀᴜᴘ ᴛɪᴄᴋᴇᴛ : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                            except Exception as e:
                                sendTextTemplate(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
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
                                    gCreator = "🔹ᴛɪᴅᴀᴋ ᴅɪ ᴛᴇᴍᴜᴋᴀɴ"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "🔹ᴛᴇʀᴛᴜᴛᴜᴘ"
                                    gTicket = "♦️ᴛɪᴅᴀᴋ ᴀᴅᴀ"
                                else:
                                    gQr = "🔹ᴛᴇʀʙᴜᴋᴀ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "🔹ᴄᴍᴅ ɢʀᴜᴘ ɪɴғᴏ🔹\n"
                                ret_ += "\n🔹ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(G.name)
                                ret_ += "\n🔹ɪᴅ ɢʀᴜᴘ : {}".format(G.id)
                                ret_ += "\n🔹ᴘᴇᴍʙᴜᴀᴛ : {}".format(gCreator)
                                ret_ += "\n🔹ᴡᴀᴋᴛᴜ ᴅɪʙᴜᴀᴛ : {}".format(str(timeCreated))
                                ret_ += "\n🔹ᴊᴜᴍʟᴀʜ ᴀɴɢɢᴏᴛᴀ : {}".format(str(len(G.members)))
                                ret_ += "\n🔹ᴊᴜᴍʟᴀʜ ᴘᴇɴᴅɪɴɢᴀɴ : {}".format(gPending)
                                ret_ += "\n🔹ɢʀᴜᴘ ǫʀ : {}".format(gQr)
                                ret_ += "\n🔹ɢʀᴜᴘ ᴛɪᴄᴋᴇᴛ : {}".format(gTicket)
                                ret_ += ""
                                sendTextTemplate8(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
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
                                    ret_ += "\n " "├🔹"+ str(no) + ". " + mem.displayName
                                sendTextTemplate(to," 🔹ɢʀᴜᴘ ɴᴀᴍᴇ : [ " + str(G.name) + " ]\n\n   [ʟɪsᴛ ᴀɴɢɢᴏᴛᴀ ]\n" + ret_ + "\n\n🔹ᴛᴏᴛᴀʟ %i ᴀɴɢɢᴏᴛᴀ🔹" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    km.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    ko.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    kf.leaveGroup(i)
                                    kg.leaveGroup(i)
                                    kh.leaveGroup(i)
                                    sendTextTemplate4(msg.to,"🔹ᴅᴏɴᴇ ᴋᴇʟᴜᴀʀ ɢʀᴜᴘ" +str(ginfo.name))

                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├🔹" + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate(msg.to,"╭── 🔹ɢʀᴏᴜᴘ ʟɪsᴛ🔹\n│\n"+ma+"│\n╰──🔹ᴛᴏᴛᴀʟ"+str(len(gid))+"ɢʀᴏᴜᴘ🔹")

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
                                   ma += "├🔹" + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate(msg.to,"╭── 🔹ɢʀᴏᴜᴘ ʟɪsᴛ🔹\n│\n"+ma+"│\n╰──🔹ᴛᴏᴛᴀʟ"+str(len(gid))+"ɢʀᴏᴜᴘ🔹")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├🔹" + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╭── 🔹ɢʀᴏᴜᴘ ʟɪsᴛ🔹\n│\n"+ma+"│\n╰──🔹ᴛᴏᴛᴀʟ"+str(len(gid))+"ɢʀᴏᴜᴘ🔹")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├🔹" + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╭── 🔹ɢʀᴏᴜᴘ ʟɪsᴛ🔹\n│\n"+ma+"│\n╰──🔹ᴛᴏᴛᴀʟ"+str(len(gid))+"ɢʀᴏᴜᴘ🔹")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├🔹" + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╭── 🔹ɢʀᴏᴜᴘ ʟɪsᴛ🔹\n│\n"+ma+"│\n╰──🔹ᴛᴏᴛᴀʟ"+str(len(gid))+"ɢʀᴏᴜᴘ🔹")
                               
                        elif cmd == "gruplist4":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ko.getGroupIdsJoined()
                               for i in gid:
                                   G = ko.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├🔹" + str(a) + ". " +G.name+ "\n"
                               ko.sendMessage(msg.to,"╭── 🔹ɢʀᴏᴜᴘ ʟɪsᴛ🔹\n│\n"+ma+"│\n╰──🔹ᴛᴏᴛᴀʟ"+str(len(gid))+"ɢʀᴏᴜᴘ🔹")                               

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   sendTextTemplate(msg.to, "🔹ᴏᴘᴇɴ ᴜʀʟ")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendTextTemplate(msg.to, "🔹ᴄʟᴏsᴇ ᴜʀʟ")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(x.name)+ "\nᴜʀʟ ɢʀᴜᴘ : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif cmd == "gantifoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif cmd == "bot1":
                            if msg._from in admin:
                                Setmain["RAfoto"][Amid] = True
                                ki.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif cmd == "bot2":
                            if msg._from in admin:
                                Setmain["RAfoto"][Bmid] = True
                                kk.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif cmd == "bot3":
                            if msg._from in admin:
                                Setmain["RAfoto"][Cmid] = True
                                kc.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif cmd == "bot4":
                            if msg._from in admin:
                                Setmain["RAfoto"][Dmid] = True
                                ko.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")                                
                                
                        elif cmd == "bot5":
                            if msg._from in admin:
                                Setmain["RAfoto"][Emid] = True
                                sw.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")                                
                                
                        elif cmd == "bot6":
                            if msg._from in admin:
                                Setmain["RAfoto"][Fmid] = True
                                sw.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")                                
                                
                        elif cmd == "bot7":
                            if msg._from in admin:
                                Setmain["RAfoto"][Gmid] = True
                                sw.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")                                
                                
                        elif cmd == "bot8":
                            if msg._from in admin:
                                Setmain["RAfoto"][Hmid] = True
                                sw.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")                                
                                
                        elif cmd == "bot9":
                            if msg._from in admin:
                                Setmain["RAfoto"][Imid] = True
                                sw.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")                                
                                
                        elif cmd == "bot10":
                            if msg._from in admin:
                                Setmain["RAfoto"][Jmid] = True
                                sw.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")                                
                                
                        elif cmd == "bot11":
                            if msg._from in admin:
                                Setmain["RAfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                sendTextTemplate(msg.to,"🔹ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")

                        elif cmd.startswith("bot1gname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"🔹ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")

                        elif cmd.startswith("bot2gname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"🔹ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")

                        elif cmd.startswith("bot3gname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"🔹ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")
                                
                        elif cmd.startswith("bot4gname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ko.getProfile()
                                profile.displayName = string
                                ko.updateProfile(profile)
                                ko.sendMessage(msg.to,"🔹ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")

                        elif cmd.startswith("bot5gname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"🔹ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "woy" or text.lower() == 'colok':
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

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"🔹ʟɪsᴛ ʙᴏᴛ🔹\n\n"+ma+"\n🔹ᴛᴏᴛᴀʟ ʙᴏᴛ ᴀʙɪ「%s」🔹" %(str(len(Bots))))

                        elif cmd == "ladmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
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
                                sendTextTemplate3(msg.to,"♦️ADMIN CANNIBAL♦️\n\n♦️sᴜᴘᴇʀ ᴀᴅᴍɪɴ :\n"+ma+"\n♦️ᴀᴅᴍɪɴ :\n"+mb+"\n♦️sᴛᴀғғ :\n"+mc+"\n♦️JUMLAH ADMIN CANNIBAL「%s」♦️" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
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
                                sendTextTemplate3(msg.to,"🔹ADMIN CANNIBAL🔹\n\n🔹sᴜᴘᴇʀ ᴀᴅᴍɪɴ :\n"+ma+"\n🔹ᴀᴅᴍɪɴ :\n"+mb+"\n🔹sᴛᴀғғ :\n"+mc+"\n🔹JUMLAH ADMIN CANNIBAL「%s」🔹" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                sendTextTemplate(msg.to,"🔹ᴄᴇᴋ ᴘʀᴏ ɢʀᴏᴜᴘ🔹\n\n🔹ᴘʀᴏ ᴜʀʟ :\n"+ma+"\n🔹ᴘʀᴏ ᴋɪᴄᴋ :\n"+mb+"\n🔹ᴘʀᴏ ᴊᴏɪɴ :\n"+md+"\n🔹ᴘʀᴏ ᴄᴀɴᴄᴇʟ :\n"+mc+"\n🔹ᴊᴜᴍʟᴀʜ  %s ɢʀᴏᴜᴘ CANNIBAL JAGA🔹" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "cannibal":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                ko.sendMessage(msg.to,responsename4)
                                jk.sendMessage(msg.to,responsename5)

                        elif cmd == "join":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    ki.acceptGroupInvitation(msg.to)
                                    ko.acceptGroupInvitation(msg.to)
                                    jk.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                    
                        elif cmd == "stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    sendTextTemplate(msg.to,"[ ɢʀᴏᴜᴘ ] \n🔹"+str(ginfo.name)+"\n 🔹sɪᴀᴘ ʙᴀsᴍɪ ᴋɪᴋɪʟ ᴛᴇᴍᴘᴇ")
                                except:
                                    pass             
                            

                        elif cmd == "out":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                ko.leaveGroup(msg.to)
                                jk.leaveGroup(msg.to)
                                
                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sendTextTemplate(msg.to, "🔹ɢᴏᴏᴅ ʙʏᴇ ᴄᴀʏᴀɴᴋ🔹\n       "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("joinall "):
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
                                ki.acceptGroupInvitationByTicket(group,Ticket)
                                kk.acceptGroupInvitationByTicket(group,Ticket)
                                kc.acceptGroupInvitationByTicket(group,Ticket)
                                ko.acceptGroupInvitationByTicket(group,Ticket)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 ᴍᴀsᴜᴋ ɢʀᴜᴘ」\nᴄʀᴇᴀᴛᴏʀ :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
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
                                ret_ += xpesan+zxc
                                ret_ += "• Nama grup : {}".format(G.name)
                                ret_ += "\n• Group Qr : {}".format(gQr)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                sendTextTemplate3(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "🔹ᴘᴀᴘᴀʏ sᴇᴍᴜᴀ ɴʏᴀ♦️")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        ko.leaveGroup(i)                                        
                                        sendTextTemplate4(to,"🔹ᴍᴏʟᴇ ᴅᴜʟᴜ ʏᴀ ᴍᴀᴜ ɴʏᴜsᴜ♦️" +h)

                        elif cmd == "in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                jk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                
                        elif cmd == "pasukan":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ki.sendMessage(msg.to, "ʀᴇᴀᴅʏ ʙᴏssᴋᴜ")
                               kk.sendMessage(msg.to, "ʀᴇᴀᴅʏ ʙᴏssᴋᴜ")
                               kc.sendMessage(msg.to, "ʀᴇᴀᴅʏ ʙᴏssᴋᴜ")
                               ko.sendMessage(msg.to, "ʀᴇᴀᴅʏ ʙᴏssᴋᴜ")
                               jk.sendMessage(msg.to, "ʀᴇᴀᴅʏ ʙᴏssᴋᴜ")
                                
                        elif cmd == "as1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "as2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "as3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)
                                
                        elif cmd == "as4":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ko.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ko.updateGroup(G)
                                
                        elif cmd == "js in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "js out":
                            if msg._from in admin:
                                G = sw.getGroup(msg.to)
                                sw.sendMessage(msg.to, "🔹ɢᴏᴏᴅ ʙʏᴇ🔹\n       "+str(G.name))
                                sw.leaveGroup(msg.to)

                        elif cmd == "lali":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                sendTextTemplate(msg.to, " 🔹ᴋᴇᴄᴇᴘᴀᴛᴀɴ ʀᴇsᴘᴏɴ🔹\n\n🔹ɢᴇᴛ ᴘʀᴏғɪʟᴇ\n🔹   %.10f\n🔹ɢᴇᴛ ᴄᴏɴᴛᴀᴄᴛ\n🔹   %.10f\n🔹ɢᴇᴛ ɢʀᴏᴜᴘ\n🔹   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == ".speed" or cmd == "sp bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} ᴅᴇᴛɪᴋ".format(str(elapsed_time/10)))
                               ki.sendMessage(msg.to, "{} ᴅᴇᴛɪᴋ".format(str(elapsed_time/10)))
                               kk.sendMessage(msg.to, "{} ᴅᴇᴛɪᴋ".format(str(elapsed_time/10)))
                               kc.sendMessage(msg.to, "{} ᴅᴇᴛɪᴋ".format(str(elapsed_time/10)))
                               ko.sendMessage(msg.to, "{} ᴅᴇᴛɪᴋ".format(str(elapsed_time/10)))
                               jk.sendMessage(msg.to, "{} ᴅᴇᴛɪᴋ".format(str(elapsed_time/10)))
                               
                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                sendTextTemplate(msg.to, "ᴡᴀɪᴛ...")
                                sendTextTemplate(msg.to, "╭───────────────────╮\n%.10f cannibal\n╰───────────────────╯" % (get_profile_time/3))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 sendTextTemplate(msg.to, "♦️Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 sendTextTemplate(msg.to, "♦️Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
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
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    sendTextTemplate(msg.to, "User kosong...")
                            else:
                                sendTextTemplate(msg.to, "Ketik lurking on dulu")

                        elif cmd == "janda on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate(msg.to, "🔹ᴄᴇᴋ ᴊᴀɴᴅᴀ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹\n\n🔹ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n🔹ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "janda off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(msg.to, "🔹ᴄᴇᴋ ᴊᴀɴᴅᴀ ᴅɪ ᴍᴀᴛɪᴋᴀɴ🔹\n\n🔹ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n🔹ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendTextTemplate(msg.to, "🔹sᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ🔹")

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n♦️ Lokasi : " + data[0]
                                         ret_ += "\n♦️ " + data[1]
                                         ret_ += "\n♦️ " + data[2]
                                         ret_ += "\n♦️ " + data[3]
                                         ret_ += "\n♦️ " + data[4]
                                         ret_ += "\n♦️ " + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  sendTextTemplate3(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "♦️Status Cuaca♦️"
                                    ret_ += "\n♦️ Lokasi : " + data[0].replace("❄Temperatur di kota ","")
                                    ret_ += "\n♦️ Suhu : " + data[1].replace("⛄Suhu : ","") + " C"
                                    ret_ += "\n♦️ Kelembaban : " + data[2].replace("💧Kelembaban : ","") + " %"
                                    ret_ += "\n♦️ Tekanan udara : " + data[3].replace("☁Tekanan udara : ","") + " HPa"
                                    ret_ += "\n♦️ Kecepatan angin : " + data[4].replace("🌀Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\n♦️Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n♦️Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                sendTextTemplate3(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "♦️Info Lokasi♦️"
                                    ret_ += "\n ♦️Location : " + data[0]
                                    ret_ += "\n ♦️Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                sendTextTemplate3(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric🎵 ]═════════"
                                          ret_ += "\n╠➩ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠➩ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠➩ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]═════════\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendMessage(msg.to, str(ret_))
                                   except:
                                       sendTextTemplate(to, "♦️Lirik tidak ditemukan")

                        elif cmd.startswith("music "):
                            if msg._from in admin:
                               sep = msg.text.split(" ")
                               query = msg.text.replace(sep[0] + " ","")
                               cond = query.split("-")
                               search = str(cond[0])
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   result = web.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                   data = result.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                      num = 0
                                      ret_ = "「 Pencarian Musik 」\n"
                                      for music in data["result"]:
                                          num += 1
                                          ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                      ret_ += "\n\n「 Total {} Pencarian 」".format(str(len(data["result"])))
                                      cl.sendMessage(to, str(ret_))
                                      sendMention(msg.to, msg._from,"","\nJika ingin menggunakan,\nSilahkan gunakan:\n\nMusik penyanyi-angka")
                                   if len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data["result"]):
                                               music = data["result"][num - 1]
                                               with requests.session() as web:
                                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                                    result = web.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                                    data = result.text
                                                    data = json.loads(data)
                                                    if data["result"] != []:
                                                         ret_ = "「 Pencarian Musik 」"
                                                         ret_ += "\n♦️Judul : {}".format(str(data["result"]["song"]))
                                                         ret_ += "\n♦️ Album : {}".format(str(data["result"]["album"]))
                                                         ret_ += "\n♦️ Ukuran : {}".format(str(data["result"]["size"]))
                                                         ret_ += " \n♦️ Link Musik : {}".format(str(data["result"]["mp3"]))
                                                         ret_ += "\n「 Tunggu Musiknya Keluar 」"
                                                         cl.sendImageWithURL(to, str(data["result"]["img"]))
                                                         cl.sendMessage(to, str(ret_))
                                                         cl.sendAudioWithURL(to, str(data["result"]["mp3"][0]))   
                     
                        elif cmd.startswith("music: "):
                           if msg._from in admin:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══( 〘 ᴍᴜsɪᴄ 〙)═══════"
                                          ret_ += "\n╠ ᴊᴜᴅᴜʟ ʟᴀɢᴜ: {}".format(str(song[0]))
                                          ret_ += "\n╠ ᴅᴜʀᴀsɪ: {}".format(str(song[1]))
                                          ret_ += "\n╠ ʟɪɴᴋ: {}".format(str(song[3]))
                                          ret_ += "\n╚══(〘 ᴡᴀɪᴛ ᴀᴜᴅɪᴏ 〙)═══════"
                                      cl.sendMessage(msg.to, str(ret_))
                                      cl.sendMessage(msg.to, "sᴀʙᴀʀ sᴇʙᴇɴᴛᴀʀ ʟᴀɢɪ ʟᴏᴀᴅɪɴɢ")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendMessage(to, "ᴍᴜsɪᴄ ᴇʀʀᴏʀ")

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendMessage(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("Abimp4: "):
                          if msg._from in admin:
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
                                    title = "ᴊᴜᴅᴜʟ〘 " + vid.title + " 〙"
                                    author = '\n\nᴀᴜᴛʜᴏʀ : ' + str(vid.author)
                                    durasi = '\nᴅᴜʀᴀsɪ : ' + str(vid.duration)
                                    suka = '\nʟɪᴋᴇ : ' + str(vid.likes)
                                    rating = '\nʀᴀᴛɪɴɢ : ' + str(vid.rating)
                                    deskripsi = '\nᴅᴇsᴋʀɪᴘsɪ : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("Abimp3: "):
                          if msg._from in admin:
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
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "♦️ᴊᴜᴅᴜʟ ♦️〘 " + vid.title + " 〙"
                                    author = '\n\n♦️ ᴀᴜᴛʜᴏʀ : ' + str(vid.author)
                                    durasi = '\n♦️ ᴅᴜʀᴀsɪ : ' + str(vid.duration)
                                    suka = '\n♦️ ʟɪᴋᴇ : ' + str(vid.likes)
                                    rating = '\n♦️ ʀᴀᴛɪɴɢ : ' + str(vid.rating)
                                    deskripsi = '\n♦️ ᴅᴇsᴋʀɪᴘ : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "♦️ Link : " + "https://www.instagram.com/" + instagram
                                text = "♦️ Name : "+namaIG+"\n♦️ Username : "+usernameIG+"\n♦️ Biography : "+bioIG+"\n♦️ Follower : "+followerIG+"\n♦️ Following : "+followIG+"\n♦️ Post : "+mediaIG+"\n♦️ Verified : "+verifIG+"\n♦️ Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

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
                            sendTextTemplate3(msg.to,"♦️ I N F O R M A S I ♦️\n\n"+"♦️ Date Of Birth : "+lahir+"\n♦️ Age : "+usia+"\n♦️ Ultah : "+ultah+"\n♦️ Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                sendTextTemplate(msg.to,"🔹ᴛᴏᴛᴀʟ sᴛᴀɢ ᴅɪ ʀᴜʙᴀʜ ᴊᴀᴅɪ " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate(msg.to,"🔹ᴛᴏᴛᴀʟ sᴘᴀᴍᴄᴀʟʟ ᴅɪ ʀᴜʙᴀʜ ᴊᴀᴅɪ " +strnum)

                        elif cmd.startswith("stag "):
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
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        sendTextTemplate(msg.to,"🔹ᴊᴜᴍʟᴀʜ ᴍᴇʟᴇʙɪʜɪ 1000♦️")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "🔹ᴅᴏɴᴇ ᴍᴇɴɢᴜɴᴅᴀɴɢ {} ᴘᴀɴɢɢɪʟᴀɴ ɢʀᴏᴜᴘ♦️".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        cl.acquireGroupCallRoute(to)
                                        cl.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    sendTextTemplate(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "sᴀᴍʙᴜᴛᴀɴ ᴀᴋᴛɪғ"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "🔹sᴀᴍʙᴜᴛᴀɴ sᴜᴅᴀʜ ᴀᴋᴛɪғ🔹\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "ᴀᴋᴛɪғ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🔹sᴀᴍʙᴜᴛᴀɴ ᴍᴀᴛɪ🔹\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "🔹sᴀᴍʙᴜᴛᴀɴ sᴜᴅᴀʜ ᴍᴀᴛɪ🔹"
                                    sendTextTemplate(msg.to, "🔹ᴛᴇᴡᴀs🔹\n" + msgs)
                                    
                        elif 'Js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "🔹sɪᴀᴘ ʙᴀɴᴛᴀɪ ᴋɪᴋɪʟ ᴛᴇᴍᴘᴇ"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "🔹ᴀɴᴛɪ ᴊs ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "🔹sᴜᴄᴄᴇs ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🔹ᴀɴᴛɪ ᴊs ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = ""
                                    sendTextTemplate(msg.to, "🔹sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ\n" + msgs)
                                    
                        elif 'Gs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "🔹sɪᴀᴘ ʙᴀɴᴛᴀɪ ᴋɪᴋɪʟ ᴛᴇᴍᴘᴇ"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "🔹sᴜᴄᴄᴇs ɢʜᴏsᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "🔹sᴜᴅᴀʜ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🔹sᴜᴄᴄᴇs ɴᴏɴᴀᴋᴛɪғᴋᴀɴ ɢʜᴏsᴛ\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = ""
                                    sendTextTemplate(msg.to, "🔹ɢʜᴏsᴛ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ\n" + msgs)

                        elif 'Allprotect ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allprotect ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "🔹sᴇᴍᴜᴀ ᴘʀᴏ sᴜᴅᴀʜ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "🔹ᴅᴏɴᴇ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴘʀᴏ🔹\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "sᴇᴍᴜᴀ ᴘʀᴏ ᴀᴋᴛɪғ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🔹ᴅᴏɴᴇ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴘʀᴏ🔹\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🔹sᴇᴍᴜᴀ ᴘʀᴏ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    sendTextTemplate(msg.to, "sᴇᴍᴜᴀ ᴘʀᴏ ᴅɪ ᴍᴀᴛɪᴋᴀɴ\n" + msgs)

#=========== KICKOUT ============#
                        elif ("babat " in msg.text):
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
                                           random.choice(ABC).acceptGroupInvitationByTicket(msg.to,Ticket)
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass
              
                        elif "Gusur" in msg.text:
                           if msg._from in Bots:
                            if msg.toType == 2:
                             #  print "Otw cleanse"
                               _name = msg.text.replace("Gusur","")
                               gs = ki.getGroup(msg.to)
                               gs = kk.getGroup(msg.to)
                               gs = kc.getGroup(msg.to)  
                               gs = ko.getGroup(msg.to)               
                               ki.sendMessage(msg.to,"🔹ɪ ᴍ sᴏʀʀʏ🔹")
                               targets = []
                               for g in gs.members:
                                   if _name in g.displayName:
                                       targets.append(g.mid)
                               if targets == []:
                                  ki.sendMessage(msg.to,"Not found")
                              #    else:
                               for target in targets:
                                     if target not in Bots:
                                      try:
                                          klist=[ki,kk,kc,ko,jk]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except:
                                          ki.sendMessage(msg.to,"♦️ᴘᴇʀᴍɪsɪ sᴇᴍᴜᴀ ɴʏᴀ♦️") 
                                       
                        elif cmd == "kibar":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ʜʜʜᴀᴀᴀᴀɪɪɪɪ!!! \nᴀᴘᴀ ᴋᴀʙᴀʀ sᴇᴍᴜᴀ\nᴍᴀᴀᴀғғғ ʀᴏᴏᴍ ᴋᴀʟɪᴀɴ ᴅᴀʟᴀᴍ ᴘᴇɴɢɢᴜsᴜʀᴀɴ \n\nᴋᴇʙᴀɴʏᴀᴋᴀɴ ʙᴀᴄᴏᴛ ᴅᴀɴ ᴀɴᴜ\ncannibal ᴅᴀɴ ᴛᴇᴀᴍ ʜᴀᴅɪʀ\nᴍᴀᴜ ʙᴀʙᴀᴛ ɢᴄ ɢᴀᴋ ᴊᴇʟᴀs\nɴᴏ ʙᴀᴄᴏᴛ \nɴᴏ ᴅᴇsᴀʜ \nɴᴏ ᴄᴏᴍᴍᴇɴᴛ \nɴᴏ ᴋᴏᴀʀ ᴋᴏᴀʀ \nɴᴏ ɴᴀɴɢɪs \nᴋᴀsɪᴀɴ ᴅᴇʟʟʟᴏᴏᴏ\nʀᴏᴏᴍ ᴏᴋᴇᴘ \nʀᴏᴏᴍ ᴊᴜᴅɪ\nʀᴏᴏᴍ ɢᴀᴋ ᴊᴇʟᴀs\nsɪᴀᴘ ᴋɪᴛᴀ ʙᴀʙᴀᴛ ᴅᴀɴ ʙᴀɴᴛᴀɪɪɪ \n\n\n\n ʙᴀᴘᴀᴋ ᴋᴀᴜᴜᴜ...\nᴋᴇɴᴀᴘᴀ ᴋᴀᴜ ᴅɪᴀᴍ ɴᴊɪɪɪɴɴɢɢɢɢ\nᴛᴀɴɢᴋɪss ɴʏᴇᴇᴛ ᴛᴀɴɢᴋɪss ᴊᴀɴɢᴀɴ ɴʏᴀᴍᴜᴋ ᴀᴊᴀ\n\n\nᴅᴀsᴀʀ ʀᴏᴏᴍ ᴘᴇᴀ ɢᴜᴏʙʟᴏᴋ sᴇᴛᴀɴ\nᴍᴀᴀғ ᴄᴇᴇᴇɴɢɢᴇɴɢ\nɢᴄ ᴋᴀᴜ ᴀᴋᴜ sɪᴛᴀ...!!!\n\n\n sᴀʟᴀᴍ ᴅᴀʀɪ ᴋᴀᴍɪ cannibal\n\nᴍᴀᴍᴘɪʀ ᴅɪ ɢᴄ ᴋᴀʟɪᴀɴ\n\nʀᴀᴛᴀ ɢᴀᴋ ʀᴀᴛᴀ ʏᴀɴɢ ᴘᴇɴᴛɪɴɢ ᴋɪʙᴀʀ ᴅᴀɴ ᴅᴇsᴀʜɪɴ ɢᴄ ᴋᴀᴜ \nʀᴀᴛᴀ ᴀᴋᴜ sᴇɴᴀɴɢ\nᴋʟᴏ ɢᴀᴋ ʀᴀᴛᴀ ᴛᴜɴɢɢᴜ ᴋᴇʜᴀᴅɪʀᴀɴ ᴀᴋᴜ ʟᴀɢɪ\n\n\n  >>⛔sᴀʟᴀᴍ ᴛᴇᴀᴍ cannibal killer⛔<< \n\n\n>>⛔cannibal ᴋɪʟʟᴇʀ ʟᴇsᴛ ɢᴏ⛔<<\n\n\n                    ᴄʀᴇᴀᴛᴏʀ\n\n<<<<<<<<<<CANNIBAL>>>>>>>>>>\n\nhttp://line.me/ti/p/~4rman3")
                               cl.sendContact(to, mid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)        
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)        
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)        
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)  
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)        
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)        
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)        
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)  
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Zmid)
                               cl.sendMessage(to, None, contentMetadata={"STKID":"56021040","STKPKGID":"3865357","STKVER":"1"}, contentType=7)
                               cl.sendMessage(to, None, contentMetadata={"STKID":"56021040","STKPKGID":"3865357","STKVER":"1"}, contentType=7)

                        elif ("Kick " in msg.text):
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

#===========ADMIN ADD============#
                        elif ("A " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ᴀᴅᴍɪɴ🔹")
                                       except:
                                           pass

                        elif ("S " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ sᴛᴀғғ🔹")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ʙᴏᴛ🔹")
                                       except:
                                           pass

                        elif ("Ha " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀᴅᴍɪɴ🔹")
                                       except:
                                           pass

                        elif ("Hs " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs sᴛᴀғғ🔹")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀᴅᴍɪɴ🔹")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                sebdTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif cmd == "admin:off" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif cmd == "staff:off" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif cmd == "bot:off" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
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
                                sendTextTemplate(msg.to,"🔹sᴜᴅᴀʜ sᴇɢᴀʀ ʙᴏssᴋᴜ🔹")

                        elif cmd == "kojoman" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "tikungan" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = True
                                sendTextTemplate(msg.to,"🔹ᴅᴇᴛᴇᴋsɪ ᴜɴsᴇɴᴅ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ??")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = False
                                sendTextTemplate(msg.to,"🔹ᴅᴇᴛᴇᴋsɪ ᴜɴsᴇɴᴅ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")
                                
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                sendTextTemplate(msg.to,"🔹ɴᴏᴛᴀɢ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                sendTextTemplate(msg.to,"🔹ɴᴏᴛᴀɢ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sendTextTemplate(msg.to,"🔹ᴅᴇᴛᴇᴋsɪ ᴄᴏɴᴛᴀᴄᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                sendTextTemplate(msg.to,"🔹ᴅᴇᴛᴇᴋsɪ ᴄᴏɴᴛᴀᴄᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                sendTextTemplate(msg.to,"🔹ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                sendTextTemplate(msg.to,"🔹ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴅɪ ᴍᴀᴛɪᴋᴀɴ🔹")
                                
                        elif cmd == "responpm on" or text.lower() == 'responpm on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["arespon"] = True
                                sendTextTemplate(msg.to,"🔹ʀᴇsᴘᴏɴᴘᴍ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "responpm off" or text.lower() == 'responpm off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["arespon"] = False
                                sendTextTemplate(msg.to,"🔹ʀᴇsᴘᴏɴᴘᴍ ᴅɪ ᴍᴀᴛɪᴋᴀɴ🔹")          

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                sendTextTemplate(msg.to,"🔹ᴀᴜᴛᴏ ᴊᴏɪɴ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                sendTextTemplate(msg.to,"🔹ᴀᴜᴛᴏ ᴊᴏɪɴ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")
                                
                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                sendTextTemplate(msg.to,"🔹ᴅᴇᴛᴇᴋsɪ sᴛɪᴄᴋᴇʀ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")            
                                
                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                sendTextTemplate(msg.to,"🔹ᴅᴇᴛᴇᴋsɪ sᴛɪᴄᴋᴇʀ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")         

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                sendTextTemplate(msg.to,"🔹ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                sendTextTemplate(msg.to,"🔹ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                sendTextTemplate(msg.to,"🔹ᴀᴜᴛᴏᴀᴅᴅ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                sendTextTemplate(msg.to,"🔹ᴀᴜᴛᴏᴀᴅᴅ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")
                                
                        elif cmd == "left on" or text.lower() == 'left on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["left"] = True
                                sendTextTemplate(msg.to,"🔹ʟᴇғᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "left off" or text.lower() == 'left off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["left"] = False
                                sendTextTemplate(msg.to,"🔹ʟᴇғᴛ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")
                                
                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                sendTextTemplate(msg.to,"🔹ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")
                                
                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                sendTextTemplate(msg.to,"🔹ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")          

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                sendTextTemplate(msg.to,"🔹ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                sendTextTemplate(msg.to,"🔹ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ʙʟᴀᴄᴋʟɪsᴛ🔹")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ʙʟᴀᴄᴋʟɪsᴛ🔹")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ʙʟᴀᴄᴋʟɪsᴛ🔹")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ʙʟᴀᴄᴋʟɪsᴛ🔹")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛɴʏᴀ🔹")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛɴʏᴀ🔹")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate(msg.to,"🔹ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʟᴀᴄᴋʟɪsᴛ🔹")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate3(msg.to,"🔹ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ🔹\n\n"+ma+"\n🔹ᴊᴜᴍʟᴀʜ「%s」ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ🔹" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                sendTextTemplate(msg.to,"🔹ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ🔹")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"🔹ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ🔹\n\n"+ma+"\n🔹ᴊᴜᴍʟᴀʜ「%s」ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ🔹" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "tersangka" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    sendTextTemplate(msg.to,"🔹ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʟᴀᴄᴋʟɪsᴛ🔹")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」ᴜsᴇʀ ʙʟᴀᴄᴋʟɪsᴛ" % len(ragets)
                              sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ʙᴜʀᴏɴᴀɴ🔹\n  "    +mc)
                              
                        elif text.lower() == 'paymment':
                               cl.sendMessage(msg.to, "ᴘᴀʏᴍᴇɴᴛ ᴠɪᴀ ʙᴀɴᴋ\nɴᴏ ʀᴇᴋ : 481901020711531\nᴀᴛᴀs ɴᴀᴍᴀ : muhazir\nʙᴀɴᴋ ʙʀɪ\n\nᴠɪᴀ ᴘᴜʟsᴀ\n08992906209"    +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "🔹Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate(msg.to, "🔹Pesan Msg🔹\n🔹Pesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "🔹Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate(msg.to, "🔹Welcome Msg🔹\n🔹Welcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "🔹Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate(msg.to, "🔹Respon Msg🔹\n🔹Respon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set left: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set left: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "🔹Gagal mengganti Respon Msg")
                              else:
                                  wait["left"] = spl
                                  sendTextTemplate(msg.to, "🔹Respon Left🔹\n🔹Respon left diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "🔹Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  sendTextTemplate(msg.to, "🔹Spam Msg🔹\n🔹Spam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "🔹Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate(msg.to, "🔹Sider Msg🔹\n🔹Sider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔹Pesan Msg🔹\n🔹Pesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek left":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔹left Msg🔹\n🔹Left Msg mu :\n\n「 " + str(wait["left"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔹Welcome Msg🔹\n🔹Welcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔹Respon Msg🔹\n🔹Respon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔹Spam Msg🔹\n🔹Spam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔹Sider Msg🔹\n🔹Sider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

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
                               cl.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                               try:ki.inviteIntoGroup(to, [Amid]);has = "OK"
                               except:has = "NOT"
                               try:ki.kickoutFromGroup(to, [Amid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               ki.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))                               
                               try:kk.inviteIntoGroup(to, [Bmid]);has = "OK"
                               except:has = "NOT"
                               try:kk.kickoutFromGroup(to, [Bmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               kk.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                               try:kc.inviteIntoGroup(to, [Cmid]);has = "OK"
                               except:has = "NOT"
                               try:kc.kickoutFromGroup(to, [Cmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               kc.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))                               
                               try:ko.inviteIntoGroup(to, [Dmid]);has = "OK"
                               except:has = "NOT"
                               try:ko.kickoutFromGroup(to, [Dmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               ko.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))                              
                               try:jk.inviteIntoGroup(to, [Emid]);has = "OK"
                               except:has = "NOT"
                               try:jk.kickoutFromGroup(to, [Emid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               jk.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                               try:sw.inviteIntoGroup(to, [Fmid]);has = "OK"
                               except:has = "NOT"
                               try:sw.kickoutFromGroup(to, [Fmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               sw.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
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
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)

while True:
  try:
      Ops = cl.poll.fetchOperations(cl.revision, 50)
      for op in Ops:
        if op.type != 0:
          cl.revision = max(cl.revision, op.revision)
          bot(op)
  except Exception as E:
    E = str(E)
    if "reason=None" in E:
      print (E)
      time.sleep(60)
      restart_program()
      
