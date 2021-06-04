from django.contrib import admin
from django.urls import path
import crudApp.views # crudApp 폴더의 views.py를 참고

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudApp.views.main, name='main'), # runserver 하자마자 보이는 페이지
    path('detail/<str:id>', crudApp.views.detail, name='detail'),
    path('read/', crudApp.views.read, name = 'read'),
    path('new/create/', crudApp.views.create, name='create'),
    path('edit/<str:id>', crudApp.views.edit, name='edit'),
    path('delete/<str:id>', crudApp.views.delete, name='delete'),
]# <str:id> : 특정 게시물을 가져오는 것이기 때문에 id를 지정