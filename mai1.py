# - * - coding: utf-8 - * -

จากการนำเข้า  linepy *
จาก datetime นำเข้า datetime
จากการนอนหลับเข้าเวลา
จากการนำเข้า BeautifulSoup bs4
จากรูปแบบการนำเข้าที่เป็นมิตรต่อมนุษย์format_timespan, format_size, format_number, format_length
เวลานำเข้า , สุ่ม, sys, json, ตัวแปลงสัญญาณ, threading, glob, อีกครั้ง, สตริง, os, การร้องขอ, กระบวนการย่อย, หก, ast, pytz, urllib, urllib.parse
จาก GTT import gTTS
จาก googletrans import Translator
# =========================================== ============================= #
botStart = time.time ()

nadya = LINE ()
# nadya = LINE ("TOKEN KAMU")
# nadya = LINE ("อีเมล", "รหัสผ่าน")
nadya.log ( " Auth Token: "  +  str (nadya.authToken))
channelToken = nadya.getChannelResult ()
nadya.log ( "ช่อง Token: "  +  STR ( ช่อง Token ))

nadyaMID = nadya.profile.mid
nadyaProfile = nadya.getProfile ()
lineSettings = nadya.getSettings ()
oepoll = OEPoll (nadya)
# =========================================== ============================= #
readOpen = codecs.open ( " read.json " , " r " , " utf-8 " )
settingsOpen = codecs.open ( " temp.json " , " r " , " utf-8 " )

อ่าน= json.load (readOpen)
settings = json.load (settingsOpen)


myProfile = {
	" displayName " : " " ,
	" statusMessage " : " " ,
	" pictureStatus " : " "
}

myProfile [ " displayName " ] = nadyaProfile.displayName
myProfile [ " statusMessage " ] = nadyaProfile.statusMessage
myProfile [ " pictureStatus " ] = nadyaProfile.pictureStatus
# =========================================== ============================= #
def  restartBot ():
    พิมพ์ ( " [INFO] BET RESETTED " )
    สำรองข้อมูล()
#     time.sleep (3)
    python = sys.executable
    os.execl (หลาม, หลาม, * sys.argv)
    
def  backupData ():
    ลอง :
        backup = settings
        f = codecs.open ( ' temp.json ' , ' w ' , ' utf-8 ' )
        json.dump (สำรอง f, sort_keys = True , indent = 4 , ensure_ascii = เท็จ )
        backup = read
        f = codecs.open ( ' read.json ' , ' w ' , ' utf-8 ' )
        json.dump (สำรอง f, sort_keys = True , indent = 4 , ensure_ascii = เท็จ )
        คืน จริง
    ยกเว้น ข้อยกเว้น เป็นข้อผิดพลาด:
        : ฟังก์ชัน LogError (ผิด)
        กลับ เท็จ    
    
def  logError ( ข้อความ ):
    nadya.log ( " [ERROR] "  +  STR (ข้อความ))
    time_ = datetime.now ()
    กับ open ( " errorLog.txt " , " a " ) เป็นข้อผิดพลาด:
        error.write ( " \ n [ % s ] % s "  % ( str (เวลา), ข้อความ))
        
def  sendMessageWithMention ( เพื่อ , กลาง ):
    ลอง :
        aa =  ' {"S": "0", "E": "3", "M": ' + json.pumps (กลาง) + ' } '
        text_ =  ' @x '
        nadya.sendMessage (ไป text_, contentMetadata = { 'กล่าวถึง' : ' { "MENTIONEES": [ ' + AA + ' ]} ' } contentType = 0 )
    ยกเว้น ข้อยกเว้น เป็นข้อผิดพลาด:
        : ฟังก์ชัน LogError (ผิด)
        
def  helpmessage ():
    helpMessage = " ✡ MAI ✡ "  +  " \ n "  + \
                  "  "  +  " \ n "  + \
                  "เมนู +  คำสั่ง〙🔰 " + " \ n "  + \
                  " 🇳🇱➠️ H1 "  +  " \ n "  + \
                  " 🇳🇱➠️ H2 "  +  " \ n "  + \
                  " H3 "  +  " \ n "  + \
                  "  "  +  " \ n "  + \
                  " 🔰〘สเตตัส〙🔰 "  +  " \ n "  + \
                  " 🇳🇱➠️รีบอท"  +  " \ n "  + \
                  " 🇳🇱➠️ออน"  +  " \ n "  + \
                  "ความเร็ว🇳🇱➠️ "  +  " \ n "  + \
                  " 🇳🇱➠️เชคค่า"  +  " \ n "  + \
                  "ข้อมูล"  +  " \ n "  + \
                  " 🇳🇱➠️ลบรัน"  +  " \ n "  + \
                  " 🇳🇱➠️เทส"  +  " \ n "  + \
                  "ยกยก"  +  " \ n "  + \
                  " 🇳🇱➠️เชิญโทร"  +  " \ n "  + \
                  " 🇳🇱➠️พูด [สั่งสิริพูดตาม] "  +  " \ n "  + \
                  " 🇳🇱➠️คท"  +  " \ n "  + \
                  " 🇳🇱➠️มิด"  +  " \ n "  + \
                  " 🇳🇱➠️ชื่อ"  +  " \ n "  + \
                  " 🇳🇱➠️ nema [ใส่ชื่อที่จะเปลี่ยน] "  +  " \ n "  + \
                  " 🇳🇱➠️ตัส"  +  " \ n "  + \
                  " 🇳🇱➠️รูป"  +  " \ n "  + \
                  " 🇳🇱➠️รูปวีดีโอ"  +  " \ n "  + \
                  "รูปปก"  +  " \ n "  + \
                  "  "  +  " \ n "  + \
                  " 🔰〘คนอื่น〙🔰 "  +  " \ n "  + \
                  " 🇳🇱➠️รายชื่อกลุ่ม"  +  " \ n "  + \
                  " 🇳🇱➠️คท「@ คนอื่น」"  +  " \ n "  + \
                  " 🇳🇱➠มิด「@ คนอื่น」"  +  " \ n "  + \
                  " 🇳🇱➠️ชื่อ「 @ คนอื่น」"  +  " \ n "  + \
                  " 🇳🇱➠ตัส「@ คนอื่น」"  +  " \ n "  + \
                  " 🇳🇱➠️ดิส「 @ คนอื่น」"  +  " \ n "  + \
                  " 🇳🇱➠️เตะ「@ คนอื่น」"  +  " \ n "  + \
                  " 🇳🇱➠️เด้ง「@ คนอื่น」"  +  " \ n "  + \
                  " 🇳🇱➠️เชค"  +  " \ n "  + \
                  " 🇳🇱➠️ไอดีกลุ่ม"  +  " \ n "  + \
                  " 🇳🇱➠️ชื่อกลุ่ม"  +  " \ n "  + \
                  "รูปกลุ่ม"  +  " \ n "  + \
                  " 🇳🇱➠️ลิ้งกลุ่ม"  +  " \ n "  + \
                  " # เปิดลิ้ง"  +  " \ n "  + \
                  " # ปิดลิ้ง"  +  " \ n "  + \
                  " 🇳🇱➠️รายชื่อคนในห้อง"  +  " \ n "  + \
                  "  "  +  " \ n "  + \
                  " 🔰〘คำสั่งอื่น〙🔰 "  +  " \ n "  + \
                  " 🇳🇱➠️พิม ณ"  +  " \ n "  + \
                  " 🇳🇱➠พิมตาม off "  +  " \ n "  + \
                  " 🇳🇱➠️รายชื่อพิมตาม"  +  " \ n "  + \
                  " 🇳🇱➠️เพิ่มพิมตาม「@ คนอื่น」"  +  " \ n "  + \
                  " 🇳🇱➠️ลบพิมตาม「@ คนอื่น」"  +  " \ n "  + \
                  " 🇳🇱➠แทค"  +  " \ n "  + \
                  "เปิดอ่าน"  +  " \ n "  + \
                  "ปิดอ่าน"  +  " \ n "  + \
                  "คนอ่าน"  +  " \ n "  + \
                  " 🇳🇱➠️ลบเวลาอ่าน"  +  " \ n "  + \
                  "  " 
    helpMessage กลับ
    
def  helptexttospeech ():
    helpTextToSpeech =    " 🔰คำสั่ง 2 🔰 "  +  " \ n "  + \
                         " 🔜เปิดแทคชื่อ"  +  " \ n "  + \
                         " 🔜ปิดแทคชื่อ"  +  " \ n "  + \
                         " 🔜เปิดแทคภาพ"  +  " \ n "  + \
                         "ปิดการเขียนภาพ"  +  " \ n "  + \
                         " 🔜เปิดเข้ากลุ่ม"  +  " \ n "  + \
                         "เข้าสู่กลุ่ม"  +  " \ n "  + \
                         "เปิดอ่าน"  +  " \ n "  + \
                         "ปิดอ่านแชท"  +  " \ n "  + \
                         " 🔜เปิดบล็อคแอด"  +  " \ n "  + \
                         " 🔜ปิดบล็อคแอด"  +  " \ n "  + \
                         " 🔜เปิดเชคติ๊กเก้อ"  +  " \ n "  + \
                         " 🔜ปิดเชคติ๊กเก้อ"  +  " \ n "  + \
                         "เปิดตัวแชท"  +  " \ n "  + \
                         "ปิดการแชท"  +  " \ n "  + \
                         "  "
    return helpTextToSpeech
    
