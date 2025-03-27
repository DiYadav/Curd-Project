from django.shortcuts import redirect,render,HttpResponse
from .models import Member
from django.shortcuts import get_object_or_404
from django.db import connection

def index(request):
    mem=Member.objects.all()
    return render (request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect('/')

def dalate(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()

    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE newapp_member AUTO_INCREMENT = 1;")
    return redirect("/")


def update(request, id):
    member = get_object_or_404(Member, id=id)  # Get the existing member

    if request.method == "POST":
        member.firstname = request.POST.get("firstname", member.firstname)
        member.lastname = request.POST.get("lastname", member.lastname)
        member.country = request.POST.get("country", member.country)
        member.save(update_fields=["firstname", "lastname", "country"])  # Update only specified fields
        return redirect("index")  # Redirect to home page after update

    return render(request, "updated.html", {"member": member})  # Render form with existing data



