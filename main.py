import requests, random, os
from pystyle import *

class Checker:
    def __init__(self):
        self.valid = 0
        self.invalid = 0

        proxie_list = []
        with open("proxies.txt", "r") as f:                   
          for proxy in f.readlines():
            proxie_list.append(proxy.replace("\n", ""))
            self.proxies = {
                'https://': random.choice(proxie_list)
            }

    def checker(self):
        ssid = input("Enter sessionID: ")
        while True:
            os.system('cls')
            os.system(f"title Made by Sokisa#1382 ^| Valid: {self.valid} ^| Invalid: {self.invalid}")
            usernamed = open("users.txt")
            user = random.choice(usernamed.read().splitlines())
            usernamed.close()
            os.system('cls')

        #COOKIES
            cookies = {
        'sessionid': f'{ssid}',
            }
        #HEADERS
            headers = {
        'authority': 'www.tiktok.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
            }
        # PARAMS
            params = {
        'aid': '1988',
        'app_language': 'en',
        'app_name': 'tiktok_web',
        'battery_info': '1',
        'browser_language': 'en-US',
        'browser_name': 'Mozilla',
        'browser_online': 'true',
        'browser_platform': 'Win32',
        'browser_version': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
        'channel': 'tiktok_web',
        'cookie_enabled': 'true',
        'device_id': '7102861260652692998',
        'device_platform': 'web_pc',
        'focus_state': 'true',
        'from_page': 'user',
        'history_len': '3',
        'is_fullscreen': 'false',
        'is_page_visible': 'true',
        'os': 'windows',
        'priority_region': 'BE',
        'referer': '',
        'region': 'BE',
        'screen_height': '1080',
        'screen_width': '1920',
        'tz_name': 'Europe/Brussels',
        'unique_id': f'{user}',
        'webcast_language': 'en',
        'msToken': 'nTSQ3aga4re71sf6jxx7S00JXIPzeg-4sHemEVntF8SXluh5obYrch86ZH9wTvRCumbcXrx8snSk15zGwDB81VW55SD0v1psJ_51k1InI8qxCtUe0mKMF2jaKfi00MVSctUpG6c1',
        'X-Bogus': 'DFSzswVLYlTANyxdSMSB0sXyYJWn',
        '_signature': '_02B4Z6wo00001Qz7WXAAAIDAL1p33MaqfyEM-13AACB3bc',
            }
            r = requests.get('https://www.tiktok.com/api/uniqueid/check/', params=params, cookies=cookies, headers=headers, proxies=self.proxies)
            if r.json()['status_code'] == 0:
                Write.Print(f"{user} AVAILABLE", Colors.green_to_cyan)

            if r.json()['status_code'] == 3249:
                Write.Print(f"{user} TAKEN/BANNED", Colors.red_to_purple)

Checker().checker()

