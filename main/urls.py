
from django.urls import path

from main.apps import MainConfig
from main.views import UserProfileListView, UserProfileDetailView, administrative_panel, like_view, BlogListView


app_name = MainConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='main'),
    path('skylove_list_view/', UserProfileListView.as_view(), name='skylove_list_view'),
    path('main/like/', like_view, name='like_view'),
    path('administrative_panel/', administrative_panel, name='administrative_panel'),
    path('profile_view/<int:pk>', UserProfileDetailView.as_view(), name='profile_view'),

]

