print("Starting.",end='\r')
import subprocess
try:
    print("Starting..",end='\r')
    subprocess.check_call(
        ["pip3","install"]+['blessed','rich','selenium==4.9.1','telethon','requests'],
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.DEVNULL
    )
    print("Starting...",end='\r')
except subprocess.CalledProcessError as e:
    print(f"Installation failed with error: {e}")
import asyncio
import os
from time import sleep
from os import get_terminal_size
from blessed import Terminal
from rich import box
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.align import Align
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import re
from telethon.sync import TelegramClient, events
import asyncio
import requests
import shutil
import sys

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


def invert_hex_color(hex_color):
    hex_color = hex_color.lstrip('#')
    inverted_color = 0xFFFFFF - int(hex_color, 16)
    inverted_hex_color = '#' + format(inverted_color, '06x')
    return inverted_hex_color

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



# --------------- Global Variable ---------------

current_directory = os.path.dirname(os.path.abspath(__file__))
temp_folder = os.path.expanduser("~/../usr/tmp/")
console = Console()
terminal_Width = int()
term = Terminal()
keystroke = str()
totalTugas = str()
x_coordinate,y_coordinate = (int(),int())
current_state = int()

scversion = '11Mar-1112'


head_box_color = '#DFD800'
text_color_head = '#1BDF00'
money_text_color_head = "#C57CFF"

box_body_color = "#FF0000"
bg_body_color = "#380400"
cursor_color = invert_hex_color(bg_body_color)

p="#262334"
b="#3cca44"
g="#7d53ae"
o="#ab2377"
r="#f3008e"
b2="#ff8b37"
y="#f3008e"

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
    sys.exit()

from userInfo import medsos,userLogin



data = {
    ":" : "->",

    "account" : {
        "OverallIncome" : str(),
        "DailyIncome" : str(),
        "TotalTask" : int(),
        "medsos" : {
            'KomendiInstagram' : medsos[1],
            'InstagramFollower-' : medsos[2],
            'PostingInstagram-' : medsos[3],
            'ShareKeInstagram' : medsos[4],
            'KomendiYoutube' : medsos[5],
            'YoutubeSubscriber-':medsos[6],
            'Playstore' : medsos[7],
            'ShareKeTiktok' : medsos[8],
            'TiktokFollower-' : medsos[9],
            'PostingTiktok-' : medsos[10],
            'KomendiTik' : medsos[11],
            'GoogleMaps-' : medsos[12],
            'JasaView-' : medsos[13],
            'JasaRegistrasi-':medsos[14],
            'JasaSurvey-':medsos[15],
            'ShareKeX' : medsos[16],
            'PostingdiX' : medsos[17],
            'KomendiX' : medsos[18],
            'KomendiFacebook':medsos[19],
            'PostingFacebook-':medsos[20],
            'ShareKeFacebook':medsos[21],
            'Polling/Vote':medsos[22],
            'KomendiDetik.com':medsos[23],
            'Kompas.com-Open':medsos[24],
            'GoogleSearchKeyword':medsos[25],
            'TokopediaFollower-':medsos[26],
            'TokopediaWishlist-':medsos[27],
            'ShopeeFollower-':medsos[28],
            'ShopeeWishlist-':medsos[29],
            'TrendingTwit-':medsos[30]
        },
        "medsosKey": {
            1: "KomendiInstagram",
            2: "InstagramFollower-",
            3: "PostingInstagram-",
            4: "ShareKeInstagram",
            5: "KomendiYoutube",
            6: "YoutubeSubscriber-",
            7: "Playstore",
            8: "ShareKeTiktok",
            9: "TiktokFollower-",
            10: "PostingTiktok-",
            11: "KomendiTik",
            12: "GoogleMaps-",
            13: "JasaView-",
            14: "JasaRegistrasi-",
            15: "JasaSurvey-",
            16: "ShareKeX",
            17: "PostingdiX",
            18: "KomendiX",
            19: "KomendiFacebook",
            20: "PostingFacebook-",
            21: "ShareKeFacebook",
            22: "Polling/Vote",
            23: "KomendiDetik.com",
            24: "Kompas.com-Open",
            25: "GoogleSearchKeyword",
            26: "TokopediaFollower-",
            27: "TokopediaWishlist-",
            28: "ShopeeFollower-",
            29: "ShopeeWishlist-",
            30: "TrendingTwit-"
        }
    },

    "UI" : {
        "x_coordinate" : 0,
        "y_coordinate" : 0,
        "x1_x_coordinate" : 0,
        "confirm" : bool(),
    },

}


