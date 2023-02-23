from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView


from .models import UserProfile
from .forms import NewUserForm

# Create your views here.


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

class UserLogoutView(LogoutView):
    next_page = 'article_list'


class ShowProfilePageView(DetailView):
    model = User
    template_name = 'chat/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(User, id=self.kwargs['pk'])
        context['page_user'] = page_user
        if UserProfile.objects.filter(user=page_user):
            context['user_prof_exist'] = True
        else:
            context['user_prof_exist'] = False
        return context


class CreateProfilePageView(CreateView):
    model = UserProfile

    template_name = 'chat/create_profile.html'
    fields = ['profile_pic']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('login')

class UpdateProfilePageView(UpdateView):
    model = UserProfile

    template_name = 'chat/create_profile.html'
    fields = ['profile_pic']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('login')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user.username)
            login(request, user)
            # messages.success(request, "Registration successful." )
            return redirect('user_profile',pk = user.pk)
        # messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form":form})


def start_page(request):
    return render(request = request, template_name = "default.html")
