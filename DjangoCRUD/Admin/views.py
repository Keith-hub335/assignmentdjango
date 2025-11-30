from django.shortcuts import render, redirect


from django.shortcuts import render, redirect, get_object_or_404

from Admin.models import Announcements, Courses, Trainers


# Create your views here.
def dashboard(request):
    courses = Courses.objects.all()
    trainers = Trainers.objects.all()
    announcements = Announcements.objects.all()
    return render(request, 'admin.html', {'courses': courses,'trainers': trainers, 'announcements': announcements})



def add_courses(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        duration = request.POST['duration']



        Courses.objects.create(title=title, description=description, duration=duration)
        return redirect('dashboard')
    return render(request, 'courses.html')

def add_trainers(request):
    if request.method == 'POST':
        name = request.POST['name']
        bio = request.POST['bio']
        experience_years = int(request.POST['experience_years'])



        Trainers.objects.create(name=name, bio=bio, experience_years=experience_years)
        return redirect('dashboard')
    return render(request, 'trainers.html')

def add_announcements(request):
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        date_posted = request.POST['date_posted']



        Announcements.objects.create(title=title, message=message, date_posted=date_posted)
        return redirect('dashboard')
    return render(request, 'announcements.html')


def delete_course(request, id):
    course = get_object_or_404(Courses, id=id)
    course.delete()
    return redirect('dashboard')

def delete_trainer(request, id):
    trainer = get_object_or_404(Trainers, id=id)
    trainer.delete()
    return redirect('dashboard')

def delete_announcement(request, id):
    announcement = get_object_or_404(Announcements, id=id)
    announcement.delete()
    return redirect('dashboard')

