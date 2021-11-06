from django.shortcuts import redirect, render
from .models import Car
from .forms import Car_form

# Display objects.
def display(request):
    context = {'display' : Car.objects.all()}
    return render(request, 'main/display.html', context)

# Create and update.
def create(request, id=0):
    if request.method=='GET':
        if id==0:
            form = Car_form()
        else:	
            car = Car.objects.get(pk=id)
            form = Car_form(instance = car)
        return render(request, 'main/create.html', {'form': form})
    else:
        if id==0:
            form = Car_form(request.POST)
        else:
            car = Car.objects.get(pk=id)
            form = Car_form(request.POST,instance = car)
        if form.is_valid():
            form.save()
        return redirect('/cars/display')
    
# Delete
def delete(request, id):
    car = Car.objects.get(pk=id)
    car.delete()
    return redirect('/cars/display')