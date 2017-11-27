# ClubWeb在线社团运营

## 功能概述
1.在线报名
- 在线提交报名表单
- 发送邮件，验证邮箱
- 自动生成帐号密码
- 相关信息录入数据库
2.用户账户系统
- COOKIE登录
- 查看并更改个人信息
- 修改密码。
3.信息推送
- 基于账户信息从数据库检索
- 在管理主页推送课程，消息，任务
4.在线笔试
- 发送笔试通知信息
- 登录笔试网址，答题并提交
- 答题表单保存至数据库
5.统一批改
- 管理员登录，进入管理系统
- 随机获取答题文件并呈现
- 管理员给出并录入成绩
6.档案查询
- 面试时实时查询档案
- 管理员面试打分
7. 权限
- 管理员有最高权限对数据库信息进行修改
- 管理员对用户授权，分层次和级别


### 开发环境需求：
- Python 3.6 
- Django
如有不便请安装virtualenv


### 架构说明：
基于Django的MVT架构：
Model-View-Template
参见：https://docs.djangoproject.com/en/1.11/

ClubWeb为项目根目录，负责wsgi和应用连接配置
其余文件夹，如enroll为Django的app，即独立功能模块
- enroll 在线报名注册
- accounts 用户帐户信息管理
- exam 在线测试
- dashboard 计分板 信息通知界面
每个app模块目录中
- templates: html模版
- models.py: 数据模型
- urls.py: 控制url定向
- views.py: 视图和逻辑控制，处理请求

数据库采用Sqlite3

manage.py为Django管理文件。

### 测试-localhost
在该文件夹路径下打开cmd或者terminal
$ python manage.py runserver 运行本地Host进行测试
具体操作详见Django文档
https://docs.djangoproject.com/en/1.11/ref/django-admin/

可用登录：
User
用户名：testUser 
密码：test1234
Manager：
$ python manage.py createsuperuser
可自由创建用户，参见：
https://docs.djangoproject.com/en/1.11/topics/auth/default/

### 待实现：
- 在线测试：模型到template的映射函数
- 自动邮件发送
- UI界面的优化（目前为纯静态HTML）
- 自动化测试
