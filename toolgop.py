import threading, base64, os, time, re, json, random
from datetime import datetime, timedelta
from time import sleep, strftime
from bs4 import BeautifulSoup
import requests, socket, sys

try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
  import socks
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Vui Lòng Chạy Lại Tool__')
  
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

def banner():
 banner = f"""

\033[1;97mTool By: \033[1;32mPhuocCoder      \033[1;97mPhiên Bản: \033[1;32mBeta   
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36m@phuocan.9999\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/@phuocan.123
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Auto Golike    \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1 \033[1;97m: \033[1;34mTool Auto TikTok \033[1;32m[Comingsoon]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.1 \033[1;97m: \033[1;34mTool Auto Instagram \033[1;32m[Comingsoon]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Tương Tác Chéo \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.1 \033[1;97m: \033[1;34mTool TTC Facebook \033[1;32m[Comingsoon]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.2 \033[1;97m: \033[1;34mTool TTC TikTok \033[1;32m[Comingsoon]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool TraoDoiSub.com \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.1 \033[1;97m: \033[1;34mTool TDS Facebook \033[1;32m[Comingsoon]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.2 \033[1;97m: \033[1;34mTool TDS TikTok \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.3 \033[1;97m: \033[1;34mTool TDS Instagram \033[1;32m[Comingsoon]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool FB \033[1;37m     ║   ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.1 \033[1;97m: \033[1;34mTool Share Ảo FB \033[1;32m[Online]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Spam Vip \033[1;37m      ║   ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m5 \033[1;97m: \033[1;34mTool Spam sms + call♔ (Có thể bị lỗi api)\033[1;32m[Online]")
	print(f"\033[97m════════════════════════════════════════════════════════")
	chon = input('\033[1;91m┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Nhập lựa chọn mày muốn SAYGEX với Tool Lồn 🐦\033[1;97m \n\033[1;91m└─╼\033[1;91m✈ \033[1;33m : ')
	print('\033[1;39m─────────────────────────────────────────────────────────── ')
	
	if chon == '1':
		# Thành Công
		sys.exit("Tool đang bảo.trì,chx làm dc!")
	elif chon == '1.1':
		sys.exit("Tool đang bảo.trì,chx làm dc!")
	elif chon == '2.1':
		sys.exit("Tool đang bảo.trì,chx làm dc!")
	elif chon == '2.2':
		sys.exit("Tool đang bảo.trì,chx làm dc!")
	elif chon == '3.1':
		# Thanh Công
		sys.exit("Tool đang bảo.trì,chx làm dc!")
	elif chon == '3.2':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/Phuocnifepkay/PhuocAb/refs/heads/main/tdstiktokk.py?token=GHSAT0AAAAAADCYQLEVYZKDBITTQ6O7MWUG2AKROHA').text)
	elif chon == '3.3':
		# Thanh Công
		sys.exit("Tool đang bảo.trì,chx làm dc!")
	elif chon == '4.1':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/Phuocnifepkay/PhuocAb/refs/heads/main/shareaofb.py?token=GHSAT0AAAAAADCYQLEUJOVQJQEGZIMDCRNK2AMJLCQ').text)
	elif chon == '5':
		# Thanh Công
		    exec(requests.get('https://raw.githubusercontent.com/MaulanaRyM/SpaMsmS/refs/heads/master/sms.php').text)
	
	else:
		sys.exit("")
