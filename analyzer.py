import re
import requests


def url_checker(url):
    global playlist
    if re.match(r'^https?:/{2}w{3}.bilibili.com/video/.{12}|^https?:/{2}b23.tv/.{7}', url):
        playlist = ['video', 'bilibili', url]
    elif re.match(r'^https?:/{2}space.bilibili.com/\d+/channel/', url):
        list_url = list_analyzer(url)
        playlist = ['list', 'bilibili'] + list_url
    elif re.match(r'^https?:/{2}v.douyin.com/\w+/|^https?:/{2}w{3}.douyin.com/video/\d+', url):
        playlist = ['video', 'tiktok', url]
    elif re.match(r'^https?:/{2}w{3}.zhihu.com/zvideo/\d+|^https?:/{2}w{3}.zhihu.com/answer/\w+\?type=video', url):
        playlist = ['video', 'zhihu', url]
    elif re.match(r'^https?:/{2}w{3}.pearvideo.com/video_\w+', url):
        playlist = ['video', 'pearvideo', url]
    else:
        playlist = ['none', 'none']
    print(playlist)


def list_analyzer(url):
    global list_url
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
        'Referer': url
    }
    mid = re.findall('bilibili.com/(\d+)/channel', url)[0]
    id = re.findall('sid=(\d+)', url)[0]
    if re.match(r'^https?:/{2}space.bilibili.com/\d+/channel/collectiondetail', url):
        list_url = f'https://api.bilibili.com/x/polymer/space/seasons_archives_list?mid={mid}&season_id={id}&sort_reverse=false&page_num=1&page_size=30'
    elif re.match(r'^https?:/{2}space.bilibili.com/\d+/channel/seriesdetail', url):
        list_url = f'https://api.bilibili.com/x/series/archives?mid={mid}&series_id={id}&only_normal=true&sort=desc&pn=1&ps=30'
    else:
        list_url = ''
    response = requests.get(list_url, headers=headers)
    json_data = response.json()
    total = json_data['data']['page']['total']
    url_list = []
    for item in range(total):
        bvid = json_data['data']['archives'][item]['bvid']
        url = f'https://www.bilibili.com/video/{bvid}'
        url_list.append(url)
    return url_list

# url = 'https://www.zhihu.com/answer/2324702803?type=video&content_id=1446832259152588800'
# url_checker(url)
