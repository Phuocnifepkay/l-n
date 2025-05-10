#mở source code
import time, os, requests, json, random, bs4
from rich.text import Text as tekz
from rich.panel import Panel as nel
from rich.panel import Panel
from rich.console import Console
xyz = requests.Session()
def logo():
  ban = """[green] Phuoc Coder [white]
╔═╗╔╗╔╔═╗╔═╗╔╦╗╦╦╔═  
╚═╗║║║╠═╣╠═╝ ║ ║╠╩╗  
╚═╝╝╚╝╩ ╩╩   ╩ ╩╩ ╩ """
  Console(width=50).print(Panel(ban,style='bold black'),justify='center')
  lol = """[white] Nhập link video muốn tải !!!"""
  Console(width=50).print(Panel(lol,style='bold black'),justify='center')
path = "/storage/emulated/0/Download"
try:
        os.mkdir(path)
except:
        pass
class Main:
	def __init__(self):
		pass
	def dow_tt(self, tk_vid, id_vid, nama_vid):
		nm_vid = f"tiktok_download_{nama_vid}"
		try:
			print (f' [•]Đang tải video từ link,hãy chờ 1 chút....')
			run = xyz.get(f'https://tikmate.app/download/{tk_vid}/{id_vid}.mp4?hd=1').content
			with open(f"{path}/{nm_vid}.mp4", "wb") as sv:
				sv.write(run)
				print (f' [•] Lưu thành công vào : {path}/{nm_vid}.mp4')
		except KeyError:
			exit(f' link video lỗi!')
	def get_dat(self, url):
		data = {"url": url}
		try:
			data = requests.post('https://api.tikmate.app/api/lookup',data=data).text
			resp = json.loads(data)
			if 'true' in data:
				tk_vid = resp['token']
				id_vid = resp['id']
				at_vid = resp['author_name']
				tll_up_vid = resp['create_time']
				print (f' [•] Chủ Video : {at_vid}')
				print (f' [•] Id Video       : {id_vid}')
				print (f' [•] Ngày đăng video : {tll_up_vid}')
				dwon = input(f' [?] Bạn muốn tải video? (Có/không): ')
				if dwon in ['Có','có']:
					nama_vid = input(f' [!] Nhập tên để lưu video theo tên bạn đã nhập : ')
					self.dow_tt(tk_vid, id_vid, nama_vid)
				else:
					exit(f' daubuoi!!!...')
			else:
				exit(f'Link không hợp lệ')
		except KeyError:
			exit(f'Link không hợp lệ')
	def mulai(self):
		os.system("clear")
		logo()
		url = input(f' [!] Link : ')
		if url in ['']:
			exit(f' Không tìm thấy liên kết!!' )
		else:
			self.get_dat(url)
Main().mulai()
