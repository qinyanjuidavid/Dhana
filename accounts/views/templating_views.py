from accounts.decorators import administrator_required, customer_required
from accounts.forms import (AdministratorProfileUpdate,
                            CustomerProfileUpdateForm, UserSignUpForm,
                            UserUpdateForm)
from accounts.models import Administrator, Customer, User
from accounts.sendMails import send_activation_mail, send_password_reset_email
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView

decorators = [never_cache, login_required, administrator_required]


# @method_decorator(decorators, name='dispatch')
class AdministratorSignupView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "accounts/adminSignup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Admin"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.is_staff = True
            user.role = "administrator"
            user.save()
            send_activation_mail(user, self.request)

        return render(self.request, "accounts/sign_alert.html")


class CustomerSignupView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "accounts/customerSignup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Customer"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "customer"
            user.save()

            send_activation_mail(user, self.request)
        return render(self.request, "accounts/sign_alert.html")


def RequestPasswordReset(request):
    context = {

    }
    return render(request, "accounts/RequestPasswordReset.html", context)