def  helptranslate ():
    helpTranslate =     " ╔══ [คำสั่งแปลภาษา] "  +  " \ n "  + \
                       " ╠ af: afrikaans "  +  " \ n "  + \
                       " ╠ sq: albanian "  +  " \ n "  + \
                       " ╠ am: amharic "  +  " \ n "  + \
                       " ╠ ar: arabic "  +  " \ n "  + \
                       " ╠ hy: armenian "  +  " \ n "  + \
                       " ╠ az: azerbaijani "  +  " \ n "  + \
                       " ╠ eu: basque "  +  " \ n "  + \
                       " ╠ be: belarusian "  +  " \ n "  + \
                       " ╠ bn: bengali "  +  " \ n "  + \
                       " bs: bosnian "  +  " \ n "  + \
                       " bg: bulgarian "  +  " \ n "  + \
                       " ca: catalan "  +  " \ n "  + \
                       " ╠ ceb: cebuano "  +  " \ n "  + \
                       " ny: chichewa "  +  " \ n "  + \
                       " ╠ zh-cn: chinese (simplified) "  +  " \ n "  + \
                       " ╠ zh-tw: ภาษาจีน (ดั้งเดิม) "  +  " \ n "  + \
                       " ╠ co: corsican "  +  " \ n "  + \
                       " hr: croatian "  +  " \ n "  + \
                       " cs: czech "  +  " \ n "  + \
                       " ╠ da: danish "  +  " \ n "  + \
                       " nl: ดัตช์"  +  " \ n "  + \
                       " ╠ en: english "  +  " \ n "  + \
                       " ╠ eo: esperanto "  +  " \ n "  + \
                       " ╠เอต: estonian "  +  " \ n "  + \
                       " ╠ tl: filipino "  +  " \ n "  + \
                       " ╠ fi: finnish "  +  " \ n "  + \
                       " ╠ fr: french "  +  " \ n "  + \
                       " ╠ fy: frisian "  +  " \ n "  + \
                       " ╠ gl: galician "  +  " \ n "  + \
                       " ╠ ka: georgian "  +  " \ n "  + \
                       " ╠เดอ: เจอร์แมน"  +  " \ n "  + \
                       " ╠ el: greek "  +  " \ n "  + \
                       " ╠ gu: gujarati "  +  " \ n "  + \
                       " ╠ ht: haitian creole "  +  " \ n "  + \
                       " ha: hausa "  +  " \ n "  + \
                       " haw: hawaiian "  +  " \ n "  + \
                       " ╠ iw: hebrew "  +  " \ n "  + \
                       " ╠ hi: hindi "  +  " \ n "  + \
                       " hmn: hmong "  +  " \ n "  + \
                       " ╠ hu: hungarian "  +  " \ n "  + \
                       " ╠คือไอซ์แลนด์"  +  " \ n "  + \
                       " ╠ ig: igbo "  +  " \ n "  + \
                       " ╠ id: indonesian "  +  " \ n "  + \
                       " ╠ ga: irish "  +  " \ n "  + \
                       " ╠ it: italian "  +  " \ n "  + \
                       " ╠ ja: japanese "  +  " \ n "  + \
                       " jw: javanese "  +  " \ n "  + \
                       " ╠ kn: กั ณ ณาท"  +  " \ n "  + \
                       " ╠ kk: kazakh "  +  " \ n "  + \
                       " ╠กม.: khmer "  +  " \ n "  + \
                       " ╠ ko: korean "  +  " \ n "  + \
                       " ╠ ku: kurdish (kurmanji) "  +  " \ n "  + \
                       " ╠ ky: kyrgyz "  +  " \ n "  + \
                       " ╠ lo: lao "  +  " \ n "  + \
                       " ╠ la: latin "  +  " \ n "  + \
                       " lv: latvian "  +  " \ n "  + \
                       " ╠ lt: lithuanian "  +  " \ n "  + \
                       " lb: luxembourgish "  +  " \ n "  + \
                       " mk: macedonian "  +  " \ n "  + \
                       " mg: malagasy "  +  " \ n "  + \
                       " ╠ ms: malay "  +  " \ n "  + \
                       " ╠ ml: malayalam "  +  " \ n "  + \
                       " mt: maltese "  +  " \ n "  + \
                       " ╠ mi: maori "  +  " \ n "  + \
                       " ╠ mr: marathi "  +  " \ n "  + \
                       " ╠ mn: mongolian "  +  " \ n "  + \
                       " ╠ฉัน: พม่า (พม่า) "  +  " \ n "  + \
                       " ╠ ne: nepali "  +  " \ n "  + \
                       " ╠ no: norwegian "  +  " \ n "  + \
                       " ╠ ps: pashto "  +  " \ n "  + \
                       " ╠ fa: persian "  +  " \ n "  + \
                       " ╠ pl: polish "  +  " \ n "  + \
                       " pt pt: portuguese "  +  " \ n "  + \
                       " ╠ pa: punjabi "  +  " \ n "  + \
                       " ╠ ro: romanian "  +  " \ n "  + \
                       " ╠ ru: russian "  +  " \ n "  + \
                       " ╠ sm: samoan "  +  " \ n "  + \
                       " ╠ gd: scots gaelic "  +  " \ n "  + \
                       " ╠ sr: serbian "  +  " \ n "  + \
                       " ╠ st: sesotho "  +  " \ n "  + \
                       " ╠ sn: shona "  +  " \ n "  + \
                       " sd: sindhi "  +  " \ n "  + \
                       " ╠ si: sinhala "  +  " \ n "  + \
                       " ╠ sk: slovak "  +  " \ n "  + \
                       " ╠ sl: สโลแกน"  +  " \ n "  + \
                       " ╠ดังนั้น: somali "  +  " \ n "  + \
                       " ╠ es: spanish "  +  " \ n "  + \
                       " su: sundanese "  +  " \ n "  + \
                       " ╠ sw: swahili "  +  " \ n "  + \
                       " sv: szwedzki "  +  " \ n "  + \
                       " ╠ tg: tajik "  +  " \ n "  + \
                       " ╠ ta: tamil "  +  " \ n "  + \
                       " ╠ Te: telugu "  +  " \ n "  + \
                       " ╠ th: thai "  +  " \ n "  + \
                       " ╠ tr: turkish "  +  " \ n "  + \
                       " ╠ uk: ukrainian "  +  " \ n "  + \
                       " ╠ ur: urdu "  +  " \ n "  + \
                       " ╠ uz: uzbek "  +  " \ n "  + \
                       " ╠ vi: vietnamese "  +  " \ n "  + \
                       " cy: เวลส์"  +  " \ n "  + \
                       " xh: xhosa "  +  " \ n "  + \
                       " yi: yiddish "  +  " \ n "  + \
                       " yo: yoruba "  +  " \ n "  + \
                       " ╠ zu: zulu "  +  " \ n "  + \
                       " ╠ fil: Filipino "  +  " \ n "  + \
                       " ╠เขา: ฮีบรู"  +  " \ n "  + \
                       " ╚══ [] "  +  " \ n "  +  " \ n \ n "  + \
                         "วิธีใช้ tr- ตามด้วยตัวย่อประเทศ\ nเช่น tr-th สวัสดีเป็นต้น"
    helpTranslate กลับ
# =========================================== ============================= #
def  lineBot ( op ):
    ลอง :
        ถ้า op.type ==  0 :
            พิมพ์ ( " [0] END OF OPERATION " )
            กลับ
        ถ้า op.type ==  5 :
            พิมพ์ ( " [5] NOTIFIED ADD CONTACT " )
            ถ้าการตั้งค่า [ " autoAdd " ] ==  True :
            	nadya.blockContact (op.param1)
                # nadya.sendMessage (op.param1, "Halo {} เทอร์มินัลเทเลแม็กซ์ที่มีคำว่า saya sebagai teman: D" .format (str (nadya.getContact (op.param1) .displayName)))
        if op.type ==  13 :
            พิมพ์ ( " [13] เชิญชวนกลุ่ม" )
            group = nadya.getGroup (op.param1)
            ถ้าการตั้งค่า [ " autoJoin " ] ==  True :
                nadya.acceptGroupInvitation (op.param1)
        ถ้า op.type ==  24 :
            พิมพ์ ( " [24] NOTAVED LEAVE ROOM " )
            ถ้าการตั้งค่า [ " autoLeave " ] ==  True :
                nadya.leaveRoom (op.param1)
        ถ้า op.type ==  25 :
            พิมพ์ ( " [25] ส่งข้อความ" )
            msg = op.message
            text = msg.text
            msg_id = msg.id
            ผู้รับ= msg.to
            ผู้ส่ง= msg._from
            ถ้า msg.toType ==  0 :
                ถ้าผู้ส่ง= nadya.profile.mid:
                    to = sender
                อื่น :
                    ถึง=รับ
            อื่น :
                ถึง=รับ
            ถ้า msg.contentType ==  0 :
                ถ้าข้อความเป็น ไม่มี :
                    กลับ
# =========================================== ============================= #
                ถ้า text.lower () ==  ' h1 ' :
                    helpMessage = helpmessage ()
                    nadya.sendMessage (ถึง, str (helpMessage))
                elif text.lower () ==  ' h2 ' :
                    helpTextToSpeech = helptexttospeech ()
                    nadya.sendMessage (ถึง, str (helpTextToSpeech))
                elif text.lower () ==  ' h3 ' :
                    helpTranslate = helptranslate ()
                    nadya.sendMessage (ถึง, str (helpTranslate))
