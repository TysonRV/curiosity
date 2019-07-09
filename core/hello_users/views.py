from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


class UsersListView(ListView):
    template_name = 'core/hello_users/users_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'core/hello_users/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(
            self.request,
            'We are generating your random users! Wait a moment and refresh this page.'
        )
        return redirect('users_list')
