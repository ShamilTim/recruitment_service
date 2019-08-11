from django.urls import path

from rservice.views import index, sith, recruit_list, test, add_and_save, result_test, shadow_hand

urlpatterns = [
    path('', index, name='index'),
    path('sith/', sith, name='sith'),
    path('sith/<int:sith_id>/', recruit_list, name='recruit_list'),
    path('sith/shadow_hand/', shadow_hand, name='shadow_hand'),
    path('recruit/', add_and_save, name='recruit'),
    path('recruit/<int:recruit_id>/', test, name='test'),
    path('recruit/result_test/', result_test, name='result_test')
]
