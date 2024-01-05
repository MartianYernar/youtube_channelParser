import requests
from bs4 import BeautifulSoup
import json

cookies = {
    'VISITOR_INFO1_LIVE': 'PHVJvzgafXc',
    'VISITOR_PRIVACY_METADATA': 'CgJLWhIEGgAgEA%3D%3D',
    '__Secure-1PSIDTS': 'sidts-CjEBPVxjSrRIlEZvzngda2HEPUNHAI3lUFRcNoNbhOB-uuKlGqRGCNWe2lHqeIzZ34wfEAA',
    '__Secure-3PSIDTS': 'sidts-CjEBPVxjSrRIlEZvzngda2HEPUNHAI3lUFRcNoNbhOB-uuKlGqRGCNWe2lHqeIzZ34wfEAA',
    'HSID': 'ALNib1XeryqlKGK4j',
    'SSID': 'ALOtIWBH326AMTpRY',
    'APISID': 'AF9Yr18Z1F4RN3X6/AsixaFJZ5y1U5Xe6o',
    'SAPISID': '7kxSPYshnEDkH8zV/AElQUbvjy4vgIllmT',
    '__Secure-1PAPISID': '7kxSPYshnEDkH8zV/AElQUbvjy4vgIllmT',
    '__Secure-3PAPISID': '7kxSPYshnEDkH8zV/AElQUbvjy4vgIllmT',
    'SID': 'eghfVdAg7hsri9JExZCVjJeYsPREF6Y66lf49InjfcJy1bla12eyvK6Bob6fLpFV3fcC4Q.',
    '__Secure-1PSID': 'eghfVdAg7hsri9JExZCVjJeYsPREF6Y66lf49InjfcJy1blaaGsevxShECw-U2bcpNYhiA.',
    '__Secure-3PSID': 'eghfVdAg7hsri9JExZCVjJeYsPREF6Y66lf49InjfcJy1blaeR0zhfz0Dd4_UPIaKHCTnQ.',
    'LOGIN_INFO': 'AFmmF2swRgIhAJl80OjKMiyVKS2blpytxNZ0jbmZQ9Y3VVtgcrOiKzYnAiEA2BkpPrDucFYxR7JP2VK1Nu4NwXwWNDXVgYwf53h-9-o:QUQ3MjNmeXRiRGhMWkswdjNNRTMzMXhDMTdhVjJkc2RCa2JuWURCbUVqamltcVEtODlRUURfZUV2VjdmLWduMzhPcnJ2Y2ZGTVRUcHJoMkY2MGstdTdHSy1CV25MMktLZjJJenQzdHFOWmFKOFRBckp5ZTltajk1a1hnVU1BaUVQQVQ5M3VyY2pBSGpETElnMnhBMHZ3WTFUekRvVVFka0N3',
    'PREF': 'f6=40000000&tz=Asia.Almaty&f5=20000&f7=100&f4=4000000',
    'YSC': 'XEa4hYHgwcU',
    'SIDCC': 'ABTWhQHUPJHsaQpgS2FrVx_UdmI_KbjHyxWQOwX6OQd-ckseq_f8T9biEDx1eoBKEex9NNhtbMM',
    '__Secure-1PSIDCC': 'ABTWhQEgfg5RNMnllRyweJMRqvqKcyyMirxINyEVrZXOzs1rQ2B1r2uFQX4A5cFLedOW03FMpTQ',
    '__Secure-3PSIDCC': 'ABTWhQHCXrMCtFIrYyBqEJY5hom5asoqEuEQo2dTU1INdN4jbniyrbpTFmYQWBI8P47c3mV7PgHt',
}

