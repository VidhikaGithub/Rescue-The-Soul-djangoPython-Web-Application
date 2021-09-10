from django.urls import path,include
from . import views
app_name='soul'

urlpatterns=[
    path('home/',views.homepage,name="homepage"),
    #path('try/',views.tr,name="try"),
    path('login/',views.check_login,name='login'),
    #path('log/',views.log,name='log'),
    path('register/',views.register,name='register'),
    path('forgot/', views.forgot, name='forgot'),
    path('forgotPage/', views.forgotPage, name='forgotPage'),
    path('ngoConsultation/',views.ngoConsultation, name='ngoConsultation'),
    path('vetConsultation/',views.vetConsultation, name='vetConsultation'),
    path('login_render/',views.login_render, name='login_render'),
    path('contacts/',views.contacts, name='contacts'),
    path('donate/',views.donate,name='donate'),
    path('success/',views.success,name='success'),
    path('petfinder/',views.petfinder,name='petfinder'),
    path('app/',views.app,name='app'),
    path('share/',views.share,name='share'),
    path('petfinderform/',views.petfinderform,name='petfinderform'),
    path('logout/',views.logout, name='logout'),
    path('changePassword/',views.changePassword, name='changePassword'),
    path('update/',views.update, name='update'),
    path('check_login/',views.check_login, name='check_login'),
]