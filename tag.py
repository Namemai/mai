# -*- coding: utf-8 -*-

from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

nadya = LINE()
#nadya = LINE("TOKEN KAMU")
#nadya = LINE("Email","Password")
nadya.log("Auth Token : " + str(nadya.authToken))
channelToken = nadya.getChannelResult()
nadya.log("Channel Token : " + str(channelToken))

nadyaMID = nadya.profile.mid
nadyaProfile = nadya.getProfile()
lineSettings = nadya.getSettings()
oepoll = OEPoll(nadya)
#==============================================================================#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)


myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = nadyaProfile.displayName
myProfile["statusMessage"] = nadyaProfile.statusMessage
myProfile["pictureStatus"] = nadyaProfile.pictureStatus
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
#    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
    
def logError(text):
    nadya.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        nadya.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage =" ✡ M A I ✡" + "\n" + \
                  " " + "\n" + \
                  "🔰〘เมนูคำสั่ง〙🔰" + "\n" + \
                  "🇳🇱➠️ H1" + "\n" + \
                  "🇳🇱➠️ H2" + "\n" + \
                  "🇳🇱➠️ H3" + "\n" + \
                  " " + "\n" + \
                  "🔰〘สเตตัส〙🔰" + "\n" + \
                  "🇳🇱➠️ รีบอท" + "\n" + \
                  "🇳🇱➠️ ออน" + "\n" + \
                  "🇳🇱➠️ Speed" + "\n" + \
                  "🇳🇱➠️ เชคค่า" + "\n" + \
                  "🇳🇱➠️ ข้อมูล" + "\n" + \
                  "🇳🇱➠️ ลบรัน" + "\n" + \
                  "🇳🇱➠️ เทส" + "\n" + \
                  "🇳🇱➠️ ยกเชิญ" + "\n" + \
                  "🇳🇱➠️ เชิญโทร" + "\n" + \
                  "🇳🇱➠️ พูด [สั่งสิริพูดตาม]" + "\n" + \
                  "🇳🇱➠️ คท" + "\n" + \
                  "🇳🇱➠️ มิด" + "\n" + \
                  "🇳🇱➠️ ชื่อ" + "\n" + \
                  "🇳🇱➠️ nema[ใส่ชื่อที่จะเปลี่ยน]" + "\n" + \
                  "🇳🇱➠️ ตัส" + "\n" + \
                  "🇳🇱➠️ รูป" + "\n" + \
                  "🇳🇱➠️ รูปวีดีโอ" + "\n" + \
                  "🇳🇱➠️ รูปปก" + "\n" + \
                  " " + "\n" + \
                  "🔰〘คนอื่น〙🔰" + "\n" + \
                  "🇳🇱➠️ รายชื่อกลุ่ม" + "\n" + \
                  "🇳🇱➠️ คท「@คนอื่น」" + "\n" + \
                  "🇳🇱➠ มิด「@คนอื่น」" + "\n" + \
                  "🇳🇱➠️ ชื่อ「@คนอื่น」" + "\n" + \
                  "🇳🇱➠ ตัส「@คนอื่น」" + "\n" + \
                  "🇳🇱➠️ ดิส「@คนอื่น」" + "\n" + \
                  "🇳🇱➠️ เตะ「@คนอื่น」" + "\n" + \
                  "🇳🇱➠️ เด้ง「@คนอื่น」" + "\n" + \
                  "🇳🇱➠️ เชคห้อง" + "\n" + \
                  "🇳🇱➠️ ไอดีกลุ่ม" + "\n" + \
                  "🇳🇱➠️ ชื่อกลุ่ม" + "\n" + \
                  "🇳🇱➠️ รูปกลุ่ม" + "\n" + \
                  "🇳🇱➠️ ลิ้งกลุ่ม" + "\n" + \
                  "🇳🇱➠ #เปิดลิ้ง" + "\n" + \
                  "🇳🇱➠️ #ปิดลิ้ง" + "\n" + \
                  "🇳🇱➠️ รายชื่อคนในห้อง" + "\n" + \
                  " " + "\n" + \
                  "🔰〘คำสั่งอื่น〙🔰" + "\n" + \
                  "🇳🇱➠️ เขียน [ใส่ข้อความ]" + "\n" + \
                  "🇳🇱➠️ พิมตาม on " + "\n" + \
                  "🇳🇱➠ พิมตาม off " + "\n" + \
                  "🇳🇱➠️ รายชื่อพิมตาม" + "\n" + \
                  "🇳🇱➠️ เพิ่มพิมตาม「@คนอื่น」" + "\n" + \
                  "🇳🇱➠️ ลบพิมตาม「@คนอื่น」" + "\n" + \
                  "🇳🇱➠ แทค" + "\n" + \
                  "🇳🇱➠ เปิดอ่าน" + "\n" + \
                  "🇳🇱➠️ ปิดอ่าน" + "\n" + \
                  "🇳🇱➠️ คนอ่าน" + "\n" + \
                  "🇳🇱➠️ ลบเวลาอ่าน" + "\n" + \
                  " " 
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "🔰 คำสั่ง2 🔰" + "\n" + \
                         "🔜 เปิดแทคชื่อ" + "\n" + \
                         "🔜 ปิดแทคชื่อ" + "\n" + \
                         "🔜 เปิดแทคภาพ" + "\n" + \
                         "🔜 ปิดแทคภาพ" + "\n" + \
                         "🔜 เปิดเข้ากลุ่ม" + "\n" + \
                         "🔜 ปิดเข้ากลุ่ม" + "\n" + \
                         "🔜 เปิดอ่านแชท" + "\n" + \
                         "🔜 ปิดอ่านแชท" + "\n" + \
                         "🔜 เปิดบล็อคแอด" + "\n" + \
                         "🔜 ปิดบล็อคแอด" + "\n" + \
                         "🔜 เปิดเชคติ๊กเก้อ" + "\n" + \
                         "🔜 ปิดเชคติ๊กเก้อ" + "\n" + \
                         "🔜 เปิดออกแชท" + "\n" + \
                         "🔜 ปิดออกแชท" + "\n" + \
                         " "
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╔══[ คำสั่งแปลภาษา ]" + "\n" + \
                       "╠ af : afrikaans" + "\n" + \
                       "╠ sq : albanian" + "\n" + \
                       "╠ am : amharic" + "\n" + \
                       "╠ ar : arabic" + "\n" + \
                       "╠ hy : armenian" + "\n" + \
                       "╠ az : azerbaijani" + "\n" + \
                       "╠ eu : basque" + "\n" + \
                       "╠ be : belarusian" + "\n" + \
                       "╠ bn : bengali" + "\n" + \
                       "╠ bs : bosnian" + "\n" + \
                       "╠ bg : bulgarian" + "\n" + \
                       "╠ ca : catalan" + "\n" + \
                       "╠ ceb : cebuano" + "\n" + \
                       "╠ ny : chichewa" + "\n" + \
                       "╠ zh-cn : chinese (simplified)" + "\n" + \
                       "╠ zh-tw : chinese (traditional)" + "\n" + \
                       "╠ co : corsican" + "\n" + \
                       "╠ hr : croatian" + "\n" + \
                       "╠ cs : czech" + "\n" + \
                       "╠ da : danish" + "\n" + \
                       "╠ nl : dutch" + "\n" + \
                       "╠ en : english" + "\n" + \
                       "╠ eo : esperanto" + "\n" + \
                       "╠ et : estonian" + "\n" + \
                       "╠ tl : filipino" + "\n" + \
                       "╠ fi : finnish" + "\n" + \
                       "╠ fr : french" + "\n" + \
                       "╠ fy : frisian" + "\n" + \
                       "╠ gl : galician" + "\n" + \
                       "╠ ka : georgian" + "\n" + \
                       "╠ de : german" + "\n" + \
                       "╠ el : greek" + "\n" + \
                       "╠ gu : gujarati" + "\n" + \
                       "╠ ht : haitian creole" + "\n" + \
                       "╠ ha : hausa" + "\n" + \
                       "╠ haw : hawaiian" + "\n" + \
                       "╠ iw : hebrew" + "\n" + \
                       "╠ hi : hindi" + "\n" + \
                       "╠ hmn : hmong" + "\n" + \
                       "╠ hu : hungarian" + "\n" + \
                       "╠ is : icelandic" + "\n" + \
                       "╠ ig : igbo" + "\n" + \
                       "╠ id : indonesian" + "\n" + \
                       "╠ ga : irish" + "\n" + \
                       "╠ it : italian" + "\n" + \
                       "╠ ja : japanese" + "\n" + \
                       "╠ jw : javanese" + "\n" + \
                       "╠ kn : kannada" + "\n" + \
                       "╠ kk : kazakh" + "\n" + \
                       "╠ km : khmer" + "\n" + \
                       "╠ ko : korean" + "\n" + \
                       "╠ ku : kurdish (kurmanji)" + "\n" + \
                       "╠ ky : kyrgyz" + "\n" + \
                       "╠ lo : lao" + "\n" + \
                       "╠ la : latin" + "\n" + \
                       "╠ lv : latvian" + "\n" + \
                       "╠ lt : lithuanian" + "\n" + \
                       "╠ lb : luxembourgish" + "\n" + \
                       "╠ mk : macedonian" + "\n" + \
                       "╠ mg : malagasy" + "\n" + \
                       "╠ ms : malay" + "\n" + \
                       "╠ ml : malayalam" + "\n" + \
                       "╠ mt : maltese" + "\n" + \
                       "╠ mi : maori" + "\n" + \
                       "╠ mr : marathi" + "\n" + \
                       "╠ mn : mongolian" + "\n" + \
                       "╠ my : myanmar (burmese)" + "\n" + \
                       "╠ ne : nepali" + "\n" + \
                       "╠ no : norwegian" + "\n" + \
                       "╠ ps : pashto" + "\n" + \
                       "╠ fa : persian" + "\n" + \
                       "╠ pl : polish" + "\n" + \
                       "╠ pt : portuguese" + "\n" + \
                       "╠ pa : punjabi" + "\n" + \
                       "╠ ro : romanian" + "\n" + \
                       "╠ ru : russian" + "\n" + \
                       "╠ sm : samoan" + "\n" + \
                       "╠ gd : scots gaelic" + "\n" + \
                       "╠ sr : serbian" + "\n" + \
                       "╠ st : sesotho" + "\n" + \
                       "╠ sn : shona" + "\n" + \
                       "╠ sd : sindhi" + "\n" + \
                       "╠ si : sinhala" + "\n" + \
                       "╠ sk : slovak" + "\n" + \
                       "╠ sl : slovenian" + "\n" + \
                       "╠ so : somali" + "\n" + \
                       "╠ es : spanish" + "\n" + \
                       "╠ su : sundanese" + "\n" + \
                       "╠ sw : swahili" + "\n" + \
                       "╠ sv : swedish" + "\n" + \
                       "╠ tg : tajik" + "\n" + \
                       "╠ ta : tamil" + "\n" + \
                       "╠ te : telugu" + "\n" + \
                       "╠ th : thai" + "\n" + \
                       "╠ tr : turkish" + "\n" + \
                       "╠ uk : ukrainian" + "\n" + \
                       "╠ ur : urdu" + "\n" + \
                       "╠ uz : uzbek" + "\n" + \
                       "╠ vi : vietnamese" + "\n" + \
                       "╠ cy : welsh" + "\n" + \
                       "╠ xh : xhosa" + "\n" + \
                       "╠ yi : yiddish" + "\n" + \
                       "╠ yo : yoruba" + "\n" + \
                       "╠ zu : zulu" + "\n" + \
                       "╠ fil : Filipino" + "\n" + \
                       "╠ he : Hebrew" + "\n" + \
                       "╚══[]" + "\n" + "\n\n" + \
                         "วิธีใช้ tr-ตามด้วยตัวย่อประเทศ\nเช่น tr-th สวัสดี เป็นต้น"
    return helpTranslate
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
            	nadya.blockContact(op.param1)
                #nadya.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(nadya.getContact(op.param1).displayName)))
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            group = nadya.getGroup(op.param1)
            if settings["autoJoin"] == True:
                nadya.acceptGroupInvitation(op.param1)
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                nadya.leaveRoom(op.param1)
        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#