headers = {
    'authority': 'www.youtube.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-GB;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'VISITOR_INFO1_LIVE=PHVJvzgafXc; VISITOR_PRIVACY_METADATA=CgJLWhIEGgAgEA%3D%3D; __Secure-1PSIDTS=sidts-CjEBPVxjSrRIlEZvzngda2HEPUNHAI3lUFRcNoNbhOB-uuKlGqRGCNWe2lHqeIzZ34wfEAA; __Secure-3PSIDTS=sidts-CjEBPVxjSrRIlEZvzngda2HEPUNHAI3lUFRcNoNbhOB-uuKlGqRGCNWe2lHqeIzZ34wfEAA; HSID=ALNib1XeryqlKGK4j; SSID=ALOtIWBH326AMTpRY; APISID=AF9Yr18Z1F4RN3X6/AsixaFJZ5y1U5Xe6o; SAPISID=7kxSPYshnEDkH8zV/AElQUbvjy4vgIllmT; __Secure-1PAPISID=7kxSPYshnEDkH8zV/AElQUbvjy4vgIllmT; __Secure-3PAPISID=7kxSPYshnEDkH8zV/AElQUbvjy4vgIllmT; SID=eghfVdAg7hsri9JExZCVjJeYsPREF6Y66lf49InjfcJy1bla12eyvK6Bob6fLpFV3fcC4Q.; __Secure-1PSID=eghfVdAg7hsri9JExZCVjJeYsPREF6Y66lf49InjfcJy1blaaGsevxShECw-U2bcpNYhiA.; __Secure-3PSID=eghfVdAg7hsri9JExZCVjJeYsPREF6Y66lf49InjfcJy1blaeR0zhfz0Dd4_UPIaKHCTnQ.; LOGIN_INFO=AFmmF2swRgIhAJl80OjKMiyVKS2blpytxNZ0jbmZQ9Y3VVtgcrOiKzYnAiEA2BkpPrDucFYxR7JP2VK1Nu4NwXwWNDXVgYwf53h-9-o:QUQ3MjNmeXRiRGhMWkswdjNNRTMzMXhDMTdhVjJkc2RCa2JuWURCbUVqamltcVEtODlRUURfZUV2VjdmLWduMzhPcnJ2Y2ZGTVRUcHJoMkY2MGstdTdHSy1CV25MMktLZjJJenQzdHFOWmFKOFRBckp5ZTltajk1a1hnVU1BaUVQQVQ5M3VyY2pBSGpETElnMnhBMHZ3WTFUekRvVVFka0N3; PREF=f6=40000000&tz=Asia.Almaty&f5=20000&f7=100&f4=4000000; YSC=XEa4hYHgwcU; SIDCC=ABTWhQHUPJHsaQpgS2FrVx_UdmI_KbjHyxWQOwX6OQd-ckseq_f8T9biEDx1eoBKEex9NNhtbMM; __Secure-1PSIDCC=ABTWhQEgfg5RNMnllRyweJMRqvqKcyyMirxINyEVrZXOzs1rQ2B1r2uFQX4A5cFLedOW03FMpTQ; __Secure-3PSIDCC=ABTWhQHCXrMCtFIrYyBqEJY5hom5asoqEuEQo2dTU1INdN4jbniyrbpTFmYQWBI8P47c3mV7PgHt',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"120.0.6099.130"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.130", "Google Chrome";v="120.0.6099.130"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'service-worker-navigation-preload': 'true',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-client-data': 'CJG2yQEIorbJAQipncoBCMf/ygEIlaHLAQi   FoM0BCI2nzQEI3L3NAQiO4c0BCNTpzQEIou7NAQiD8M0BCIXwzQEYyeHNARin6s0BGLDvzQE=',
}
# link = str(input('Link: '))
link = 'https://www.youtube.com/@Apple/videos'

response = requests.get(link, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser') 

json_data1 = soup.find_all('script')[35].text.strip()[20:-1]


data = json.loads(json_data1)
all_titles = []
for i in range(10): # getting the title of ten last videos that was uploaded by certain channel
    all_titles.append(data['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['richGridRenderer']['contents'][i]['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text'])

a = 1
for i in all_titles:
    print(f"{a}. {i}")
    a += 1



