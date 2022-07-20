from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name = 'authors/pages;profile.hhtml'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)