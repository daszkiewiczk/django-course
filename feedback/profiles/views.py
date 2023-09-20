from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserModel
from django.views.generic.edit import CreateView
from django.views.generic import ListView

def store_file(file):
    with open('temp/resume.pdf', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             'form': form,
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             # store_file(request.FILES['user_image'])
#             profile = UserModel(user_image = request.FILES['user_image'])
#             profile.save()
#             print(request.FILES['user_image'])
#             print('created')
#             return HttpResponseRedirect('/profiles')
#         return render(request, "profiles/create_profile.html", {
#             'form': submitted_form,
#         })

class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserModel
    success_url = '/profiles'
    fields = '__all__'
    
class ProfilesView(ListView):
    model = UserModel
    template_name = 'profiles/user_profiles.html'
    context_object_name = 'profiles'
    