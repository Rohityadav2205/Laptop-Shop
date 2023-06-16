from django.shortcuts import render

from .models import laptopModel


# Create your views here.
# def rohit(request):
#     return HttpResponse("hello Ram") hi.

def create(request):
    sno = 0
    company_name = 0
    ram=0
    rom=0
    model_name = 0
    price=0

    submit = 0
    if request.GET:
        sno = int(request.GET["sno"])
        company_name = request.GET["company_name"]
        ram = request.GET["ram"]
        rom = request.GET["rom"]
        model_name = request.GET["model_name"]
        price=int(request.GET["price"])

        # print("mobile number", mobile_number)

        # opt = request.GET["option"]
        ms = laptopModel()
        ms.sno = sno
        ms.company_name = company_name
        ms.ram = ram
        ms.rom = rom
        ms.model_name = model_name
        ms.price = price


        ms.save()
        print("saved data")



    return render(request, "create.html",
                  {"sno": sno, "company_name": company_name, "ram": ram,"rom":rom,"model_name":model_name,"price":price, "submit": submit})

#
def retrieve(request):
    laptopapp_laptopModel = laptopModel.objects.all()
    return render(request, "retrieve.html", {'laptopapp_laptopModel': laptopapp_laptopModel})

def edit(request):
    id = request.GET["id"]
    laptopapp_laptopModel = laptopModel.objects.get(id=id)
    return render(request, 'edit.html', {'laptopapp_laptopModel': laptopapp_laptopModel})


def update(request):
    id = request.GET["id"]
    laptopapp_laptopModel = laptopModel.objects.get(id=id)
    if request.POST:
        sno = request.POST["sno"]
        company_name = request.POST["company_name"]
        ram = request.POST["ram"]
        rom = request.POST["rom"]
        model_name= request.POST["model_name"]
        price=request.POST["price"]
        laptopapp_laptopModel.sno = sno
        laptopapp_laptopModel.company_name =company_name
        laptopapp_laptopModel.ram =ram
        laptopapp_laptopModel.rom =rom
        laptopapp_laptopModel.model_name=model_name
        laptopapp_laptopModel.price=price
        laptopapp_laptopModel.save()

    return render(request, 'edit.html', {'laptopapp_laptopModel': laptopapp_laptopModel})


def delete(request):
    if request.GET:
        id = request.GET["id"]
        laptopapp_laptopModel = laptopModel.objects.filter(id=id)[0]
        laptopapp_laptopModel.delete()

    return render(request, "delete.html", {"laptopapp_laptopModel": laptopapp_laptopModel})
#
