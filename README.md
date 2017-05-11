# diting
a website

项目结构如下：
./app
存放后台程序，下面是已经放到里面的（肯定不全，所有东西都是空的）
__init__.py 初始化脚本
db_....py 数据库有关操作，create是创建数据库,migrate是更新数据库
forms.py 表单有关数据结构
models.py 数据库表有关数据结构
views.py 视图，也就是页面跳转的处理部分
./app/static 静态资源存放的文件夹（还没建），网站logo之类的
./app/templates 模板文件夹，前端网页基本都在这里
./flask 依赖库和虚拟环境
./tmp 临时文件
config.py 网站初始化数据，例如数据库连接用到的用户名密码之类的设置
run.py 运行网站的脚本

依赖库和虚拟环境使用方法：打开pycharm的settings，选择project.diting->第一个->点右面的解释器，下面有一个show all，弹出窗口
点击绿色的+,add local，找到本项目目录，进入flask/diting/scripts，找到python.exe，点击确定。

安装新的包：选择解释器的页面点右面的+，然后搜索自己要的包，这个安装不会影响自己本机安装的python环境，安装以后记得在git推送上去，
然后告诉我。