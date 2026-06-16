from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.db.models import Q
from.models import Note
# from django.http import HttpResponse
# Create your views here.
def home(request):
     
    search = request.GET.get('search')
    print(search)
    if search:
            notes = Note.objects.filter(Q(title__icontains=search)|Q(subject__icontains=search)|Q(description__icontains =search))

    else:
          notes=Note.objects.all()
          total_notes = notes.count()

    return render(request,'home.html', {'notes': notes, 'total_notes': total_notes})

def upload_note(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        title = request.POST['title']
        subject = request.POST['subject']
        description = request.POST['description']
        author = request.user.username
        uploaded_file = request.FILES.get('file')
        Note.objects.create(title=title, subject = subject, description=description,author=author, file=uploaded_file)
        return redirect('/')
    return render(request,'upload.html')

def delete_note(request, id):
    note = Note.objects.get(id = id)
    if note.author == request.user.username:
      note.delete()
    return redirect('/')

def edit_note(request, id):
    note = Note.objects.get(id = id)
    if note.author != request.user.username:
            return redirect('/')
    if request.method == 'POST':
        note.title = request.POST['title']
        note.subject = request.POST['subject']
        note.description = request.POST['description']
        
        if request.FILES.get('file'):
            note.file = request.FILES.get('file')
        note.save()
        return redirect('/')
    return render(request, 'edit.html', {'note': note})

def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        confirm_password = request.POST['confirm_password']
        if password ==  confirm_password:
            User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            return redirect('/login/')
    return render(request,'register.html')  

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,  username =username , password =password)
        if user is not None: 
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html', {'error': 'Invalid credentials'})
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')

def my_notes(request):
    notes = Note.objects.filter( author = request.user.username)
    my_notes_count = notes.count()

    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'my_notes.html', {'notes':notes, 'my_notes_count': my_notes_count})

def subject_notes(request, subject):
    notes = Note.objects.filter(subject = subject)
    return render(request, 'home.html', {'notes':notes})

def profile(request):
    total_notes = Note.objects.filter( author = request.user.username).count()

    return render(request, 'profile.html', {'total_notes': total_notes})