#==============================================================================#
                if text.lower() == 'h1':
                    helpMessage = helpmessage()
                    nadya.sendMessage(to, str(helpMessage))
                elif text.lower() == 'h2':
                    helpTextToSpeech = helptexttospeech()
                    nadya.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'h3':
                    helpTranslate = helptranslate()
                    nadya.sendMessage(to, str(helpTranslate))
#==============================================================================#
                elif "เชิญโทร" in msg.text.lower():
                    if msg.toType == 2:
                       sep = text.split(" ")
                       strnum = text.replace(sep[0] + " ","")
                       num = int(strnum)
                       nadya.sendMessage(to, "เชิญโทรแล้วครับเจ้านายʕ•ᴥ•ʔ")
                       for var in range(0,num):
                          group = line.getGroup(to)
                          members = [mem.mid for mem in group.members]
                          naday.acquireGroupCallRoute(to)
                elif "ไวรัส." == msg.text.lower():
                    msg.contentType = 13
                    nadya.sendMessage(to,)
                    nadya.sendContact(to, "u1f41296217e740650e0448b96851a3e2")
                elif "เทส" == msg.text.lower():
                    nadya.sendMessage(to,"LOADING:▒...0%")
                    nadya.sendMessage(to,"███████████..100.0%")
                    nadya.sendMessage(to,"บอทไม่ได้หลุดครับเจ้านายʕ•ᴥ•ʔ")
                elif "name " in msg.text.lower():
                    spl = re.split("name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                       prof = nadya.getProfile()
                       prof.displayName = spl[1]
                       nadya.updateProfile(prof)
                       nadya.sendMessage(to, "เปลี่ยนชื่อแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif "ยกเชิญ" == msg.text.lower():
                    if msg.toType == 2:
                        group = nadya.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            nadya.cancelGroupInvitation(msg.to,[_mid])
                        nadya.sendMessage(to,"ลบค้างเชิญหมดแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif "ลบรัน" in msg.text.lower():
                    spl = re.split("ลบรัน",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = nadya.getGroupIdsInvited()
                        txt = "กำลังลบให้ครับเจ้านายʕ•ᴥ•ʔ "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        nadya.sendMessage(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                          try:
                             nadya.acceptGroupInvitation(gr)
                             if spl[1] != "":
                                 nadya.sendMessage(gr,spl[1])
                             nadya.leaveGroup(gr)
                             nadya.sendMessage(msg.to,"ลบรันหมดแล้วครับเจ้านายʕ•ᴥ•ʔ")
                          except:
                             pass
                elif text.lower() == 'speed':
                    start = time.time()
                    nadya.sendMessage(to, "ช้ามากครับเจ้านาย")
                    elapsed_time = time.time() - start
                    nadya.sendMessage(to, "\n\n{}วินาที\n\n✍️".format(str(elapsed_time)))
                elif text.lower() == 'รีบอท':
                    nadya.sendMessage(to, "กำลังรีบอท กรุณารอสักครู่.....")
                    time.sleep(5)
                    nadya.sendMessage(to, "รีบอทเส็ดแล้วครับ กดลิ้งล็อคบอทใหม่ด้วยครับเจ้านาย")
                    restartBot()
                elif text.lower() == 'ออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    nadya.sendMessage(to, "ʕ•ᴥ•ʔระยะเวลาการทำงานของบอทʕ•ᴥ•ʔ\n{}".format(str(runtime)))
                elif text.lower() == 'ข้อมูล':
                    try:
                        arr = []
                        owner = "ude3230559bf63a55b9c28aa20ea194e3"
                        creator = nadya.getContact(owner)
                        contact = nadya.getContact(nadyaMID)
                        grouplist = nadya.getGroupIdsJoined()
                        contactlist = nadya.getAllContactIds()
                        blockedlist = nadya.getBlockedContactIds()
                        ret_ = "╔══[ ข้อมูลไอดีคุณ ]"
                        ret_ += "\n╠ ชื่อ : {}".format(contact.displayName)
                        ret_ += "\n╠ กลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ เพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ บล็อค : {}".format(str(len(blockedlist)))
                        ret_ += "\n╚══[ ข้อมูลไอดีคุณ ]"
                        nadya.sendMessage(to, str(ret_))
                    except Exception as e:
                        nadya.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'เชคค่า':
                    try:
                        ret_ = "╔════════════"
                        if settings["autoAdd"] == True: ret_ += "\n║ ระบบออโต้บล็อคแอด ✔"
                        else: ret_ += "\n║ ระบบออโต้บล็อคแอด ✘"
                        if settings["autoJoin"] == True: ret_ += "\n║ ระบบเข้ากลุ่มออโต้ ✔"
                        else: ret_ += "\n║ ระบบเข้ากลุ่มออโต้ ✘"
                        if settings["autoLeave"] == True: ret_ += "\n║ ระบบออกแชทรวม  ✔"
                        else: ret_ += "\n║ ระบบออกแชทรวม ✘"
                        if settings["autoRead"] == True: ret_ += "\n║ ระบบอ่านข้อความออโต้  ✔"
                        else: ret_ += "\n║ ระบบอ่านข้อความออโต้ ✘"
                        if settings["checkSticker"] == True: ret_ += "\n║ ระบบเช็คสติ้กเกอร์ ✔"
                        else: ret_ += "\n║ ระบบเช็คสติ้กเกอร์ ✘"
                        if settings["detectMention"] == True: ret_ += "\n║ ระบบข้อความแทค ✔"
                        else: ret_ += "\n║ ระบบข้อความแทค ✘"
                        if settings["detectMention"] == True: ret_ += "\n║ ระบบแทคส่งรูป ✔"
                        else: ret_ += "\n║ ระบบแทคส่งรูป ✘"
                        ret_ += "\n╚════════════"
                        nadya.sendMessage(to, str(ret_))
                    except Exception as e:
                        nadya.sendMessage(msg.to, str(e))
                elif text.lower() == 'เปิดบล็อคแอด':
                    settings["autoAdd"] = True
                    nadya.sendMessage(to, "เปิดระบบบล็อคแล้วแอดแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'ปิดบล็อคแอด':
                    settings["autoAdd"] = False
                    nadya.sendMessage(to, "ปิดระบบบล็อคแอดแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'เปิดเข้ากลุ่ม':
                    settings["autoJoin"] = True
                    nadya.sendMessage(to, "เปิดระบบเข้ากลุ่มออโต้แล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'ปิดเข้ากลุ่ม':
                    settings["autoJoin"] = False
                    nadya.sendMessage(to, "ปิดระบบเข้ากลุ่มออโต้แล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'เปิดออกแชท':
                    settings["autoLeave"] = True
                    nadya.sendMessage(to, "เปิดระบบออกแชทรวมแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'ปิดออกแชท':
                    settings["autoLeave"] = False
                    nadya.sendMessage(to, "ปิดระบบออกแชทรวมแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'เปิดอ่านแชท':
                    settings["autoRead"] = True
                    nadya.sendMessage(to, "เปิดระบบอ่านแชทแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'ปิดอ่านแชท':
                    settings["autoRead"] = False
                    nadya.sendMessage(to, "ปิดระบบอ่านแชทแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'เปิดเชคติ๊กเก้อ':
                    settings["checkSticker"] = True
                    nadya.sendMessage(to, "เปิดระบบเช็คสติ้กเกอร์แล้วʕ•ᴥ•ʔ")
                elif text.lower() == 'ปิดเชคติ๊กเก้อ':
                    settings["checkSticker"] = False
                    nadya.sendMessage(to, "ปิดระบบเช็คสติ้กเกอร์แล้วʕ•ᴥ•ʔ")
                elif text.lower() == 'เปิดแทคชื่อ':
                    settings["detectMention"] = True
                    nadya.sendMessage(to, "เปิดระบบข้อความแทคแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'ปิดแทคชื่อ':
                    settings["detectMention"] = False
                    nadya.sendMessage(to, "ปิดระบบข้อความแทคแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'เปิดแทคภาพ':
                    settings["potoMention"] = True
                    nadya.sendMessage(msg.to,"เปิดแทคส่งรูปแล้วแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'ปิดแทคภาพ':
                    settings["potoMention"] = False
                    nadya.sendMessage(msg.to,"ปิดแทคส่งรูปแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'clonecontact':
                    settings["copy"] = True
                    nadya.sendMessage(to, "ก็อปปี้ด้วยคอนแทคʕ•ᴥ•ʔ")
                elif msg.text.lower().startswith("เขียน "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    nadya.sendImageWithURL(msg.to, urlnya)
#==============================================================================#

                elif text.lower() == '!แทค':
                    gs = nadya.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendMessage(to, "ไม่มีคนใส่ชื่อร่องหนครับเจ้านายʕ•ᴥ•ʔ")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        nadya.sendMessage(to, mc)
                elif text.lower() == '!มิด':
                    gs = nadya.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        nadya.sendMessage(to, "ไม่มีคนใส่ชื่อร่องหนครับเจ้านายʕ•ᴥ•ʔ")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        nadya.sendMessage(to,mc)
                elif text.lower() == '!คท':
                    gs = nadya.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        nadya.sendMessage(to, "ไม่มีคนใส่ชื่อร่องหนครับเจ้านายʕ•ᴥ•ʔ")
                    else:
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            mi_d = contact.mid
                            nadya.sendContact(to, mi_d)
                elif text.lower() == 'คท':
                    sendMessageWithMention(to, nadyaMID)
                    nadya.sendContact(to, nadyaMID)
                elif text.lower() == 'มิด':
                    nadya.sendMessage(msg.to, nadyaMID)
                elif text.lower() == 'ชื่อ':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendMessage(msg.to, me.displayName)
                elif text.lower() == 'ตัส':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendMessage(msg.to, me.statusMessage)
                elif text.lower() == 'รูป':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'รูปวีดีโอ':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'รูปปก':
                    me = nadya.getContact(nadyaMID)
                    cover = nadya.getProfileCoverURL(nadyaMID)    
                    nadya.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            mi_d = contact.mid
                            nadya.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("มิด "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "\n"
                        for ls in lists:
                            ret_ += ls
                        nadya.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendMessage(msg.to, contact.displayName)
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendMessage(msg.to, contact.statusMessage)
                elif msg.text.lower().startswith("รูป "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + nadya.getContact(ls).pictureStatus
                            nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("รูปวีดีโอ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + nadya.getContact(ls).pictureStatus + "/vp"
                            nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("รูปปก "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = "http://dl.profile.line-cdn.net/" + nadya.getProfileCoverURL(ls)
                                nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("ท้าไม้ตาย "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            nadya.sendMessage(msg.to,"2นาฬิกาฟาเรนไฮต์อุณหภูมิ155เซลเซียสแรงปืน32อุณหภูมิความชื้น22นาฬิกาปาดขวายิงเพื่อหวังผล..")
                            nadya.kickoutFromGroup(msg.to,[target])
                            nadya.sendMessage(msg.to,"!!แตกก")
                        except:
                            nadya.sendText(msg.to,"Error")
                elif msg.text.lower().startswith("เตะ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            nadya.kickoutFromGroup(msg.to,[target])
                        except:
                            nadya.sendText(msg.to,"Error")
#==============================================================================#
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    nadya.sendContact(to, mmid)
                elif msg.text.lower().startswith("เพิ่มพิมตาม "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            nadya.sendMessage(msg.to,"เพิ่มคนพิมตามแล้วครับเจ้านายʕ•ᴥ•ʔ")
                            break
                        except:
                            nadya.sendMessage(msg.to,"เพิ่มคนพิมตามแล้วครับเจ้านายʕ•ᴥ•ʔ")
                            break
                elif msg.text.lower().startswith("ลบพิมตาม "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            nadya.sendMessage(msg.to,"ลบการเลียนแบบแล้วครับเจ้านายʕ•ᴥ•ʔ")
                            break
                        except:
                            nadya.sendMessage(msg.to,"ลบการเลียนแบบแล้วครับเจ้านายʕ•ᴥ•ʔ")
                            break
                elif text.lower() == 'รายชื่อพิมตาม':
                    if settings["mimic"]["target"] == {}:
                        nadya.sendMessage(msg.to,"ไม่มีเป้าหมายʕ•ᴥ•ʔ")
                    else:
                        mc = "╔══[ รายชื่อคนพิมตาม ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+nadya.getContact(mi_d).displayName
                        nadya.sendMessage(msg.to,mc + "\n╚══[ ทั้งหมด ]")
                    
                elif "พิมตาม" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            nadya.sendMessage(msg.to,"เปิดระบบพิมตามแล้วครับเจ้านายʕ•ᴥ•ʔ")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            nadya.sendMessage(msg.to,"ปิดระบบพิมตามแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif "เด้ง:" in text:
                    midd = msg.text.replace("เด้ง:","")
                    nadya. kickoutFromGroup(msg.to,[midd])
                    nadya. findAndAddContactsByMid(midd)
                    nadya.inviteIntoGroup(msg.to,[midd])
                    nadya.cancelGroupInvitation(msg.to,[midd])
                elif "เด้ง " in msg.text:
                        vkick0 = msg.text.replace("เด้ง ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = nadya.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    nadya.kickoutFromGroup(msg.to,[target])
                                    nadya.findAndAddContactsByMid(target)
                                    nadya. inviteIntoGroup(msg.to,[target])
                                except:
                                    pass
#==============================================================================#
                elif text.lower() == 'เชคแอด':
                    group = nadya.getGroup(to)
                    GS = group.creator.mid
                    nadya.sendContact(to, GS)
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendMessage(to, "\n" + gid.id)
                elif text.lower() == 'รูปกลุ่ม':
                    group = nadya.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    nadya.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendMessage(to, "\n" + gid.name)
                elif text.lower() == 'ลิ้งกลุ่ม':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = nadya.reissueGroupTicket(to)
                            nadya.sendMessage(to, "https://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            nadya.sendMessage(to, "กรุณาเปิดลิ้งกลุ่มก่อน\nลงคำสั่งนี้ด้วยครับเจ้านายʕ•ᴥ•ʔ".format(str(settings["keyCommand"])))
                elif text.lower() == '#เปิดลิ้ง':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            nadya.sendMessage(to, "เปิดแล้วครับเจ้านายʕ•ᴥ•ʔ")
                        else:
                            group.preventedJoinByTicket = False
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "เปิดแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == '#ปิดลิ้ง':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            nadya.sendMessage(to, "ปิดแล้วครับเจ้านายʕ•ᴥ•ʔ")
                        else:
                            group.preventedJoinByTicket = True
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "ปิดแล้วครับเจ้านายʕ•ᴥ•ʔ")
                elif text.lower() == 'เชคห้อง':
                    group = nadya.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ไม่พบผู้สร้าง"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ลิ้งถูกปิดอยู่.."
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(nadya.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลกลุ่ม ]"
                    ret_ += "\n╠ ชื่อกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีกลุ่ม:{}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ สมาชิกกลุ่ม : {}".format(str(len(group.members)))
                    ret_ += "\n╠ ค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ กลุ่มตั๋ว:{}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม : {}".format(gTicket)
                    ret_ += "\n╚══[ M a i ]"
                    nadya.sendMessage(to, str(ret_))
                    nadya.sendImageWithURL(to,)
                elif text.lower() == 'รายชื่อคนในห้อง':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        ret_ = "╔══[ รายชื่อสมชิกกลุ่ม ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวนสมาชิก {} คนครับ้จ้านายʕ•ᴥ•ʔ ]".format(str(len(group.members)))
                        nadya.sendMessage(to, str(ret_))
                elif text.lower() == 'รายชื่อกลุ่ม':
                        groups = nadya.groups
                        ret_ = "╔══[ รายชื่อกลุ่ม ]"
                        no = 0 + 1
                        for gid in groups:
                            group = nadya.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวนกลุ่ม {} กลุ่มครับเจ้านายʕ•ᴥ•ʔ ]".format(str(len(groups)))
                        nadya.sendMessage(to, str(ret_))
#==============================================================================#          
                elif text.lower() == 'แทค':
                    group = nadya.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        nadya.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        nadya.sendMessage(to, "จำนวนสมาชิก {} คนครับเจ้านายʕ•ᴥ•ʔ".format(str(len(nama))))          
                elif text.lower() == 'เปิดอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                nadya.sendMessage(msg.to,"เปิดหาคนซุ่มʕ•ᴥ•ʔ")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            nadya.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'ปิดอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        nadya.sendMessage(msg.to,"ปิดหาคนซุ่มʕ•ᴥ•ʔ")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        nadya.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'ลบเวลาอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        nadya.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        nadya.sendMessage(msg.to, "ไม่ได้เปิดการหาʕ•ᴥ•ʔ")
                        
                elif text.lower() == 'คนอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            nadya.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = nadya.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            nadya.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        nadya.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================#
                elif msg.text.lower().startswith("พูด "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    nadya.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#   
                elif text.lower() == 'ปฎิทิน':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["วันจัน", "วันอังคาร", "วันพุธ", "วันพฤหั", "วันศุก","วันเสา", "วันอาทิต"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["มกราคม", "กุมภาพัน", "มีนาคม", "เมษายน", "พฤษาภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    nadya.sendMessage(msg.to, readTime)                 
                elif "เว็บไซต์ภาพหน้าจอ" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        nadya.sendImageWithURL(to, data["result"])
                elif "ตรวจสอบวันที่" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    nadya.sendMessage(to, str(ret_))
                elif "ข้อมูลIG" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ ชื่อ : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ ชื่อผู้ใช้ : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            nadya.sendImageWithURL(to, str(path))
                            nadya.sendMessage(to, str(ret_))
                        except:
                            nadya.sendMessage(to, "Pengguna tidak ditemukan")
                elif "โพสIG" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
                        end_cursor = ''
                        for count in range(1, 999):
                            print('PAGE: ', count)
                            r = x.get(profile, params={'max_id': end_cursor})
                        
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)
                        
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                if node['is_video']:
                                    page = 'https://www.instagram.com/p/' + node['code']
                                    r = x.get(page)
                                    url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                    print(url)
                                    nadya.sendVideoWithURL(msg.to,url)
                                else:
                                    print (node['display_src'])
                                    nadya.sendImageWithURL(msg.to,node['display_src'])
                            end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                elif "รูปภาพ" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            nadya.sendImageWithURL(to, str(path))
                elif "ยูทูป" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html5lib")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        nadya.sendMessage(to, str(ret_))
                elif "ขอเพลง" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                ret_ = "╔══[ Music ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ reading Audio ]"
                                nadya.sendMessage(to, str(ret_))
                                nadya.sendAudioWithURL(to, song[3])
                        except:
                            nadya.sendMessage(to, "Musik tidak ditemukan")
                elif "เนื้อเพลง" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
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
                                ret_ = "╔══[ Lyric ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                nadya.sendMessage(to, str(ret_))
                        except:
                            nadya.sendMessage(to, "Lirik tidak ditemukan")
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══( ข้อมูลสติกเกอร์ )"
                    ret_ += "\n╠ สติกเกอร์ id : {}".format(stk_id)
                    ret_ += "\n╠ แพคเกจสติกเกอร์ : {}".format(pkg_id)
                    ret_ += "\n╠ เวอร์ชั่นสติกเกอร: {}".format(stk_ver)
                    ret_ += "\n╠ ลิ้งสติกเกอร์ : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══( ข้อมูลสติกเกอร์ )"
                    nadya.sendMessage(to, str(ret_))
                    
            elif msg.contentType == 13:
                if settings["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = nadya.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Copy")
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        nadya.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                nadya.cloneContactProfile(target)
                                nadya.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                                settings['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     settings["copy"] = False
                                     break                     
                    
                    
#==============================================================================#
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    nadya.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        nadya.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in nadyaMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                        if settings['potoMention'] == True:
                             contact = nadya.getContact(msg._from)
                             cName = contact.pictureStatus
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in nadyaMID:
                                          nadya.sendImageWithURL(to,ret_)
                                          break
                if msg.contentType == 0 and sender not in nadyaMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = nadya.getContact(msg._from)
                             cName = contact.displayName
                             balas = ["(ข้อความออโต้) เจ้าของไลน์ไม่อยู่ครับ ติดต่อซื้อบอททักแชทมาเลยครับ กดที่ลิ้งไอดี http://line.me/ti/p/~mai06555mai"]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in nadyaMID:
                                          nadya.sendMessage(to,ret_)
                                          sendMessageWithMention(to,)
                                          break
                if msg.text in ["maitag","Maitag","แท็ค","tag","Tagall","Tag"]:
                    nadya.sendMessage(to, "แทค")
                if msg.text in ["เปิดเข้ากลุ่ม"]:
                    nadya.sendMessage(to, "เปิดเข้ากลุ่ม")
                if msg.text in ["ปิดเข้ากลุ่ม"]:
                    nadya.sendMessage(to, "ปิดเข้ากลุ่ม")
                if msg.text in ["set","เชค","Set"]:
                    nadya.sendMessage(to, "เชคค่า")
                if msg.text in ["เปิดแทคชื่อ"]:
                    nadya.sendMessage(to, "เปิดแทคชื่อ")
                if msg.text in ["เปิดแทครูป"]:
                    nadya.sendMessage(to, "เปิดแทครูป")
                if msg.text in ["เปิดอ่านแชท"]:
                    nadya.sendMessage(to, "เปิดอ่านแชท")
                if msg.text in ["เชคห้อง"]:
                    nadya.sendMessage(to, "เชคห้อง")
                if msg.text in ["sp","Sp","Speed","speed"]
                    nadya.sendMessage(to, "แรงมองแทบไม่ทันเลยครับเจ้านาย")
#==============================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
