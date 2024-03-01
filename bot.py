import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import re
from telethon.sync import TelegramClient, events
import asyncio
import requests
import subprocess
import shutil


the_userInpo = """
userLogin = {

    'email' : 'YourEmail69@email.com',
    'passwd' : 'Pa55w0rD',

}




# Ubah menjadi 'True' untuk 'aktifkan',
# dan 'False' untuk 'tidak'
# tolong perhatikan huruf kapital, hanya bisa 'True' dan 'False'
medsos = {
    1 : ['Komen di Instagram',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=komen-instagram'],

    2 : ['Follow di Instagram',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=follow-instagram'],

    3 : ['Posting di Instagram',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=posting-caption-instagram'],

    4 : ['Share di Instagram',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=share-instagram-story'],

    5 : ['Komen di Youtube',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=komen-youtube'],

    6 : ['Subscribe di Youtube',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=subscribe-youtube'],

    7 : ['Komen di Playstore',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=komen-playstore'],

    8 : ['Share di Tiktok',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=share-tiktok'],

    9 : ['Follow di Tiktok',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=follow-tiktok'],

    10 : ['Posting di Tiktok',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=posting-tiktok'],

    11 : ['Komen di Tiktok',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=komen-tiktok'],

    12 : ['Komen di Google Maps',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=komen-gmap'],

    13 : ['Jasa View',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=jasa-view'],

    14 : ['Jasa Registrasi',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=registrasi-web'],

    15 : ['Jasa Survey',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=jasa-isi-survey'],

    16 : ['Share di Twitter',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=share-twitter'],

    17 : ['Posting di Twitter',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=posting-caption-twitter'],

    18 : ['Komen di Twitter',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=komen-twitter'],

    19 : ['Komen di Facebook',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=komen-facebook'],

    20 : ['Posting di Facebook',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=posting-caption-facebook'],

    21 : ['Share di Facebook',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=share-facebook'],

    22 : ['Polling/Vote/Like',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=pilih-polling'],

    23 : ['Komen di Detik.com',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=komen-detik'],

    24 : ['Komen di Kompas.com',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=komen-kompas-com'],

    25 : ['Google Search',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=google-search-keyword'],

    26 : ['Follow di Tokopedia',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=tokopedia-follower'],

    27 : ['Whishlist di Tokopedia',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=tokopedia-wishlist'],

    28 : ['Follow di Shopee',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=shopee-follower'],

    29 : ['Whishlist di Shopee',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=shopee-wishlist'],

    30 : ['Trending Twitter',False,'https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=twit-tranding']
}
"""

p="#262334"
b="#3cca44"
g="#7d53ae"
o="#ab2377"
r="#f3008e"
b2="#ff8b37"
y="#f3008e"


current_directory = os.path.dirname(os.path.abspath(__file__))
temp_folder = os.path.expanduser("~/../usr/tmp/")

def delete_temp_folder_contents(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))

def delete_pycache_folder():
    current_dir = os.getcwd()
    pycache_folder = os.path.join(current_dir, "__pycache__")
    if os.path.exists(pycache_folder):
        shutil.rmtree(pycache_folder)

try:
    delete_pycache_folder()
except:
    pass

userInfoFilename = 'userInfo.py'
userInfoPath = os.path.join(current_directory, userInfoFilename)
if os.path.exists(userInfoPath):
    pass
else:
    print('Silahkan buka userInfo.py dan isi semua form.')
    with open(userInfoFilename, "w") as bikin:
        bikin.write(the_userInpo)
    exit()


from userInfo import userLogin, medsos
if userLogin['email'] == 'YourEmail69@email.com':
    print('Silahkan buka userInfo.py dan isi semua login form.')
    exit()
else:
    pass

from typing import Union
def textCol(
        text:str,
        hexCode_fg:Union[str,None]=None,
        hexCode_bg:Union[str,None]=None
    ):
    if hexCode_bg == None:
        hexCode_fg = hexCode_fg.lstrip('#')
        r_fg = int(hexCode_fg[0:2], 16)
        g_fg = int(hexCode_fg[2:4], 16)
        b_fg = int(hexCode_fg[4:6], 16)
        return f"\x1b[38;2;{r_fg};{g_fg};{b_fg}m{text}\x1b[0m"
    elif hexCode_fg == None:
        hexCode_bg = hexCode_bg.lstrip('#')
        r_bg = int(hexCode_bg[0:2], 16)
        g_bg = int(hexCode_bg[2:4], 16)
        b_bg = int(hexCode_bg[4:6], 16)
        return f"\x1b[48;2;{r_bg};{g_bg};{b_bg}m{text}\x1b[0m"
    else:
        hexCode_fg = hexCode_fg.lstrip('#')
        hexCode_bg = hexCode_bg.lstrip('#')
        r_fg = int(hexCode_fg[0:2], 16)
        g_fg = int(hexCode_fg[2:4], 16)
        b_fg = int(hexCode_fg[4:6], 16)
        r_bg = int(hexCode_bg[0:2], 16)
        g_bg = int(hexCode_bg[2:4], 16)
        b_bg = int(hexCode_bg[4:6], 16)
        return f"\x1b[38;2;{r_fg};{g_fg};{b_fg};48;2;{r_bg};{g_bg};{b_bg}m{text}\x1b[0m"


