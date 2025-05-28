from django.shortcuts import render ,redirect
from .models import Teacher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# def teacher_list(request):
#     if 'q' in request.GET:
#         q = request.GET['q']
#         teachers = Teacher.objects.filter(name__icontain=q)
#     else:
#         teachers = Teacher.objects.all()
#     return render(request,"index.html",{"allteachers":teachers})

def teacher_list(request):
    if 'q' in request.GET:
        q = request.GET.get('q')  # Fixed this line
        teacher = Teacher.objects.filter(name__icontains=q)  # Fixed 'icontains'
    else:
        teacher = Teacher.objects.all()
    return render(request, "index.html", {"allteachers": teacher})


def add_teacher(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        
        teacher = Teacher(
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save()
        return redirect("allteachers")
    return render(request,"index.html")

def delete(request,id):
    teacher = Teacher.objects.filter(id = id)
    teacher.delete()
    return redirect("allteachers")

def update_teacher(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        teacher = Teacher(
            id = id,
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save()
        return redirect("allteachers")
    return render(request, 'index.html',{'teacher': teacher} )

def delete_selected_teachers(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_teachers')
        if selected_ids:
            Teacher.objects.filter(id__in=selected_ids).delete()
    return redirect('allteachers')

@login_required(login_url='login')
def home_page(request):
    return render(request,'index.html')

# def login_user(request):
#      if request.method =='POST':
#         name = request.POST.get('username')
#         pass1 = request.POST.get('password1')
        
#         user = authenticate(request,username=name,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return redirect('login')
        
#      return render(request,'login.html')

def login_user(request):
     if request.method =='POST':
        name = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print("Trying to login:", name)

        user = authenticate(request, username=name, password=pass1)
        if user is not None:
            print("Login successful")
            login(request, user)
            return redirect('allteachers')
        else:
            print("Login failed")
            return redirect('login')
        
     return render(request, 'login.html')

def signup_user(request):
    if request.method =='POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            return redirect('login')
        else:
            user = User.objects.create_user(name,email,pass1)
            user.save()
            return redirect('login')
    return render(request,'signup.html')
            
        

def logout_user(request):
    logout(request)
    return redirect('login')
