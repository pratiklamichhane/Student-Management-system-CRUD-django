from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Student
from .forms import studentForm
# Create your views here.
def index(request):
    query = request.GET.get('q')
    students = Student.objects.all()
    return render(request, 'students/index.html', {
        'students': students,
    })

def view_student(request , id):
    student = Student.objects.all( pk = id )
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']
            
            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa,
            )
            new_student.save()
            return render(request  , 'students/add.html',{
                'form': studentForm(),
                'success': True
            })
    else:
        form = studentForm()
    return render(request , 'students/add.html', {
        'form': studentForm()
    })
def edit(request , id):
    if request.method == 'POST':
        student= Student.objects.get(pk=id)
        form = studentForm(request.POST , instance=student)
        if form.is_valid():
            form.save()
            return render(request , 'students/edit.html', {
                'form' : form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = studentForm(instance=student)
    return render(request , 'students/edit.html', {
        'form':form
    })
def delete(request , id):
    if request.method =='POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))

