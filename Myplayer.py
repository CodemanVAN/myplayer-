import requests
import json
import random
from UI import donate
import sys
from UI import myplayer_ui
from PyQt5.QtWidgets import QPushButton,QLineEdit,QWidget, QApplication,QMessageBox
import os
from PyQt5 import QtMultimedia
from  PyQt5.QtCore import QUrl

header = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'appver=1.5.9; os=osx; channel=netease; osver=%E7%89%88%E6%9C%AC%2010.13.2%EF%BC%88%E7%89%88%E5%8F%B7%2017C88%EF%BC%89; __remember_me=true; __csrf=7f4dca8d579178e8eb89bb4c3996246f; MUSIC_U=08a567a216480ddc13b9e6d3e15379323d32bafc53674035c61796d2e017dd990931c3a9fbfe3df2; undefined',
'Host':'musicapi.leanapp.cn',
'If-None-Match':'W/"5a72d-XemM4vwCTGosxDHpBT51ruN3vaU"',
'Upgrade-Insecure-Requests':'1',
'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        }

def get_songlist_detail(id):
    me.songlist_name.clear()
    me.songlist_id.clear()
    base_url='http://musicapi.leanapp.cn/playlist/detail?id=%s'%id
    resp=requests.get(url=base_url,headers=header)
    json_text=decode_json(resp.text)
    songlist=json_text["playlist"]["tracks"]
    for song in songlist:
        me.songlist_name.append(song['name'])
        me.songlist_id.append(song['id'])

def download(name,baseurl):
    try:
        if name in player.localsong:
            return
        resp= requests.get(baseurl,stream=True)
        i=0
        totalsize=int(resp.headers['Content-Length'])
        with open('./downloads/'+name, "wb") as code:
            for a in resp.iter_content(chunk_size=1024):
                code.write(a)
                if(i==5):
                    filesize=os.path.getsize('./downloads/'+name)
                    main_wd.set_downloadbar(float(filesize / totalsize)*100)
                    i=0
                i+=1
    except:
        main_wd.showmsg("下载失败")

def record_text(name,text):
    if not os.path.exists('./user'):
	    os.makedirs('./user')
    file_handle=open('./user/%s.txt'%name,mode='w')
    file_handle.write(text)
    file_handle.close

def decode_json(html_text):
    return json.loads(html_text)
def ms_to_m(ms):
    s=int(ms/1000)%60
    m=int(ms/60000)
    h=int(s/10)
    s=s%10
    return str(m)+':'+str(h)+str(s)

def posi():
    if(player.duration()-player.position()<500&player.position()>10):
        player.auto_play()
    main_wd.set_progess_text()
class user():
    def __init__(self):
        self.username=''
        self.userid=''
        self.userplaylist={}
        self.playlist_name=[]
        self.songlist = {}
        self.songlist_name = []
        self.songlist_id = []

class music_player(QtMultimedia.QMediaPlayer):
    def __init__(self):
        super(music_player,self).__init__()
        self.play_mode=0
        self.num=0
        self.localsong=[]
        self.init_localsong()

    def init_localsong(self):
        if (os.path.exists('./downloads')):
            for music in os.listdir('./downloads'):
                if music.endswith((".mp3", '.wav', '.ogg')):
                    self.localsong.append(music)

    def get_user_playlist(self,id):
        base_url='http://musicapi.leanapp.cn/user/playlist?uid=%s'%id
        resp=requests.get(url=base_url,headers=header)
        json_text=decode_json(resp.text)
        playlist=json_text['playlist']
        i=len(playlist)
        for mylist in playlist:
            me.userplaylist[mylist["name"]]=mylist["id"]
        me.playlist_name=list(me.userplaylist.keys())
        get_songlist_detail(me.userplaylist[me.playlist_name[0]])

    def play_pre(self):
        if (self.num <= 0):
            if (len(self.localsong)):
                self.num = len(self.localsong) - 1
        else:
            self.num -= 1
        self.playsong(self.localsong[self.num])

    def add_song_to_localsong(self,song):
        if song in self.localsong:
            return
        else:
            self.localsong.append(song)

    def playsong(self,name):
        if (len(self.localsong) == 0):
            return
        file = QUrl.fromLocalFile('./downloads/' + name)  # 音频文件路径
        content = QtMultimedia.QMediaContent(file)
        self.setMedia(content)
        self.play()
        main_wd.set_nowplay_info(name)

    def auto_play(self):
        if(self.play_mode==0):
            self.num+=1
        elif(self.play_mode==1):
            self.num=self.num
        else:
            self.num=random.randint(0,len(self.localsong))
        if(self.num>=len(self.localsong)):
            self.num=0
        self.playsong(self.localsong[self.num])

