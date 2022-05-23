from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mofast, Trade2w, Eglobal, Unateus, Halisi, Mainstream, Clinton, WarehouseKe, Adlat, BNE, Vital
import datetime


def get_percentage_per_agent(request):
    user = User.objects.all()
    mofast = Mofast.objects.all()
    trade = Trade2w.objects.all()
    eglobal = Eglobal.objects.filter(owner=request.user)
    unateus = Unateus.objects.filter(owner=request.user)
    halisi = Halisi.objects.filter(owner=request.user)
    mainstream = Mainstream.objects.filter(owner=request.user)
    clinton = Clinton.objects.filter(owner=request.user)
    warehouse = WarehouseKe.objects.filter(owner=request.user)
    adlat = Adlat.objects.filter(owner=request.user)
    bne = BNE.objects.filter(owner=request.user)
    paginator = Paginator(mofast, 4)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    if Trade2w.objects.filter(owner=request.user).exists():
        percentage = Trade2w.objects.get(owner=request.user).percentage
    else:
        percentage = 0
    context = {
        'page_obj': page_obj,
        'mofast': mofast,
        'user': user,
        'trade': trade,
        'percentage': percentage


    }
    return render(request, 'orders/view.html', context)


@login_required(login_url='/authentication/login')
def home(request):
    return render(request, 'orders/index.html')


