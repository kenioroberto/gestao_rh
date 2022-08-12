from apps.registro_hora_extra.models import RegistroHoraExtra
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)