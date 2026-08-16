from django.shortcuts import render, redirect
from . models import Destination, KeyFeat, KeySpecs, EngineTrans, FuelPerf, DimensionsCap, Entertainment_Comm, Images, Sales, Home, Feedback
from . forms import FeedbackForm

def index(request,id):
    homes = Home.objects.get(id=id)
    n = homes.Comp
    h = Destination.objects.filter(comp=n)
    return render(request, 'index.html', {'dests': h})

def feedback(request):
    return render(request, 'feedback.html')

def home(request):
    coms = Home.objects.all()
    return render(request, 'home.html', {'coms': coms})

def show(request, id):
    employee = Destination.objects.get(id=id)
    n = employee.name
    imgs = Images.objects.filter(name=n)
    keys = KeySpecs.objects.get(name=n)
    keyf = KeyFeat.objects.get(name=n)
    eng = EngineTrans.objects.get(name=n)
    fuel = FuelPerf.objects.get(name=n)
    dim = DimensionsCap.objects.get(name=n)
    ent = Entertainment_Comm.objects.get(name=n)
    sale = Sales.objects.get(name=n)

    # Fetch related cars from the same brand or other cars (excluding current car)
    related_cars = Destination.objects.filter(comp=employee.comp).exclude(id=id)
    if not related_cars.exists():
        related_cars = Destination.objects.exclude(id=id)[:4]

    return render(request, 'destinations.html', {
        'employee': employee,
        'keys': keys,
        'keyf': keyf,
        'eng': eng,
        'fuel': fuel,
        'dim': dim,
        'ent': ent,
        'sale': sale,
        'related_cars': related_cars
    })

# Create your views here.
def register(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show1')
            except:
                print('Did not save')
    else:
        form = FeedbackForm()
    return render(request,'feedback.html', {'form': form})

def show1(request):
    feed = Feedback.objects.all()
    return render(request,"show.html", {'feed': feed})

def destroy(request, id):
    feed = Feedback.objects.get(id=id)
    feed.delete()
    return redirect("/show1")

def compare(request):
    coms = Destination.objects.all()
    return render(request, "compare.html", {'comp': coms})

def Comp_result(request):
    if request.method == 'POST':
        value = request.POST['value']
        value1 = request.POST['value1']
    else:
        print('something went wrong')
    employee = Destination.objects.get(name=value)
    imgs = Images.objects.filter(name=value)
    keys = KeySpecs.objects.get(name=value)
    keyf = KeyFeat.objects.get(name=value)
    eng = EngineTrans.objects.get(name=value)
    fuel = FuelPerf.objects.get(name=value)
    dim = DimensionsCap.objects.get(name=value)
    ent =Entertainment_Comm.objects.get(name=value)
    sale = Sales.objects.get(name=value)
    feed = Feedback.objects.get(name=value)

    r = feed.price+ feed.int_design + feed.ext_design + feed.mileage + feed.service_cost + feed.safety_score
    rate = r/6
    rate = round(rate, 2)
    employee1 = Destination.objects.get(name=value1)
    imgs1 = Images.objects.filter(name=value1)
    keys1 = KeySpecs.objects.get(name=value1)
    keyf1 = KeyFeat.objects.get(name=value1)
    eng1 = EngineTrans.objects.get(name=value1)
    fuel1 = FuelPerf.objects.get(name=value1)
    dim1 = DimensionsCap.objects.get(name=value1)
    ent1 = Entertainment_Comm.objects.get(name=value1)
    sale1 = Sales.objects.get(name=value1)
    feed1 = Feedback.objects.get(name=value1)
    r1 = feed1.price + feed1.int_design + feed1.ext_design + feed1.mileage + feed1.service_cost + feed1.safety_score
    rate1 = r1/6
    rate1 = round(rate1, 2)

    return render(request, 'comp_result.html', {'employee': employee, 'keys': keys, 'keyf': keyf, 'eng': eng, 'fuel': fuel, 'dim': dim, 'ent': ent, 'sale': sale, 'rate': rate, 'rate1': rate1, 'employee1': employee1, 'keys1': keys1, 'keyf1': keyf1, 'eng1': eng1, 'fuel1': fuel1, 'dim1': dim1, 'ent1': ent1, 'sale1': sale1})

