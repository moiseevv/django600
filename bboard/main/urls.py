from django.urls import path
from .views import BBLoginView
from .views import BBLogoutView
from .views import profile

from .views import index, other_page

app_name = 'main'
urlpatterns = [
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name = 'login'),
    path('<str:page>/',other_page, name='other'),
    path('', index, name='index'),
]