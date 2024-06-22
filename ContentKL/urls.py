from django.urls import path
from . import views
urlpatterns=[
    
    path("",views.home,name='home'), 
 
    path('signup',views.signup,name='signup'),
    path('login',views.login, name='login'),
    path('logout',views.logout,name='logout'),
    path("subject",views.courses,name="subjects"),
    path('<str:sub>',views.topic,name='topics'),
    path("subtopic/<str:pk>",views.subtopics,name="subtopic"),
    path('<str:sometext>/next/<str:pk>',views.nextpage,name='nextpage'),
    path('<str:somestring>/previous/<str:pk>',views.previouspage,name='previouspage'),
    path('<str:something>/this_subtopic/<str:pk>',views.sidebar,name='sidebar'),
    
   
]