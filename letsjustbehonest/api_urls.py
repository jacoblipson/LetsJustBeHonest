from django.conf.urls import include, url


urlpatterns = [
    url(r'^politicians/', include('letsjustbehonest.apps.politicians.urls.api')),
]
