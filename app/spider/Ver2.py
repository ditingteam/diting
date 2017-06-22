# coding=utf-8
import requests
from bs4 import BeautifulSoup
import json


class spider(object):
    def prime_time(self):
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
        infos = soup.select('div#m_86821 div.yk-row div.yk-col4 div.v-meta.va div.v-meta-entry a')  # 简介
        for img in imgs:
            prime_time_dict['img'] = imgs[i]['_src']  # 图片
            prime_time_dict['title'] = Title_Hrefs[i]['title']  # 剧名
            soup1 =self.get_soup(url=Title_Hrefs[i]['href'])
            links = soup1.select('div.p1 div:nth-of-type(4) input')
            prime_time_dict['link'] = links[0]['value']  # 播放链接
            prime_time_dict['info'] = infos[i].get_text()  # 简介
            prime_time_list.append(prime_time_dict.copy())
            i = i + 1
        return prime_time_list

    def online_teleplay(self):
        '''
        超级网剧
        :return:
        '''
        soup = self.get_soup()
        i = 0
        online_teleplay_dict = dict()
        online_teleplay_list = list()
        imgs = soup.select(
            'div#m_86869 div.yk-row.yk-tv-index-7 div.yk-w970-col12.yk-w1190-col16 div.v-thumb img')  # 图片
        infos1 = soup.select(
            'div#m_86869 div.yk-row.yk-tv-index-7 div.yk-w970-col12.yk-w1190-col16 div.v-meta.vb div.v-meta-entry span')
        infos2 = soup.select(
            'div#m_86869 div.yk-row.yk-tv-index-7 div.yk-w970-col12.yk-w1190-col16 div.v-meta.vb div.v-meta-entry span.v-num')  # 简介
        for infos in infos2:  # infos1-infos2
            v = infos
            infos1.remove(v)
        Title_Href = soup.select(
            'div#m_86869 div.yk-row.yk-tv-index-7 div.yk-w970-col12.yk-w1190-col16 div.v-link a')  # 播放视频链接+剧名
        for title in Title_Href:
            online_teleplay_dict['img'] = imgs[i]['_src']  # 图片
            online_teleplay_dict['title'] = Title_Href[i]['title']  # 剧名
            soup1 = self.get_soup(url=Title_Href[i]['href'])
            links = soup1.select('div.p1 div:nth-of-type(4) input')
            online_teleplay_dict['link'] = links[0]['value']  # 播放链接
            online_teleplay_dict['info'] = infos1[i].get_text()  # 简介
            online_teleplay_list.append(online_teleplay_dict.copy())
            i = i + 1
        return online_teleplay_list

    def exclusive_planning(self):
        '''独家策划'''
        soup = self.get_soup()
        i = 0
        exclusive_planning_dict = dict()
        exclusive_planning_list = list()
        imgs = soup.select('div#m_86905 div.yk-w970-col12.yk-w1190-col16 div.v-thumb img')  # 图片
        Title_Hrefs = soup.select('div#m_86905 div.yk-w970-col12.yk-w1190-col16 div.v-link a')  # 播放视频链接+剧名
        infos = soup.select('div#m_86905 div.yk-w970-col12.yk-w1190-col16 div.v-meta-entry span')  # 简介
        for img in imgs:
            exclusive_planning_dict['img'] = imgs[i]['_src']  # 图片
            exclusive_planning_dict['title'] = Title_Hrefs[i]['title']  # 剧名
            soup1 = self.get_soup(url=Title_Hrefs[i]['href'])
            links = soup1.select('div.p1 div:nth-of-type(4) input')
            exclusive_planning_dict['link'] = links[0]['value']  # 播放链接
            exclusive_planning_dict['info'] = infos[i].get_text()  # 简介
            exclusive_planning_list.append(exclusive_planning_dict.copy())
            i = i + 1
        return exclusive_planning_list

    def get_soup(self, url=u'http://tv.youku.com/'):
        html = requests.get(url)  # 获取网页
        html.encoding = 'utf-8'  # 中文编码
        soup = BeautifulSoup(html.text, 'html.parser')  # 解析网页
        return soup

    def search(self, key_word):
        '''

        :param key_word: 搜索的关键字
        :return:
        '''
        base_url = u'http://www.soku.com/search_video/q_'

        search_url = base_url + key_word
        soup = self.get_soup(url=search_url)
        posters = soup.select('div.s_poster')  # img,info,href
        informs = soup.select('div.s_inform')  # 剧集信息
        result = []
        for i in range(len(posters)):
            try:
                dramas = {}
                dramas['img'] = posters[i].select('div.s_target')[0].img['src']
                dramas['title'] = posters[i].select('div.s_link')[0].a['_log_title']
                dramas['info'] = informs[i].select('div.s_info p.c_dark span')[0]['data-text']
                links = []
                if len(informs[i].select('div.s_items.all.site14')) != 0:
                    all_link = informs[i].select('div.s_items.all.site14')[0]
                elif len(informs[i].select('div.s_items.gp.site14_0'))!=0:
                    all_link = informs[i].select('div.s_items.gp.site14_0')[0]
                else:
                    all_link = informs[i].select('div.s_items.site14')[0]
                for link in all_link.select('li'):
                    if not str(link.a['href']).startswith('java') and len(link.select('i.ico_partpre'))==0:
                        soup1 = self.get_soup(url=link.a['href'])
                        linkss = soup1.select('div.p1 div:nth-of-type(4) input')
                        links.append(linkss[0]['value'])  # 播放链接
                dramas['links'] = links
                result.append(dramas)
            except Exception:
                pass
        return result

    def Rank(self):
        '''
        热剧排行
        :return:
        '''
        soup = self.get_soup()
        i = 0
        rank_dict = dict()
        rank_list = list()
        infos = soup.select('div.yk-body div.item')
        info = soup.select('div.yk-body div.item span')
        for inf in info:
            rank_dict['label'] = infos[i].label.get_text()#排名
            rank_dict['name'] = infos[i].a.get_text()#剧名
            rank_dict['paly_times'] = infos[i].span.get_text()#播放量
            soup1=self.get_soup(url=infos[i].a['href'])
            links = soup1.select('div.p1 div:nth-of-type(4) input')
            rank_dict['link'] = links[0]['value']  # 播放链接
            rank_list.append(rank_dict.copy())
            i=i+1
        return rank_list

    def new_drama_preview(self):
        soup = self.get_soup()
        i = 0
        new_drama_preview_dict = dict()
        new_drama_preview_list = list()
        items = soup.select('div#m_86974 div.yk-box div.yk-body div.v.v-mini.v-horiz')
        for item in items:
            new_drama_preview_dict['img']=items[i].select('div.v-thumb')[0].img['src']#图片
            new_drama_preview_dict['title']=items[i].select('div.v-link')[0].a['title']#标题
            soup1 = self.get_soup(url=items[i].select('div.v-link')[0].a['href'])
            links = soup1.select('div.p1 div:nth-of-type(4) input')
            new_drama_preview_dict['link']=links[0]['value']#链接
            new_drama_preview_dict['info']=items[i].select('div.v-meta div.v-meta-entry')[0].get_text()#简介
            new_drama_preview_list.append(new_drama_preview_dict.copy())
            i = i + 1
        return new_drama_preview_list

    def Exclusive_video_website(self):
        '''
        独家视频官网
        :return:
        '''
        soup = self.get_soup()
        i = 0
        Exclusive_video_website_dict = dict()
        Exclusive_video_website_list = list()
        items = soup.select('div#m_86976 div.yk-box div.yk-body div.v.v-mini.v-horiz')
        for item in items:
            Exclusive_video_website_dict['img']= items[i].select('div.v-thumb')[0].img['src']#图片
            Exclusive_video_website_dict['title'] = items[i].select('div.v-link')[0].a['title']#标题
            Exclusive_video_website_dict['link'] = items[i].select('div.v-link')[0].a['href']#官网链接
            Exclusive_video_website_dict['info'] = items[i].select('div.v-meta div.v-meta-entry')[0].get_text()  # 简介
            Exclusive_video_website_list.append(Exclusive_video_website_dict.copy())
            i=i+1
        return Exclusive_video_website_list
    def Posters(self):
        soup = self.get_soup()
        str1=''
        t=0
        Exclusive_video_website_dict = dict()
        Exclusive_video_website_list = list()
        items = soup.select('div#m_86804 script')
        str=items[1].text
        for i in range(len(str)):
           if t==1:
               str1=str1+str[i]
           if str[i]=='[':
               t=1
               str1=str1+str[i]
           if str[i]==']':
               t=0

    def get_data(self):
        data = {}
        data[u'黄金档'] = self.prime_time()
        data[u'超级网剧'] = self.online_teleplay()
        data[u'独家策划'] = self.exclusive_planning()
        data[u'热剧榜单'] = self.Rank()
        data[u'新剧预告'] = self.new_drama_preview()
        data[u'独家视频官网'] = self.Exclusive_video_website()
        return data


if __name__ == '__main__':
    a = spider()
   # print json.dumps(a.get_data(), ensure_ascii=False)
    key = u'楚乔传'
    #a.search(key.decode('utf-8'))
    #print json.dumps(a.search(key.decode('utf-8')), ensure_ascii=False)
    print(a.exclusive_planning())
    data = a.search(key)