@login_required(login_url='/authentication/login')
def add_mofast(request):
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'orders/add_mofast.html', context)
    if request.method == 'POST':
        date = request.POST['date']
        mofast_total = request.POST['mofasttotal']
        mofast_scheduled = request.POST['mofastscheduled']
        mofast_pending = request.POST['mofastpending']
        mofast_cancelled = request.POST['mofastcancelled']
        percentage = (int(mofast_scheduled) / (int(mofast_total)))*100
        if not mofast_total:
            messages.error(request, 'Total Orders are required')
            return render(request, 'orders/add_mofast.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'orders/add_mofast.html', context)
        Mofast.objects.create(owner=request.user, total=mofast_total, date=date, scheduled=mofast_scheduled,
                              pending=mofast_pending, cancelled=mofast_cancelled, percentage=percentage)

        messages.success(request, "Mofast details added successfully")
        return redirect('add_mofast')



@login_required(login_url='/authentication/login')
def add_2wtrade(request):
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'orders/add_2wtrade.html', context)
    if request.method == 'POST':
        date = request.POST['date']
        wtotal = request.POST['2wtotal']
        wscheduled = request.POST['2wscheduled']
        wpending = request.POST['2wpending']
        wcancelled = request.POST['2wcancelled']
        percentage = (int(wscheduled) / (int(wtotal))) * 100
        if not wtotal:
            messages.error(request, 'Total Orders are required')
            return render(request, 'orders/add_2wtrade.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'orders/2wtrade.html', context)
        Mofast.objects.create(owner=request.user, total=wtotal, date=date, scheduled=wscheduled,
                              pending=wpending, cancelled=wcancelled, percentage=percentage)

        messages.success(request, "2W Trade details added successfully")
        return redirect('add_2wtrade')


@login_required(login_url='/authentication/login')
def add_eglobal(request):
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'orders/add_eglobal.html', context)
    if request.method == 'POST':
        date = request.POST['date']
        eglobaltotal = request.POST['eglobaltotal']
        eglobalscheduled = request.POST['eglobalscheduled']
        eglobalpending = request.POST['eglobalpending']
        eglobalcancelled = request.POST['eglobalcancelled']
        percentage = (int(eglobalscheduled) / (int(eglobaltotal))) * 100
        if not eglobaltotal:
            messages.error(request, 'Total Orders are required')
            return render(request, 'orders/add_eglobal.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'orders/add_eglobal.html', context)
        Mofast.objects.create(owner=request.user, total=eglobaltotal, date=date, scheduled=eglobalscheduled,
                              pending=eglobalpending, cancelled=eglobalcancelled, percentage=percentage)

        messages.success(request, "Eglobal details added successfully")
        return redirect('add_eglobal')


@login_required(login_url='/authentication/login')
def add_unateus(request):
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'orders/add_unateus.html', context)
    if request.method == 'POST':
        date = request.POST['date']
        unateustotal = request.POST['unateustotal']
        unateusscheduled = request.POST['unateusscheduled']
        unateuspending = request.POST['unateuspending']
        unateuscancelled = request.POST['unateuscancelled']
        percentage = (int(unateusscheduled) / (int(unateustotal))) * 100
        if not unateustotal:
            messages.error(request, 'Total Orders are required')
            return render(request, 'orders/add_unateus.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'orders/add_unateus.html', context)
        Mofast.objects.create(owner=request.user, total=unateustotal, date=date, scheduled=unateusscheduled,
                              pending=unateuspending, cancelled=unateuscancelled, percentage=percentage)

        messages.success(request, "Unateus details added successfully")
        return redirect('add_unateus')


@login_required(login_url='/authentication/login')
def add_halisi(request):
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'orders/add_halisi.html', context)
    if request.method == 'POST':
        date = request.POST['date']
        halisitotal = request.POST['halisitotal']
        halisischeduled = request.POST['halisischeduled']
        halisipending = request.POST['halisipending']
        halisicancelled = request.POST['halisicancelled']
        percentage = (int(halisischeduled) / (int(halisitotal))) * 100
        if not halisitotal:
            messages.error(request, 'Total Orders are required')
            return render(request, 'orders/add_halisi.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'orders/add_unateus.html', context)
        Mofast.objects.create(owner=request.user, total=halisitotal, date=date, scheduled=halisischeduled,
                              pending=halisipending, cancelled=halisicancelled, percentage=percentage)

        messages.success(request, "Halisi Labs details have been added successfully")
        return redirect('add_halisi')


@login_required(login_url='/authentication/login')
def add_mainstream(request):
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'orders/add_mainstream.html', context)
    if request.method == 'POST':
        date = request.POST['date']
        mainstreamtotal = request.POST['mainstreamtotal']
        mainstreamscheduled = request.POST['mainstreamscheduled']
        mainstreampending = request.POST['mainstreampending']
        mainstreamcancelled = request.POST['mainstreamcancelled']
        percentage = (int(mainstreamscheduled) / (int(mainstreamtotal))) * 100
        if not mainstreamtotal:
            messages.error(request, 'Total Orders are required')
            return render(request, 'orders/add_mainstream.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'orders/add_mainstream.html', context)
        Mofast.objects.create(owner=request.user, total=mainstreamtotal, date=date, scheduled=mainstreamscheduled,
                              pending=mainstreampending, cancelled=mainstreamcancelled, percentage=percentage)

        messages.success(request, "Mainstream details have been added successfully")
        return redirect('add_mainstream')


@login_required(login_url='/authentication/login')
def add_clinton(request):
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'orders/add_clinton.html', context)
    if request.method == 'POST':
        date = request.POST['date']
        clintontotal = request.POST['clintontotal']
        clintonscheduled = request.POST['clintonscheduled']
        clintonpending = request.POST['clintonpending']
        clintoncancelled = request.POST['clintoncancelled']
        percentage = (int(clintonscheduled) / (int(clintontotal))) * 100
        if not clintontotal:
            messages.error(request, 'Total Orders are required')
            return render(request, 'orders/add_mainstream.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'orders/add_mainstream.html', context)
        Mofast.objects.create(owner=request.user, total=clintontotal, date=date, scheduled=clintonscheduled,
                              pending=clintonpending, cancelled=clintoncancelled, percentage=percentage)

        messages.success(request, "Clinton Stores details have been added successfully")
        return redirect('add_clinton')


@login_required(login_url='/authentication/login')
def add_ke(request):
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'orders/add_kewarehouse.html', context)
    if request.method == 'POST':
        date = request.POST['date']
        ketotal = request.POST['ketotal']
        kescheduled = request.POST['kescheduled']
        kepending = request.POST['kepending']
        kecancelled = request.POST['kecancelled']
        percentage = (int(kescheduled) / (int(ketotal))) * 100
        if not ketotal:
            messages.error(request, 'Total Orders are required')
            return render(request, 'orders/add_mainstream.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'orders/add_kewarehouse.html', context)
        Mofast.objects.create(owner=request.user, total=ketotal, date=date, scheduled=kescheduled,
                              pending=kepending, cancelled=kecancelled, percentage=percentage)

        messages.success(request, "Ke-Warehouse details have been added successfully")
        return redirect('add_ke')


@login_required(login_url='/authentication/login')
def add_adlat(request):
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'orders/add_adlat.html', context)
    if request.method == 'POST':
        date = request.POST['date']
        adlattotal = request.POST['adlattotal']
        adlatscheduled = request.POST['adlatscheduled']
        adlatpending = request.POST['adlatpending']
        adlatcancelled = request.POST['adlatcancelled']
        percentage = (int(adlatscheduled) / (int(adlattotal))) * 100
        if not adlattotal:
            messages.error(request, 'Total Orders are required')
            return render(request, 'orders/add_mainstream.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'orders/add_adlat.html', context)
        Mofast.objects.create(owner=request.user, total=adlattotal, date=date, scheduled=adlatscheduled,
                              pending=adlatpending, cancelled=adlatcancelled, percentage=percentage)

        messages.success(request, "Adlat details have been added successfully")
        return redirect('add_adlat')


@login_required(login_url='/authentication/login')
def add_2b(request):
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'orders/add_2b.html', context)
    if request.method == 'POST':
        date = request.POST['date']
        btotal = request.POST['2btotal']
        bscheduled = request.POST['2bscheduled']
        bpending = request.POST['2bpending']
        bcancelled = request.POST['2bcancelled']
        percentage = (int(bscheduled) / (int(btotal))) * 100
        if not btotal:
            messages.error(request, 'Total Orders are required')
            return render(request, 'orders/add_mainstream.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'orders/add_adlate.html', context)
        Mofast.objects.create(owner=request.user, total=btotal, date=date, scheduled=bscheduled,
                              pending=bpending, cancelled=bcancelled, percentage=percentage)

        messages.success(request, "2BNE details have been added successfully")
        return redirect('add_2b')


@login_required(login_url='/authentication/login')
def add_vital(request):
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'orders/add_vital.html', context)
    if request.method == 'POST':
        date = request.POST['date']
        vitaltotal = request.POST['vitaltotal']
        vitalscheduled = request.POST['vitalscheduled']
        vitalpending = request.POST['vitalpending']
        vitalcancelled = request.POST['vitalcancelled']
        percentage = (int(vitalscheduled) / (int(vitaltotal))) * 100
        if not vitaltotal:
            messages.error(request, 'Total Orders are required')
            return render(request, 'orders/add_vital.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'orders/add_vital.html', context)
        Mofast.objects.create(owner=request.user, total=vitaltotal, date=date, scheduled=vitalscheduled,
                              pending=vitalpending, cancelled=vitalcancelled, percentage=percentage)

        messages.success(request, "Vital details have been added successfully")
        return redirect('add_vital')














