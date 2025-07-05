from django.shortcuts import render,redirect

from attendance_app.forms import teacherLoginForm, studentLoginForm

def index(request):
  return render(request,'index.html')

def login(request):
  user_type = request.GET.get('user')

  student_form = studentLoginForm()
  teacher_form = teacherLoginForm()
  message = ''

  if request.method == 'POST':
        if request.POST.get('user_type') == 'student':
            student_form = studentLoginForm(request.POST)
            if student_form.is_valid():
                enrollment = student_form.cleaned_data['enrollment']
                password = student_form.cleaned_data['password']
                # authenticate student logic here
                message = f"Student logged in as {enrollment}"
        elif request.POST.get('user_type') == 'teacher':
            teacher_form = teacherLoginForm(request.POST)
            if teacher_form.is_valid():
                email = teacher_form.cleaned_data['email']
                password = teacher_form.cleaned_data['password']
                # authenticate teacher logic here
                message = f"Teacher logged in as {email}"

  return render(request, 'login.html', {
        'user_type': user_type,
        'student_form': student_form,
        'teacher_form': teacher_form,
        'message': message
    })

