
#OLENG OFFICIAL
# sᴄʀɪᴘᴇ ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ ᴜᴘᴅᴀᴛᴇ 17-7-2020
# ᴛᴇᴀᴍ ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ
#ᴊᴀɴɢᴀɴ sᴏᴋ ʙɪsᴀ ɴɢᴇᴅɪᴛ ᴋʟᴏ ɢᴋ ʙɪsᴀ ɴɢᴇᴅɪᴛ
#ᴄʀᴇᴀᴛᴏʀ ʙʏᴇ ᴀʙɪ ᴛᴇᴀᴍ ᴏʟᴇɴɢ
from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from thrift import transport, protocol, server
from datetime import datetime, timedelta
import pytz, pafy, livejson, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, tweepy, codecs, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, goslate, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
import youtube_dl
from time import sleep
import pyimgflip
from zalgo_text import zalgo
from threading import Thread,Event
import requests,uvloop
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
loop = uvloop.new_event_loop()
try:
    AbiOlengKiller = "api keyMu"
    headers = {
        "apiKey":AbiOlengKiller,
        "appName": "CHROMEOS\t2.3.8\tChrome OS\t1",
        "cert" : None,
        "server": random.choice(["pool-1","pool-2"]),
        "sysname": "AbiOleng"
        }
    main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
    print("QR Oleng: " + main["result"]["qr_link"])
    if not headers["cert"]:
        result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
        print("Code Oleng: " + result["result"])
    result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
    if result["status"] != 200:
        print("[ Error ] "+ result["reason"])
    else:
        AbiOlengKiller = LINE(result["result"]["token"],appName="CHROMEOS\t2.3.8\tChrome OS\t1")
        print ("== ʟᴏɢɪɴ sᴜᴄᴄᴇs ʙᴏssᴋᴜ ᴀʙɪ ==")
