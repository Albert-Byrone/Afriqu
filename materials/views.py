from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages

def all_materials(request):
    materials = Material.objects.all()
    total_materials = Material.objects.all().count()
    return render(request, 'materials/materials.html', locals())

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_materials')
    else:
        form = cls()  
        return render(request, 'materials/add_materials.html', locals())

def add_material(request):
    return add_item(request, MaterialForm)

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('all_materials')
    else:
        form = cls(instance=item)
        return render(request, 'materials/edit_material.html', locals())

def edit_material(request, pk):
    return edit_item(request, pk, Material, MaterialForm)

def delete_material(request, pk):
    template = 'materials/materials.html'
    Material.objects.filter(id=pk).delete()
    materials = Material.objects.all()
   
    return render(request, template, locals())
def search_materials(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_materials = Material.search(search_term)
        message = f"{search_term}"

        return render(request, 'materials/search.html',{"message":message,"materials": searched_materials})

    else:
        message = "You haven't searched for any term"
        return render(request, 'materials/search.html',{"message":message})


def reorder_materials(request):
    materials = Material.objects.all()
    total = Material.quantity 
    total = 0
    for material in materials:
        total = total  + int(material.quantity)
    if total < 20:
        messages.warning(request, 'Stock  running low ' f"{total}" ' materials left')
    else:
        messages.success(request, f"{total}" ' materials stock')
    return render(request, 'materials/search.html',locals())


def use_item(request, cls):
    sum = 0
    quantity = 0
    materials = Material.objects.all()
    used_material = Usematerial.objects.all()
    for item in materials:
        quantity = item.quantity
        sum += int(quantity)
        print(sum , 'yyyyyyyyyyyyyyyyyy')

        
    # for item in used_material:
    #     quantity = Material.objects.order_by('quantity')
    #     print(quantity)
    #     total_materials = sum + quantity[1]
        # used_materials = Usematerial.objects.order_by('quantity')
        # remaining = total_materials - used_materials
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_materials')
    else:
        form = cls()  
        return render(request, 'materials/use_materials.html', locals())
        
def use_material(request):
    return use_item(request, UseMaterialForm)
   