cursor = [
    # ---------------------- BodyHeadTable -----------------------
    # -------- output - eksekutor - config - tentang --------------
    [cursor_color,bg_body_color,bg_body_color,bg_body_color,[bg_body_color,bg_body_color]],
    # ---------------------------------
    [
        medsos[1][0],
        medsos[2][0],
        medsos[3][0],
        medsos[4][0],
        medsos[5][0],
        medsos[6][0],
        medsos[7][0],
        medsos[8][0],
        medsos[9][0],
        medsos[10][0],
        medsos[11][0],
        medsos[12][0],
        medsos[13][0],
        medsos[14][0],
        medsos[15][0],
        medsos[16][0],
        medsos[17][0],
        medsos[18][0],
        medsos[19][0],
        medsos[20][0],
        medsos[21][0],
        medsos[22][0],
        medsos[23][0],
        medsos[24][0],
        medsos[25][0],
        medsos[26][0],
        medsos[27][0],
        medsos[28][0],
        medsos[29][0],
        medsos[30][0],
    ],
    [
        medsos[1][1],
        medsos[2][1],
        medsos[3][1],
        medsos[4][1],
        medsos[5][1],
        medsos[6][1],
        medsos[7][1],
        medsos[8][1],
        medsos[9][1],
        medsos[10][1],
        medsos[11][1],
        medsos[12][1],
        medsos[13][1],
        medsos[14][1],
        medsos[15][1],
        medsos[16][1],
        medsos[17][1],
        medsos[18][1],
        medsos[19][1],
        medsos[20][1],
        medsos[21][1],
        medsos[22][1],
        medsos[23][1],
        medsos[24][1],
        medsos[25][1],
        medsos[26][1],
        medsos[27][1],
        medsos[28][1],
        medsos[29][1],
        medsos[30][1],
    ],
]

outputPrint = list()
theDict = data['account']['medsos']



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
        console.print(f'[bold {y} on {p}]Script kamu adalah yang terbaru [/][bold {r} on {b2}] ✓ [/]')
        sleep(3)
        pass
    else:
        console.print(f'[{b2}].\nUpdating the script...\n.')
        if script_namespace['rmuserInfo'] == True:
            os.system(f'rm {userInfoPath}')
        else:
            pass
        githubUrl = "https://raw.githubusercontent.com/Nf-Jza/RKSCinstaller/main/bot.py"
        scriptUrl = githubUrl
        command = ['curl', '-o', f'{current_directory}/bot.py', scriptUrl]
        with subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) as process:
            process.wait()
        console.print(f'[{y} on {p}]Update done[/][bold {r} on {b2}] ✓ [/][{o}]\nSilahkan jalankan script kembali.\n[/]')
        sys.exit()

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



# --------------- Functions ----------------
def getEntity():
    driver.get(f'{url}/profil.php')
    entity = driver.page_source.split("""<div class="label_form">Email</div>\n\t\t\t<div class="field_form put_left">\n\t\t\t\t""")[1].split(" <span class=")[0]
    return entity

def captcha():
    console.print(f"[{o}]Getting captcha")
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
        console.print(f"[{o}]Captcha telah terunduh di [/][{b2}]/sdcard/Download/recaptcha.mp3[/][{o}] silahkan buka filenya dan masukan captcha dibawah.[/]")
        input_captcha = driver.find_element(By.ID, "audio-response")
        input_captcha.send_keys(input(f"Masukan captcha : "))
        driver.find_element(By.ID, 'recaptcha-verify-button').click()

    def recurs():
        try:
            driver.switch_to.default_content()
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, captFrame)))
            WebDriverWait(driver,5).until(EC.text_to_be_present_in_element_attribute((By.ID, 'recaptcha-anchor'), 'aria-checked','true'))
            console.print(f"[{g} on {p}] Captcha benar. [/][{b2}] ✓")
            pass
        except:
            driver.switch_to.default_content()
            console.print(f"[{y} on {p}] ! [/][bold red]Captcha yang anda masukan salah! silahkan coba lagi.[/][{y} on {p}] ! [/]")
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge expires in two minutes']")))
            src = driver.find_element(By.ID, 'audio-source').get_attribute('src')
            urllib.request.urlretrieve(src, "/sdcard/Download/recaptcha.mp3")
            console.print(f"[{o}]Captcha telah terunduh di [{b2}]/sdcard/Download/recaptcha.mp3[{o}] silahkan buka kembali filenya dan masukan captcha dibawah.[/]")
            input_captcha = driver.find_element(By.ID, "audio-response")
            input_captcha.send_keys(input(f"Masukan captcha : "))
            driver.find_element(By.ID, 'recaptcha-verify-button').click()
            recurs()
    recurs()

