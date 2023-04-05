from django.shortcuts import render

from .models import crudModel




def create(request):
    user_name = 0
    user_address = 0
    user_mobilenumber = 0

    submit = 0
    if request.GET:
        user_name = request.GET["user_name"]
        user_address = request.GET["user_address"]
        user_mobilenumber = request.GET["user_mobilenumber"]
        print("user_mobilenumber", user_mobilenumber)

        opt = request.GET["option"]
        p = crudModel()
        p.user_name = user_name
        p.user_address = user_address
        p.user_mobilenumber = user_mobilenumber

        p.save()
        print("saved")

        if opt == "submit":
            submit = user_name

    return render(request, "create.html",
                  {"user_name": user_name, "user_address": user_address, "user_mobilenumber": user_mobilenumber, "submit": submit})


def read(request):
    crud= crudModel.objects.all()
    return render(request, "read.html", {'cruds':crud })


def edit(request):
    id = request.GET["id"]
    crud = crudModel.objects.get(id=id)
    return render(request, 'edit.html', {'cruds': crud})


def update(request):
    id = request.GET["id"]
    crud = crudModel.objects.get(id=id)
    if request.POST:
        user_name = request.POST["user_name"]
        # user_address = request.POST["user_address"]

        user_mobilenumber = request.POST["user_mobilenumber"]
        crud.user_name = user_name
        # crud.user_address = user_address
        crud.user_mobilenumber = user_mobilenumber
        crud.save()

    return render(request, 'edit.html', {'cruds': crud})


def delete(request):
    if request.GET:
        id = request.GET["id"]
        crud = crudModel.objects.filter(id=id)[0]
        crud.delete()

    return render(request, "delete.html", {"cruds": crud})
#