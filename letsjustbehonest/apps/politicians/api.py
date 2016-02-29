from rest_framework.generics import ListAPIView
from .models import Politician
from .serializers import PoliticianSerializer


class PoliticianListView(ListAPIView):
    serializer_class = PoliticianSerializer

    def get_queryset(self):
        party = self.request.GET.get('party', None)
        roles = self.request.GET.get('roles', None)
        queryset = Politician.objects.all()
        if roles:
            queryset = queryset.filter(roles__contains=roles)
        if party:
            queryset = queryset.filter(party=party)

        return queryset