def login(em:str, pw:str):
    os.system('clear')
    console.print(f"[{b}]Mencoba untuk login...")
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
        console.print(f"[{g} on {p}] Login berhasil. [/][{b2}] ✓")
    else:
        errText = driver.page_source.split("""<div class="field_form color_red">""")[1].split("""</div>\n\t\t\t\t\t\t\t\t</div>""")[0]
        console.print(f'[bold {y} on {r}] ! [/][{r}]{errText}[/][bold {y} on {r}] ! [/]')
        console.print(f'[{y} on {p}]Silahkan buka file [/][{b2} on {p}]userInfo.py[/][{y} on {p}] dan isi informasi login kamu dengan benar.[/]')
        sys.exit()



def myWallet() -> list:
    """
    Return -> [str(OverallIncome),str(DailyIncome)]
    """
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

def updateTotalTask(target:str='')->None:
    """
    Akan mengupdate jumlah tugas yang tersimpan di TotalTask.
    """
    global data
    global keepAliveCount
    if target != '':
        driver.get(theDict.get(target)[2])
    else:
        driver.get(theDict.get('KomendiInstagram')[2])
    keepAliveCount = 0
    try:
        data["account"]['TotalTask'] = int(driver.page_source.split("""Konfirmasi Komentar <span class="badge badge-info">""")[1].split('</span></a>')[0])
    except:
        data['account']['TotalTask'] = int(0)

    

def getTask(theKey:str):
    """Akan mengambil tugas menggunakan kata kunci theKey"""
    global keepAliveCount
    global data
    global outputPrint
    updateOutputPrint(newValue=f'Mencoba mengambil tugas {theDict.get(theKey)[0]}')
    updateTotalTask(target=theKey)
    if int(data['account']['TotalTask']) >= 2:
        updateOutputPrint(newValue=f"[bold {y}] »[{r}] ! [{y}]« [/][{head_box_color}]Telah mencapai maksimal tugas, tolong segera selesaikan.")
        pass
    else:
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
            await asyncio.gather(*countTask)
        
        async def run():
            await startClick()
            updateTotalTask()
            UpdateUserWallet()
            updateOutputPrint(f"Selesai mengambil.[{invert_hex_color(cursor_color)}]✓[/]")
            print_EntireScreen()

        asyncio.create_task(run())



def UpdateUserWallet():
    global keepAliveCount
    global data
    # driver.get('https://rajakomen.com/myaccount/open-order.php?gservice=show-tiket&gsosmed=komen-tiktok')
    keepAliveCount=0
    # try:
    #     data['account']['TotalTask'] = int(driver.page_source.split("""Konfirmasi Komentar <span class="badge badge-info">""")[1].split('</span></a>')[0])
    # except:
    #     data['account']['TotalTask'] = int(0)
    balance = myWallet()
    data['account']['OverallIncome'] = f"Rp. {balance[0]},-"
    data['account']['DailyIncome'] = f"Rp. {balance[1]},-"

def updateOutputPrint(newValue:str):
    global outputPrint
    newValue = str(newValue)
    if len(outputPrint) >= 11:
        outputPrint.pop(0)
        outputPrint.append(newValue)
    elif len(outputPrint) < 11:
        outputPrint.append(newValue)


