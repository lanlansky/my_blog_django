# my_blog_django
Python3 和 Django 的一个简单博客
# 教程
https://andrew-liu.gitbooks.io/django-blog/content/
# 注意事项
* 尝试使用django-admin-bootstrap美化后台管理界面的时候，在my_blog/my_blog/setting.py中修改INSTALLED_APPS时，作者给出的是Django的写法，更高版本的写法在
  https://github.com/django-admin-bootstrap/django-admin-bootstrap
* 在my_blog/my_blog/urls.py中进行url设置的时候，作者给出的也是低版本的写法，django 1.10之后不在支持URL用字符串表示了 ，新的写法是
```pytthon
from article.views import home
urlpatterns = [ 
    url(r'^home', home),
]
```
