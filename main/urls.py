from django.urls import path


from main.apps import MainConfig
from main.views import QuestionnaireCreateView, QuestionnaireListView, QuestionnaireDetailView, QuestionnaireUpdateView, \
    QuestionnaireDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', QuestionnaireListView.as_view(), name='main'),
    path('new_questionnaire/', QuestionnaireCreateView.as_view(), name='create_questionnaire'),
    path('profile_view/<int:pk>', QuestionnaireDetailView.as_view(), name='profile_view'),
    path('questionnaire_update/<int:pk>', QuestionnaireUpdateView.as_view(), name='questionnaire_update'),
    path('questionnaire_delete/<int:pk>', QuestionnaireDeleteView.as_view(), name='questionnaire_delete'),

]
