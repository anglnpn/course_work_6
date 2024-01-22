
from django.urls import path


from main.apps import MainConfig
from main.views import UserProfileListView, UserProfileDetailView, like_view

app_name = MainConfig.name

urlpatterns = [
    path('', UserProfileListView.as_view(), name='main'),
    path('main/like/', like_view, name='like_view'),
    path('profile_view/<int:pk>', UserProfileDetailView.as_view(), name='profile_view'),


]

