# coding=utf-8
import requests
from bs4 import BeautifulSoup

class spider(object):
    def __init__(self, url):
        self.url=url

    def prime_time(self, c):
        '''
        黄金档
        :return: 
        '''
        soup = self.get_soup()
        i = 0
        prime_time_dict = dict()
        prime_time_list = list()
        imgs = soup.select('div#m_86821 div.yk-row div.yk-col4 div.v-thumb img')  # 图片
        Title_Hrefs = soup.select('div#m_86821 div.yk-row div.yk-col4 div.v-link a')  # 播放视频链接+剧名
        infos = soup.select('div#m_86821 div.yk-row div.yk-col4 div.v-meta.va div.v-meta-entry a')#简介
        for img in imgs:
            prime_time_dict['img'] = imgs[i]['_src']  # 图片
            prime_time_dict['title'] = Title_Hrefs[i]['title']  # 剧名
            html = requests.get(Title_Hrefs[i]['href'])
            html.encoding = 'utf-8'  # 中文编码
            soup1 = BeautifulSoup(html.text, 'html.parser')  # 解析网页
            links = soup1.select('div.p1 div:nth-of-type(4) input')
            prime_time_dict['link'] = links[0]['value']  # 播放链接
            prime_time_dict['info'] = infos[i].get_text()#简介
            prime_time_list.append(prime_time_dict.copy())
            i=i+1
        print prime_time_list


    def online_teleplay(self):
        '''
        超级网剧
        :return: 
        '''
        soup = soup = self.get_soup()
        i = 0
        online_teleplay_dict = dict()
        online_teleplay_list = list()
        imgs = soup.select('div#m_86869 div.yk-row.yk-tv-index-7 div.yk-w970-col12.yk-w1190-col16 div.v-thumb img')  # 图片
        infos1 = soup.select('div#m_86869 div.yk-row.yk-tv-index-7 div.yk-w970-col12.yk-w1190-col16 div.v-meta.vb div.v-meta-entry span')
        infos2 = soup.select('div#m_86869 div.yk-row.yk-tv-index-7 div.yk-w970-col12.yk-w1190-col16 div.v-meta.vb div.v-meta-entry span.v-num')  # 简介
        for infos in infos2:  # infos1-infos2
            v = infos
            infos1.remove(v)
        Title_Href = soup.select('div#m_86869 div.yk-row.yk-tv-index-7 div.yk-w970-col12.yk-w1190-col16 div.v-link a')  # 播放视频链接+剧名
        for title in Title_Href:
            online_teleplay_dict['img'] = imgs[i]['_src']  # 图片
            online_teleplay_dict['title'] = Title_Href[i]['title']  # 剧名
            html = requests.get(Title_Href[i]['href'])
            html.encoding = 'utf-8'  # 中文编码
            soup1 = BeautifulSoup(html.text, 'html.parser')  # 解析网页
            links = soup1.select('div.p1 div:nth-of-type(4) input')
            online_teleplay_dict['link'] = links[0]['value']  # 播放链接
            online_teleplay_dict['info'] = infos1[i].get_text()  # 简介
            online_teleplay_list.append(online_teleplay_dict.copy())
            i = i + 1
        print online_teleplay_list

    def exclusive_planning(self):
        '''独家策划'''
        html = requests.get(self.url)  # 获取网页
        html.encoding = 'utf-8'  # 中文编码
        soup = BeautifulSoup(html.text, 'html.parser')  # 解析网页
        i = 0
        exclusive_planning_dict = dict()
        exclusive_planning_list = list()
        imgs = soup.select('div#m_86905 div.yk-w970-col12.yk-w1190-col16 div.v-thumb img')  # 图片
        Title_Hrefs = soup.select('div#m_86905 div.yk-w970-col12.yk-w1190-col16 div.v-link a')  # 播放视频链接+剧名
        infos = soup.select('div#m_86905 div.yk-w970-col12.yk-w1190-col16 div.v-meta-entry span')  # 简介
        for img in imgs:
            exclusive_planning_dict['img'] = imgs[i]['_src']  # 图片
            exclusive_planning_dict['title'] = Title_Hrefs[i]['title']  # 剧名
            html = requests.get(Title_Hrefs[i]['href'])
            html.encoding = 'utf-8'  # 中文编码
            soup1 = BeautifulSoup(html.text, 'html.parser')  # 解析网页
            links = soup1.select('div.p1 div:nth-of-type(4) input')
            exclusive_planning_dict['link'] = links[0]['value']  # 播放链接
            exclusive_planning_dict['info'] = infos[i].get_text()#简介
            exclusive_planning_list.append(exclusive_planning_dict.copy())
            i=i+1
        print exclusive_planning_list

    def get_soup(self):
        html = requests.get(self.url)#获取网页
        html.encoding = 'utf-8'  #中文编码
        soup = BeautifulSoup(html.text, 'html.parser')  # 解析网页
        return soup

if __name__ == '__main__':
    a = spider('http://tv.youku.com/')
    a.prime_time()
    a.online_teleplay()
    a.exclusive_planning()