
from django.urls import path

import blog.views
import include
urlpatterns = [
    path('',blog.views.allblogs,name='allblogs'),
    path('<int:blog_id>/',blog.views.detail, name='detail')



    ]

