# -*- coding: utf-8 -*-
from app.spider.Ver2 import spider
from app.models import *
import json


class HomePageManagement(object):
    @staticmethod
    def init_homepage():
        my_spider = spider()
        data = my_spider.get_data()
        data_superdrama = data.get(u'超级网剧')
        i = 0
        for data_sall in data_superdrama:
            info = data_sall.get('info')
            link = data_sall.get('link')
            image =data_sall.get('img')
            title =data_sall.get('title')
            new_drama = SuperDrama(Sid=i, Sinfo=info, Slink=link, Simg=image, Stitle=title)
            db.session.add(new_drama)
            i += 1
        data_hotlist = data.get(u'热剧榜单')
        i=0
        for data_hall in data_hotlist:
            paly1 = data_hall.get('paly_times')
            link1 = data_hall.get('link')
            name1 = data_hall.get('name')
            label1 = data_hall.get('label')
            new_hot = HotList(Hid=i, Hpaly_times=paly1, Hlink=link1, Hname=name1, Hlabel=label1)
            db.session.add(new_hot)
            i += 1
        data_exclusive_planning = data.get(u'独家策划')
        i=0
        for data_eall in data_exclusive_planning:
            info2 = data_eall.get('info')
            link2 = data_eall.get('link')
            image2 = data_eall.get('img')
            title2 = data_eall.get('title')
            ExclusivePlanning.query.all()
            new_planning = ExclusivePlanning(Eid=i, Einfo=info2, Elink=link2, Eimg=image2, Etitle=title2)
            db.session.add(new_planning)
            i += 1
        data_peak_viewing_time = data.get(u'黄金档')
        i=0
        for data_pall in data_peak_viewing_time:
            info3 = data_pall.get('info')
            link3 = data_pall.get('link')
            image3 = data_pall.get('img')
            title3 = data_pall.get('title')
            new_peak = PeakViewingTime(Pid=i, Pinfo=info3, Plink=link3, Pimg=image3, Ptitle=title3)
            db.session.add(new_peak)
            i += 1
        data_exclusive_video_website = data.get(u'独家视频官网')
        i=0
        for data_exall in data_exclusive_video_website:
            info4 = data_exall.get('info')
            link4 = data_exall.get('link')
            image4 = data_exall.get('img')
            title4 = data_exall.get('title')
            new_exclusive = ExclusiveVideoWebsite(Eid=i, Einfo=info4, Elink=link4, Eimg=image4, Etitle=title4)
            db.session.add(new_exclusive)
            i += 1
        data_new_drama_trailer = data.get(u'新剧预告')
        i=0
        for data_new_all in data_new_drama_trailer:
            info5 = data_new_all.get('info')
            link5 = data_new_all.get('link')
            image5 = data_new_all.get('img')
            title5 = data_new_all.get('title')
            new_new_drama_trarker = NewDramaTrailer(Nid=i, Ninfo=info5, Nlink=link5, Nimg=image5, Ntitle=title5)
            db.session.add(new_new_drama_trarker)
            i += 1


        db.session.commit()
        return '20143624a'
    @staticmethod
    def get_homepage():
        data = {}
        super_drama_all_data = SuperDrama.query.all()
        super_dramer_list=[]
        for super_drama_data in  super_drama_all_data:
            super_dramar_dict = {}
            super_dramar_dict['info'] = super_drama_data.Sinfo
            super_dramar_dict['link'] = super_drama_data.Slink
            super_dramar_dict['img'] = super_drama_data.Simg
            super_dramar_dict['title'] = super_drama_data.Stitle
            super_dramer_list.append(super_dramar_dict)
        hot_list_all_data = HotList.query.all()
        hot_list_list=[]
        for hot_list_data in  hot_list_all_data:
            hot_list_dict = {}
            hot_list_dict['play_times'] = hot_list_data.Hpaly_times
            hot_list_dict['link'] = hot_list_data.Hlink
            hot_list_dict['name'] = hot_list_data.Hname
            hot_list_dict['label'] = hot_list_data.Hlabel
            hot_list_list.append(hot_list_dict)
        exclusive_planning_all_data = ExclusivePlanning.query.all()
        exclusive_planning_list=[]
        for exclusive_planning_data in  exclusive_planning_all_data:
            exclusive_planning_dict = {}
            exclusive_planning_dict['info'] = exclusive_planning_data.Einfo
            exclusive_planning_dict['link'] = exclusive_planning_data.Elink
            exclusive_planning_dict['img'] = exclusive_planning_data.Eimg
            exclusive_planning_dict['title'] = exclusive_planning_data.Etitle
            exclusive_planning_list.append(exclusive_planning_dict)
        peak_viewing_time_all_data = PeakViewingTime.query.all()
        peak_viewing_time_list=[]
        for peak_viewing_time_data in  peak_viewing_time_all_data:
            peak_viewing_time_dict = {}
            peak_viewing_time_dict['info'] = peak_viewing_time_data.Pinfo
            peak_viewing_time_dict['link'] = peak_viewing_time_data.Plink
            peak_viewing_time_dict['img'] = peak_viewing_time_data.Pimg
            peak_viewing_time_dict['title'] = peak_viewing_time_data.Ptitle
            peak_viewing_time_list.append(peak_viewing_time_dict)
        exclusive_video_website_all_data = ExclusiveVideoWebsite.query.all()
        exclusive_video_website_list = []
        for exclusive_video_website_data in exclusive_video_website_all_data:
            exclusive_video_website_dict = {}
            exclusive_video_website_dict['info'] = exclusive_video_website_data.Einfo
            exclusive_video_website_dict['link'] = exclusive_video_website_data.Elink
            exclusive_video_website_dict['img'] = exclusive_video_website_data.Eimg
            exclusive_video_website_dict['title'] = exclusive_video_website_data.Etitle
            exclusive_video_website_list.append(exclusive_video_website_dict)
        new_drama_trailer_all_data= NewDramaTrailer.query.all()
        new_drama_trailer_list = []
        for new_drama_trailer_data in new_drama_trailer_all_data:
            new_drama_trailer_dict = {}
            new_drama_trailer_dict['info'] = new_drama_trailer_data.Ninfo
            new_drama_trailer_dict['link'] = new_drama_trailer_data.Nlink
            new_drama_trailer_dict['img'] =new_drama_trailer_data.Nimg
            new_drama_trailer_dict['title'] = new_drama_trailer_data.Ntitle
            new_drama_trailer_list.append(new_drama_trailer_dict)
        data[u'黄金档'] = peak_viewing_time_list
        data[u'超级网剧'] = super_dramer_list
        data[u'独家策划'] = exclusive_planning_list
        data[u'热剧榜单'] = hot_list_list
        data[u'新剧预告'] = new_drama_trailer_list
        data[u'独家视频官网'] = exclusive_video_website_list
        return json.dumps(data, ensure_ascii=False)
    @staticmethod
    def upgrade():
        my_spider = spider()
        data = my_spider.get_data()
        data_superdrama = data.get(u'超级网剧')
        i = 0
        for data_sall in data_superdrama:
            info = data_sall.get('info')
            link = data_sall.get('link')
            image = data_sall.get('img')
            title = data_sall.get('title')
            db.session.query(SuperDrama).filter(SuperDrama.Sid == i).update({'Sinfo':info,
                                                                             'Slink':link,
                                                                             'Simg':image,
                                                                             'Stitle':title})
            i += 1
        data_hotlist = data.get(u'热剧榜单')
        i = 0
        for data_hall in data_hotlist:
            paly1 = data_hall.get('paly_times')
            link1 = data_hall.get('link')
            name1 = data_hall.get('name')
            label1 = data_hall.get('label')
            db.session.query(HotList).filter(HotList.Hid == i).update({'Hpaly_times': paly1,
                                                                             'Hlink': link1,
                                                                             'Hname': name1,
                                                                             'Hlabel': label1})
            i += 1
        data_exclusive_planning = data.get(u'独家策划')
        i = 0
        for data_eall in data_exclusive_planning:
            info2 = data_eall.get('info')
            link2 = data_eall.get('link')
            image2 = data_eall.get('img')
            title2 = data_eall.get('title')
            ExclusivePlanning.query.all()
            db.session.query(ExclusivePlanning).filter(ExclusivePlanning.Eid == i).update({'Einfo': info2,
                                                                       'Elink': link2,
                                                                       'Eimg': image2,
                                                                       'Etitle': title2})
            i += 1
        data_peak_viewing_time = data.get(u'黄金档')
        i = 0
        for data_pall in data_peak_viewing_time:
            info3 = data_pall.get('info')
            link3 = data_pall.get('link')
            image3 = data_pall.get('img')
            title3 = data_pall.get('title')
            db.session.query(PeakViewingTime).filter(PeakViewingTime.Pid == i).update({'Pinfo': info3,
                                                                       'Plink': link3,
                                                                       'Pimg': image3,
                                                                       'Ptitle': title3})
            i += 1
        data_exclusive_video_website = data.get(u'独家视频官网')
        i = 0
        for data_exall in data_exclusive_video_website:
            info4 = data_exall.get('info')
            link4 = data_exall.get('link')
            image4 = data_exall.get('img')
            title4 = data_exall.get('title')
            db.session.query(ExclusiveVideoWebsite).filter(ExclusiveVideoWebsite.Eid == i).update({'Einfo': info4,
                                                                       'Elink': link4,
                                                                       'Eimg': image4,
                                                                       'Etitle': title4})
            i += 1
        data_new_drama_trailer = data.get(u'新剧预告')
        i = 0
        for data_new_all in data_new_drama_trailer:
            info5 = data_new_all.get('info')
            link5 = data_new_all.get('link')
            image5 = data_new_all.get('img')
            title5 = data_new_all.get('title')
            db.session.query(NewDramaTrailer).filter(NewDramaTrailer.Nid == i).update({'Ninfo': info5,
                                                                       'Nlink': link5,
                                                                       'Nimg': image5,
                                                                       'Ntitle': title5})
            i += 1

        db.session.commit()