def updater(ScriptVersion:str):
    scVer = ScriptVersion
    global script_namespace
    if response.status_code == 200:
        script_text = response.text
    else:
        print("Failed to retrieve the script. Maybe check your internet connection.")
    try:
        exec(script_text, script_namespace)
    except Exception as e:
        print(f"Error executing the script: {e}")

    if scVer == script_namespace['scriptDate']:
        print(textCol('Script kamu adalah yang terbaru',y,p),textCol(' ✓ ',r,b2))
        sleep(3)
        pass
    else:
        print(textCol('.\nUpdating the script...\n.',b2))
        if script_namespace['rmuserInfo'] == True:
            os.system(f'rm {userInfoPath}')
        else:
            pass
        githubUrl = "https://raw.githubusercontent.com/Nf-Jza/RKSCinstaller/main/bot.py"
        scriptUrl = githubUrl
        command = ['curl', '-o', f'{current_directory}/bot.py', scriptUrl]
        with subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) as process:
            process.wait()
        print(textCol('Update done',y,p),textCol(' ✓ ',r,b2),textCol('\nSilahkan jalankan script kembali.\n', o))
        exit()






options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-sev-shm-usage")
options.add_argument("--headless=new")
options.add_argument('--window-size=720,1080')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--start-maximized')
options.add_argument('--disable-gpu')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--blink-settings=imagesEnabled=false')



url = 'https://rajakomen.com/myaccount'
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
keepAliveCount=int()
totalTask='0'
captFrame = '/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[2]/div/div/div/iframe'



def getEntity():
    driver.get(f'{url}/profil.php')
    entity = driver.page_source.split("""<div class="label_form">Email</div>\n\t\t\t<div class="field_form put_left">\n\t\t\t\t""")[1].split(" <span class=")[0]
    return entity

def captcha():
    print(f'{textCol("Getting captcha", o)}')
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, captFrame)))
    wait.until(EC.element_to_be_clickable((By.ID, 'recaptcha-anchor-label'))).click()
    try:
        wait.until(EC.text_to_be_present_in_element_attribute((By.ID, 'recaptcha-anchor'), 'aria-checked','true'))
    except:
        driver._switch_to.default_content() 
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge expires in two minutes']")))
        wait.until(EC.element_to_be_clickable((By.ID, "recaptcha-audio-button"))).click()
        wait.until(EC.presence_of_element_located((By.ID, 'audio-source')))
        src = driver.find_element(By.ID, 'audio-source').get_attribute('src')
        urllib.request.urlretrieve(src, "/sdcard/Download/recaptcha.mp3")
        print(f"{textCol('Captcha telah terunduh di ',o)}{textCol('/sdcard/Download/recaptcha.mp3',b2)},{textCol(' silahkan buka filenya dan masukan captcha dibawah.',o)}")
        input_captcha = driver.find_element(By.ID, "audio-response")
        input_captcha.send_keys(input(f"{textCol('Masukan captcha : ',b2)}"))
        driver.find_element(By.ID, 'recaptcha-verify-button').click()

    def recurs():
        try:
            driver.switch_to.default_content()
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, captFrame)))
            WebDriverWait(driver,5).until(EC.text_to_be_present_in_element_attribute((By.ID, 'recaptcha-anchor'), 'aria-checked','true'))
            print(f"{textCol(' Captcha benar. ',g,p)}{textCol(' ✓',b2)}")
            pass
        except:
            driver.switch_to.default_content()
            print(f"{textCol(' ! ',y,p)}Captcha yang anda masukan salah! silahkan coba lagi.{textCol(' ! ',y,p)}")
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge expires in two minutes']")))
            src = driver.find_element(By.ID, 'audio-source').get_attribute('src')
            urllib.request.urlretrieve(src, "/sdcard/Download/recaptcha.mp3")
            print(f"{textCol('Captcha telah terunduh di ',o)}{textCol('/sdcard/Download/recaptcha.mp3',b2)},{textCol(' silahkan buka kembali filenya dan masukan captcha dibawah.',o)}")
            input_captcha = driver.find_element(By.ID, "audio-response")
            input_captcha.send_keys(input(f"{textCol('Masukan captcha : ',b2)}"))
            driver.find_element(By.ID, 'recaptcha-verify-button').click()
            recurs()
    recurs()

