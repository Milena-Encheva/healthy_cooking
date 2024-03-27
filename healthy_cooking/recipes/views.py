from django.shortcuts import render
from django.views import generic as view

# Create your views here.


class PetCreateView(view.CreateView):
    form_class = PetCreateForm
    template_name = 'pets/create_pet.html'

    def get_success_url(self):
        return reverse('details pet', kwargs={
            'username': "milenae",
            'pet_slug': self.object.slug,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance.user = self.request.user
        return form