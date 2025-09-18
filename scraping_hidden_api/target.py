import requests

product_title = []
price = []
brand = []
average_review = []
review_count = []

import pandas as pd
for i in range(0,240,24):
    cookies = {
        'TealeafAkaSid': '0OJBEc1nD24LPjAXI2i9Qv3DXOyo6X8R',
        'sapphire': '1',
        'visitorId': '01992E73AB3A0201903F60293D77D096',
        'UserLocation': '67062|11.850|75.400|KL|IN',
        '_pxvid': '9c3e5530-8d78-11f0-b170-b40b346272a2',
        'fiatsCookie': 'DSI_1945|DSN_Wichita%20NW|DSZ_67205',
        'fs_uid': '#o-221JN4-na1#c364b40c-6c58-4d1c-9476-6a19ee668af2:57a1e207-2eaa-4884-8729-f691cf18e412:1757420962674::21#/1788957002',
        'adScriptData': 'TN',
        'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiJhMjFkMDM0NC1mMGNiLTRiNzctYjA3NS1hZmYwZDZmYTdiOGEiLCJpc3MiOiJNSTYiLCJleHAiOjE3NTgyMDk0MDksImlhdCI6MTc1ODEyMzAwOSwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZm51IjpudWxsLCJlbSI6bnVsbCwicGgiOmZhbHNlLCJsZWQiOm51bGwsImx0eSI6ZmFsc2UsInN0IjoiVE4iLCJzbiI6bnVsbH19.',
        'refreshToken': '8E41QDTX1LqO534QAXVMQP4zZFc6qG4UpEOZNc5djlopK_FiFdf31rq876jJ2bB6p7wagpgHP0K8JVcs49RGuQ',
        'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJhMjFkMDM0NC1mMGNiLTRiNzctYjA3NS1hZmYwZDZmYTdiOGEiLCJpc3MiOiJNSTYiLCJleHAiOjE3NTgyMDk0MDksImlhdCI6MTc1ODEyMzAwOSwianRpIjoiVEdULmViMGE0MGY4ZjVmMzRmYTFiZmQ1MjFjN2YxNTNjOTdkLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjZkYzJjYTJjY2Y4ZWFhMjUwZTUzZDk2MGQwMWE3MDMyOGJlZmE3NzVkYWU3Y2VlOGViNzI4N2FhOTRjZDgzY2UiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.rWKUuOn1Y5Xc9fQ1kqfwKlh2qRdlL4SXljiGDw2MPvvGJwKalihga6ajAwif2YUoVYt8j1RxUQ8_p22mrY18K3t3PANGCybCui0DgesDcFYS0ZTMaC-BnlA-5BSeewFldU8knXAK-YKtjBoqifDPfIQUI906-xWrKZqrFvCbjppBFj-asYgQZFWpMUbOEp3vVZMFwAOTWiEXn681ZkJ64Uk2jI-imlKI0-c400WA078u83ShRtkG1uIej2e2Jz7osCp11q0JqSkeGaH7XMVFc61bUlEYSdQRYncVtOZQ_xelH9xW7CG5Q8yLAE9VjK5kwfsNWQorDzU4sJ5MljIwRw',
        'egsSessionId': '3ed7182c-43c1-452c-8567-bde21bdd9a6b',
        'pxcts': '332f2f72-93db-11f0-b31c-4f18f2d7d58f',
        '_fs_cd_cp_pRdRgnTnF68pCV2F': 'AbJovpAu284MsZe_CdB4RgIFHz5DEt8Mmj3ze8NF9Jre7hkfLSVON4MQR5bRI6O3sqtkCEg6hw54Ix50jQ6r5I0HIq_U7iW44CqxeCk7ynOoNE2I6fmHmygiN6huEzIe-oWnndE8NRja5pQRh3r8Xnmc2g==',
        '_px3': 'b83ae899032ad4353b2da8a0f652d6377e79acc182714979743b2a966be212ef:H2kUwtmzhnmUY89SrvdODIpApsGTnSOCg8VX2wcrPJzokFPcMTM+OkueKQc27pbIYxsoZ15zXMspWjspmRd9fg==:1000:lnIAT8K2/bwLgzoXAsSca/LgdnyGVbj6stsFNkiQ2aZ2tIci1lf9VDoyGStUgTpY5DDZlPaYfDq/pVq/jafJHVrVSeG4VAQrghSZz6cl47d2Db3tff13+E0Rgv2DC9LK77veHFdwBW+jVNa4s20bhX+dL36TypEy1zfqz9poha1+F+CCtVI+B+N+de8ZcljgGV9DnK5yGQGMMKMlPR5Qly8W7kTqqPApyLCU2uWkeKg=',
        'ffsession': '{%22sessionHash%22:%22104bd3463824081758123013187%22}',
        '_tgt_session': 'b21da4496b8b45518109905a1aa1403b.34988279611d212a01d5342945c70fd876b065f6cdc73392714cf60e3a3527d352795b5e2503688fe6652e79a28341ece73d76fd5415c64c830aa978835f096576141be91e47af717299978b52fea25a47f67ce7e89e33ee52809eb53f9234975ecc61406c8678e6c1904cf792a1a9e896c6388d9fa83d374a9321157469c854f7a50e1b8f4bb1ad7f5bc39ae0d50b1151061b5763384aa852768908446af10dfce143bd887347ae84410745a91cbc9e78683728e9dc2561d344c417edb4aff2d7bc47ddd782621398c8f0c02a97ad514d094f007aa4a6515db618557ba9e652a2.0xd238601f2297717bcb3093a2a94e7b4b9c15e3d7efdbeeba809a7e28f4e568eb',
        '__gads': 'ID=97875076b45ae915:T=1757420963:RT=1758123015:S=ALNI_Mbsl4pEvOmYhfJkkxh0JF2ogfUKsA',
        '__gpi': 'UID=00001193b0d77c53:T=1757420963:RT=1758123015:S=ALNI_MaPYGVnoiyn16FvH6nYmEdz73fLDA',
        '__eoi': 'ID=a3f7867e97ad65d4:T=1757420963:RT=1758123015:S=AA-AfjbMI8F11VpwGM8K4Pqc92DQ',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,la;q=0.7',
        'origin': 'https://www.target.com',
        'priority': 'u=1, i',
        'referer': 'https://www.target.com/s?searchTerm=smart+tv&category=0%7CAll%7Cmatchallpartial%7Call+categories&searchTermRaw=',
        'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        # 'cookie': 'TealeafAkaSid=0OJBEc1nD24LPjAXI2i9Qv3DXOyo6X8R; sapphire=1; visitorId=01992E73AB3A0201903F60293D77D096; UserLocation=67062|11.850|75.400|KL|IN; _pxvid=9c3e5530-8d78-11f0-b170-b40b346272a2; fiatsCookie=DSI_1945|DSN_Wichita%20NW|DSZ_67205; fs_uid=#o-221JN4-na1#c364b40c-6c58-4d1c-9476-6a19ee668af2:57a1e207-2eaa-4884-8729-f691cf18e412:1757420962674::21#/1788957002; adScriptData=TN; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiJhMjFkMDM0NC1mMGNiLTRiNzctYjA3NS1hZmYwZDZmYTdiOGEiLCJpc3MiOiJNSTYiLCJleHAiOjE3NTgyMDk0MDksImlhdCI6MTc1ODEyMzAwOSwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZm51IjpudWxsLCJlbSI6bnVsbCwicGgiOmZhbHNlLCJsZWQiOm51bGwsImx0eSI6ZmFsc2UsInN0IjoiVE4iLCJzbiI6bnVsbH19.; refreshToken=8E41QDTX1LqO534QAXVMQP4zZFc6qG4UpEOZNc5djlopK_FiFdf31rq876jJ2bB6p7wagpgHP0K8JVcs49RGuQ; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJhMjFkMDM0NC1mMGNiLTRiNzctYjA3NS1hZmYwZDZmYTdiOGEiLCJpc3MiOiJNSTYiLCJleHAiOjE3NTgyMDk0MDksImlhdCI6MTc1ODEyMzAwOSwianRpIjoiVEdULmViMGE0MGY4ZjVmMzRmYTFiZmQ1MjFjN2YxNTNjOTdkLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjZkYzJjYTJjY2Y4ZWFhMjUwZTUzZDk2MGQwMWE3MDMyOGJlZmE3NzVkYWU3Y2VlOGViNzI4N2FhOTRjZDgzY2UiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.rWKUuOn1Y5Xc9fQ1kqfwKlh2qRdlL4SXljiGDw2MPvvGJwKalihga6ajAwif2YUoVYt8j1RxUQ8_p22mrY18K3t3PANGCybCui0DgesDcFYS0ZTMaC-BnlA-5BSeewFldU8knXAK-YKtjBoqifDPfIQUI906-xWrKZqrFvCbjppBFj-asYgQZFWpMUbOEp3vVZMFwAOTWiEXn681ZkJ64Uk2jI-imlKI0-c400WA078u83ShRtkG1uIej2e2Jz7osCp11q0JqSkeGaH7XMVFc61bUlEYSdQRYncVtOZQ_xelH9xW7CG5Q8yLAE9VjK5kwfsNWQorDzU4sJ5MljIwRw; egsSessionId=3ed7182c-43c1-452c-8567-bde21bdd9a6b; pxcts=332f2f72-93db-11f0-b31c-4f18f2d7d58f; _fs_cd_cp_pRdRgnTnF68pCV2F=AbJovpAu284MsZe_CdB4RgIFHz5DEt8Mmj3ze8NF9Jre7hkfLSVON4MQR5bRI6O3sqtkCEg6hw54Ix50jQ6r5I0HIq_U7iW44CqxeCk7ynOoNE2I6fmHmygiN6huEzIe-oWnndE8NRja5pQRh3r8Xnmc2g==; _px3=b83ae899032ad4353b2da8a0f652d6377e79acc182714979743b2a966be212ef:H2kUwtmzhnmUY89SrvdODIpApsGTnSOCg8VX2wcrPJzokFPcMTM+OkueKQc27pbIYxsoZ15zXMspWjspmRd9fg==:1000:lnIAT8K2/bwLgzoXAsSca/LgdnyGVbj6stsFNkiQ2aZ2tIci1lf9VDoyGStUgTpY5DDZlPaYfDq/pVq/jafJHVrVSeG4VAQrghSZz6cl47d2Db3tff13+E0Rgv2DC9LK77veHFdwBW+jVNa4s20bhX+dL36TypEy1zfqz9poha1+F+CCtVI+B+N+de8ZcljgGV9DnK5yGQGMMKMlPR5Qly8W7kTqqPApyLCU2uWkeKg=; ffsession={%22sessionHash%22:%22104bd3463824081758123013187%22}; _tgt_session=b21da4496b8b45518109905a1aa1403b.34988279611d212a01d5342945c70fd876b065f6cdc73392714cf60e3a3527d352795b5e2503688fe6652e79a28341ece73d76fd5415c64c830aa978835f096576141be91e47af717299978b52fea25a47f67ce7e89e33ee52809eb53f9234975ecc61406c8678e6c1904cf792a1a9e896c6388d9fa83d374a9321157469c854f7a50e1b8f4bb1ad7f5bc39ae0d50b1151061b5763384aa852768908446af10dfce143bd887347ae84410745a91cbc9e78683728e9dc2561d344c417edb4aff2d7bc47ddd782621398c8f0c02a97ad514d094f007aa4a6515db618557ba9e652a2.0xd238601f2297717bcb3093a2a94e7b4b9c15e3d7efdbeeba809a7e28f4e568eb; __gads=ID=97875076b45ae915:T=1757420963:RT=1758123015:S=ALNI_Mbsl4pEvOmYhfJkkxh0JF2ogfUKsA; __gpi=UID=00001193b0d77c53:T=1757420963:RT=1758123015:S=ALNI_MaPYGVnoiyn16FvH6nYmEdz73fLDA; __eoi=ID=a3f7867e97ad65d4:T=1757420963:RT=1758123015:S=AA-AfjbMI8F11VpwGM8K4Pqc92DQ',
    }

    params = {
        'key': '9f36aeafbe60771e321a7cc95a78140772ab3e96',
        'channel': 'WEB',
        'count': '24',
        'default_purchasability_filter': 'true',
        'include_dmc_dmr': 'true',
        'include_sponsored': 'true',
        'include_review_summarization': 'true',
        'keyword': 'smart tv',
        'new_search': 'true',
        'offset': str(i),
        'page': '/s/smart tv',
        'platform': 'desktop',
        'pricing_store_id': '1945',
        'spellcheck': 'true',
        'store_ids': '1945,1943,1944,2448,905',
        'useragent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        'visitor_id': '01992E73AB3A0201903F60293D77D096',
        'zip': '67062',
    }

    response = requests.get(
        'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2',
        params=params,
        cookies=cookies,
        headers=headers,
    )


    result_json = response.json()

    result_items = result_json['data']['search']['products']

    for product in result_items:
        # Product_titile
        try:
            product_title.append(product['item']['product_description']['title'].replace('32&#34', ''))
        except:
            product_title.append('')
        # Price
        try:
            price.append(product['price']['current_retail'])
        except:
            price.append('')
        # Brand
        try:
            brand.append(product['item']['primary_brand']['name'])
        except:
            brand.append('')
        # Average_review
        try:
            average_review.append(product['ratings_and_reviews']['statistics']['rating']['average'])
        except:
            average_review.append('')
        # review_count
        try:
            review_count.append(product['ratings_and_reviews']['statistics']['rating']['count'])
        except:
            review_count.append('')

        target_df = pd.DataFrame(
            {'product_title': product_title, 'price': price, 'brand': brand, 'average_review': average_review,
             'review_count': review_count})

target_df.to_excel('target_multiple_pages.xlsx', index=False)