# =========================================== ============================= #
                elif  "เชิญโทร" ใน msg.text.lower ():
                    ถ้า msg.toType ==  2 :
                       sep = text.split ( "  " )
                       strnum = text.replace (sep [ 0 ] +  "  " , " " )
                       num =  int (strnum)
                       nadya.sendMessage (to, "เชิญโทรเลยครับเจ้านายʕ•ᴥ•ʔ " )
                       สำหรับ var ใน ช่วง ( 0 , num):
                          group = line.getGroup (to)
                          members = [mem.mid สำหรับ mem ในกลุ่มสมาชิก]
                          naday.acquireGroupCallRoute (เพื่อ)
                elif  "ทีมงาน"  == msg.text.lower ():
                    msg.contentType =  13
                    nadya.sendMessage (เพื่อ)
                    nadya.sendContact (เพื่อ)
                elif  "เทส"  == msg.text.lower ():
                    nadya.sendMessage (เป็น" LOADING: ▒ ... 0% " )
                    nadya.sendMessage (to, " ███████████..100.0% " )
                    nadya.sendMessage (to, "บอทม้ได้หลุดครับเจ้านายʕ•ᴥ•ʔ " )
                elif  " name " ใน msg.text.lower ():
                    spl = re.split ( " name " , msg.text, flags =ใหม่IGNORECASE )
                    ถ้า spl [ 0 ] ==  " " :
                       prof = nadya.getProfile ()
                       prof.displayName = spl [ 1 ]
                       nadya.updateProfile (ศ)
                       nadya.sendMessage (to, "เปลี่ยนชื่อแล้วครับเจ้านายʕ•ᴥ•ʔ " )
                elif  "ยกเชิญ"  == msg.text.lower ():
                    ถ้า msg.toType ==  2 :
                        กลุ่ม= nadya.getGroup (msg.to)
                        gMembMids = [contact.mid สำหรับการติดต่อใน group.invitee]
                        สำหรับ _mid ใน gMembMids:
                            nadya.cancelGroupInvitation (msg.to [_ กลาง])
                        nadya.sendMessage (to, "ลบหมดเชิญหมดแล้วครับเจสันไ¸•ᴥ•ʔ " )
                elif  "ลบรัน" ใน msg.text.lower ():
                    spl = re.split ( "ลบรัน" , msg.text, flags =ใหม่IGNORECASE )
                    ถ้า spl [ 0 ] ==  " " :
                        spl [ 1 ] = spl [ 1 ] .strip ()
                        ag = nadya.getGroupIdsInvited ()
                        txt =  "กำลังลบให้ครับเจ้านายʕ•ᴥ •ʔ " + STR ( len (AG)) + "กลุ่ม"
                        ถ้า spl [ 1 ] ! =  " " :
                            txt = txt +  "ด้วยข้อความ\" " + spl [ 1 ] + " \ " "
                        txt = txt +  " \ nกรุณารอสักครู่ .. "
                        nadya.sendMessage (msg.to, TXT)
                        procLock =  len (ag)
                        สำหรับ gr ใน ag:
                          ลอง :
                             nadya.acceptGroupInvitation (กรัม)
                             ถ้า spl [ 1 ] ! =  " " :
                                 nadya.sendMessage (gr, spl [ 1 ])
                             nadya.leaveGroup (กรัม)
                             nadya.sendMessage (msg.to, "ลบแล้วหมดเลย" เจ้านายʕ•ᴥ•ʔ " )
                          ยกเว้น :
                             ผ่านไป
                elif text.lower () ==  'ความเร็ว' :
                    เริ่มต้น= time.time ()
                    nadya.sendMessage (to, "ช้ามากเลยเจ้านาย" )
                    elapsed_time = time.time () -เริ่มต้น
                    nadya.sendMessage (เพื่อ, " \ n \ n {}วินาที\ n \ n ✍️ " .format ( STR (ELAPSED_TIME)))
                elif text.lower () ==  'รีบอท' :
                    nadya.sendMessage (to, "กำลังรีบอทรอสักครู่ ..... " )
                    time.sleep ( 5 )
                    nadya.sendMessage (to, "รีบอทเส็กแล้วกดลิ้งล็อคบอทใหม่ด้วยครับเจซีย์" )
                    restartBot ()
                elif text.lower () ==  'ออน' :
                    timeNow = time.time ()
                    runtime = timeNow - botStart
                    runtime = format_timespan (รันไทม์)
                    nadya.sendMessage (to, " ʕ•ᴥ•ʔระยะเวลาการทำงานของบอทʕ•ᴥ•ʔ \ n {} " .format ( str (รันไทม์)))
                elif text.lower () ==  'ข้อมูล' :
                    ลอง :
                        arr = []
                        owner =  " ude3230559bf63a55b9c28aa20ea194e3 "
                        creator = nadya.getContact (เจ้าของ)
                        contact = nadya.getContact (nadyaMID)
                        grouplist = nadya.getGroupIdsJoined ()
                        contactlist = nadya.getAllContactIds ()
                        blockedlist = nadya.getBlockedContactIds ()
                        ret_ =  " ╔══ [ข้อมูลดีดี] "
                        ret_ + =  " \ nชื่อ: {} "รูปแบบ (contact.displayName)
                        ret_ + =  " \ nกลุ่ม: {} "รูปแบบ ( str ( len (grouplist)))
                        ret_ + =  " \ n ╠เพื่อน: {} "รูปแบบ ( str ( len (contactlist)))
                        ret_ + =  " \ n ╠บล็อค: {} "รูปแบบ ( str ( len (บล็อค)))
                        ret_ + =  " \ n ╚══ [ข้อมูลไอดีคุณ] "
                        nadya.sendMessage (ถึง, str (ret_))
                    ยกเว้น ข้อยกเว้น เช่น e:
                        nadya.sendMessage (msg.to, str (e))
# =========================================== ============================= #
                elif text.lower () ==  'เชคค่า' :
                    ลอง :
                        ret_ =  " ╔════════════ "
                        ถ้าการตั้งค่า [ " autoAdd " ] ==  True : ret_ + =  " \ nระบบ" ออโต้บรอนซ์แอด"
                        อื่น : ret_ + =  " \ n ║ระบบออโต้บล็อคแอด✘ "
                        ถ้าการตั้งค่า [ " autoJoin " ] ==  True : ret_ + =  " \ nระบบเข้ากลุ่มออโต้✔ "
                        อื่น : ret_ + =  " \ nระบบเข้ากลุ่มออโต้✘ "
                        ถ้าการตั้งค่า [ " autoLeave " ] ==  True : ret_ + =  " \ nระบบการออกกลุ่มออโต้✔ "
                        อื่น : ret_ + =  " \ nระบบการออกกลุ่มออโต้✘ "
                        ถ้าการตั้งค่า [ " autoRead " ] ==  จริง : ret_ + =  " \ n ║ระบบอ่านข้อความออโต้โต้✔ "
                        อื่น : ret_ + =  " \ n ║ระบบอ่านข้อความออโต้โต้✘ "
                        ถ้าการตั้งค่า [ " checksticker " ] ==  True : ret_ + =  " \ nเช็คระบบติ๊กกเกอร์✔ "
                        อื่น : ret_ + =  " \ nระบบตรวจเช็คติ๋กเกอร์✘ "
                        ถ้าการตั้งค่า [ " detectMention " ] == ความ จริง : ret_ + =  " \ nระบบข้อความแทค✔ "
                        อื่น : ret_ + =  " \ n ║ระบบข้อความแทค✘ "
                        ถ้าการตั้งค่า [ " detectMention " ] ==  จริง : ret_ + =  " \ n "ระบบแทคส่งรูป✔ "
                        อื่น : ret_ + =  " \ n "ระบบแทคส่งรูป✘ "
                        ret_ + =  " \ n ╚════════════ "
                        nadya.sendMessage (ถึง, str (ret_))
                    ยกเว้น ข้อยกเว้น เช่น e:
                        nadya.sendMessage (msg.to, str (e))
                elif text.lower () ==  'เปิดบล็อคแอด' :
                    ตั้งค่า [ " autoAdd " ] =  True
                    nadya.sendMessage (to, "เปิดระบบบล็อคแล้วแอดเดี๋ยวค่ะเจ้านายʕ•ᴥ•ʔ " )
                elif text.lower () ==  'ปิดบล็อคแอด' :
                    การตั้งค่า [ " autoAdd " ] =  เท็จ
                    nadya.sendMessage (to, "ปิดระบบบล็อคแอดแล้วครับเจสันไ¸•ᴥ•ʔ " )
                elif text.lower () ==  'เปิดเข้ากลุ่ม' :
                    การตั้งค่า [ " autoJoin " ] =  True
                    nadya.sendMessage (to, "เปิดระบบเข้ากลุ่มออโต้แล้วครับเจสันไ¸•ᴥ•ʔ " )
                elif text.lower () ==  'ปิดเข้ากลุ่ม' :
                    การตั้งค่า [ " autoJoin " ] =  เท็จ
                    nadya.sendMessage (to, "ปิดระบบเข้ากลุ่มออโต้แล้วครับเจสันไ¸•ᴥ•ʔ " )
                elif text.lower () ==  'เปิดแสงแชมพู' :
                    ตั้งค่า [ " autoLeave " ] =  True
                    nadya.sendMessage (to, "เปิดระบบแชทรวมแล้วครับเจสันไ¸•ᴥ•ʔ " )
                elif text.lower () ==  'ปิดออกแชท' :
                    การตั้งค่า [ " autoLeave " ] =  เท็จ
                    nadya.sendMessage (to, "ปิดระบบออกแชทรวมแล้วครับเจ้านายʕ•ᴥ•ʔ " )
                elif text.lower () ==  'เปิดอ่านแชท' :
                    การตั้งค่า [ " autoRead " ] =  True
                    nadya.sendMessage (to, "เปิดระบบอ่านแล้วไม่ได้เจ้านายʕ•ᴥ•ʔ " )
                elif text.lower () ==  'ปิดอ่านแชท' :
                    การตั้งค่า [ " autoRead " ] =  เท็จ
                    nadya.sendMessage (ไป"ปิดระบบอ่านแชทแล้วครับเจ้านาย ʕ•ᴥ•ʔ " )
                elif text.lower () ==  'เปิดเชคติ๊กเก้อ' :
                    การตั้งค่า [ " checkSticker " ] =  True
                    nadya.sendMessage (ไป"เปิดระบบเช็คสติ้กเกอร์แล้ว ʕ•ᴥ•ʔ " )
                elif text.lower () ==  'ปิดเชคติกเก้อ' :
                    การตั้งค่า [ " checkSticker " ] =  เท็จ
                    nadya.sendMessage (to, "ปิดระบบเช็คเช็คว่าถูกต้องหรือไม่?" )
                elif text.lower () ==  'เปิดแทคชื่อ' :
                    การตั้งค่า [ " datectMention " ] =  True
                    nadya.sendMessage (to, "เปิดระบบข้อความแล้วค่อยๆเจสันไห่•ᴥ•ʔ " )
                elif text.lower () ==  'ปิดแทคชื่อ' :
                    การตั้งค่า [ " datectMention " ] =  เท็จ
                    nadya.sendMessage (ไป"ปิดระบบข้อความแทคแล้วครับเจ้านาย ʕ•ᴥ•ʔ " )
                elif text.lower () ==  'เปิดแทคภาพ' :
                    การตั้งค่า [ " potoMention " ] =  True
                    nadya.sendMessage (msg.to, "เปิดแท๊กซี่แล้ว"เจสันไ่ห่ʕ•ᴥ•ʔ " )
                elif text.lower () ==  'ปิดแทคภาพ' :
                    การตั้งค่า [ " potoMention " ] =  เท็จ
                    nadya.sendMessage (msg.to, "ปิดแทร็ครูปแล้วครับเจสันไ¸•ᴥ•ʔ " )
                elif text.lower () ==  ' clonecontact ' :
                    ตั้งค่า [ " copy " ] =  True
                    nadya.sendMessage (to, "ก็อปปี้ด้วยคอนแทคʕ•ᴥ•ʔ " )
# =========================================== ============================= #
                elif text.lower () ==  ' ! แทค' :
                    gs = nadya.getGroup (to)
                    เป้าหมาย= []
                    สำหรับ g ใน gs.members:
                        ถ้า g.displayName ใน " " :
                            targets.append (g.mid)
                    ถ้าเป้าหมาย== []:
                        nadya.sendMessage (to, "ไม่มีคนใส่ชื่อริงโทนหนอนไฝ่• " • " )
                    อื่น :
                        mc =  " "
                        สำหรับเป้าหมายในเป้าหมาย:
                            mc + = sendMessageWithMention (ไปยังเป้าหมาย) +  " \ n "
                        nadya.sendMessage (ถึง, mc)
                elif text.lower () ==  ' ! มิด' :
                    gs = nadya.getGroup (to)
                    lists = []
                    สำหรับ g ใน gs.members:
                        ถ้า g.displayName ใน " " :
                            lists.append (g.mid)
                    ถ้ารายการ== []:
                        nadya.sendMessage (to, "ไม่มีคนใส่ชื่อริงโทนหนอนไฝ่• " • " )
                    อื่น :
                        mc =  " "
                        สำหรับ mi_d ในรายการ:
                            mc + =  " -> "  + mi_d +  " \ n "
                        nadya.sendMessage (เพื่อ, MC)
                elif text.lower () ==  ' ! คท' :
                    gs = nadya.getGroup (to)
                    lists = []
                    สำหรับ g ใน gs.members:
                        ถ้า g.displayName ใน " " :
                            lists.append (g.mid)
                    ถ้ารายการ== []:
                        nadya.sendMessage (to, "ไม่มีคนใส่ชื่อริงโทนหนอนไฝ่• " • " )
                    อื่น :
                        สำหรับ ls ในรายการ:
                            contact = nadya.getContact (ls)
                            mi_d = contact.mid
                            nadya.sendContact (to, mi_d)
                elif text.lower () ==  'คท' :
                    sendMessageWithMention (เป็น nadyaMID)
                    nadya.sendContact (to, nadyaMID)
                elif text.lower () ==  'มิด' :
                    nadya.sendMessage (msg.to, nadyaMID)
                elif text.lower () ==  'ชื่อ' :
                    ฉัน= nadya.getContact (nadyaMID)
                    nadya.sendMessage (msg.to, me.displayName)
                elif text.lower () ==  'ตัส' :
                    ฉัน= nadya.getContact (nadyaMID)
                    nadya.sendMessage (msg.to, me.statusMessage)
                elif text.lower () ==  'รูป' :
                    ฉัน= nadya.getContact (nadyaMID)
                    nadya.sendImageWithURL (msg.to, " http://dl.profile.line-cdn.net/ "  + me.pictureStatus)
                elif text.lower () ==  'รูปวีดีโอ' :
                    ฉัน= nadya.getContact (nadyaMID)
                    nadya.sendVideoWithURL (msg.to, " http://dl.profile.line-cdn.net/ "  + me.pictureStatus +  " / vp " )
                elif text.lower () ==  'รูปปก' :
                    ฉัน= nadya.getContact (nadyaMID)
                    cover = nadya.getProfileCoverURL (nadyaMID)    
                    nadya.sendImageWithURL (msg.to, cover)
                elif msg.text.lower (). startswith ( "คท" ):
                    ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys () =!  ไม่มี :
                        ชื่อ= re.findall ( r ' @ ( \ w + ) 'ข้อความ)
                        กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                        mentionees =พูดถึง [ ' MENTIONEES ' ]
                        lists = []
                        สำหรับการกล่าวถึงใน mentionees:
                            ถ้าพูดถึง [ " M " ] ไม่ อยู่ในรายการ:
                                lists.append (พูดถึง [ " M " ])
                        สำหรับ ls ในรายการ:
                            contact = nadya.getContact (ls)
                            mi_d = contact.mid
                            nadya.sendContact (msg.to, mi_d)
                elif msg.text.lower (). startswith ( "มิด" ):
                    ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys () =!  ไม่มี :
                        ชื่อ= re.findall ( r ' @ ( \ w + ) 'ข้อความ)
                        กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                        mentionees =พูดถึง [ ' MENTIONEES ' ]
                        lists = []
                        สำหรับการกล่าวถึงใน mentionees:
                            ถ้าพูดถึง [ " M " ] ไม่ อยู่ในรายการ:
                                lists.append (พูดถึง [ " M " ])
                        ret_ =  " \ n "
                        สำหรับ ls ในรายการ:
                            ret_ + = ls
                        nadya.sendMessage (msg.to, str (ret_))
                elif msg.text.lower (). startswith ( "ชื่อ" ):
                    ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys () =!  ไม่มี :
                        ชื่อ= re.findall ( r ' @ ( \ w + ) 'ข้อความ)
                        กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                        mentionees =พูดถึง [ ' MENTIONEES ' ]
                        lists = []
                        สำหรับการกล่าวถึงใน mentionees:
                            ถ้าพูดถึง [ " M " ] ไม่ อยู่ในรายการ:
                                lists.append (พูดถึง [ " M " ])
                        สำหรับ ls ในรายการ:
                            contact = nadya.getContact (ls)
                            nadya.sendMessage (msg.to, contact.displayName)
                elif msg.text.lower (). startswith ( "ตัส" ):
                    ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys () =!  ไม่มี :
                        ชื่อ= re.findall ( r ' @ ( \ w + ) 'ข้อความ)
                        กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                        mentionees =พูดถึง [ ' MENTIONEES ' ]
                        lists = []
                        สำหรับการกล่าวถึงใน mentionees:
                            ถ้าพูดถึง [ " M " ] ไม่ อยู่ในรายการ:
                                lists.append (พูดถึง [ " M " ])
                        สำหรับ ls ในรายการ:
                            contact = nadya.getContact (ls)
                            nadya.sendMessage (msg.to, contact.statusMessage)
                elif msg.text.lower (). startswith ( "รูป" ):
                    ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys () =!  ไม่มี :
                        ชื่อ= re.findall ( r ' @ ( \ w + ) 'ข้อความ)
                        กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                        mentionees =พูดถึง [ ' MENTIONEES ' ]
                        lists = []
                        สำหรับการกล่าวถึงใน mentionees:
                            ถ้าพูดถึง [ " M " ] ไม่ อยู่ในรายการ:
                                lists.append (พูดถึง [ " M " ])
                        สำหรับ ls ในรายการ:
                            เส้นทาง=  " http://dl.profile.line-cdn.net/ "  + nadya.getContact (ls) .pictureStatus
                            nadya.sendImageWithURL (msg.to, str (เส้นทาง))
                elif msg.txt.lower (). startswith ( "รูปวีดีโอ" ):
                    ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys () =!  ไม่มี :
                        ชื่อ= re.findall ( r ' @ ( \ w + ) 'ข้อความ)
                        กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                        mentionees =พูดถึง [ ' MENTIONEES ' ]
                        lists = []
                        สำหรับการกล่าวถึงใน mentionees:
                            ถ้าพูดถึง [ " M " ] ไม่ อยู่ในรายการ:
                                lists.append (พูดถึง [ " M " ])
                        สำหรับ ls ในรายการ:
                            เส้นทาง=  " http://dl.profile.line-cdn.net/ "  + nadya.getContact (ls) .pictureStatus +  " / vp "
                            nadya.sendImageWithURL (msg.to, str (เส้นทาง))
                elif msg.txt.lower (). startswith ( "รูปปก" ):
                    ถ้าบรรทัด=  ไม่มี :
                        ถ้า 'กล่าวถึง' ใน msg.contentMetadata.keys () =!  ไม่มี :
                            ชื่อ= re.findall ( r ' @ ( \ w + ) 'ข้อความ)
                            กล่าวถึง= ast.literal_eval (msg.contentMetadata [ 'กล่าวถึง' ])
                            mentionees =พูดถึง [ ' MENTIONEES ' ]
                            lists = []
                            สำหรับการกล่าวถึงใน mentionees:
                                ถ้าพูดถึง [ " M " ] ไม่ อยู่ในรายการ:
                                    lists.append (พูดถึง [ " M " ])
                            สำหรับ ls ในรายการ:
                                เส้นทาง=  " http://dl.profile.line-cdn.net/ "  + nadya.getProfileCoverURL (ls)
                                nadya.sendImageWithURL (msg.to, str (เส้นทาง))
                elif msg.text.lower (). startswith ( "ท้าไม้ตาย" ):
                    เป้าหมาย= []
                    ที่สำคัญ=  EVAL (msg.contentMetadata [ "กล่าวถึง" ])
                    คีย์ [ " MENTIONEES " ] [ 0 ] [ " M " ]
                    สำหรับ x ในคีย์ [ " MENTIONEES " ]:
                        targets.append (x [ " M " ])
                    สำหรับเป้าหมายในเป้าหมาย:
                        ลอง :
                            nadya.sendMessage (msg.to, " 2 นาฬิกาแฟร์เรอนแบบอุณหภูมิ 155 เซลเซียสแรงดันสูง 32 องศาเซลเซียส 22 นาฬิกาสำหรับใส่ผลึกเพื่อความหวัง .. " )
                            nadya.kickoutFromGroup (msg.to [เป้าหมาย])
                            nadya.sendMessage (msg.to, " !! แตกก" )
                        ยกเว้น :
                            nadya.sendText (msg.to, " Error " )
                elif msg.txt.lower () startswith ( "เตะ" ):
                    เป้าหมาย= []
                    ที่สำคัญ=  EVAL (msg.contentMetadata [ "กล่าวถึง" ])
                    คีย์ [ " MENTIONEES " ] [ 0 ] [ " M " ]
                    สำหรับ x ในคีย์ [ " MENTIONEES " ]:
                        targets.append (x [ " M " ])
                    สำหรับเป้าหมายในเป้าหมาย:
                        ลอง :
                            nadya.kickoutFromGroup (msg.to [เป้าหมาย])
                        ยกเว้น :
                            nadya.sendText (msg.to, " Error " )
# =========================================== ============================= #
                elif  " Mc " ใน msg.text:
                    mmid = msg.text.replace ( " Mc " , " " )
                    nadya.sendContact (to, mmid)
                elif msg.text.lower (). startswith ( "เพิ่มพิม" ):
                    เป้าหมาย= []
                    ที่สำคัญ=  EVAL (msg.contentMetadata [ "กล่าวถึง" ])
                    คีย์ [ " MENTIONEES " ] [ 0 ] [ " M " ]
                    สำหรับ x ในคีย์ [ " MENTIONEES " ]:
                        targets.append (x [ " M " ])
                    สำหรับเป้าหมายในเป้าหมาย:
                        ลอง :
                            การตั้งค่า [ "เลียนแบบ" ] [ "เป้าหมาย" ] [เป้าหมาย] =  จริง
                            nadya.sendMessage (msg.to, "เพิ่มคนพิมตามแล้วครับเจ้านาย ʕ•ᴥ•ʔ " )
                            หยุด
                        ยกเว้น :
                            nadya.sendMessage (msg.to, "เพิ่มคนพิมตามแล้วครับเจ้านาย ʕ•ᴥ•ʔ " )
                            หยุด
                elif msg.text.lower (). startswith ( "ลบพิมตาม" ):
                    เป้าหมาย= []
                    ที่สำคัญ=  EVAL (msg.contentMetadata [ "กล่าวถึง" ])
                    คีย์ [ " MENTIONEES " ] [ 0 ] [ " M " ]
                    สำหรับ x ในคีย์ [ " MENTIONEES " ]:
                        targets.append (x [ " M " ])
                    สำหรับเป้าหมายในเป้าหมาย:
                        ลอง :
                            ตั้งค่าdel [ "เลียนแบบ" ] [ "เป้าหมาย" ] [เป้าหมาย]
                            nadya.sendMessage (msg.to, "ลบแบบเลียนแบบแล้วครับเจ้านาย" • " ᴥ " )
                            หยุด
                        ยกเว้น :
                            nadya.sendMessage (msg.to, "ลบแบบเลียนแบบแล้วครับเจ้านาย" • " ᴥ " )
                            หยุด
                elif text.lower () ==  'รายชื่อพิมตาม' :
                    ถ้าตั้งค่า [ "เลียนแบบ" ] [ " target " ] == {}:
                        nadya.sendMessage (msg.to, "ไม่มีเป้าหมายʕ•ᴥ•ʔ " )
                    อื่น :
                        mc =  " ╔══ [รายชื่อคนพิมตาม] "
                        สำหรับ mi_d ในการตั้งค่า [ "เลียนแบบ" ] [ " target " ]:
                            mc + =  " \ n ╠ " + nadya.getContact (mi_d) .displayName
                        nadya.sendMessage (msg.to, mc +  " \ n ╚══ [ทั้งหมด] " )
                    
                elif  "พิมตาม" ใน msg.txt.lower ():
                    sep = text.split ( "  " )
                    mic = text.replace (sep [ 0 ] +  "  " , " " )
                    ถ้า mic ==  " on " :
                        ถ้าตั้งค่า [ "เลียนแบบ" ] [ "สถานะ" ] ==  เท็จ :
                            ตั้งค่า [ "เลียนแบบ" ] [ "สถานะ" ] =  จริง
                            nadya.sendMessage (msg.to, "เปิดระบบพิมพ์แล้วครับเจ้านาย" • " ᴥ•ʔ " )
                    elif mic ==  "ปิด" :
                        ถ้าตั้งค่า [ "เลียนแบบ" ] [ "สถานะ" ] ==  จริง :
                            ตั้งค่า [ "เลียนแบบ" ] [ "สถานะ" ] =  เท็จ
                            nadya.sendMessage (msg.to, "ปิดระบบพิมพ์แล้วครับเจสันไ¸•ᴥ•ʔ " )
                elif  "เด้ง: " ในข้อความ:
                    midd = msg.text.replace ( "เด้ง: " , " " )
                    Nadya kickoutFromGroup (msg.to [midd])
                    Nadya findAndAddContactsByMid (midd)
                    nadya.inviteIntoGroup (msg.to [midd])
                    nadya.cancelGroupInvitation (msg.to [midd])
                elif  "เด้ง" ใน msg.text:
                        vkick0 = msg.text.replace ( "เด้ง" , " " )
                        vkick1 = vkick0.rstrip ()
                        vkick2 = vkick1.replace ( " @ " , " " )
                        vkick3 = vkick2.rstrip ()
                        _name = vkick3
                        gs = nadya.getGroup (msg.to)
                        เป้าหมาย= []
                        สำหรับ s ใน gs.members:
                            ถ้า _name ใน s.displayName:
                                targets.append (s.mid)
                        ถ้าเป้าหมาย== []:
                            ผ่านไป
                        อื่น :
                            สำหรับเป้าหมายในเป้าหมาย:
                                ลอง :
                                    nadya.kickoutFromGroup (msg.to [เป้าหมาย])
                                    nadya.findAndAddContactsByMid (เป้าหมาย)
                                    Nadya inviteIntoGroup (msg.to [เป้าหมาย])
                                ยกเว้น :
                                    ผ่านไป
# =========================================== ============================= #
                elif text.lower () ==  'เชคแอด' :
                    group = nadya.getGroup (to)
                    GS  = group.creator.mid
                    nadya.sendContact (to, GS )
                elif text.lower () ==  'ไอดีกลุ่ม' :
                    gid = nadya.getGroup (to)
                    nadya.sendMessage (to, " \ n "  + gid.id)
                elif text.lower () ==  'รูปกลุ่ม' :
                    group = nadya.getGroup (to)
                    path =  " http://dl.profile.line-cdn.net/ "  + group.pictureStatus
                    nadya.sendImageWithURL (ไป, เส้นทาง)
                elif text.lower () ==  'ชื่อกลุ่ม' :
                    gid = nadya.getGroup (to)
                    nadya.sendMessage (to, " \ n "  + gid.name)
                elif text.lower () ==  'ลิ้งกลุ่ม' :
                    ถ้า msg.toType ==  2 :
                        group = nadya.getGroup (to)
                        ถ้า group.preventedJoinByTicket ==  เท็จ :
                            ticket = nadya.reissueGroupTicket (to)
                            nadya.sendMessage (to " https://line.me/R/ti/g/ {} "รูปแบบ ( str (ticket)))
                        อื่น :
                            nadya.sendMessage (ไป"กรุณาเปิดลิ้งกลุ่มก่อน\ nลงคำสั่งนี้ด้วยครับเจ้านายʕ •ᴥ•ʔ " .format ( STR (การตั้งค่า [ " keyCommand " ])))
                elif text.lower () ==  ' # เปิดลิ้ง' :
                    ถ้า msg.toType ==  2 :
                        group = nadya.getGroup (to)
                        ถ้า group.preventedJoinByTicket ==  เท็จ :
                            nadya.sendMessage (to, "เปิดแล้วครับเจ้านายʕ•ᴥ•ʔ " )
                        อื่น :
                            group.preventedJoinByTicket =  เท็จ
                            nadya.updateGroup (กลุ่ม)
                            nadya.sendMessage (to, "เปิดแล้วครับเจ้านายʕ•ᴥ•ʔ " )
                elif text.lower () ==  ' # ปิดลิ้ง' :
                    ถ้า msg.toType ==  2 :
                        group = nadya.getGroup (to)
                        ถ้า group.preventedJoinByTicket ==  จริง :
                            nadya.sendMessage (to, "ปิดแล้วครับเจ้านายʕ•ᴥ•ʔ " )
                        อื่น :
                            group.preventedJoinByTicket =  จริง
                            nadya.updateGroup (กลุ่ม)
                            nadya.sendMessage (to, "ปิดแล้วครับเจ้านายʕ•ᴥ•ʔ " )
                elif text.lower () ==  'ข้อมูลกลุ่ม' :
                    group = nadya.getGroup (to)
                    ลอง :
                        gCreator = group.creator.displayName
                    ยกเว้น :
                        gCreator =  "ไม่พบผู้สร้าง"
                    ถ้า group.invitee ไม่มีคือ  :
                        gPending =  " 0 "
                    อื่น :
                        gPending =  str ( len (group.invitee))
                    ถ้า group.preventedJoinByTicket ==  จริง :
                        gQr =  "ปิด"
                        gTicket =  "ลิ้งถูกปิดอยู่ .. "
                    อื่น :
                        gQr =  "เปิด"
                        gTicket =  " https://line.me/R/ti/g/ {} "รูปแบบ ( str (nadya.reissueGroupTicket (group.id)))
                    path =  " http://dl.profile.line-cdn.net/ "  + group.pictureStatus
                    ret_ =  " ╔══ [ข้อมูลกลุ่ม] "
                    ret_ + =  " \ n ╠ชื่อกลุ่ม: {} " .format ( str (group.name))
                    ret_ + =  " \ n ╠ไอดีกลุ่ม: {} " .format (group.id)
                    ret_ + =  " \ nผู้สร้างกลุ่ม: {} " .format ( str (gCreator))
                    ret_ + =  " \ nสมาชิกกลุ่ม: {} "รูปแบบ ( str ( len (group.members)))
                    ret_ + =  " \ n ╠ค้างไว้: {} "รูปแบบ (gPending)
                    ret_ + =  " \ nกลุ่ม╠: {} "รูปแบบ (gQr)
                    ret_ + =  " \ n ╠ลิ้งกลุ่ม: {} "รูปแบบ (gTicket)
                    ret_ + =  " \ n ╚══ [M ai] "
                    nadya.sendMessage (ถึง, str (ret_))
                    nadya.sendImageWithURL (ไป, เส้นทาง)
                elif text.lower () ==  'รายชื่อคนในห้อง' :
                    ถ้า msg.toType ==  2 :
                        group = nadya.getGroup (to)
                        ret_ =  " ╔══ [รายชื่อกลุ่มสมชิก] "
                        no =  0  +  1
                        สำหรับ mem ในกลุ่มสมาชิก:
                            ret_ + =  " \ n ╠ {} . {} " .format ( str (no), str (mem.displayName))
                            no + =  1
                        ret_ + =  " \ n ╚══ [จำนวนสมาชิก{}คนครับ้จ้านายʕ• ᴥ•ʔ ] " .format ( STR ( len (group.members)))
                        nadya.sendMessage (ถึง, str (ret_))
                elif text.lower () ==  'รายชื่อกลุ่ม' :
                        groups = nadya.groups
                        ret_ =  " ╔══ [รายชื่อกลุ่ม] "
                        no =  0  +  1
                        สำหรับ gid ในกลุ่ม:
                            กลุ่ม= nadya.getGroup (gid)
                            ret_ + =  " \ n ╠ {} . {} | {} " .format ( STR (ไม่) STR (group.name) STR ( len (group.members)))
                            no + =  1
                        ret_ + =  " \ n [กลุ่มจำนวน{ @ }กลุ่มเจ้านายʕ•ᴥ•ʔ] " .format ( str ( len (groups)))
                        nadya.sendMessage (ถึง, str (ret_))
# =========================================== ============================= #          
                elif text.lower () ==  'แทค' :
                    กลุ่ม= nadya.getGroup (msg.to)
                    nama = [contact.mid สำหรับการติดต่อในกลุ่มสมาชิก]
                    k =  len (nama) / 100
                    สำหรับใน ช่วง (k + 1 ):
                        txt =  u ' '
                        s = 0
                        b = []
                        สำหรับฉันใน group.members [เป็น* 100 (a + 1 ) * 100 ]:
                            b.append ({ " S " : str (s), " E " : str (s + 6 ), " M " : i.mid})
                            s + =  7
                            txt + =  u ' @Alin \ n '
                        nadya.sendMessage (ถึงข้อความ= txt, contentMetadata = { U 'กล่าวถึง' : json.dumps ({ ' MENTIONEES ' : ข})} contentType = 0 )
                        nadya.sendMessage (to, "จำนวนสมาชิก{}คนครับเจ้านายʕ•ᴥ•ʔ " .format ( str ( len (nama))))          
                elif text.lower () ==  'เปิดอ่าน' :
                    tz = pytz.timezone ( "เอเชีย / จาการ์ตา" )
                    timeNow = datetime.now ( tz = tz)
                    วัน= [ " Sunday " , " Monday " , " Tuesday " , " Wednesday " , " Thursday " , " Friday " , " Saturday " ]
                    hari = [ " Minggu " , " Senin " , " Selasa " , " Rabu " , " Kamis " , " Jumat " , " Sabtu " ]
                    bulan = [ " Januari " , " Februari " , " Maret " , " April " , " Mei " , " Juni " , " Juli " , " Agustus " , " September " , " Oktober " , " November " , " Desember "]
                    hr = timeNow.strftime ( " % A " )
                    bln = timeNow.strftime ( " % m " )
                    สำหรับ i ใน ช่วง ( len (day)):
                        if hr == day [i]: hasil = hari [i]
                    สำหรับ k ใน ช่วง ( 0 , len (bulan)):
                        ถ้า bln ==  str (k): bln = bulan [k - 1 ]
                    readTime = Hasil +  " "  + timeNow.strftime ( ' % d ' ) +  " - "  +พันล้าน+  " - "  + timeNow.strftime ( ' % Y ' ) +  " \ n Jam: [ "  + timeNow.strftime ( ' % H:% M:% S ' ) +  " ] "
                    ถ้า msg.to ในการอ่าน [ ' readPoint ' ]:
                            ลอง :
                                delอ่าน [ ' readPoint ' ] [msg.to]
                                delอ่าน [ ' readMember ' ] [msg.to]
                                delอ่าน [ ' readTime ' ] [msg.to]
                            ยกเว้น :
                                ผ่านไป
                            อ่าน [ ' readPoint ' ] [msg.to] = msg.id
                            อ่าน [ ' readMember ' ] [msg.to] =  " "
                            อ่าน [ ' readTime ' ] [msg.to] = datetime.now (). strftime ( ' % H:% M:% S ' )
                            อ่าน [ ' ROM ' ] [msg.to] = {}
                            กับ open ( ' read.json ' , ' w ' ) เป็น fp:
                                json.dump (อ่าน, fp, sort_keys = True , indent = 4 )
                                nadya.sendMessage (msg.to, "หาคนซุ่มซ่ามʕ•ᴥ•ʔ " )
                    อื่น :
                        ลอง :
                            delอ่าน [ ' readPoint ' ] [msg.to]
                            delอ่าน [ ' readMember ' ] [msg.to]
                            delอ่าน [ ' readTime ' ] [msg.to]
                        ยกเว้น :
                            ผ่านไป
                        อ่าน [ ' readPoint ' ] [msg.to] = msg.id
                        อ่าน [ ' readMember ' ] [msg.to] =  " "
                        อ่าน [ ' readTime ' ] [msg.to] = datetime.now (). strftime ( ' % H:% M:% S ' )
                        อ่าน [ ' ROM ' ] [msg.to] = {}
                        กับ open ( ' read.json ' , ' w ' ) เป็น fp:
                            json.dump (อ่าน, fp, sort_keys = True , indent = 4 )
                            nadya.sendMessage (msg.to, "กำหนดจุดอ่าน: \ n "  + readTime)
                            
                elif text.lower () ==  'ปิดอ่าน' :
                    tz = pytz.timezone ( "เอเชีย / จาการ์ตา" )
                    timeNow = datetime.now ( tz = tz)
                    วัน= [ " Sunday " , " Monday " , " Tuesday " , " Wednesday " , " Thursday " , " Friday " , " Saturday " ]
                    hari = [ " Minggu " , " Senin " , " Selasa " , " Rabu " , " Kamis " , " Jumat " , " Sabtu " ]
                    bulan = [ " Januari " , " Februari " , " Maret " , " April " , " Mei " , " Juni " , " Juli " , " Agustus " , " September " , " Oktober " , " November " , " Desember "]
                    hr = timeNow.strftime ( " % A " )
                    bln = timeNow.strftime ( " % m " )
                    สำหรับ i ใน ช่วง ( len (day)):
                        if hr == day [i]: hasil = hari [i]
                    สำหรับ k ใน ช่วง ( 0 , len (bulan)):
                        ถ้า bln ==  str (k): bln = bulan [k - 1 ]
                    readTime = Hasil +  " "  + timeNow.strftime ( ' % d ' ) +  " - "  +พันล้าน+  " - "  + timeNow.strftime ( ' % Y ' ) +  " \ n Jam: [ "  + timeNow.strftime ( ' % H:% M:% S ' ) +  " ] "
                    ถ้า msg.to ไม่ อยู่ใน read [ ' readPoint ' ]:
                        nadya.sendMessage (msg.to, "หาคนซุ่มซ่ามʕ•ᴥ•ʔ " )
                    อื่น :
                        ลอง :
                            delอ่าน [ ' readPoint ' ] [msg.to]
                            delอ่าน [ ' readMember ' ] [msg.to]
                            delอ่าน [ ' readTime ' ] [msg.to]
                        ยกเว้น :
                              ผ่านไป
                        nadya.sendMessage (msg.to, "ลบจุดอ่าน: \ n "  + readTime)
    
                elif text.lower () ==  'ลบเวลาอ่าน' :
                    tz = pytz.timezone ( "เอเชีย / จาการ์ตา" )
                    timeNow = datetime.now ( tz = tz)
                    วัน= [ " Sunday " , " Monday " , " Tuesday " , " Wednesday " , " Thursday " , " Friday " , " Saturday " ]
                    hari = [ " Minggu " , " Senin " , " Selasa " , " Rabu " , " Kamis " , " Jumat " , " Sabtu " ]
                    bulan = [ " Januari " , " Februari " , " Maret " , " April " , " Mei " , " Juni " , " Juli " , " Agustus " , " September " , " Oktober " , " November " , " Desember "]
                    hr = timeNow.strftime ( " % A " )
                    bln = timeNow.strftime ( " % m " )
                    สำหรับ i ใน ช่วง ( len (day)):
                        if hr == day [i]: hasil = hari [i]
                    สำหรับ k ใน ช่วง ( 0 , len (bulan)):
                        ถ้า bln ==  str (k): bln = bulan [k - 1 ]
                    readTime = Hasil +  " "  + timeNow.strftime ( ' % d ' ) +  " - "  +พันล้าน+  " - "  + timeNow.strftime ( ' % Y ' ) +  " \ n Jam: [ "  + timeNow.strftime ( ' % H:% M:% S ' ) +  " ] "
                    ถ้า msg.to ในการอ่าน [ " readPoint " ]:
                        ลอง :
                            delอ่าน [ " readPoint " ] [msg.to]
                            delอ่าน [ " readMember " ] [msg.to]
                            delอ่าน [ " readTime " ] [msg.to]
                        ยกเว้น :
                            ผ่านไป
                        nadya.sendMessage (msg.to, "รีเซ็ตจุดอ่าน: \ n "  + readTime)
                    อื่น :
                        nadya.sendMessage (msg.to, "ไม่ได้เปิดการหาʕ•ᴥ•ʔ " )
                        
                elif text.lower () ==  'คนอ่าน' :
                    tz = pytz.timezone ( "เอเชีย / จาการ์ตา" )
                    timeNow = datetime.now ( tz = tz)
                    วัน= [ " Sunday " , " Monday " , " Tuesday " , " Wednesday " , " Thursday " , " Friday " , " Saturday " ]
                    hari = [ " Minggu " , " Senin " , " Selasa " , " Rabu " , " Kamis " , " Jumat " , " Sabtu " ]
                    bulan = [ " Januari " , " Februari " , " Maret " , " April " , " Mei " , " Juni " , " Juli " , " Agustus " , " September " , " Oktober " , " November " , " Desember "]
                    hr = timeNow.strftime ( " % A " )
                    bln = timeNow.strftime ( " % m " )
                    สำหรับ i ใน ช่วง ( len (day)):
                        if hr == day [i]: hasil = hari [i]
                    สำหรับ k ใน ช่วง ( 0 , len (bulan)):
                        ถ้า bln ==  str (k): bln = bulan [k - 1 ]
                    readTime = Hasil +  " "  + timeNow.strftime ( ' % d ' ) +  " - "  +พันล้าน+  " - "  + timeNow.strftime ( ' % Y ' ) +  " \ n Jam: [ "  + timeNow.strftime ( ' % H:% M:% S ' ) +  " ] "
                    ถ้ารับในการอ่าน [ ' readPoint ' ]:
                        ถ้าอ่าน [ " ROM " ] [ตัวรับ] .items () == []:
                            nadya.sendMessage (receiver, " [Reader]: \ nไม่มี" )
                        อื่น :
                            chiya = []
                            สำหรับ rom in read [ " ROM " ] [receiver] .items ():
                                chiya.append (rom [ 1 ])
                            cmem = nadya.getContacts (chiya)
                            zx =  " "
                            zxc =  " "
                            zx2 = []
                            xpesan =  ' [Reader]: \ n '
                        สำหรับ x ใน ช่วง ( len (cmem)):
                            xname =  str (cmem [x] .displayName)
                            pesan =  ' '
                            pesan2 = pesan + " @c \ n "
                            xlen =  str ( len (zxc) + len (xpesan))
                            xlen2 =  str ( len (zxc) + len (pesan2) + len (xpesan) - 1 )
                            zx = { ' S ' : xlen, ' E ' : xlen2, ' M ' : cmem [x] .mid}
                            zx2.append (ZX)
                            zxc + = pesan2
                        text = xpesan + zxc +  " \ n [เวลาที่ซุ่มซ่อน]: \ n "  + readTime
                        ลอง :
                            nadya.sendMessage (เครื่องรับ, ข้อความ, contentMetadata = { 'กล่าวถึง' : STR ( ' { "MENTIONEES": ' + json.dumps (ZX2) .replace ( '  ' , ' ' ) + ' } ' )} contentType = 0 )
                        ยกเว้น ข้อยกเว้น เป็นข้อผิดพลาด:
                            พิมพ์ (ข้อผิดพลาด)
                        ผ่านไป
                    อื่น :
                        nadya.sendMessage (ผู้รับ"ไม่ได้รับการซุ่มซ่อนอยู่" )
# =========================================== ============================= #
                elif msg.text.lower (). startswith ( "พูด" ):
                    sep = text.split ( "  " )
                    พูด= text.replace (กันยายน [ 0 ] +  "  " , " " )
                    lang =  ' th '
                    tts = gTTS ( text =พูดlang = lang)
                    tts.save ( " hasil.mp3 " )
                    nadya.sendAudio (msg.to, " hasil.mp3 " )
# =========================================== ============================= #   
                elif text.lower () ==  'ปอยิทิน' :
                    tz = pytz.timezone ( " Asia / Makassar " )
                    timeNow = datetime.now ( tz = tz)
                    วัน= [ "วันจัน" , "วันอังคาร" , "วันพุธ" , "วันพฤหั" , "วันศุก" , "วันเสา" , "วันอาทิต" ]
                    hari = [ " Minggu " , " Senin " , " Selasa " , " Rabu " , " Kamis " , " Jumat " , " Sabtu " ]
                    Bulan = [ "มกราคม" , "กุมภาพัน" , "มีนาคม" , "เมษายน" , "พฤษาภาคม" , "มิถุนายน" , "กรกฎาคม" , "สิงหาคม" , "กันยายน" , "ตุลาคม" , "พฤศจิกายน" , "ธันวาคม" ]
                    hr = timeNow.strftime ( " % A " )
                    bln = timeNow.strftime ( " % m " )
                    สำหรับ i ใน ช่วง ( len (day)):
                        if hr == day [i]: hasil = hari [i]
                    สำหรับ k ใน ช่วง ( 0 , len (bulan)):
                        ถ้า bln ==  str (k): bln = bulan [k - 1 ]
                    readTime = Hasil +  " "  + timeNow.strftime ( ' % d ' ) +  " - "  +พันล้าน+  " - "  + timeNow.strftime ( ' % Y ' ) +  " \ n Jam: [ "  + timeNow.strftime ( ' % H:% M:% S ' ) +  " ] "
                    nadya.sendMessage (msg.to, readTime
                 elif  " screenshotwebsite " ใน msg.text.lower ():
                    sep = text.split ( "  " )
                    query = text.replace (sep [ 0 ] +  "  " , " " )
                    กับ requests.session () เป็นเว็บ:
                        r = web.get ( " http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link= {} "รูปแบบ (urllib.parse.quote (แบบสอบถาม))))
                        ข้อมูล= r.text
                        data = json.loads (data)
                        nadya.sendImageWithURL (ถึง, data [ " result " ]))
                elif  " checkdate " ใน msg.text.lower ():
                    sep = msg.text.split ( "  " )
                    ตามวัน= msg.text.replace (กันยายน [ 0 ] +  "  " , " " )
                    r = requests.get ( ' https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal= ' + tanggal)
                    ข้อมูล= r.text
                    data = json.loads (data)
                    ret_ =  " ╔══ [DATE] "
                    ret_ + =  " \ n ╠วันเดือนปีเกิด: {} "รูปแบบ ( str (data [ " data " ] [ " lahir " ]))
                    ret_ + =  " \ n ╠อายุ: {} "รูปแบบ ( str (ข้อมูล [ "ข้อมูล" ] [ " usia " ]))
                    ret_ + =  " \ n ╠วันเกิด: {} "รูปแบบ ( str (ข้อมูล [ "ข้อมูล" ] [ " ultah " ]))
                    ret_ + =  " \ n ╠ Zodiak: {} " .format ( str (data [ " data " ] [ " zodiak " ]))
                    ret_ + =  " \ n ╚══ [ความสำเร็จ] "
                    nadya.sendMessage (ถึง, str (ret_))
                elif  " instagraminfo " ใน msg.text.lower ():
                    sep = text.split ( "  " )
                    search = text.replace (sep [ 0 ] +  "  " , " " )
                    กับ requests.session () เป็นเว็บ:
                        web.headers [ " User-Agent " ] = random.choice (การตั้งค่า [ " userAgent " ])
                        r = web.get ( " https://www.instagram.com/ {} /? __ a = 1 "รูปแบบ (ค้นหา))
                        ลอง :
                            data = json.loads (r.text)
                            ret_ =  " ╔══ [Instagram โปรไฟล์] "
                            ret_ + =  " \ n ╠ Nama: {} "รูปแบบ ( str (ข้อมูล [ " user " ] [ " full_name " ]))
                            ret_ + =  " \ n ╠ชื่อผู้ใช้: {} "รูปแบบ ( str (ข้อมูล [ " user " ] [ " username " ]))
                            ret_ + =  " \ nชีววิทยา: {} "รูปแบบ ( str (ข้อมูล [ " user " ] [ "ประวัติ" ])))
                            ret_ + =  " \ n ╠ Pengikut: {} " .format (format_number (ข้อมูล [ "ผู้ใช้" ] [ " followed_by " ] [ "นับ" ]))
                            ret_ + =  " \ n ╠ Diikuti: {} " .format (format_number (ข้อมูล [ "ผู้ใช้" ] [ "ดังนี้" ] [ "นับ" ]))
                            ถ้าข้อมูล [ "ผู้ใช้" ] [ " is_verified " ] ==  จริง :
                                ret_ + =  " \ n ╠ Verified: Sudah "
                            อื่น :
                                ret_ + =  " \ n ╠ Verifikasi: Belum "
                            ถ้าข้อมูล [ " user " ] [ " is_private " ] ==  True :
                                ret_ + =  " \ n ╠ Akun Pribadi: Iya "
                            อื่น :
                                ret_ + =  " \ n ╠ Akun Pribadi: Tidak "
                            ret_ + =  " \ nรวมทั้งหมด: {} " .format (format_number (data [ " user " ] [ " media " ] [ " count " ]))
                            ret_ + =  " \ n ╚══ [https://www.instagram.com/ {} ] " .format (ค้นหา)
                            path =ข้อมูล [ " user " ] [ " profile_pic_url_hd " ]
                            nadya.sendImageWithURL (ถึง, str (เส้นทาง))
                            nadya.sendMessage (ถึง, str (ret_))
                        ยกเว้น :
                            nadya.sendMessage (ถึง" Pengguna tidak ditemukan " )
                elif  " instagrampost " ใน msg.text.lower ():
                    แยก= msg.text.split ( "  " )
                    user = msg.text.replace (แยก [ 0 ] +  "  " , " " )
                    โปรไฟล์=  " https://www.instagram.com/ "  +ผู้ใช้
                    กับ requests.session () เป็น x:
                        x.headers [ ' user-agent ' ] =  ' Mozilla / 5.0 '
                        end_cursor =  ' '
                        สำหรับการนับใน ช่วง ( 1 , 999 ):
                            พิมพ์ ( ' PAGE: ' , นับ)
                            r = x.get (โปรไฟล์, params = { ' max_id ' : end_cursor})
                        
                            ข้อมูล= re.search ( R 'หน้าต่าง. _sharedData = ( \ { . + } ) ; </ script> ' , r.text) .group ( 1 )
                            j     = json.loads (ข้อมูล)
                        
                            สำหรับโหนดในเจ [ ' entry_data ' ] [ ' ProfilePage ' ] [ 0 ] [ 'ใช้' ] [ 'สื่อ' ] [ 'โหน' ]:
                                if node [ ' is_video ' ]:
                                    page =  ' https://www.instagram.com/p/ '  + node [ ' code ' ]
                                    r = x.get (หน้า)
                                    URL = re.search ( R ' "video_url": " ( [ ^ " ] + ) " ' , r.text) .group ( 1 )
                                    พิมพ์ (URL)
                                    nadya.sendVideoWithURL (msg.to, URL)
                                อื่น :
                                    พิมพ์ (โหนด [ ' display_src ' ])
                                    nadya.sendImageWithURL (msg.to, node [ ' display_src ' ])
                            end_cursor = re.search ( r ' "end_cursor": " ( [ ^ " ] + ) " ' , r.text) กลุ่ม ( 1 )
                elif  " searchimage " ใน msg.text.lower ():
                    แยก= msg.text.split ( "  " )
                    search = msg.text.replace (แยก [ 0 ] +  "  " , " " )
                    กับ requests.session () เป็นเว็บ:
                        web.headers [ " User-Agent " ] = random.choice (การตั้งค่า [ " userAgent " ])
                        r = web.get ( " http://rahandiapi.herokuapp.com/imageapi?key=betakey&q= {} "รูปแบบ (urllib.parse.quote (ค้นหา))))
                        ข้อมูล= r.text
                        data = json.loads (data)
                        ถ้าข้อมูล [ " result " ] ! = []:
                            รายการ=ข้อมูล [ "ผล" ]
                            เส้นทาง= random.choice (รายการ)
                            a = item.index (เส้นทาง)
                            b =  len (รายการ)
                            nadya.sendImageWithURL (ถึง, str (เส้นทาง))
                elif  " searchyoutube " ใน msg.text.lower ():
                    sep = text.split ( "  " )
                    search = text.replace (sep [ 0 ] +  "  " , " " )
                    params = { " search_query " : search}
                    กับ requests.session () เป็นเว็บ:
                        web.headers [ " User-Agent " ] = random.choice (การตั้งค่า [ " userAgent " ])
                        r = web.get ( " https://www.youtube.com/rasults " , params  = params)
                        ซุป= BeautifulSoup (r.content, " html5lib " )
                        ret_ =  " ╔══ [YouTube ผลลัพธ์] "
                        datas = []
                        สำหรับข้อมูลใน soup.select ( " .yt-lockup-title> a [title] " ):
                            ถ้า " & รายการ" ไม่ อยู่ในข้อมูล [ " href " ]:
                                datas.append (ข้อมูล)
                        สำหรับข้อมูลในข้อมูล:
                            ret_ + =  " \ n ╠══ [ {} ] " .format ( str (ข้อมูล [ " title " ])))
                            ret_ + =  " \ n ╠ https://www.youtube.com {} " .format ( str (data [ " href " ]))
                        ret_ + =  " \ n ╚══ [Total {} ] " .format ( len (datas))
                        nadya.sendMessage (ถึง, str (ret_))
                elif  " searchmusic " ใน msg.text.lower ():
                    sep = text.split ( "  " )
                    search = text.replace (sep [ 0 ] +  "  " , " " )
                    params = { ' songname ' : search}
                    กับ requests.session () เป็นเว็บ:
                        web.headers [ " User-Agent " ] = random.choice (การตั้งค่า [ " userAgent " ])
                        r = web.get ( " https://ide.fdlrcn.com/workspace/yumi-apis/joox? "  + urllib.parse.urlencode (params))
                        ลอง :
                            data = json.loads (r.text)
                            สำหรับเพลงในข้อมูล:
                                ret_ =  " ╔══ [ดนตรี] "
                                ret_ + =  " \ n ╠ Nama lagu: {} "รูปแบบ ( str (เพลง [ 0 ]))
                                ret_ + =  " \ n ╠ Durasi: {} "รูปแบบ ( str (เพลง [ 1 ]))
                                ret_ + =  " \ nลิงค์: {} "รูปแบบ ( str (เพลง [ 4 ]))
                                ret_ + =  " \ n ╚══ [อ่านเสียง] "
                                nadya.sendMessage (ถึง, str (ret_))
                                nadya.sendAudioWithURL (ถึงเพลง [ 3 ])
                        ยกเว้น :
                            nadya.sendMessage (to, " Musik tidak ditemukan " )
                elif  " searchlyric " ใน msg.text.lower ():
                    sep = text.split ( "  " )
                    search = text.replace (sep [ 0 ] +  "  " , " " )
                    params = { ' songname ' : search}
                    กับ requests.session () เป็นเว็บ:
                        web.headers [ " User-Agent " ] = random.choice (การตั้งค่า [ " userAgent " ])
                        r = web.get ( " https://ide.fdlrcn.com/workspace/yumi-apis/joox? "  + urllib.parse.urlencode (params))
                        ลอง :
                            data = json.loads (r.text)
                            สำหรับเพลงในข้อมูล:
                                เพลง=เพลง [ 5 ]
                                lyric = songs.replace ( ' ti: ' , ' Title - ' )
                                lyric = lyric.replace ( ' ar: ' , ' Artist - ' )
                                lyric = lyric.replace ( ' al: ' , 'อัลบั้ม - ' )
                                removeString =  " [1234567890 .:] "
                                สำหรับ char ใน removeString:
                                    lyric = lyric.replace (char, ' ' )
                                ret_ =  " ╔══ [บทกวี] "
                                ret_ + =  " \ n ╠ Nama lagu: {} "รูปแบบ ( str (เพลง [ 0 ]))
                                ret_ + =  " \ n ╠ Durasi: {} "รูปแบบ ( str (เพลง [ 1 ]))
                                ret_ + =  " \ nลิงค์: {} "รูปแบบ ( str (เพลง [ 4 ]))
                                ret_ + =  " \ n ╚══ [เสร็จสิ้น] \ n {} " .format ( STR (บทกวี))
                                nadya.sendMessage (ถึง, str (ret_))
                        ยกเว้น :
                            nadya.sendMessage (ถึง" Lirik tidak ditemukan " )
            elif msg.contentType ==  7 :
                ถ้าการตั้งค่า [ "สติกเกอร์" ] ==  True :
                    stk_id = msg.contentMetadata [ ' STKID ' ]
                    stk_ver = msg.contentMetadata [ ' STKVER ' ]
                    pkg_id = msg.contentMetadata [ ' STKPKGID ' ]
                    ret_ =  " ╔══ (ข้อมูลสติกเกอร์) "
                    ret_ + =  " \ n ╠สติกเกอร์ id: {} "รูปแบบ (stk_id)
                    ret_ + =  " \ nเกร็ดความรู้: {} " .format (pkg_id)
                    ret_ + =  " \ n ╠เวอร์ชั่นสติก: {} "รูปแบบ (stk_ver)
                    ret_ + =  " \ n ╠ลิ้งสติกเกอร์: บรรทัด: // ร้าน / รายละเอียด / {} " .format (pkg_id)
                    ret_ + =  " \ n ╚══ (ข้อมูลสติกเกอร์) "
                    nadya.sendMessage (ถึง, str (ret_))
                    
            elif msg.contentType ==  13 :
                ถ้าการตั้งค่า [ " copy " ] ==  True :
                    _name = msg.contentMetadata [ " displayName " ]
                    copy = msg.contentMetadata [ " mid " ]
                    groups = nadya.getGroup (msg.to)
                    เป้าหมาย= []
                    สำหรับ s ในกลุ่มสมาชิก:
                        ถ้า _name ใน s.displayName:
                            พิมพ์ ( " [Target] Copy " )
                            หยุด                             
                        อื่น :
                            targets.append (สำเนา)
                    ถ้าเป้าหมาย== []:
                        nadya.sendText (msg.to, "ไม่พบ ... " )
                        ผ่านไป
                    อื่น :
                        สำหรับเป้าหมายในเป้าหมาย:
                            ลอง :
                                nadya.cloneContactProfile (เป้าหมาย)
                                nadya.sendMessage (msg.to, "สมาชิก Berhasil โคลนทังสเตนเบรียนซาปาร์" )
                                settings [ ' copy ' ] =  เท็จ
                                หยุด
                            ยกเว้น :
                                     msg.contentMetadata = { ' mid ' : target}
                                     การตั้งค่า [ " copy " ] =  เท็จ
                                     หยุด                     
                    
                    
# =========================================== ============================= #
        if op.type ==  26 :
            พิมพ์ ( " [26] ข้อความที่ได้รับ" )
            msg = op.message
            text = msg.text
            msg_id = msg.id
            ผู้รับ= msg.to
            ผู้ส่ง= msg._from
            ถ้า msg.toType ==  0 :
                ถ้าผู้ส่ง= nadya.profile.mid:
                    to = sender
                อื่น :
                    ถึง=รับ
            อื่น :
                ถึง=รับ
                ถ้าการตั้งค่า [ " autoRead " ] ==  True :
                    nadya.sendChatChecked (to, msg_id)
                ถ้าไปในการอ่าน [ " readPoint " ]:
                    ถ้าผู้ส่งไม่ได้ ในการอ่าน [ "รอม" ] [จะ]:
                        อ่าน [ " ROM " ] [to] [ผู้ส่ง] =  จริง
                ถ้าผู้ส่งในการตั้งค่า [ "เลียนแบบ" ] [ "กำหนดเป้าหมาย" ] และการตั้งค่า [ "เลียนแบบ" ] [ "สถานะ" ] ==  ทรู และการตั้งค่า [ "เลียนแบบ" ] [ "เป้าหมาย" ] [ส่ง] ==  True :
                    text = msg.text
                    ถ้าข้อความเป็น ไม่ได้ ไม่มี :
                        nadya.sendMessage (msg.to ข้อความ)
                ถ้า msg.contentType ==  0  และผู้ส่งไม่ได้ อยู่ใน nadyaMID และ msg.toType ==  2 :
                    ถ้า " MENTION " ใน รายการ (msg.contentMetadata.keys ()) ! =  ไม่มี :
                        ถ้าการตั้งค่า [ ' Tag2 ' ] ==  True :
                             contact = nadya.getContact (msg._from)
                             cName = contact.pictureStatus
                             balas = [ " http://dl.profile.line-cdn.net/ "  + cName]
                             ret_ = random.choice (balas)
                             กล่าวถึง= ast.literal_eval (msg.contentMetadata [ "กล่าวถึง" ])
                             mentionees =พูดถึง [ " MENTIONEES " ]
                             สำหรับการกล่าวถึงใน mentionees:
                                   ถ้าพูดถึง [ " M " ] ใน nadyaMID:
                                          nadya.sendImageWithURL (ไป ret_)
                                          หยุด
                ถ้า msg.contentType ==  0  และผู้ส่งไม่ได้ อยู่ใน nadyaMID และ msg.toType ==  2 :
                    ถ้า " MENTION " ใน รายการ (msg.contentMetadata.keys ()) ! =  ไม่มี :
                         ถ้าการตั้งค่า [ ' detectMention ' ] ==  True :
                             contact = nadya.getContact (msg._from)
                             cName = contact.displayName
                             balas = [ "แทึคกูนี้แอบชอบกูไช้ ป่ะ😁 " ]
                             ret_ =  " "  + random.choice (balas)
                             ชื่อ= re.findall ( r ' @ ( \ w + ) ' , msg.text)
                             กล่าวถึง= ast.literal_eval (msg.contentMetadata [ "กล่าวถึง" ])
                             mentionees =พูดถึง [ ' MENTIONEES ' ]
                             สำหรับการกล่าวถึงใน mentionees:
                                   ถ้าพูดถึง [ ' M ' ] ใน nadyaMID:
                                          nadya.sendMessage (ไป ret_)
                                          sendMessageWithMention (ถึง, contact.mid)
                                          หยุด

# =========================================== ============================= #
        ถ้า op.type ==  55 :
            พิมพ์ ( " [55] NOTIVEED READ MESSAGE " )
            ลอง :
                ถ้า op.param1 ในการอ่าน [ ' readPoint ' ]:
                    ถ้า op.param2 ในการอ่าน [ ' readMember ' ] [op.param1]:
                        ผ่านไป
                    อื่น :
                        อ่าน [ ' readMember ' ] [op.param1] + = op.param2
                    อ่าน [ ' ROM ' ] [op.param1] [op.param2] = op.param2
                    สำรองข้อมูล()
                อื่น :
                   ผ่านไป
            ยกเว้น :
                ผ่านไป
    ยกเว้น ข้อยกเว้น เป็นข้อผิดพลาด:
        : ฟังก์ชัน LogError (ผิด)
# =========================================== ============================= #
ขณะที่ True :
    ลอง :
        ops = oepoll.singleTrace ( นับ= 50 )
        ถ้า Ops เป็น ไม่ได้ ไม่มี :
            สำหรับ op ใน ops:
                lineBot (สหกรณ์)
                oepoll.setRevision (op.revision)
    ยกเว้น ข้อยกเว้น เช่น e:
        : ฟังก์ชัน LogError (จ)
