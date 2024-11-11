from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

# def about(request):
#     return render(request,'about.html')

# def home(request):
#     return render(request,'home.html')

# def contact(request):
#     return render(request,'contact.html')

# def booking(request):
#     return render(request,'booking.html')

# def department(request):
#     return render(request,'department.html')

# def doctors(request):
#     return render(request,'doctors.html')


# def deptt(request):
#     dict1 = {
#         'dept' : department.objects.all()
#     }
#     return render(request, 'department.html',dict1)

# def doctor(request):
#     dict_docs = {
#         'doctors': Doctors.objects.all()     
#     }
#     return render(request, 'doctors.html', dict_docs)



# def create_todo(request):
#     if request.method == 'GET':
#         return render(request, 'booking.html')
#     elif request.method == 'POST':
#         title1= request.POST['title']
#         description1= request.POST.get('des', None)
#         rating= request.POST.get('rating', None)
#         status= request.POST.get('satus', 'off')
#         if status == 'on':
#             status = True
#         else:
#             status = False
#         todo = Todo(title=title1, description=description1, rating=rating, status=status)
#         todo.save()
#         return HttpResponse('<h1>Completed</h1>')
    


# def create_cnt(request):
#     if request.method == 'GET':
#         return render(request, 'contact.html')
#     elif request.method == 'POST':
#         contactname1= request.POST['contactname']
#         contactno1= request.POST.get('contactno', None)
#         s = contact(contname=contactname1, contnumb=contactno1)
#         s.save()
#         return HttpResponse('<h1>Completed</h1>')
    


# from .forms import BookingForm

# def bookingss(request):
#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#     form = BookingForm()
#     dict_form = {
#         'form':form
#     }
#     return render(request, 'booking1.html', dict_form)





# from django.views.generic import ListView
# class TaskListviews(ListView):
#     model = department
#     template_name = 'department.html'
#     context_object_name = 'dept'


# from django.views.generic.detail import DetailView
# class TaskDetailtview(DetailView):
#     model = department
#     template_name = 'dep_detailview.html'
#     context_object_name = 'dept'


# from django.views.generic.edit import UpdateView,DeleteView
# from django.urls import reverse_lazy
# class TaskUpdateView(UpdateView):
#     model = department
#     template_name = 'update.html'
#     fields = ('deptname','description')

#     def get_success_url(self):
#         return reverse_lazy('cbdetail', kwargs = {'pk':self.object.id})
    

# class TaskDeleteView(DeleteView):
#     model = department
#     template_name = 'delete.html'
#     success_url = reverse_lazy('home')


# from django.views.generic.edit import CreateView
# class EmployeeCreate(CreateView):
#     model = department
#     template_name = 'create_view.html'
#     fields = '__all__'
#     success_url = reverse_lazy('home')



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required()
def home(request):
    return render (request, 'pages/home.html')

from django.urls import reverse
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    return render(request, 'pages/register.html', {'form':form})