def makeNew_BodyTable(callback:int):
    """This will make a new whole head and body for the UI
    callback :

    0 -> eksekutor's body
    1 -> output's body
    2 -> config's body
    3 -> tentang's body
    """
    global MainTable
    global BodyHeadTable
    headTable = Table(
        show_edge=False,
        show_lines=False,
        show_header=False,
        expand=True,
        padding=0,
        box=box.SIMPLE
    )
    headTable2 = Table(
        show_edge=False,
        show_lines=False,
        show_header=False,
        expand=False,
        padding=0,
        box=box.SIMPLE
    )
    MainTable = Table(
        show_edge=False,
        show_lines=False,
        show_header=False,
        expand=True,
        padding=(0,5),
        box=box.SQUARE,
    )
    BodyHeadTable = Table(
        show_edge=True,
        show_lines=True,
        show_header=False,
        expand=True,
        padding=0,
        box=box.HEAVY,
        style=f"{box_body_color} on {bg_body_color}",
        title="\n[#ffffff][bold]•[/] Gunakan panah untuk menggerakan.\n[#ffffff][bold]•[/] Tekan ctrl+c untuk menghentikan bot.",
        title_justify="left"
    )

    headTable.add_row(
        Text("Overall Income",style=f"{text_color_head}",justify="right"),
        Text(str(data[":"]),style="#ffffff",justify="center"),
        Text(data["account"]["OverallIncome"],style=f"italic {money_text_color_head}",justify="left"),
        # Text(str(terminal_Width),style=f"italic {money_text_color_head}",justify="left"),
    )

    headTable.add_row(
        Text("Daily Income",style=f"{text_color_head}",justify="right"),
        Text(str(data[":"]),style="#ffffff",justify="center"),
        Text(data["account"]["DailyIncome"],style=f"italic {money_text_color_head}",justify="left"),
        # Text(f"{tes}()",style=f"italic {money_text_color_head}",justify="left"),
    )

    headTable2.add_row(
        Text("Total Tugas",style=f"{text_color_head}",justify="right"),
        Text(str(data[":"]),style="#ffffff",justify="center"),
        Text(str(data["account"]["TotalTask"]),style=f"italic {money_text_color_head}",justify="left")
        # Text(str(data["total task"]),style=f"italic {money_col_head}",justify="left")
    )

    MainTable.add_row(
        Panel(
            renderable=headTable,
            box=box.SQUARE,
            padding=0,
            style = f"{head_box_color}"
        ),
    )
    MainTable.add_row(
        Panel(
            renderable=Align.center(
                renderable=headTable2,
                vertical="middle"
            ),
            box=box.SQUARE,
            padding=0,
            style=f"{head_box_color}",
        )

    )
    BodyHeadTable.add_row(
        Text("💻 Output", style=f"bold {invert_hex_color(cursor[0][0])} on {cursor[0][0]}",justify="center"),
        Text("🍎 Eksekutor", style=f"bold {invert_hex_color(cursor[0][1])} on {cursor[0][1]}",justify="center"),
        Text("🔧 Config", style=f"bold {invert_hex_color(cursor[0][2])} on {cursor[0][2]}",justify="center"),
        Text("📃 Tentang", style=f"bold {invert_hex_color(cursor[0][3])} on {cursor[0][3]}",justify="center"),
    )


    if callback == 0:
        output()
    elif callback == 1:
        eksekutor()
    elif callback == 2:
        config()
    elif callback == 3:
        tentang()

    # --------------- User Interface -----------------
def eksekutor():
    global BodyMainTable
    BodyMainTable = Table(
        show_edge=True,
        show_lines=False,
        show_header=False,
        expand=True,
        padding=0,
        box=box.HEAVY,
        style=f"{box_body_color} on {bg_body_color}",
    )
    switch = Table(
        show_edge=False,
        show_lines=False,
        show_header=False,
        expand=False,
        box=box.SIMPLE,
        padding=(0),
        style=f"on {bg_body_color}"
    )
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row(
        Text(" Ambil tugas : ", style=f"italic #EE9800 on {bg_body_color}", justify="left")
    )

    BodyMainTable.add_row(
        Text("    • Tekan enter untuk jalankan", style=f"#9A9A9A on {bg_body_color}",justify="left")
    )
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    switch.add_row(
        Text(f" <- ", style=f"bold #ee9800 on {bg_body_color}", justify="right"),
        Text(f" {cursor[1][data['UI']['x1_x_coordinate']]} ", style=f"Bold {invert_hex_color(cursor[0][4][0])} on {cursor[0][4][0]}", justify="center",),
        Text(f" -> ", style=f"bold #ee9800 on {bg_body_color}", justify="left"),
    )
    BodyMainTable.add_row(
        Align.center(
            switch,
            style=f"on {bg_body_color}"
        )
    )
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
def output():
    global outputPrint
    global BodyMainTable
    BodyMainTable = Table(
        show_edge=True,
        show_lines=False,
        show_header=False,
        expand=True,
        padding=0,
        box=box.DOUBLE_EDGE,
        style=f"{box_body_color} on {bg_body_color}",
    )

    for _ in outputPrint:
        BodyMainTable.add_row(str(f' [bold {text_color_head}]>>> [/][{head_box_color}]{_}'),style=f"on {bg_body_color}")
    if len(outputPrint)!=11:
        for _ in range((11-len(outputPrint))):
            BodyMainTable.add_row('',style=f"on {bg_body_color}")
