from django.views.generic.base import TemplateView

class AuthorPage(TemplateView):
   template_name = 'about/Author.html'

class TechPage(TemplateView):
   template_name = 'about/Tech.html'