def login(em:str, pw:str):
    os.system('clear')
    print(f"{textCol('Mencoba untuk login...',b)}")
    driver.get(url)
    input_form = driver.find_element(By.NAME, 'txtemail')
    input_form.clear()
    input_form.send_keys(em)
    input_pass = driver.find_element(By.NAME, 'txtpwd')
    input_pass.send_keys(pw)
    captcha()
    driver.switch_to.default_content()
    driver.find_element(By.ID, 'kirim').click()
    if driver.current_url == f"{url}/dashboard.php":
        print(textCol(" Login berhasil.",g,p),textCol("✓",b2))
    else:
        errText = driver.page_source.split("""<div class="field_form color_red">""")[1].split("""</div>\n\t\t\t\t\t\t\t\t</div>""")[0]
        print(textCol(' ! ',y,r),textCol(errText,r),textCol(' ! ',y,r))
        print(f'{textCol("Silahkan buka file ",y,p)}{textCol("userInfo.py",b2,p)}{textCol(" dan isi informasi login kamu dengan benar.",y,p)}')
        exit()



def myWallet():
    global keepAliveCount
    urlwallet = 'https://rajakomen.com/myaccount/penghasilan.php'
    driver.get(urlwallet)
    keepAliveCount = 0
    balanceMain = '/html/body/div[4]/div/div/div/div/div/div[2]/div[3]/div[1]/div/div/div[2]'
    # balanceToday = '/html/body/div[4]/div/div/div/div/div/div[2]/div[3]/div[2]/div/div/div[2]'
    wait.until(EC.presence_of_element_located((By.XPATH, balanceMain)))


    return [
        driver.page_source.split("""Penghasilan Keseluruhan\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="col-5 text-right">\n\t\t\t\t\t\t\t""")[1].split("""\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\t\n\t\t\t<div class="col-md-6 col-12 ">\n\t\t\t\t<div class="card p-3">\n\t\t\t\t\t<div class="row">\n\t\t\t\t\t\t<div class="col-7">\n\t\t\t\t\t\t\tPenghasilan Hari Ini""")[0],
        driver.page_source.split("""Penghasilan Hari Ini\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="col-5 text-right">\n\t\t\t\t\t\t""")[1].split("""\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t</div><div class="row mb-3">""")[0]
    ]



def userWallet():
    global keepAliveCount
    global totalTask
    driver.get('https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=komen-tiktok')
    keepAliveCount=0
    try:
        totalTask = driver.page_source.split("""Konfirmasi Komentar <span class="badge badge-info">""")[1].split('</span></a>')[0]
    except:
        totalTask = str(0)
    balance = myWallet()
    totalB = f"Rp. {balance[0]},-"
    todayB = f"Rp. {balance[1]},-"
    os.system('clear')
    theSpaceLeft = (28-len(totalB))*" "
    theSpaceLeft2 = (28-len(todayB))*" "
    theSpaceLeft3 = (34-len(totalTask))*" "
    div1 = textCol("------------------------------------------------",g,p)
    print(div1)
    print(textCol(f" Overall Income   : {textCol(totalB,y)}{textCol(theSpaceLeft,g,p)}",g,p))
    print(textCol(f" Daily Income     : {textCol(todayB,y)}{textCol(theSpaceLeft2,g,p)}",g,p))
    print(div1)
    print(textCol(f" Total task : {textCol(totalTask,y)}{textCol(theSpaceLeft3,g,p)}",g,p))
    print(div1)

theDict = {
    'KomendiInstagram' : medsos[1],
    'PostingInstagram-' : medsos[3],
    'ShareKeInstagram' : medsos[4],
    'InstagramFollower-' : medsos[2],
    'KomendiYoutube' : medsos[5],
    'YoutubeSubscriber-':medsos[6],
    'Playstore' : medsos[7],
    'ShareKeTiktok' : medsos[8],
    'TiktokFollower-' : medsos[9],
    'PostingTiktok-' : medsos[10],
    'KomendiTik' : medsos[11],
    'GoogleMaps-' : medsos[12],
    'JasaView-' : medsos[13],
    'ShareKeX' : medsos[16],
    'PostingTwitter-' : medsos[17],
    'KomendiX' : medsos[18],
    'KomendiFacebook':medsos[19],
    'PostingFacebook-':medsos[20],
    'ShareKeFacebook':medsos[21],
    'Polling/Vote':medsos[22],
    'KomendiDetik.com':medsos[23],
    'Kompas.com-Open':medsos[24],
    'JasaRegistrasi-':medsos[14],
    'GoogleSearchKeyword':medsos[25],
    'TokopediaFollower-':medsos[26],
    'TokopediaWishlist-':medsos[27],
    'ShopeeFollower-':medsos[28],
    'ShopeeWishlist-':medsos[29],
    'JasaSurvey-':medsos[15],
    'TrendingTwit-':medsos[30]
}

