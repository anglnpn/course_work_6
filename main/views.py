from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from blog.forms import BlogForm
from blog.models import Blog
from main.models import Likes
from users.models import User
# from main.models import Match
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from main.utils import record_like


class UserProfileListView(LoginRequiredMixin, ListView):
    """
    Класс для создания списка анкет
    """
    model = User
    template_name = 'main/skylove_list_view.html'
    # permission_required = 'user.view_user'


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    """
    Класс для отображения анкеты
    """

    model = User
    template_name = 'main/profile_view.html'
    # permission_required = 'user.view_user'


@csrf_exempt
@require_POST
def like_view(request):
    try:
        # Получаем id текущего пользователя
        user_id = request.user.id

        # Получаем id пользователя, которого лайкнули
        liked_user_id = request.POST.get('liked_user_id')
        print('current_user_id:', user_id)
        print('liked_user_id:', liked_user_id)

        # Вызываем функцию для записи лайка
        record_like(user_id, int(liked_user_id))

        return JsonResponse({'status': 'success'})
    except Exception as e:
        print('Error:', e)
        return JsonResponse({'status': 'error', 'message': str(e)})


def administrative_panel(request):
    return render(request, 'main/administrative_panel.html')


class BlogListView(ListView):
    """
    Класс для создания списка блоговых записей
    """
    model = Blog
    form_class = BlogForm
    template_name = 'main/index.html'
