from django.shortcuts import render, redirect
from django.views import View
from .models import Student, Resource
from .forms import AddStudentForm, AddResourceForm
# Create your views here.

class Home(View):
    def get(self, request):
        stu_data = Resource.objects.all()
        return render(request, 'core/home.html', {'studata': stu_data})

class ResourceList(View):
    def get(self, request):
        resourceData = Resource.objects.all()
        return render(request, 'core/resource-list.html', {'resource-data': resourceData})
    
class Add_Resource(View):
    def get(self, request):
        fm = AddResourceForm()
        print(fm)
        return render(request, 'core/add-resource.html', {'form': fm} )    

    def post(self, request):
        fm = AddResourceForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add-resource.html', {'form': fm} )    


class Add_Student(View):
    def get(self, request):
        fm = AddStudentForm()
        return render(request, 'core/add-student.html', {'form': fm} )    

    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add-student.html', {'form': fm} )    

class Delete_Student(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        studata = Student.objects.get(id = id)
        studata.delete()
        return redirect("/")

class Edit_Student(View):
    def get(self, request, id):
        stu = Student.objects.get(id = id)
        fm = AddStudentForm(instance = stu)
        return render(request, 'core/edit-student.html', {'form': fm})    
    
    def post(self, request, id):
        #print(id)
        stu = Student.objects.get(id = id)
        fm = AddStudentForm(request.POST, instance = stu )
        #print(fm)
        if fm.is_valid():
            fm.save()
            return redirect('/ ')
        