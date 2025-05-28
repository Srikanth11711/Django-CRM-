from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def student_list(request):
    if 'q' in request.GET:
        q = request.GET.get('q')  # Fixed this line
        students = Student.objects.filter(name__icontains=q)  # Fixed 'icontains'
    else:
        students = Student.objects.all()
    return render(request, "student.html", {"allstudents": students})


def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        Student.objects.create(
            name=name,
            contact=contact,
            email=email,
            image=image if image else None
        )
        return redirect("allstudents")
    
    return redirect("allstudents")

def delete(request, id):
    Student.objects.filter(id=id).delete()
    return redirect("allstudents")

def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.contact = request.POST.get('contact')
        student.email = request.POST.get('email')
        image = request.FILES.get('image')
        if image:
            student.image = image
        student.save()
        return redirect("allstudents")

    return render(request, 'student.html', {'student': student})

def delete_selected_students(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_students')
        if selected_ids:
            Student.objects.filter(id__in=selected_ids).delete()
    return redirect('allstudents')
