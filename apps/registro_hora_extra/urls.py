from django.urls import path, include
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraNovo

urlpatterns = [

    path('', HoraExtraList.as_view(), name='list_hora_estra'),
    path('novo/', HoraExtraNovo.as_view(), name='create_hora_estra'),
    path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_estra'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(),
        name='delete_hora_estra'),
]
