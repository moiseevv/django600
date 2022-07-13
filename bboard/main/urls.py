from django.urls import path
from .views import BBLoginView
from .views import BBLogoutView
from .views import profile
from .views import ChangeUserInfoView
from .views import BBPaswordChangeView
from .views import RegisterDoneView, RegisterUserView
from .views import user_activate
from .views import DeleteUserView

from .views import index, other_page

app_name = 'main'
urlpatterns = [
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(), name = 'register_done'),
    path('accoount/register/', RegisterUserView.as_view(), name= 'register'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name = 'profile_change'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', BBPaswordChangeView.as_view(), name = 'password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name = 'login'),
    path('<str:page>/',other_page, name='other'),
    path('', index, name='index'),
]