def config():
    global BodyMainTable
    BodyMainTable = Table(
        show_edge=True,
        show_lines=False,
        show_header=False,
        expand=True,
        padding=0,
        box=box.HEAVY,
        style=f"{box_body_color} on {bg_body_color}",
    )
    switch = Table(
        show_edge=False,
        show_lines=False,
        show_header=False,
        expand=False,
        box=box.SIMPLE,
        padding=(0),
        style=f"on {bg_body_color}"
    )
    switch2 = Table(
        show_edge=False,
        show_lines=False,
        show_header=False,
        expand=False,
        box=box.SIMPLE,
        padding=(0),
        style=f"on {bg_body_color}"
    )
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row(
        Text(" Ubah realtime tracking notif : ", style=f"italic #EE9800 on {bg_body_color}", justify="left")
    )
    BodyMainTable.add_row(
        Text("    • Tekan enter untuk merubah", style=f"#9A9A9A on {bg_body_color}",justify="left")
    )
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    switch.add_row(
        Text(f"Status", style=f"bold {text_color_head} on {bg_body_color}", justify="right"),
        Text(":",style=f"Bold {invert_hex_color(cursor[0][4][0])} on {cursor[0][4][0]}",justify="center"),
        Text(f"{cursor[2][data['UI']['x1_x_coordinate']]}", style=f"bold {money_text_color_head} on {bg_body_color}", justify="left"),
    )
    switch2.add_row(
        Text(f" <- ", style=f"bold #ee9800 on {bg_body_color}", justify="right"),
        Text(f" {cursor[1][data['UI']['x1_x_coordinate']]} ", style=f"Bold {invert_hex_color(cursor[0][4][1])} on {cursor[0][4][1]}", justify="center",),
        Text(f" -> ", style=f"bold #ee9800 on {bg_body_color}", justify="left"),
    )
    BodyMainTable.add_row(Align.center(switch,style=f"on {bg_body_color}"))
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row(Align.center(switch2,style=f"on {bg_body_color}"))
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
def tentang():
    global BodyMainTable
    BodyMainTable = Table(
        show_edge=True,
        show_lines=False,
        show_header=False,
        expand=True,
        padding=0,
        box=box.HEAVY,
        style=f"{box_body_color} on {bg_body_color}",
    )
    contact = Table(
        show_edge=False,
        show_lines=False,
        show_header=False,
        expand=False,
        padding=0,
        box=box.SIMPLE,
        style=f"on {bg_body_color}"
    )
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row(
        Align.center("Dibuat dengan ♥️ oleh :",style=f"{cursor_color} on {bg_body_color}")
    )
    BodyMainTable.add_row(
        Align.center("- Nf -",style=f"{box_body_color} on {bg_body_color}")
    )
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    contact.add_row( 
        Text("📱Telegram",style=f"{cursor_color} on {bg_body_color}"), 
        Text(" : ",style=f"{cursor_color} on {bg_body_color}"), 
        Text("@ShhutUpPls",style=f"{box_body_color} on {bg_body_color}")
    ) 
    BodyMainTable.add_row(
        Align.center(
            contact,
            style=f'on {bg_body_color}'
        )
    )
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row("",style=f"on {bg_body_color}")
    BodyMainTable.add_row(Align.center(f"v.{scversion}",style=f"{cursor_color} on {bg_body_color}"))
    BodyMainTable.add_row("",style=f"on {bg_body_color}")