except:pass
oepoll = OEPoll(AbiOlengKiller)
mid = AbiOlengKiller.profile.mid
mid = AbiOlengKiller.getProfile().mid
OlengKiller1 = [AbiOlengKiller]
OlengKiller2 = [AbiOlengKiller]
OlengKillerBots = [mid]
BackupAbi = ["u3f9c3061f8e7a7c4e07d5f6be08b9339"]
BackupOlengKiller = ["u3f9c3061f8e7a7c4e07d5f6be08b9339"]
admin = ["u7bc7c4ef5e1c254e06c24f7070a86a3a"]
OlengKiller = admin
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
responsename1 = AbiOlengKiller.getProfile().displayName
settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "comment":"╭──────────────────╮\n├🔹ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴀᴋᴀᴋ    \n╰──────────────────╯\n╭──────────────────\n├🔹ʀᴇᴀᴅʏ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n├🔹ʀᴏᴏᴍ sᴍᴜʟᴇ / ᴇᴠᴇɴᴛ \n├🔹ʀᴇᴀᴅʏ sʙ ᴏɴʟʏ \n├🔹sʙ ᴏɴʟʏ + ᴀᴊs \n├🔹sʙ + ᴀssɪsᴛ + ᴀᴊs \n├🔹ʟᴏɢɪɴ ᴊs / ʙʏᴘᴀs\n├🔹ɴᴇᴡ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴄ ʙᴏᴛ \n├🔹ɴᴇᴡ ʙᴇʟᴀᴊᴀʀ ʙᴏᴛ \n├🔹ᴘᴇᴍᴀsᴀɴɢ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ\n├🔹ʀᴇᴀᴅʏ ᴀᴋᴜɴ ᴄᴏɪɴ\n├🔹ʀᴇᴀᴅʏ ᴄᴏɪɴ ɢɪғᴛ \n╰────────────────── \n╭─────────────────\n├ line.me/ti/p/~olengkiller\n╰─────────────────",
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
    'leaveMsg':True,
    'left':True,
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
    "mention1":True,
    "Respontag":"sᴇᴋᴀʟɪ ʟᴀɢɪ ᴛᴀɢ, ᴍᴀᴜ ᴀʙɪ ᴅᴇsᴀʜɪɴ",
    "welcome":"Selamat datang & semoga betah n bahagia",
    "message":"╭──────────────────╮\n├🔹ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴀᴋᴀᴋ    │\n╰──────────────────╯\n╭──────────────────\n├🔹ʀᴇᴀᴅʏ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n├🔹ʀᴏᴏᴍ sᴍᴜʟᴇ / ᴇᴠᴇɴᴛ \n├🔹ʀᴇᴀᴅʏ sʙ ᴏɴʟʏ \n├🔹sʙ ᴏɴʟʏ + ᴀᴊs \n├🔹sʙ + ᴀssɪsᴛ + ᴀᴊs \n├🔹ʟᴏɢɪɴ ᴊs / ʙʏᴘᴀs\n├🔹ɴᴇᴡ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴄ ʙᴏᴛ \n├🔹ɴᴇᴡ ʙᴇʟᴀᴊᴀʀ ʙᴏᴛ \n├🔹ᴘᴇᴍᴀsᴀɴɢ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ\n├🔹ʀᴇᴀᴅʏ ᴀᴋᴜɴ ᴄᴏɪɴ\n├🔹ʀᴇᴀᴅʏ ᴄᴏɪɴ ɢɪғᴛ \n╰────────────────── \n╭─────────────────\n├ line.me/ti/p/~olengkiller\n╰─────────────────",
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
        textx = "╭──[ᴅᴀғᴛᴀʀ ᴊᴀɴᴅᴀ {}]──\n├ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@AbiOlengKiller\n"
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
                    textx += "╰──[ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ]──".format(str(AbiOlengKiller.getGroup(to).name))
                except:
                    pass
        AbiOlengKiller.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        AbiOlengKiller.sendMessage(to, "[ ɪɴғᴏ ] ᴇʀᴏʀ :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@AbiOlengKiller\n"
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
                    no = "\n???[ {} ]".format(str(AbiOlengKiller.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        AbiOlengKiller.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = AbiOlengKiller.getGroup(to)
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
                    no = "\n???[ {} ]".format(str(AbiOlengKiller.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        #AbiOlengKiller.sendMessage(to, textx)
      #  client.sendMessage(to, textx)
    except Exception as error:
        AbiOlengKiller.sendMessage(to)

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Keluar「{}」\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = AbiOlengKiller.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leftmsg"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        AbiOlengKiller.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
        
def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd.startswith('ex\n'):
      if sender in AbiOlengKiller:
        try:
            sep = text.split('\n')
            AbiGanteng = text.replace(sep[0] + '\n','')
            f = open('exec.txt', 'w')
            sys.stdout = f
            print(' ')
            exec(AbiGanteng)
            print('\n%s' % str(datetime.now()))
            f.close()
            sys.stdout = sys.__stdout__
            with open('exec.txt','r') as r:
                txt = r.read()
            AbiOlengKiller.sendMessage(to, txt)
        except Exception as e:
            pass
      else:
        AbiOlengKiller.sendMessage(to, 'ᴀᴘᴀʟᴜ !')
    elif cmd.startswith('exc\n'):
      if sender in AbiOlengKiller:
        sep = text.split('\n')
        AbiGanteng = text.replace(sep[0] + '\n','')
        if 'print' in AbiGanteng:
        	AbiGanteng = AbiGanteng.replace('print(','AbiOlengKiller.sendExecMessage(to,')
        	exec(AbiGanteng)
        else:
        	exec(AbiGanteng)
      else:
        AbiOlengKiller.sendMessage(to, 'ᴀᴘᴀʟᴜ !')        

def logError(text):
    AbiOlengKiller.log("[ ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ ] {}".format(str(text)))
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
            "altText": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
            "text": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
      "backgroundColor": "#ff0000"
    }
  }
}
}
    AbiOlengKiller.postTemplate(to, data)
 
def sendTextTemplate8(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(AbiOlengKiller.getProfile().displayName),
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
          "uri": "http://line.me/ti/p/~olengkiller"
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
        "text": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
    AbiOlengKiller.postTemplate(to, data)
    
def sendTextTemplate7(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(AbiOlengKiller.getProfile().displayName),
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
          "uri": "http://line.me/ti/p/muhajir_alwi"
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
          "uri": "http://line.me/ti/p/~muhaziralwi"
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
        "text": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
    AbiOlengKiller.postTemplate(to, data)
    
def sendTextTemplate6(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(AbiOlengKiller.getProfile().displayName),
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
          "uri": "http://line.me/ti/p/~muhaziralwi"
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
          "uri": "http://line.me/ti/p/~muhaziralwi"
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
        "text": "ᴏʟᴇɴɢ ʙᴏᴛ",
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
    AbiOlengKiller.postTemplate(to, data)
    
def sendTextTemplate4(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(AbiOlengKiller.getProfile().displayName),
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
          "uri": "http://line.me/ti/p/~muhaziralwi"
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
          "uri": "http://line.me/ti/p/~muhaziralwi"
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
        "text": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
    AbiOlengKiller.postTemplate(to, data)
    
def sendTextTemplate5(to, text):
    data = {
            "type": "flex",
            "altText": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
    AbiOlengKiller.postTemplate(to, data)
    
def sendTextTemplate1(to, text):
    data = {
                "type": "template",
                "altText": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
    AbiOlengKiller.postTemplate(to, data)
    
def sendTextTemplate2(to, text):
    data = {
            "type": "flex",
            "altText": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
    AbiOlengKiller.postTemplate(to, data)
    
def sendTextTemplate3(to, text):
    data = {
            "type": "flex",
            "altText": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
          "uri": "http://line.me/ti/p/~muhaziralwi"
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
        "text": "ᴏʟᴇɴɢʙᴏᴛ",
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
    AbiOlengKiller.postTemplate(to, data)
    
def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(AbiOlengKiller.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~muhaziralwi"
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
                          "altText": "{} sent a sticker".format(AbiOlengKiller.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~muhaziralwi"
           }                                                
 }
]
                          }
                      }
    AbiOlengKiller.postTemplate(to, data)    
    
def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output oleng.mp3 {}'.format(link))
    try:
        AbiOlengKiller.sendAudio(to, 'oleng.mp3')
        time.sleep(2)
        os.remove('oleng.mp3')
    except Exception as e:
        AbiOlengKiller.sendMessage(to, 'ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ\nʟɪɴᴋ ᴀɴᴅᴀ sᴀʟᴀʜ')
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output oleng.mp4 {}'.format(link))
    try:
        AbiOlengKiller.sendVideo(to, "oleng.mp4")
        time.sleep(2)
        os.remove('oleng.mp4')
    except Exception as e:
        AbiOlengKiller.sendMessage(to, ' ᴇʀʀᴏʀ\nʟɪɴᴋ ᴀɴᴅᴀ sᴀʟᴀʜ', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+AbiOlengKiller.getContact(AbiOlengKiller).pictureStatus, 'AGENT_NAME': 'ᴇʀʀᴏʀ', 'AGENT_LINK': 'https://line.me/ti/p/~olengkiller'})

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        AbiMuhazir = "ʙᴏᴛ ᴀᴋᴛɪғ ʙᴏssᴋᴜ"
                        AbiOlengKiller.sendMessage(tmp, AbiMuhazir, {'AGENT_LINK': "https://line.me/ti/p/~olengkiller", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)

def delExpirev2():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        AbiMuhazir = "ʙᴏᴛ ᴀᴋᴛɪғ ʙᴏssᴋᴜ"
                        AbiOlengKiller.sendMessage(tmp, AbiMuhazir, {'AGENT_LINK': "https://line.me/ti/p/~muhaziralwi", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)    

def musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+AbiOlengKiller.getContact(mid).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': AbiOlengKiller.getContact(mid).statusMessage if AbiOlengKiller.getContact(mid).statusMessage != '' else 'http://line.me/ti/p/~muhaziralwi', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': AbiOlengKiller.getContact(mid).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.cl.cl/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+mid,'MSG_SENDER_NAME':  AbiOlengKiller.getContact(mid).displayName,}
    return AbiOlengKiller.sendMessage(to, AbiOlengKiller.getContact(mid).displayName, contentMetadata, 19)

def sendMention2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@AbiOlengKiller "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        AbiOlengKiller.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        AbiOlengKiller.sendImageWithURL(msg.to,image)
    except Exception as error:
        AbiOlengKiller.sendMessage(to, "[ INFO ] Error :\n" + str(error))
    
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def AbiMuhazir1():
    key = Setmain["keyCommand"]
    key = key.title()
    CmdOlengKiller1 = "╭──────────╮" + "\n" + \
                  "├  🔹ᴄᴏᴍᴍᴇɴᴅ ᴏʟᴇɴɢ" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "├🔹" + key + "ᴍᴇ\n" + \
                  "├🔹" + key + "ᴍɪᴅ「@」\n" + \
                  "├🔹" + key + "ɪɴғᴏ「@」\n" + \
                  "├🔹" + key + "ʀᴇsᴛᴀʀᴛ\n" + \
                  "├🔹" + key + "ʀᴜɴᴛɪᴍᴇ\n" + \
                  "├🔹" + key + "kick「@」\n" + \
                  "├🔹" + key + "sᴘ\n" + \
                  "├🔹" + key + "sᴀʏᴀɴɢ / ᴘᴇᴀ\n" + \
                  "├🔹" + key + "ᴘᴀᴘᴀʏ (ʟᴇғᴛ ɢᴄ)\n" + \
                  "├🔹" + key + "ɢɪɴғᴏ\n" + \
                  "├🔹" + key + "sᴇʟғ ᴏɴ「@」\n" + \
                  "├🔹" + key + "ᴏᴘᴇɴ\n" + \
                  "├🔹" + key + "ᴄʟᴏsᴇ\n" + \
                  "├🔹" + key + "ᴜʀʟɢʀᴜᴘ\n" + \
                  "├🔹" + key + "ɪɴғᴏɢʀᴜᴘ「ɴᴏ」\n" + \
                  "├🔹" + key + "ɪɴғᴏᴍᴇᴍ「ɴᴏ」\n" + \
                  "├🔹" + key + "ʜᴀᴘᴜsᴄʜᴀᴛ\n" + \
                  "├🔹" + key + "ғʀɪᴇɴᴅʟɪsᴛ\n" + \
                  "├🔹" + key + "ɢʀᴏᴜᴘʟɪsᴛ\n" + \
                  "├🔹" + key + "ᴜᴘᴅᴀᴛᴇғᴏᴛᴏ\n" + \
                  "├🔹" + key + "ᴜᴘᴅᴀᴛᴇɢʀᴜᴘ\n" + \
                  "├🔹" + key + "ᴜᴘᴅᴀᴛᴇʙᴏᴛ\n" + \
                  "├🔹" + key + "sᴇᴛᴋᴇʏ「ɴᴇᴡᴋᴇʏ」\n" + \
                  "├🔹" + key + "sᴇʟғ 「ᴏɴ/ᴏғғ」\n" + \
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
                  "├🔹" + key + "myset\n" + \
                  "╰──────────╯"
    return CmdOlengKiller1

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
                    if AbiOlengKiller.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in OlengKillerBots and op.param2 not in BackupAbi and op.param2 not in admin:
                            AbiOlengKiller.reissueGroupTicket(op.param1)
                            MataMu = AbiOlengKiller.getGroup(op.param1)
                            MataMu.preventedJoinByTicket = True
                            Ticket = AbiOlengKiller.reissueGroupTicket(op.param1)
                            AbiOlengKiller.acceptGroupInvitationByTicket(op.param1,Ticket)
                            AbiOlengKiller.kickoutFromGroup(op.param1,[op.param2])
                            AbiOlengKiller.updateGroup(MataMu)                           
                except:
                    pass
                    
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in OlengKillerBots and op.param2 not in BackupAbi and op.param2 not in admin:
                        AbiOlengKiller.acceptGroupInvitation(op.param1)
                        ginfo = AbiOlengKiller.getGroup(op.param1)
                        AbiOlengKiller.leaveGroup(op.param1)
                    else:
                        AbiOlengKiller.acceptGroupInvitation(op.param1)
                        ginfo = AbiOlengKiller.getGroup(op.param1)
                  
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in OlengKillerBots and op.param2 not in BackupAbi and op.param2 not in admin:
                        AbiOlengKiller.acceptGroupInvitation(op.param1)
                        ginfo = AbiOlengKiller.getGroup(op.param1)
                        sendTextTemplate(op.param1,"ʜᴀʏ sᴇᴍᴜᴀ\nᴀʙɪ ᴅᴀᴛᴀɴɢ\nᴅɪ ɢʀᴏᴜᴘ " +str(ginfo.name))
                    else:
                        AbiOlengKiller.acceptGroupInvitation(op.param1)
                        ginfo = AbiOlengKiller.getGroup(op.param1)
                        sendTextTemplate(op.param1,"ʜᴀʏ sᴇᴍᴜᴀ\nᴀʙɪ ᴅᴀᴛᴀɴɢ\nᴅɪ ɢʀᴏᴜᴘ " + str(ginfo.name))
                        
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in OlengKillerBots and op.param2 not in BackupAbi and op.param2 not in admin:
                    wait["blacklist"][op.param2] = True
                    try:
                        AbiOlengKiller.findAndAddContactsByMid(op.param3)
                        AbiOlengKiller.kickoutFromGroup(op.param1,[op.param2])
                        AbiOlengKiller.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        pass
                        

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                AbiOlengKiller.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 15:
            if wait["leaveMsg"] == True:
                ginfo = AbiOlengKiller.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])
                contact = AbiOlengKiller.getContact(op.param2)
                data = {
                        "type": "flex",
                        "altText": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
                        "contents": {
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(AbiOlengKiller.getContact(op.param2).pictureStatus),
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
                    "text": "  {}".format(AbiOlengKiller.getContact(op.param2).displayName),
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
                        "text": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
                AbiOlengKiller.postTemplate(op.param1, data)
              
        if op.type == 17:
            if wait["welcomeOn"] == True:
                ginfo = AbiOlengKiller.getGroup(op.param1)
                welcomeMembers(op.param1, [op.param2])
                contact = AbiOlengKiller.getContact(op.param2)
                data = {
                        "type": "flex",
                        "altText": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
                        "contents": {
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(AbiOlengKiller.getContact(op.param2).pictureStatus),
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
                    "text": "  {}".format(AbiOlengKiller.getContact(op.param2).displayName),
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
                        "text": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
                AbiOlengKiller.postTemplate(op.param1, data)
        if op.type == 5:
            print ("[ 5 ] ɴᴏᴛɪғɪᴇᴅ ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ")
            if wait["autoBlock"] == True:
                AbiOlengKiller.blockContact(op.param1)
                AbiOlengKiller.sendMessage(op.param1, wait["ᴍᴀᴀғ ᴀɪᴍ ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴀɪᴍ ᴀᴋᴛɪғ"])
                
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in OlengKillerBots and op.param2 not in BackupAbi and op.param2 not in admin:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        AbiOlengKiller.sendMessage(op.param1, wait["message"])
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    OlengKillerGaes = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'ɢᴀᴍʙᴀʀɴʏᴀ ᴅɪ ʙᴀᴡᴀʜ':
                                AbiKoplak = AbiOlengKiller.getGroup(OlengKillerGaes)
                                AbiMadura = AbiOlengKiller.getContact(msg_dict[msg_id]["from"])
                                Madura = ""
                                DerehMadura = ""
                                MaduraOleng = []
                                SoratNaJiah =  "「 ɢᴀᴍʙᴀʀ ᴅɪ ʜᴀᴘᴜs 」\nᴘᴇɴɢɪʀɪᴍ : "
                                AbiMuhazirGG = "ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(AbiKoplak.name))
                                AbiMuhazirGG += "\nᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                Ptk = str(AbiMadura.displayName)
                                Sorat = ''
                                SoratNa = Sorat+"@AbiMuhazir \n"
                                MatanaJiah = str(len(DerehMadura)+len(SoratNaJiah))
                                PokehNa = str(len(DerehMadura)+len(SoratNa)+len(SoratNaJiah)-1)
                                Madura = {'S':MatanaJiah, 'E':PokehNa, 'M':AbiMadura.mid}
                                MaduraOleng.append(Madura)
                                DerehMadura += SoratNa
                                AbiAhk = SoratNaJiah + DerehMadura + AbiMuhazirGG + ""
                                AbiOlengKiller.sendMessage(OlengKillerGaes, AbiAhk, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(MaduraOleng).replace(' ','')+'}')}, contentType=0)
                                AbiOlengKiller.sendImage(OlengKillerGaes, msg_dict[msg_id]["data"])
                           else:
                                AbiKoplak = AbiOlengKiller.getGroup(OlengKillerGaes)
                                AbiMadura = AbiOlengKiller.getContact(msg_dict[msg_id]["from"])
                                AbiMuhazirGG =  "ᴘᴇsᴀɴ ᴅɪ ʜᴀᴘᴜs\n"
                                AbiMuhazirGG += "ᴘᴇɴɢɪʀɪᴍ : {}".format(str(AbiMadura.displayName))
                                AbiMuhazirGG += "\nɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(AbiKoplak.name))
                                AbiMuhazirGG += "\nᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                AbiMuhazirGG += "\nᴘᴇsᴀɴ ɴʏᴀ : {}".format(str(msg_dict[msg_id]["text"]))
                                AbiOlengKiller.sendMessage(OlengKillerGaes, str(AbiMuhazirGG))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    OlengKillerGaes = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                AbiKoplak = AbiOlengKiller.getGroup(OlengKillerGaes)
                                AbiMadura = AbiOlengKiller.getContact(msg_dict1[msg_id]["from"])
                                AbiMuhazirGG =  "sᴛɪᴄᴋᴇʀ ᴅɪ ʜᴀᴘᴜs\n"
                                AbiMuhazirGG += "ᴘᴇɴɢɪʀɪᴍ : {}".format(str(AbiMadura.displayName))
                                AbiMuhazirGG += "\nɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(AbiKoplak.name))
                                AbiMuhazirGG += "\nᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                AbiMuhazirGG += "{}".format(str(msg_dict1[msg_id]["text"]))
                                AbiOlengKiller.sendMessage(OlengKillerGaes, str(AbiMuhazirGG))
                                AbiOlengKiller.sendImage(OlengKillerGaes, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
            
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in OlengKillerBots:
                    pass
                if op.param2 in BackupAbi:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        AbiOlengKiller.kickoutFromGroup(op.param1,[op.param2])
                        AbiOlengKiller.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        pass
                return
              
        if op.type == 13:
            if op.param1 in protectkick:
                if op.param2 not in OlengKillerBots and op.param2 not in BackupAbi and op.param2 not in admin:
                    wait["blacklist"][op.param2] = True
                    try:
                        AbiOlengKiller.kickoutFromGroup(op.param1,[op.param2])
                        AbiOlengKiller.inviteIntoGroup(op.param1,[AjsAbi])
                    except:
                        pass
        
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in OlengKillerBots and op.param2 not in BackupAbi and op.param2 not in admin:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            AbiOlengKiller.kickoutFromGroup(op.param1,[op.param2])
                            AbiOlengKiller.inviteIntoGroup(op.param1,[op.param3])
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
                AbiOlengKiller.kickoutFromGroup(op.param1,[op.param2])
                AbiOlengKiller.cancelGroupInvitation(op.param1,[op.param3])
            else:
                pass

        
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = AbiOlengKiller.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = AbiOlengKiller.getContact(op.param2)
                        data = {
                                "type": "flex",
                                "altText": "ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
                                "contents":{
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
            "url": str(AbiOlengKiller.getProfileCoverURL(op.param2)),
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
                "type": "text",
                "text": "{}".format(AbiOlengKiller.getContact(op.param2).displayName),
                "color": "#ffffff",
                "size": "xs",
                "margin": "xxl",
                "style": "normal",
                "decoration": "underline",
                "offsetStart": "5px"
              }
            ],
            "position": "absolute",
            "margin": "none",
            "width": "220px",
            "offsetTop": "215px",
            "offsetStart": "33px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(AbiOlengKiller.getContact(op.param2).pictureStatus),
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "154px",
            "height": "150px",
            "cornerRadius": "100px",
            "position": "absolute",
            "borderWidth": "3px",
            "borderColor": "#ff0000",
            "offsetBottom": "40px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "S C T V",
                "size": "sm",
                "color": "#ffffff",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "2px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://5.top4top.net/p_1440pn8030.jpg",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "30px",
            "offsetStart": "5px",
            "offsetBottom": "2px",
            "borderColor": "#ff0000",
            "borderWidth": "1px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "2px",
        "cornerRadius": "10px",
        "position": "relative",
        "borderColor": "#ff0000"
      }
    }
  ]
}
}
                        AbiOlengKiller.postTemplate(op.param1, data)
                
        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in OlengKillerBots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          AbiOlengKiller.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              AbiOlengKiller.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              AbiOlengKiller.kickoutFromGroup(msg.to, [msg._from])
                                        
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = AbiOlengKiller.getContact(msg._from)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in OlengKillerBots:
                           sendTextTemplate(msg.to, wait["Respontag"])
                           break
                           
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in OlengKillerBots:
                           AbiOlengKiller.mentiontag(msg.to,[msg._from])
                           AbiOlengKiller.sendMessage(msg.to, "ᴊᴀɴɢᴀɴ ᴛᴀǫ ᴀʙɪ....")
                           AbiOlengKiller.kickoutFromGroup(msg.to, [msg._from])
                           break
                           
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["arespon"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   lists = []
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           contact = AbiOlengKiller.getContact(msg._from)
                           AbiOlengKiller.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                           sendMention1(sender, "╭──────────────────╮\n├🔹ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴀᴋᴀᴋ    │\n╰──────────────────╯\n╭──────────────────\n├🔹ʀᴇᴀᴅʏ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n├🔹ʀᴏᴏᴍ sᴍᴜʟᴇ / ᴇᴠᴇɴᴛ \n├🔹ʀᴇᴀᴅʏ sʙ ᴏɴʟʏ \n├🔹sʙ ᴏɴʟʏ + ᴀᴊs \n├🔹sʙ + ᴀssɪsᴛ + ᴀᴊs \n├🔹ʟᴏɢɪɴ ᴊs / ʙʏᴘᴀs / ɴɪɴᴊᴀ\n├🔹ɴᴇᴡ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴄ ʙᴏᴛ \n├🔹ɴᴇᴡ ʙᴇʟᴀᴊᴀʀ ʙᴏᴛ \n├🔹ᴘᴇᴍᴀsᴀɴɢ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ\n├🔹ʀᴇᴀᴅʏ ᴀᴋᴜɴ ᴄᴏɪɴ\n├🔹ʀᴇᴀᴅʏ ᴄᴏɪɴ ɢɪғᴛ \n╰────────────────── \n╭─────────────────\n├ line.me/ti/p/~olengkiller\n╰─────────────────", [sender])
                           break
                           
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    AbiOlengKiller.sendMessage(msg.to,"「ᴄᴇᴋ ɪᴅ sᴛɪᴄᴋᴇʀ」\nsᴛᴋɪᴅ : " + msg.contentMetadata["STKID"] + "\nsᴛᴋᴘᴋɢɪᴅ : " + msg.contentMetadata["STKPKGID"] + "\nsᴛᴋᴠᴇʀ : " + msg.contentMetadata["STKVER"]+ "\n\n「ʟɪɴᴋ sᴛɪᴄᴋᴇʀ」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    AbiOlengKiller.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = AbiOlengKiller.getContact(msg.contentMetadata["mid"])
                        path = AbiOlengKiller.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        AbiOlengKiller.sendMessage(msg.to,"ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\nᴍɪᴅ : " + msg.contentMetadata["mid"] + "\nsᴛᴀᴛᴜs ᴍsɢ : " + contact.statusMessage + "\nᴘɪᴄᴛᴜʀᴇ ᴜʀʟ : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        AbiOlengKiller.sendImageWithURL(msg.to, image)
                        
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 16:
                        url = msg.contentMetadata["postEndUrl"]
                        AbiOlengKiller.likePost(url[25:58], url[66:], likeType=1004)
                        AbiOlengKiller.createComment(url[25:58], url[66:], settings["comment"])
                        print ("ᴀᴜᴛᴏ ʟɪᴋᴇ ᴅᴏɴᴇ")
                        sendTextTemplate(msg.to,"👍 ᴀᴜᴛᴏ ʟɪᴋᴇ ᴅᴏɴᴇ")
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
                    AbiOlengKiller.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = AbiOlengKiller.getContact(msg.contentMetadata["mid"])
                        path = AbiOlengKiller.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sendTextTemplate(msg.to,"ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\nᴍɪᴅ : " + msg.contentMetadata["mid"] + "\nsᴛᴀᴛᴜs ᴍsɢ : " + contact.statusMessage + "\nᴘɪᴄᴛᴜʀᴇ ᴜʀʟ: http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        AbiOlengKiller.sendImageWithURL(msg.to, image)
                         
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            AbiOlengKiller.downloadObjectMsg(msg_id,'path','video.mp4')
                            sendTextTemplate(msg.to,"sᴇɴᴅ ɢᴀᴍʙᴀʀɴʏᴀ...")
                            
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            AbiOlengKiller.downloadObjectMsg(msg_id,'path','image.jpg')
                            AbiOlengKiller.nadyacantikimut('video.mp4','image.jpg')
                            sendTextTemplate(msg.to,"ɢᴀɴᴛɪ ᴠɪᴅɪᴏ ᴘʀᴏғɪʟ ᴅᴏɴᴇ!!!")
#===================================[ ] ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in OlengKillerBots:
                        sendTextTemplate(msg.to,"🔹sᴜᴅᴀʜ ᴊᴀᴅɪ ʙᴏᴛ")
                        wait["addbots"] = True
                    else:
                        OlengKillerBots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in OlengKillerBots:
                        OlengKillerBots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate(msg.to,"🔹ɪᴛᴜ ʙᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")
                        
#===================================[ ]  ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        AbiOlengKiller.sendMessage(msg.to,"🔹sᴜᴅᴀʜ ᴊᴀᴅɪ sᴛᴀғғ")
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
                        headers = AbiOlengKiller.Talk.Headers
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
                     path = AbiOlengKiller.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     AbiOlengKiller.updateGroupPicture(msg.to, path)
                     sendTextTemplate(msg.to, "🔹ᴅᴏɴᴇ ᴍᴇɴɢᴜʙᴀʜ ғᴏᴛᴏ ɢʀᴏᴜᴘ")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["RAfoto"]:
                            path = AbiOlengKiller.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            AbiOlengKiller.updateProfilePicture(path)
                            sendTextTemplate(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        AbiOlengKiller.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "menu":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               CmdOlengKiller1 = AbiMuhazir1()
                               sendTextTemplate(msg.to, str(CmdOlengKiller1))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sendTextTemplate(msg.to, "🔹ᴛᴇᴍᴘʟᴀᴛᴇ ᴀᴋᴛɪғ ʙᴏssᴋᴜ")
                           
                        elif cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate(msg.to, "╭─────╮\n├🔹ʜᴇʟᴘ\n├🔹ᴍᴇɴᴜ\n╰──────╯")
 
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate(msg.to, "ᴛᴇᴍᴘʟᴀᴛᴇ ᴏғғ ʙᴏssᴋᴜ")
                        
                        elif cmd.startswith("bcast "):
                           if msg._from in admin:
                             AbiUye = text.split(" ")
                             AbiCroot = text.replace(AbiUye[0] + " ","")
                             AbiGituLoh = AbiOlengKiller.getGroupIdsJoined()
                             for AbiOlengKillerBots in AbiGituLoh:
                                AbiMuhazir = AbiOlengKiller.getContact(mid)
                                OlengKillerBotss = ""
                                OlengKillerBots1 = ""
                                OlengKillerBots2 = []
                                OlengKillerBots3 =  "ʙʀᴏᴀᴅᴄᴀsᴛ ʙʏᴇ "
                                OlengKillerBots0 = "{}".format(str(AbiCroot))
                                AbiCrott = str(AbiMuhazir.displayName)
                                OlengKillerBots4 = ''
                                OlengKillerBots5 = OlengKillerBots4+"@OlengKillerBots\n"
                                OlengKillerBots6 = str(len(OlengKillerBots1)+len(OlengKillerBots3))
                                OlengKillerBots7 = str(len(OlengKillerBots1)+len(OlengKillerBots5)+len(OlengKillerBots3)-1)
                                OlengKillerBotss = {'S':OlengKillerBots6, 'E':OlengKillerBots7, 'M':AbiMuhazir.mid}
                                OlengKillerBots2.append(OlengKillerBotss)
                                OlengKillerBots1 += OlengKillerBots5
                                OlengKillerBots8 = OlengKillerBots3 + OlengKillerBots1 + OlengKillerBots0 + ""
                                AbiOlengKiller.sendMessage(AbiOlengKillerBots, OlengKillerBots8, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(OlengKillerBots2).replace(' ','')+'}')}, contentType=0)
                                
                        elif cmd == "me":
                                contact = AbiOlengKiller.getProfile()
                                mids = [contact.mid]
                                status = AbiOlengKiller.getContact(sender)                               	
                                data = {
                                        "type": "flex",
                                        "altText": "ᴀʙɪ ᴏʟᴇɴɢ",
                                        "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(AbiOlengKiller.getContact(sender).pictureStatus),
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
                    "text": "          ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
        "url": "https://3.top4top.net/p_1438ohk5b0.jpg",
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
                "text": "ᴀᴘʀɪʟʏᴀɴᴛɪ",
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
                    "text": "          ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
        "url": "https://5.top4top.net/p_1440pn8030.jpg",
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
                "text": "ᴀʙɪ ᴍᴜʜᴀᴊɪʀ",
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
                    "text": "          ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ",
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
                                AbiOlengKiller.postTemplate(to, data)
 
                        elif cmd == "myset":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭──ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ──\n"
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

                        elif cmd == "payment":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴘᴀʏᴍᴇɴᴛ ᴠɪᴀ ʙᴀɴᴋ\nɴᴏ ʀᴇᴋ : 481901020711531\nᴀᴛᴀs ɴᴀᴍᴀ : muhazir\nʙᴀɴᴋ ʙʀɪ\n\nᴠɪᴀ ᴘᴜʟsᴀ\n08992906209 ")

                        elif cmd == "wa'alaikumsalam" or text.lower() == 'waalaikumsalam':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ɴᴀʜ ɢɪᴛᴜ ᴊᴀᴡᴀʙ sᴀʟᴀᴍ sᴇsᴀᴍᴀ ᴍᴜsʟɪᴍ😘😍")

                        elif cmd == "jandeee":
                          if wait["selfbot"] == True:                            
                               AbiOlengKiller.sendMessage(msg.to, "nyaman nyaman nyaman nyaman nyaman nyaman    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿 ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.")
                               
                        elif cmd == "about":
                                groups = AbiOlengKiller.getGroupIdsJoined()
                                contacts = AbiOlengKiller.getAllContactIds()
                                blockeds = AbiOlengKiller.getBlockedContactIds()
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
            "url": "https://obs.line-scdn.net/{}".format(AbiOlengKiller.getContact(mid).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "ᴏʟᴇɴɢ\nᴋɪʟʟᴇʀ\nᴛᴇᴀᴍ\nsᴇʟғʙᴏᴛ",
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
                "text": " {}".format(AbiOlengKiller.getProfile().displayName),
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
        "text": "ᴏʟᴇɴɢ",
        "size": "xs",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~muhaziralwi"
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
          "uri": "http://line.me/ti/p/~muhaziralwi"
        },
        "align": "center"
      }
    ]
  }
}
}
                                AbiOlengKiller.postTemplate(to, data)

                        elif cmd == "aim":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                  musik(to)
                                  
                        elif cmd == ".me" or text.lower() == 'gue':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': mid}
                                AbiOlengKiller.sendContact(to, mid)

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
                               AbiOlengKiller.sendMessage(msg.to, msg._from)
                        elif text.lower() == "mymid":
                               AbiOlengKiller.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = AbiOlengKiller.getContact(key1)
                               AbiOlengKiller.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(mi.displayName)+"\nᴍɪᴅ : " +key1)
                               AbiOlengKiller.sendMessage(msg.to, None, contentMetadata={'u03addfbbbdb20585381383e5d173d28d': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = AbiOlengKiller.getContact(key1)
                               sendTextTemplate(msg.to, "ɴᴀᴍᴀ : "+str(mi.displayName)+"\nᴍɪᴅ : " +key1+"\nsᴛᴀᴛᴜs ᴍsɢ"+str(mi.statusMessage))
                               AbiOlengKiller.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(AbiOlengKiller.getContact(key1)):
                                   AbiOlengKiller.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   AbiOlengKiller.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in creator:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               AbiOlengKiller.sendMessage1(msg)
                               msg.contentType = 13

                        elif text.lower() == "hapus":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   AbiOlengKiller.removeAllMessages(op.param2)
                                   sendTextTemplate(msg.to,"🔹ʜᴀᴘᴜs ᴄʜᴀᴛ ᴅᴏɴᴇ")
                               except:
                                   pass
                                   
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
                               bot = "🔹ʙᴏᴛ ᴀᴋᴛɪғ sᴇʟᴀᴍᴀ\n" +waktu(eltime)
                               sendTextTemplate(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = AbiOlengKiller.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "🔹ᴛᴇʀᴛᴜᴛᴜᴘ"
                                    gTicket = "♦️ᴛɪᴅᴀᴋ ᴀᴅᴀ"
                                else:
                                    gQr = "🔹ᴛᴇʀʙᴜᴋᴀ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(AbiOlengKiller.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate(msg.to, "🔹ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ🔹ɢʀᴜᴘ ɪɴғᴏ\n\n🔹ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(G.name)+ "\n🔹ɪᴅ ɢʀᴜᴘ : {}".format(G.id)+ "\n🔹ᴘᴇᴍʙᴜᴀᴛ : {}".format(G.creator.displayName)+ "\n🔹ᴡᴀᴋᴛᴜ ᴅɪ ʙᴜᴀᴛ : {}".format(str(timeCreated))+ "\n🔹ᴊᴜᴍʟᴀʜ ᴀɴɢɢᴏᴛᴀ : {}".format(str(len(G.members)))+ "\n🔹ᴊᴜᴍʟᴀʜ ᴘᴇɴᴅɪɴɢᴀɴ : {}".format(gPending)+ "\n🔹ɢʀᴜᴘ ǫʀ : {}".format(gQr)+ "\n🔹ɢʀᴜᴘ ᴛɪᴄᴋᴇᴛ : {}".format(gTicket))
                                AbiOlengKiller.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                            except Exception as e:
                                sendTextTemplate(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = AbiOlengKiller.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = AbiOlengKiller.getGroup(group)
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
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(AbiOlengKiller.reissueGroupTicket(G.id)))
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
                                sendTextTemplate(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = AbiOlengKiller.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = AbiOlengKiller.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "├🔹"+ str(no) + ". " + mem.displayName
                                sendTextTemplate(to," 🔹ɢʀᴜᴘ ɴᴀᴍᴇ : [ " + str(G.name) + " ]\n\n   [ʟɪsᴛ ᴀɴɢɢᴏᴛᴀ ]\n" + ret_ + "\n\n🔹ᴛᴏᴛᴀʟ %i ᴀɴɢɢᴏᴛᴀ🔹" % len(G.members))
                            except: 
                                pass

                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = AbiOlengKiller.getAllContactIds()
                               for i in gid:
                                   G = AbiOlengKiller.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├🔹" + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate(msg.to,"╭── 🔹ɢʀᴏᴜᴘ ʟɪsᴛ🔹\n│\n"+ma+"│\n╰──🔹ᴛᴏᴛᴀʟ"+str(len(gid))+"ɢʀᴏᴜᴘ🔹")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = AbiOlengKiller.getGroupIdsJoined()
                               for i in gid:
                                   G = AbiOlengKiller.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├🔹" + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate(msg.to,"╭── 🔹ɢʀᴏᴜᴘ ʟɪsᴛ🔹\n│\n"+ma+"│\n╰──🔹ᴛᴏᴛᴀʟ"+str(len(gid))+"ɢʀᴏᴜᴘ🔹")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = AbiOlengKiller.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   AbiOlengKiller.updateGroup(X)
                                   sendTextTemplate(msg.to, "🔹ᴏᴘᴇɴ ᴜʀʟ")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = AbiOlengKiller.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   AbiOlengKiller.updateGroup(X)
                                   sendTextTemplate(msg.to, "🔹ᴄʟᴏsᴇ ᴜʀʟ")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = AbiOlengKiller.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      AbiOlengKiller.updateGroup(x)
                                   gurl = AbiOlengKiller.reissueGroupTicket(msg.to)
                                   AbiOlengKiller.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(x.name)+ "\nᴜʀʟ ɢʀᴜᴘ : http://line.me/R/ti/g/"+gurl)

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
                                
                        elif cmd == "gf":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["ChangeVideoProfilevid"][msg._from] = True
                                sendTextTemplate(msg.to,"sᴇɴᴅ ᴠɪᴅɪᴏ ɴʏᴀ...")
                                
                        elif cmd.startswith("changedualurl: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ","")                            
                                AbiOlengKiller.downloadFileURL(url,'path','video.mp4')
                                settings["ChangeVideoProfilePicture"][msg._from] = True
                                sendTextTemplate(msg.to, "sᴇɴᴅ ɢᴀᴍʙᴀʀ ɴʏᴀ.....")
                                
                        elif cmd == "cp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                sendTextTemplate(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")

                        elif cmd.startswith("cn: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = AbiOlengKiller.getProfile()
                                profile.displayName = string
                                AbiOlengKiller.updateProfile(profile)
                                sendTextTemplate(msg.to,"🔹ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "abioleng" or text.lower() == 'abigaes':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = AbiOlengKiller.getGroup(msg.to)
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
                                AbiOlengKiller.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in OlengKillerBots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +AbiOlengKiller.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"🔹ʟɪsᴛ ʙᴏᴛ\n\n"+ma+"\n🔹ᴛᴏᴛᴀʟ ʙᴏᴛ ᴀʙɪ「%s」" %(str(len(OlengKillerBots))))

                        elif cmd == "ladmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in BackupAbi:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +AbiOlengKiller.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +AbiOlengKiller.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"♦️ᴀᴅᴍɪɴ ᴀʙɪ\n\n♦️sᴜᴘᴇʀ ᴀᴅᴍɪɴ :\n"+ma+"\n♦️ᴀᴅᴍɪɴ :\n"+mb+"\n♦️ᴊᴜᴍʟᴀʜ ᴀᴅᴍɪɴ ᴀʙɪ「%s」♦️" %(str(len(BackupAbi)+len(admin))))

                        elif cmd == "cekpro":
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
                                    ma += str(a) + ". " +AbiOlengKiller.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +AbiOlengKiller.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +AbiOlengKiller.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +AbiOlengKiller.getGroup(group).name + "\n"
                                sendTextTemplate(msg.to,"🔹ᴘʀᴏ ɢʀᴏᴜᴘ\n"+ma+(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "oleng":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                AbiOlengKiller.sendMessage(msg.to,responsename1)
                                
                        elif cmd == "papay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = AbiOlengKiller.getGroup(msg.to)
                                sendTextTemplate(msg.to, "🔹ɢᴏᴏᴅ ʙʏᴇ ᴄᴀʏᴀɴᴋ🔹\n       "+str(G.name))
                                AbiOlengKiller.leaveGroup(msg.to)
                               
                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = AbiOlengKiller.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                sendTextTemplate(msg.to, "ᴡᴀɪᴛ...")
                                sendTextTemplate(msg.to, "╭───────────────────╮\n          %.10f ᴏʟᴇɴɢ\n╰───────────────────╯" % (get_profile_time/3))

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
                                                    no = "[ {} ]".format(str(AbiOlengKiller.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        AbiOlengKiller.sendMessage1(msg)
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

                        elif cmd == "sctv on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate(msg.to, "🔹ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n🔹 "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n🔹 "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sctv off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(msg.to, "🔹ᴅɪ ᴍᴀᴛɪᴋᴀɴ\n🔹 "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n🔹 "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  sendTextTemplate(msg.to, "🔹sᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ")

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
                                  sendTextTemplate(msg.to, str(ret_))

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
                                sendTextTemplate(msg.to, str(ret_))

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
                                sendTextTemplate(msg.to,str(ret_))

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
                                          AbiOlengKiller.sendMessage(msg.to, str(ret_))
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
                                      AbiOlengKiller.sendMessage(to, str(ret_))
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
                                                         AbiOlengKiller.sendImageWithURL(to, str(data["result"]["img"]))
                                                         AbiOlengKiller.sendMessage(to, str(ret_))
                                                         AbiOlengKiller.sendAudioWithURL(to, str(data["result"]["mp3"][0]))   
                     
                        elif cmd.startswith("music: "):
                           if msg._from in owner or msg._from in admin or msg._from in staff:
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
                                      AbiOlengKiller.sendMessage(msg.to, str(ret_))
                                      AbiOlengKiller.sendMessage(msg.to, "sᴀʙᴀʀ sᴇʙᴇɴᴛᴀʀ ʟᴀɢɪ ʟᴏᴀᴅɪɴɢ")
                                      AbiOlengKiller.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      AbiOlengKiller.sendMessage(to, "ᴍᴜsɪᴄ ᴇʀʀᴏʀ")

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
                                    AbiOlengKiller.sendMessage(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    AbiOlengKiller.sendImageWithURL(msg.to, str(path))

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
                                    title = "ᴊᴜᴅᴜʟ [ " + vid.title + " ]"
                                    author = '\n\nᴀᴜᴛʜᴏʀ : ' + str(vid.author)
                                    durasi = '\nᴅᴜʀᴀᴛɪᴏɴ : ' + str(vid.duration)
                                    suka = '\nʟɪᴋᴇs : ' + str(vid.likes)
                                    rating = '\nʀᴀᴛɪɴɢ : ' + str(vid.rating)
                                    deskripsi = '\nᴅᴇsᴋʀɪᴘsɪ : ' + str(vid.description)
                                AbiOlengKiller.sendVideoWithURL(msg.to, me)
                                sendTextTemplate(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                sendTextTemplate(msg.to,str(e))

                        elif cmd.startswith("abimp3: "):
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
                                AbiOlengKiller.sendImageWithURL(msg.to, me)
                                AbiOlengKiller.sendAudioWithURL(msg.to, shi)
                                AbiOlengKiller.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                AbiOlengKiller.sendText(msg.to,str(e))

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
                                AbiOlengKiller.sendImageWithURL(msg.to, profileIG)
                                AbiOlengKiller.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    AbiOlengKiller.sendMessage(msg.to, str(e))

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
                            sendTextTemplate(msg.to,"♦️ I N F O R M A S I ♦️\n\n"+"♦️ Date Of Birth : "+lahir+"\n♦️ Age : "+usia+"\n♦️ Ultah : "+ultah+"\n♦️ Zodiak : "+zodiak)

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
                                                AbiOlengKiller.sendMessage(msg)
                                            except Exception as e:
                                                AbiOlengKiller.sendMessage(msg.to,str(e))
                                    else:
                                        sendTextTemplate(msg.to,"🔹ᴊᴜᴍʟᴀʜ ᴍᴇʟᴇʙɪʜɪ 1000")
                                        
                        elif cmd == "scall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = AbiOlengKiller.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                AbiOlengKiller.sendMessage(msg.to, "🔹ᴅᴏɴᴇ ᴍᴇɴɢᴜɴᴅᴀɴɢ {} ᴘᴀɴɢɢɪʟᴀɴ ɢʀᴏᴜᴘ".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        AbiOlengKiller.acquireGroupCallRoute(to)
                                        AbiOlengKiller.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        AbiOlengKiller.sendText(msg.to,str(e))
                                else:
                                    sendTextTemplate(msg.to,"Jumlah melebihi batas")

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = AbiOlengKiller.findContactsByUserid(msgs)
                              if True:
                                  AbiOlengKiller.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  AbiOlengKiller.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "sᴀᴍʙᴜᴛᴀɴ ᴀᴋᴛɪғ"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = AbiOlengKiller.getGroup(msg.to)
                                       msgs = "🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "ᴀᴋᴛɪғ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = AbiOlengKiller.getGroup(msg.to)
                                         msgs = "🔹sᴀᴍʙᴜᴛᴀɴ ᴍᴀᴛɪ\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "🔹sᴀᴍʙᴜᴛᴀɴ sᴜᴅᴀʜ ᴍᴀᴛɪ"
                                    sendTextTemplate(msg.to, "🔹ᴛᴇᴡᴀs\n" + msgs)

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
                                      ginfo = AbiOlengKiller.getGroup(msg.to)
                                      msgs = "🔹ᴘʀᴏ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = AbiOlengKiller.getGroup(msg.to)
                                      msgs = "🔹ᴘʀᴏ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n🔹ᴅɪ ɢʀᴏᴜᴘ \n🔹 " +str(ginfo.name)
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
                                         ginfo = AbiOlengKiller.getGroup(msg.to)
                                         msgs = "🔹ᴅᴏɴᴇ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴘʀᴏ\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         ginfo = AbiOlengKiller.getGroup(msg.to)
                                         msgs = "🔹ᴘʀᴏ ᴅɪ ᴍᴀᴛɪᴋᴀɴ\n🔹ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    sendTextTemplate(msg.to, "🔹ᴅᴏɴᴇ\n" + msgs)

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
                                   if target not in OlengKillerBots:
                                       try:
                                           G = AbiOlengKiller.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           AbiOlengKiller.updateGroup(G)
                                           invsend = 0
                                           Ticket = AbiOlengKiller.reissueGroupTicket(msg.to)
                                           random.choice(ABC).acceptGroupInvitationByTicket(msg.to,Ticket)
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                           X = AbiOlengKiller.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           AbiOlengKiller.updateGroup(X)
                                       except:
                                           pass

                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in OlengKillerBots:
                                       try:
                                           AbiOlengKiller.kickoutFromGroup(msg.to, [target])
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
                                           OlengKillerBots.append(target)
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
                                           OlengKillerBots.remove(target)
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
                                    ma = AbiOlengKiller.getContact(i)
                                    AbiOlengKiller.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "tikungan" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = AbiOlengKiller.getContact(i)
                                    AbiOlengKiller.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in OlengKillerBots:
                                    ma = AbiOlengKiller.getContact(i)
                                    AbiOlengKiller.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

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
                                wait["leaveMsg"] = True
                                sendTextTemplate(msg.to,"🔹ʟᴇғᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif cmd == "left off" or text.lower() == 'left off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["leaveMsg"] = False
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
                                    ma += str(a) + ". " +AbiOlengKiller.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"🔹ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ🔹\n\n"+ma+"\n🔹ᴊᴜᴍʟᴀʜ「%s」ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ🔹" %(str(len(wait["blacklist"]))))

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
                                    ma += str(a) + ". " +AbiOlengKiller.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"??ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ🔹\n\n"+ma+"\n🔹ᴊᴜᴍʟᴀʜ「%s」ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ🔹" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "tersangka" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    sendTextTemplate(msg.to,"🔹ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʟᴀᴄᴋʟɪsᴛ🔹")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = AbiOlengKiller.getContact(i)
                                        AbiOlengKiller.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = AbiOlengKiller.getContacts(wait["blacklist"])
                              mc = "「%i」ᴜsᴇʀ ʙʟᴀᴄᴋʟɪsᴛ" % len(ragets)
                              sendTextTemplate(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ʙᴜʀᴏɴᴀɴ🔹\n  "    +mc)
                              
                        elif text.lower() == 'payment':
                               AbiOlengKiller.sendMessage(msg.to, "ᴘᴀʏᴍᴇɴᴛ ᴠɪᴀ ʙᴀɴᴋ\nɴᴏ ʀᴇᴋ : 481901020711531\nᴀᴛᴀs ɴᴀᴍᴀ : muhazir\nʙᴀɴᴋ ʙʀɪ\n\nᴠɪᴀ ᴘᴜʟsᴀ\n08992906209"    +mc)
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
                                  AbiOlengKiller.sendMessage(msg.to, "🔹Gagal mengganti Respon Msg")
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
                               try:AbiOlengKiller.inviteIntoGroup(to, [mid]);has = "OK"
                               except:has = "NOT"
                               try:AbiOlengKiller.kickoutFromGroup(to, [mid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               AbiOlengKiller.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))

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
                                     group = AbiOlengKiller.findGroupByTicket(ticket_id)
                                     AbiOlengKiller.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     AbiOlengKiller.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)

while True:
  try:
      Ops = AbiOlengKiller.poll.fetchOperations(AbiOlengKiller.revision, 50)
      for op in Ops:
        if op.type != 0:
          AbiOlengKiller.revision = max(AbiOlengKiller.revision, op.revision)
          bot(op)
  except Exception as E:
    E = str(E)
    if "reason=None" in E:
      print (E)
      time.sleep(60)
      restart_program()
      
