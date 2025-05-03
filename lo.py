import requests
from time import sleep
import os,sys
os.system('clear')

def buff_follow_tiktok(username):
    try:
        access = requests.get('https://tikfollowers.com/free-tiktok-followers')
        session = access.cookies.get('ci_session', '')
        headers = {
            'accept': '*/*',
            'accept-language': 'vi,en;q=0.9',
            'user-agent': 'Mozilla/5.0',
            'cookie': f'ci_session={session}'
        }
        token = access.text.split("csrf_token = '")[1].split("'")[0]

        data = {"type": "follow", "q": f"@{username}", "google_token": "t", "token": token}
        search = requests.post('https://tikfollowers.com/api/free', headers=headers, json=data).json()

        if search.get('success'):
            send_data = {"google_token": "t", "token": token, "data": search['data'], "type": "follow"}
            send_follow = requests.post('https://tikfollowers.com/api/free/send', headers=headers, json=send_data).json()
            print("[FOLLOW]", send_follow.get('o', 'Gửi không thành công'))
            print("Vui lòng chờ 5d để load tài nguyên lại...")
            sleep(5)
            
        else:
            print("[FOLLOW] Gửi yêu cầu thất bại.")
    except Exception as e:
        print("[FOLLOW] Lỗi:", e)

def buff_like_tiktok(video_url):
    try:
        access = requests.get('https://tikfollowers.com/free-tiktok-like')
        session = access.cookies.get('ci_session', '')
        headers = {
            'accept': '*/*',
            'accept-language': 'vi,en;q=0.9',
            'user-agent': 'Mozilla/5.0',
            'cookie': f'ci_session={session}'
        }
        token = access.text.split("csrf_token = '")[1].split("'")[0]

        data = {"type": "like", "q": video_url, "google_token": "t", "token": token}
        search = requests.post('https://tikfollowers.com/api/free', headers=headers, json=data).json()

        if search.get('success'):
            send_data = {"google_token": "t", "token": token, "data": search['data'], "type": "like"}
            send_like = requests.post('https://tikfollowers.com/api/free/send', headers=headers, json=send_data).json()
            print("[LIKE]", send_like.get('o', 'Gửi không thành công'))
        else:
            print("[LIKE] Gửi yêu cầu thất bại.")
    except Exception as e:
        print("[LIKE] Lỗi:", e)

def buff_view_tiktok(video_url):
    try:
        access = requests.get('https://tikfollowers.com/free-tiktok-video-views')
        session = access.cookies.get('ci_session', '')
        headers = {
            'accept': '*/*',
            'accept-language': 'vi,en;q=0.9',
            'user-agent': 'Mozilla/5.0',
            'cookie': f'ci_session={session}'
        }
        token = access.text.split("csrf_token = '")[1].split("'")[0]

        data = {"type": "view", "q": video_url, "google_token": "t", "token": token}
        search = requests.post('https://tikfollowers.com/api/free', headers=headers, json=data).json()

        if search.get('success'):
            send_data = {"google_token": "t", "token": token, "data": search['data'], "type": "view"}
            send_view = requests.post('https://tikfollowers.com/api/free/send', headers=headers, json=send_data).json()
            print("[VIEW]", send_view.get('o', 'Gửi không thành công'))
        else:
            print("[VIEW] Gửi yêu cầu thất bại.")
    except Exception as e:
        print("[VIEW] Lỗi:", e)

def menu():
    print("""
 \033[1;36m██▓███ ██░ ██ █ ██ ▒█████ ▄████▄ ▄████▄ ▒█████ ▓█████▄ ▓█████ ██▀███  
\033[1;36m▓██░ ██▒▓██░ ██▒ ██ ▓██▒▒██▒ ██▒▒██▀ ▀█ ▒██▀ ▀█ ▒██▒ ██▒▒██▀ ██▌▓█ ▀ ▓██ ▒ ██▒
\033[1;36m▓██░ ██▓▒▒██▀▀██░▓██ ▒██░▒██░ ██▒▒▓█ ▄ ▒▓█ ▄ ▒██░ ██▒░██ █▌▒███ ▓██ ░▄█ ▒
\033[1;36m▒██▄█▓▒ ▒░▓█ ░██ ▓▓█ ░██░▒██ ██░▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒▒██ ██░░▓█▄ ▌▒▓█ ▄ ▒██▀▀█▄  
\033[1;36m▒██▒ ░ ░░▓█▒░██▓▒▒█████▓ ░ ████▓▒░▒ ▓███▀ ░▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒░██▓ ▒██▒
\033[1;36m▒▓▒░ ░ ░ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░▒░▒░ ░ ░▒ ▒ ░░ ░▒ ▒ ░░ ▒░▒░▒░ ▒▒▓ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
\033[1;36m░▒ ░ ▒ ░▒░ ░░░▒░ ░ ░ ░ ▒ ▒░ ░ ▒ ░ ▒ ░ ▒ ▒░ ░ ▒ ▒ ░ ░ ░ ░▒ ░ ▒░
\033[1;36m░░ ░ ░░ ░ ░░░ ░ ░ ░ ░ ░ ▒ ░ ░ ░ ░ ░ ▒ ░ ░ ░ ░ ░░ ░
         \033[1;36m ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░     
                   \033[1;36m                ░ ░ ░                      
\033[1;33m1. Buff Follow (Rd 1-15fl)
\033[1;33m2. Buff Tym (Like,có thể không lên Like)
\033[1;33m3. Buff View (Api có thể bị Lỗi)
\033[1;33m4. Buff Tất Cả (Follow + Tim + View)
\033[1;33m0. Thoát Tool
""")
    while True:
        choice = input("Chọn chức năng :")
        if choice == '1':
            username = input("Nhập Username TikTok (không @ nhé thk lồn): ")
            buff_follow_tiktok(username)
        elif choice == '2':
            link_like = input("Nhập link video TikTok để buff tym: ")
            buff_like_tiktok(link_like)
        elif choice == '3':
            link_view = input("Nhập link video TikTok để buff view: ")
            buff_view_tiktok(link_view)
        elif choice == '4':
            username = input("Nhập Username TikTok (không @ nhé thk lồn): ")
            link_like = input("Nhập link video TikTok để buff tim: ")
            link_view = input("Nhập link video TikTok để buff view: ")
            buff_follow_tiktok(username)
            buff_like_tiktok(link_like)
            buff_view_tiktok(link_view)
        elif choice == '0':
            print("Thoát tool success.")
            break
        else:
            print("Nhập lại,sai mẹ rồi!")

if __name__ == "__main__":
    menu()
