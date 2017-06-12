# -*- coding: utf-8 -*-
from app.spider.Ver2 import spider
from app.models import *


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
            image =data_sall.get('image')
            title =data_sall.get('title')
            SuperDrama.query.all()
            new_drama = SuperDrama(Sid=i, Sinfo=info, Slink=link, Simg=image, Stitle=title)
            db.session.add(new_drama)
            i += 1
        data_hotlist = data.get(u'热剧榜单')
        i=0
        for data_hall in data_hotlist:
            info1 = data_hall.get('info')
            link1 = data_hall.get('link')
            image1 = data_hall.get('image')
            title1 = data_hall.get('title')
            HotList.query.all()
            new_hot = HotList(Hid=i, Hinfo=info1, Hlink=link1, Himg=image1, Htitle=title1)
            db.session.add(new_hot)
            i += 1
        data_exclusive_planning = data.get(u'独家策划')
        i=0
        for data_eall in data_exclusive_planning:
            info2 = data_eall.get('info')
            link2 = data_eall.get('link')
            image2 = data_eall.get('image')
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
            image3 = data_pall.get('image')
            title3 = data_pall.get('title')
            PeakViewingTime.query.all()
            new_peak = PeakViewingTime(Pid=i, Pinfo=info3, Plink=link3, Pimg=image3, Ptitle=title3)
            db.session.add(new_peak)
            i += 1

        db.session.commit()
        return '20143624a'
    @staticmethod
    def get_homepage(self):
        data = {}
        super_drama_all_data = SuperDrama.query.all()
        super_dramer_list=[]
        for super_drama_data in  super_drama_all_data:
            super_dramar_dict = {}
            super_dramar_dict['info'] = super_drama_data.Sinfo
            super_dramar_dict['link'] = super_drama_data.Slink
            super_dramar_dict['img'] = super_drama_data.Simg
            super_dramar_dict['title'] = super_drama_data.Stitle
            return str(super_dramar_dict)


