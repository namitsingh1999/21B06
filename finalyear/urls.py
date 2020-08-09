from django.contrib import admin
from django.urls import path
from registration import views as reg
from college import views as coll
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',reg.base , name='base'),
    path('registration/',reg.register , name='register'),
    path('index/',coll.index,name='index'),
    path('dashboard/',coll.dashboard,name='dashboard'),
    path('index/charts/',coll.charts, name = 'charts'),
    path('index/tables/',coll.tables, name = 'tables'),

    path('', auth_views.LoginView.as_view(template_name='pages/index.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/logout.html') , name='logout'),

]