class login_w(QWidget):
    def __init__(self):
        super(login_w,self).__init__()
        self.initUI()
        if(os.path.exists("./user/user_info.txt")):
            self.aotu_login()
        
    def initUI(self):               
        self.setGeometry(400, 400, 300, 70)        
        self.setWindowTitle('登录网易云')
        self.bt_init()
        self.input_text_init()
        self.show()

    def bt_init(self):
        self.login_bt=QPushButton('登录',self)
        self.login_bt.move(180,10)
        self.login_bt.resize(70,40)
        self.login_bt.clicked.connect(self.login_in)

    def input_text_init(self):
        self.cellphone_text=QLineEdit(self)
        self.paw_text=QLineEdit(self)
        self.cellphone_text.setPlaceholderText("输入网易账号")
        self.paw_text.setPlaceholderText("输入网易密码")
        self.cellphone_text.move(10,10)
        self.paw_text.move(10,40)

    def login_in(self):
        login_result=self.login_wangyiyun(self.cellphone_text.text(),self.paw_text.text())
        QMessageBox.about(self,'登录结果:','%s'%login_result)
        if "成功" in login_result:
            main_wd.show_me()
            self.close()
    def aotu_login(self):
        file_name='./user/user_info.txt'
        file_object = open(file_name)
        user_info = file_object.read().split('\n')  #读取数据
        login_result=self.login_wangyiyun(user_info[0],user_info[1])
        QMessageBox.about(self,'自动登录结果:','%s'%login_result)
        if "成功" in login_result:
            main_wd.show_me()
            self.close()

    def login_wangyiyun(self,phone, password):
        if ('@' in phone):
            login_url = r'http://musicapi.leanapp.cn/login/email?email=%s&password=%s' % (phone, password)
        else:
            login_url = r'http://musicapi.leanapp.cn/login/cellphone?phone=%s&password=%s' % (phone, password)
        resp = requests.get(url=login_url, headers=header)
        json_text = decode_json(resp.text)
        if (json_text["code"] != 200):
            errcode = json_text["code"]
            if "msg" in json_text:
                msg = json_text["msg"]
                return str(errcode) + ':' + msg
            return errcode
        me.userid = json_text["account"]["id"]
        player.get_user_playlist(me.userid)
        me.username = json_text["profile"]["nickname"]
        record_text('user_info', phone + '\n' + password)
        return json_text["profile"]["nickname"] + "登录成功"

