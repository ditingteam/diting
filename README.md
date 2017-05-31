# diting
a website

项目结构如下：</br>
- ./app
    存放后台程序，下面是已经放到里面的（肯定不全，所有东西都是空的）</br>
- __init__.py 初始化脚本

- models.py 数据库表有关数据结构
- ./app/main/errors.py 错误页面的路由，404之类的
- ./app/main/forms.py 表单有关数据结构
- ./app/main/views.py 视图，也就是页面跳转的处理部分
- ./user  用户有关部分页面
- ./app/static 静态资源存放的文件夹（还没建），网站logo之类的
- ./app/templates 模板文件夹，前端网页基本都在这里
- ./tmp 临时文件
- ./tests 测试
- config.py 网站初始化数据，例如数据库连接用到的用户名密码之类的设置
- manage.py 运行网站的脚本

- 依赖库和虚拟环境使用方法：打开pycharm的settings，选择project.diting->第一个->点右面的解释器，下面有一个show all，弹出窗口
    点击绿色的+,新建一个2.7的虚拟环境，然后安装requirments.txt的包

- 安装新的包：选择解释器的页面点右面的+，然后搜索自己要的包

- **运行方法**
</br>正常运行-> runserver
</br>运行测试-> test
</br>创建数据库 db init 创建迁移 db migrate -m "更新信息"  更新数据库 db upgrade
run->edit config... 在里面把这些命令打进去就好了