def print_EntireScreen() -> None:
    """This will update the overall table and print it."""
    makeNew_BodyTable(current_state)
    print(term.home, end="")  # Move the cursor to the home position
    console.print('\n\n\n\n\n',MainTable, BodyHeadTable,BodyMainTable, end="\r")
    return None

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


# ------------- Asynchronous function -------------- 
async def screen_width_tracking():
    global terminal_Width
    oldWidth = int()
    OldoutputPrint = list()
    while True:
        terminal_Width = get_terminal_size().columns
        if terminal_Width != oldWidth:
            print(term.home,term.clear)
            print_EntireScreen()
            oldWidth = terminal_Width
        
        if outputPrint != OldoutputPrint:
            if current_state == 0:
                print(term.home,term.clear)
                print_EntireScreen()
                OldoutputPrint = outputPrint
            else:
                OldoutputPrint = outputPrint
        await asyncio.sleep(0)

async def keystroke_tracking():
    global keystroke
    global data
    global tes
    global current_state
    global cursor
    oldKeystroke = str()

    def keyStrk():
        with term.cbreak(), term.hidden_cursor():
            return repr(term.inkey(timeout=0.005))
    
    def update_user_info(key, new_value):
        global medsos
        global userLogin
        absKey = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22, 22: 23, 23: 24, 24: 25, 25: 26, 26: 27, 27: 28, 28: 29, 29: 30, -1: 30, -2: 29, -3: 28, -4: 27, -5: 26, -6: 25, -7: 24, -8: 23, -9: 22, -10: 21, -11: 20, -12: 19, -13: 18, -14: 17, -15: 16, -16: 15, -17: 14, -18: 13, -19: 12, -20: 11, -21: 10, -22: 9, -23: 8, -24: 7, -25: 6, -26: 5, -27: 4, -28: 3, -29: 2}
        medsos[absKey[key]][1] = new_value
        with open('userInfo.py', 'w') as file:
            file.write('userLogin = ' + str(userLogin) + '\n')
            file.write('medsos = ' + str(medsos) + '\n')
        from userInfo import userLogin, medsos
        data["account"]["medsos"] = {
            'KomendiInstagram' : medsos[1],
            'InstagramFollower-' : medsos[2],
            'PostingInstagram-' : medsos[3],
            'ShareKeInstagram' : medsos[4],
            'KomendiYoutube' : medsos[5],
            'YoutubeSubscriber-':medsos[6],
            'Playstore' : medsos[7],
            'ShareKeTiktok' : medsos[8],
            'TiktokFollower-' : medsos[9],
            'PostingTiktok-' : medsos[10],
            'KomendiTik' : medsos[11],
            'GoogleMaps-' : medsos[12],
            'JasaView-' : medsos[13],
            'JasaRegistrasi-':medsos[14],
            'JasaSurvey-':medsos[15],
            'ShareKeX' : medsos[16],
            'PostingTwitter-' : medsos[17],
            'KomendiX' : medsos[18],
            'KomendiFacebook':medsos[19],
            'PostingFacebook-':medsos[20],
            'ShareKeFacebook':medsos[21],
            'Polling/Vote':medsos[22],
            'KomendiDetik.com':medsos[23],
            'Kompas.com-Open':medsos[24],
            'GoogleSearchKeyword':medsos[25],
            'TokopediaFollower-':medsos[26],
            'TokopediaWishlist-':medsos[27],
            'ShopeeFollower-':medsos[28],
            'ShopeeWishlist-':medsos[29],
            'TrendingTwit-':medsos[30]
        },
        cursor[2] = [
            medsos[_+1][1] for _ in range(len(cursor[2]))
        ]

    while True:
        keystroke = keyStrk()
        if (keystroke != oldKeystroke):
            if keystroke == "KEY_UP":
                if data["UI"]['x_coordinate']==0 or data["UI"]["x_coordinate"]==3:
                    pass
                else:
                    if data["UI"]["y_coordinate"]==0:
                        data["UI"]["y_coordinate"]=-1
                    else:
                        data["UI"]["y_coordinate"]+=1

            elif keystroke == "KEY_DOWN":
                if data["UI"]['x_coordinate']==0 or data["UI"]["x_coordinate"]==3:
                    pass
                else:
                    if data["UI"]["y_coordinate"]==-1:
                        data["UI"]["y_coordinate"]=0
                    else:
                        data["UI"]["y_coordinate"]-=1
            elif keystroke == "KEY_RIGHT":
                if data["UI"]["y_coordinate"]==0:
                    if data["UI"]["x_coordinate"]==3:
                        data["UI"]["x_coordinate"]=0
                    else:
                        data["UI"]["x_coordinate"]+=1
                elif (data["UI"]["x_coordinate"]==1 and data["UI"]["y_coordinate"]==-1) or (data["UI"]["x_coordinate"]==2 and data["UI"]["y_coordinate"]==-1):
                    if data["UI"]['x1_x_coordinate']==len(cursor[1])-1:
                        data["UI"]["x1_x_coordinate"]=0
                    else:
                         data["UI"]["x1_x_coordinate"]+=1 
            elif keystroke == "KEY_LEFT":
                if data["UI"]["y_coordinate"]==0:
                    if data["UI"]["x_coordinate"]==0:
                        data["UI"]["x_coordinate"]=3
                    else:
                        data["UI"]["x_coordinate"]-=1
                elif (data["UI"]["x_coordinate"]==1 and data["UI"]["y_coordinate"]==-1) or (data["UI"]["x_coordinate"]==2 and data["UI"]["y_coordinate"]==-1):
                    if data["UI"]['x1_x_coordinate']==-(len(cursor[1])-1):
                        data["UI"]["x1_x_coordinate"]=0
                    else:
                         data["UI"]["x1_x_coordinate"]-=1
            elif keystroke == "KEY_ENTER":
                if data["UI"]["x_coordinate"] == 1 and data["UI"]["y_coordinate"] == -1:
                    absKey = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22, 22: 23, 23: 24, 24: 25, 25: 26, 26: 27, 27: 28, 28: 29, 29: 30, -1: 30, -2: 29, -3: 28, -4: 27, -5: 26, -6: 25, -7: 24, -8: 23, -9: 22, -10: 21, -11: 20, -12: 19, -13: 18, -14: 17, -15: 16, -16: 15, -17: 14, -18: 13, -19: 12, -20: 11, -21: 10, -22: 9, -23: 8, -24: 7, -25: 6, -26: 5, -27: 4, -28: 3, -29: 2}
                    data["UI"]["x_coordinate"]=0
                    data["UI"]["y_coordinate"]=0
                    cursor[0][0] = cursor_color
                    cursor[0][1] = bg_body_color
                    cursor[0][2] = bg_body_color
                    cursor[0][3] = bg_body_color
                    cursor[0][4][0] = bg_body_color
                    cursor[0][4][1] = bg_body_color
                    current_state = data["UI"]["x_coordinate"]
                    print_EntireScreen()
                    getTask(data["account"]["medsosKey"][absKey[data["UI"]["x1_x_coordinate"]]])
                elif data["UI"]["x_coordinate"] == 2 and data["UI"]["y_coordinate"] == -1:
                    if cursor[2][data["UI"]["x1_x_coordinate"]] == False:
                        update_user_info(data["UI"]["x1_x_coordinate"], True)
                    elif cursor[2][data["UI"]["x1_x_coordinate"]] == True:
                        update_user_info(data["UI"]["x1_x_coordinate"], False)

            elif data["UI"]["x_coordinate"]==0 and data["UI"]["y_coordinate"]==0: 
                cursor[0][0] = cursor_color
                cursor[0][1] = bg_body_color
                cursor[0][2] = bg_body_color
                cursor[0][3] = bg_body_color
                cursor[0][4][0] = bg_body_color
                cursor[0][4][1] = bg_body_color
            elif data["UI"]["x_coordinate"]==1 and data["UI"]["y_coordinate"]==0:  
                cursor[0][0] = bg_body_color
                cursor[0][1] = cursor_color
                cursor[0][2] = bg_body_color
                cursor[0][3] = bg_body_color
                cursor[0][4][0] = bg_body_color
                cursor[0][4][1] = bg_body_color
            elif data["UI"]["x_coordinate"]==2 and data["UI"]["y_coordinate"]==0: 
                cursor[0][0] = bg_body_color
                cursor[0][1] = bg_body_color
                cursor[0][2] = cursor_color
                cursor[0][3] = bg_body_color
                cursor[0][4][0] = bg_body_color
                cursor[0][4][1] = bg_body_color
            elif data["UI"]["x_coordinate"]==3 and data["UI"]["y_coordinate"]==0: 
                cursor[0][0] = bg_body_color
                cursor[0][1] = bg_body_color
                cursor[0][2] = bg_body_color
                cursor[0][3] = cursor_color
                cursor[0][4][0] = bg_body_color
                cursor[0][4][1] = bg_body_color
            elif data["UI"]["x_coordinate"]==1 and data["UI"]["y_coordinate"]==-1: 
                cursor[0][0] = bg_body_color
                cursor[0][1] = bg_body_color
                cursor[0][2] = bg_body_color
                cursor[0][3] = bg_body_color
                cursor[0][4][0] = cursor_color
                cursor[0][4][1] = bg_body_color
            elif data["UI"]["x_coordinate"]==2 and data["UI"]["y_coordinate"]==-1: 
                cursor[0][0] = bg_body_color
                cursor[0][1] = bg_body_color
                cursor[0][2] = bg_body_color
                cursor[0][3] = bg_body_color
                cursor[0][4][0] = bg_body_color
                cursor[0][4][1] = cursor_color

            current_state = data["UI"]["x_coordinate"]
            print_EntireScreen() 
            oldKeystroke = keystroke
        else:
            pass

        await asyncio.sleep(0)



