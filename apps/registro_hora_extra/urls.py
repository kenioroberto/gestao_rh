from django.urls import path, include
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraNovo, HoraExtraEditBase, UtilizouHoraExtra, NaoUtilizouHoraExtra, ExportaParaCSV, ExportarExcel

urlpatterns = [

    path('', HoraExtraList.as_view(), name='list_hora_estra'),
    path('novo/', HoraExtraNovo.as_view(), name='create_hora_estra'),
    path('editar-funcoonario/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_estra'),
    path('editar/<int:pk>/', HoraExtraEditBase.as_view(), name='update_hora_estra_base'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('nao-utilizou-hora-extra/<int:pk>/', NaoUtilizouHoraExtra.as_view(), name='nao_utilizou_hora_extra'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_estra'),
    path('exportar-csv', ExportaParaCSV.as_view(), name='exportar_csv'),
    path('exportar-excel', ExportarExcel.as_view(), name='exportar_excel'),
]
