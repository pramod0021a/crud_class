from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentForm
from .models import Student
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

# Add and show data.
class IndexView(TemplateView):
   template_name = 'mains/index.html'

   def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(**kwargs)
      fm = StudentForm()
      stud = Student.objects.all()
      context = {'stu':stud, 'form':fm}
      return context
   
   def post(self, request):
      fm = StudentForm(request.POST)
      if fm.is_valid():
         # fm.save()
         nm = fm.cleaned_data['name']
         ag = fm.cleaned_data['age']
         lcn = fm.cleaned_data['location']
         em = fm.cleaned_data['email']
         pw = fm.cleaned_data['password']
         add = Student(name=nm, age=ag, location=lcn, email=em, password=pw)
         add.save()
         return HttpResponseRedirect('/')


# Update Data
class UpdateStudentView(View):
   def get(self, request, id):
      pi = Student.objects.get(pk=id)
      fm = StudentForm(instance=pi)       
      return render(request, 'mains/update.html', {'form':fm})
   
   def post(self, request, id):
      pi = Student.objects.get(pk=id)
      fm = StudentForm(request.POST, instance=pi)
      if fm.is_valid():
         fm.save()
      # return render(request, 'mains/update.html', {'form':fm})
      return HttpResponseRedirect('/')
   

# Delete Data
class DeleteStudentView(RedirectView):
   url = '/'
   def get_redirect_url(self, *args, **kwargs):
      del_id = kwargs['id']
      Student.objects.get(pk=del_id).delete()
      return super().get_redirect_url(*args, **kwargs)


