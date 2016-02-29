from django.conf.urls import url


from letsjustbehonest.apps.politicians.api import PoliticianListView

urlpatterns = [
    url(r'^list/$', PoliticianListView.as_view()),
]