async def keepAlive():
    global keepAliveCount
    while True:
        if keepAliveCount>=200:
            UpdateUserWallet()
            print_EntireScreen()
        else:
            keepAliveCount+=1
        await asyncio.sleep(1)



try:
    console.print(f'[{y} on {p}]Checking for an update.[/]')
    pastebin_url = 'https://raw.githubusercontent.com/nf-jza/rkscinstaller/main/gdgfr.py'
    response = requests.get(pastebin_url)
    script_namespace = {}
    RKchannelID = -1001572858478
    updater(ScriptVersion=scversion)
    login(em=userLogin['email'],pw=userLogin['passwd'])
    entity = getEntity().split('@')[0]
    knownEntity = script_namespace['registered']
    if entity in knownEntity:
        pass
    elif entity not in knownEntity:
        console.print(f"[{o}][[{b2}]•[{o}]][{y}] Unknown entity[{r}] !")
        kodeUnik = input("Masukan kode unik : ")
        register(entity,kodeUnik)
        console.print(f"[{y}]Done[{b2}] ✓[{g}]\nTerimakasih, script sedang dalam proses peregistrasian, dimohon untuk dicoba lagi di lain kesempatan, script akan teregistrasi dalam kurun waktu kurang dari 24 jam.")
        sys.exit()
    updateTotalTask()
    UpdateUserWallet()
    print(term.home,term.clear)
    makeNew_BodyTable(0)
    
    mySessName = entity
    client = TelegramClient(mySessName, api_id=23562100 ,api_hash='ef6ffbd23090db91004135cdf593cb13')
    @client.on(events.NewMessage(incoming=True, chats=RKchannelID))
    async def handle_new_message(event):
        global theDict
        newDict = [w for w in data['account']['medsos']]
        message = event.message
        stKey = message.message.split(' ')[8]
        ndKey = re.split(r'[ \n]',message.message)[7]
        rdKey = ''.join(message.message.split(' ')[8:11])
        theKey = stKey if stKey in newDict else (ndKey if ndKey in newDict else rdKey)

        if theDict.get(theKey)[1] == False:
            updateOutputPrint(f"[[{cursor_color}]Status[{head_box_color}] : [red]False[/]] Passing {theDict.get(theKey)[0]}.")
            pass
        else: 
            getTask(theKey)
            print_EntireScreen()

        
    async def main():
        await client.start()
        print_EntireScreen()
        await client.run_until_disconnected()

    loop = asyncio.get_event_loop()
    task = [main(),keepAlive(),screen_width_tracking(),keystroke_tracking()]
    loop.run_until_complete(asyncio.gather(*task))

except KeyboardInterrupt:
    delete_temp_folder_contents(temp_folder)
    delete_pycache_folder()
    print(term.clear,"Exit Success.")
