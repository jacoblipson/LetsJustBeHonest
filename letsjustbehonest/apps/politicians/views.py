from django.views.generic import TemplateView


# TODO - remove this view after making the conversion to SPA
class PoliticianView(TemplateView):
    template_name = 'base.html'
