from django.shortcuts import render
from .models import main
from .models import to_approve
def inserttest():
    s = main(category = 'college', title = "G L Bajaj" , contact = '7505528469', address = "Knowladge Park 3")
    s.save()
    t = main(category = 'college', title = "Sharda University" , contact = '7505528469', address = "Knowladge Park 3")
    t.save()
    u = main(category = 'college', title = "GNIOT " , contact = '7505528469', address = "Knowladge Park 3")
    u.save()
    v = main(category = 'college', title = "ITS college" , contact = '7505528469', address = "Knowladge Park 3")
    v.save()

# Create your views here.

def index(request):
    return render(request, 'index.html')
def search(request):
    #inserttest()
    print('Iam search')
    cat = request.POST['category']
    q = request.POST['q']
    #s = main.objects.get(category= 'college')
    s = main.objects.all()
    return render(request, 'index.html',{'cat':cat,'q':q, 'rows':s})

def user_login(request):
    return render(request, 'user_login.html')
def admin_login(request):
    return render(request, 'admin_login.html')



def register(request):
    return render(request, 'register.html')


def user_main(request):
    return render(request, 'user_update.html' )
def admin_main(request):
    return render(request, 'user_update.html') 