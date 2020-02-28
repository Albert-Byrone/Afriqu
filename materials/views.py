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

# ======================= the overall number of materials in stock logic ====================

# def use_item(request, cls):
#     sum = 0
#     material_quantity = 0
#     used_quantity = 0
#     used_sum = 0
#     materials = Material.objects.all()
#     used_material = Usematerial.objects.all()
#     for item in materials:
#         materialquantity = item.quantity
#         sum += int(materialquantity)
#     # print(sum , 'materials')
#         material_name = item.material_name
    
#         print(material_name)
    
#         if material_name is material:
#             remaining_material = material_quantity - int(quantity)
#             print(remaining_material)
        
    
    

#     for item in used_material:
#         used_quantity = item.quantity
#         used_sum += int(used_quantity) 
#     # print(used_sum, 'materials used')
    
#     remaining_materials = sum - used_sum
#     # print(remaining_materials, 'remaining')
#     if request.method == "POST":
#         form = cls(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('all_materials')
#     else:
#         form = cls()  
#         return render(request, 'materials/use_materials.html', locals())
        
# def use_material(request):
#     return use_item(request, UseMaterialForm)
   

# ===========================================================================================

def use_item(request,cls):
    materials = Material.objects.all()
    if request.method == "POST":
        form = cls(request.POST)
        
        if form.is_valid():
            obj = Material.objects.filter(material_name=request.POST['material'])
            for item in obj:
                item.quantity = item.quantity - int(request.POST['quantity'])
                print(item.quantity)
                print('there are ',item.material_name , item.quantity)
                item.save()
                form.save()
            
            # obj.quantity = obj.quantity - int(request.POST['quantity'])
           
            return redirect('all_materials')

            # print(obj, 'final obj')
    else:
        form = cls()
        return render(request, 'materials/use_materials.html', locals())


def use_material(request):
    return use_item(request,UseMaterialForm)