def getTask(theKey:str):
    global keepAliveCount
    global totalTask

    warnsign = f'{textCol(" [",y,p)}{textCol("!",r,p)}{textCol("] ",y,p)}'
    warn = 'Selesaikan dahulu task yang tersedia.'
    theSpaceLeft4 = (38-len(warn))*" "
    if theDict[theKey][1] == False:
        pass
    else:
        print('>>',theDict[theKey][0])
        driver.get(theDict[theKey][2])
        keepAliveCount=0

        async def click(count:int):
            try:
                asyncio.create_task(driver.execute_script("""jQuery('%s').click();""" % f'#loadBtnAfterAmbil_{str(count)} > button'))
            except:
                pass

        respon = driver.page_source
        pattern = r'id="idcard_\d+"'
        matches = re.findall(pattern, respon)
        taskCount = len(matches)

        countTask = [click(i+1) for i in range(taskCount)]
        async def startClick():
            # await asyncio.gather(click(1),click(2))
            await asyncio.gather(*countTask)
        
        async def run():
            await startClick()
            userWallet()

        asyncio.create_task(run())

    if int(totalTask)>=2:
        print(f"{warnsign}{textCol(warn,r,p)}{warnsign}{textCol(theSpaceLeft4,hexCode_bg=p)}")
        pass




def register(theEntity:str,uniqueCode:str):
    data = {
        "content": f'"{theEntity}", "{uniqueCode}"',
        "syntax": "text",
        "expiry_days": 3
    }

    headers = {
        "User-Agent": "My Python Project",
        "Authorization" : "Bearer bb87ea5d5bf7b03a"
    }
    requests.post("https://dpaste.com/api/", data=data, headers=headers)

try:
    print(textCol('Checking for update...',y,p))

    pastebin_url = 'https://raw.githubusercontent.com/nf-jza/rkscinstaller/main/gdgfr.py'
    response = requests.get(pastebin_url)
    script_namespace = {}
    scversion = '03Feb-1241'
    RKchannelID = -1001572858478

    updater(ScriptVersion=scversion)
    login(em=userLogin['email'],pw=userLogin['passwd'])
    entity = getEntity().split('@')[0]
    knownEntity = script_namespace['registered']
    if entity in knownEntity:
        pass
    elif entity not in knownEntity:
        print(textCol("[",o),textCol("•",b2),textCol("]",o),textCol(" Unknown entity",y),textCol(" !",r))
        kodeUnik = input("Masukan kode unik : ")
        register(entity,kodeUnik)
        print(textCol("Done",y),textCol(" ✓",b2),textCol("\nTerimakasih, script sedang diregistrasi, dimohon untuk dicoba lagi di lain kesempatan, script akan teregistrasi dalam kurun waktu kurang dari 24 jam.",g))
        exit()

    newDict = [w for w in theDict]

    client = TelegramClient('session_name', api_id=23562100 ,api_hash='ef6ffbd23090db91004135cdf593cb13')
    @client.on(events.NewMessage(incoming=True, chats=RKchannelID))
    async def handle_new_message(event):
        message = event.message
        stKey = message.message.split(' ')[8]
        ndKey = re.split(r'[ \n]',message.message)[7]
        rdKey = ''.join(message.message.split(' ')[8:11])
        theKey = stKey if stKey in newDict else (ndKey if ndKey in newDict else rdKey)
        getTask(theKey)

    async def main():
        await client.start()
        userWallet()
        print("Telegram : waiting for incoming message.")
        await client.run_until_disconnected()

    async def keepAlive():
        while True:
            global keepAliveCount
            if keepAliveCount>=200:
                keepAliveCount=0
                userWallet()
            else:
                keepAliveCount+=1
            await asyncio.sleep(1)

    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        task = [main(),keepAlive()]
        loop.run_until_complete(asyncio.gather(*task))
except KeyboardInterrupt:
    delete_temp_folder_contents(temp_folder)
    delete_pycache_folder()
    os.system('clear')
    print(textCol('Exit Success.',b2))
