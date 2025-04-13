from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Student Register View
def reg_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_students')
    else:
        form = StudentForm()
    return render(request, 'registerForm.html', {'form': form})

# Student List View
def show_students(request):
    students = Student.objects.all()
    return render(request, 'showStudents.html', {'students': students})
