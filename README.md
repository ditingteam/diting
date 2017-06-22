# diting
#谛听视频网站

应用框架：
-    flask

数据库：
-    SQLAlchemy 

开发语言：
-    Python、Html、JavaScript

应用技术：
-    jQuery、Ajax、Bootstrap模板（css）、爬虫技术

开发环境：
-    PyCharm（python 2.7.13）
-    SQL server2015
    
项目结构：
- ./app 存放后台程序
- __init__.py 初始化脚本
- ./app/dataBaseBack 后台数据库管理
- ./app/main 存放html js css文件
- ./app/spider 爬虫模块
- ./user  用户有关部分页面
- ./app/static 模板文件
- ./tests 测试文件
- config.py 网站初始化数据，例如数据库连接用到的用户名密码之类的设置
- manage.py 运行网站的脚本
- models.py 数据库表有关数据结构
- 依赖库和虚拟环境使用方法：打开pycharm的settings，选择project.diting->第一个->点右面的解释器，下面有一个show all，弹出窗口
    点击绿色的+,新建一个2.7的虚拟环境，然后安装requirments.txt的包

- 安装新的包：选择解释器的页面点右面的+，然后搜索自己要的包

- **运行方法**
</br>正常运行-> runserver
</br>运行测试-> test
</br>创建数据库 db init 创建迁移 db migrate -m "更新信息"  更新数据库 db upgrade
</br>run->edit config... 在里面把这些命令打进去就好了