class main_windows(myplayer_ui.Ui_Myplayer):
    def __init__(self):
        player.positionChanged.connect(posi)
        self.donate_wd=donate.Ui_form()
        self.widget= QWidget()
        self.donat_widget= QWidget()
        self.main_w=myplayer_ui.Ui_Myplayer()
        self.main_w.setupUi(self.widget)
        self.main_w.logout_bt.clicked.connect(self.logout_user)
        self.main_w.play_bt.clicked.connect(self.play_bt_cliced)
        self.main_w.songlist.itemClicked.connect(self.download_song)
        self.main_w.songlist.itemDoubleClicked.connect(self.play_music)
        self.main_w.vulumesilider.valueChanged.connect(self.set_volmue)
        self.main_w.songlist_choice.currentIndexChanged.connect(self.updata_songlist)
        self.main_w.mode_choice.currentIndexChanged.connect(self.play_mode_choice)
        self.main_w.pre_bt.clicked.connect(self.play_pre)
        self.main_w.next_bt.clicked.connect(self.play_next)
        self.main_w.pushButton.clicked.connect(self.show_donate_wd)
        self.donate_wd.setupUi(self.donat_widget)
        self.main_w.serach_input.setPlaceholderText("搜索功能还没有完善，打赏一下马上肝")
    def play_next(self):
        self.main_w.play_bt.setText('暂停')
        player.auto_play()
    def show_donate_wd(self):
        self.donate_wd.retranslateUi(self.donat_widget)
        self.donat_widget.show()
    def play_pre(self):
        player.play_pre()
        self.main_w.play_bt.setText('暂停')
    def play_music(self):
        try:
            filename = self.main_w.songlist.currentItem().text() + '.mp3'
        except:
            filename='.mp3'
        if(filename in player.localsong):
            player.playsong(filename)
            self.main_w.play_bt.setText("暂停")
        elif(filename=='.mp3'):
            if(len(player.localsong)):
                player.playsong(player.localsong[player.num])
            else:
                self.set_nowplay_info("本地没歌曲，先选中下载再播放吧")
        else:
            self.set_nowplay_info("还没下载呢，双击下载叭")
    def show_me(self):
        self.set_all_info()
        self.widget.show()

    def play_bt_cliced(self):
        if(self.main_w.play_bt.text()=='播放'):
            self.play_music()
            self.main_w.play_bt.setText('暂停')
        elif(self.main_w.play_bt.text()=='暂停'):
            player.stop()
            self.main_w.play_bt.setText('播放')

    def set_all_info(self):
        self.set_songlist_name()
        self.set_user_name()
        self.set_songlist()

    def set_user_name(self):
        self.main_w.username_text.setText(me.username)

    def set_songlist_name(self):
        i=0
        for name in me.playlist_name:
            self.main_w.songlist_choice.addItem(me.playlist_name[i])
            i+=1
    def play_mode_choice(self):
        player.play_mode=self.main_w.mode_choice.currentIndex()
    def set_songlist(self):
        self.main_w.songlist.addItems(me.songlist_name)

    def updata_songlist(self):
        self.main_w.songlist.clear()
        get_songlist_detail(me.userplaylist[self.main_w.songlist_choice.currentText()])
        self.set_songlist()

    def logout_user(self):
        path='./user/user_info.txt'
        if os.path.exists(path):  # 如果文件存在。
            os.remove(path)
        self.widget.close()

    def download_song(self):
        if not os.path.exists('./downloads'):
            os.makedirs('./downloads')
        try:
            filename=self.main_w.songlist.currentItem().text()
            baseurl='https://link.hhtjim.com/163/%s.mp3'%me.songlist_id[me.songlist_name.index(filename)]
            filename=self.main_w.songlist.currentItem().text()+'.mp3'
            download(filename,baseurl)
            player.add_song_to_localsong(filename)
        except:
            self.showmsg(self.main_w.songlist.currentItem().text()+'下载失败')

    def showmsg(self,msg):
        QMessageBox.about(self.widget,'信息：','%s'%msg)

    def set_downloadbar(self,value):
        self.main_w.download_bar.setProperty("value", value)

    def set_volmue(self):
        player.setVolume(self.main_w.vulumesilider.value())
    def set_nowplay_info(self,info):
        self.main_w.nowplay_info.setText(info)
    def set_progess_text(self):
        now=player.position()
        self.main_w.nowplay_posi.setValue(now)
        self.main_w.nowplay_posi.setMaximum((player.duration()+1))
        total=ms_to_m(player.duration())
        now= ms_to_m(player.position())
        self.main_w.label_3.setText(now+'/'+total)


if __name__ == '__main__':
    player=music_player()
    me=user()
    app = QApplication(sys.argv)
    main_wd=main_windows()
    login_wd = login_w()
    sys.exit(app.exec_())