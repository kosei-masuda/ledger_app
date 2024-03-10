from django.shortcuts import render, get_object_or_404, redirect
from .models import BookModel, PreviousMonthData
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
import requests
import math
import configparser
from django.conf import settings
import os

# Create your views here.

#get_exchangerate
def get_exchange_rate(base_currency, target_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if 'error' in data:
        raise Exception(data['error'])
    return data['conversion_rates'][target_currency]


@login_required
def ledgerfn(request):
    object_list = BookModel.objects.filter(user=request.user)
    username = request.user.username

    total_income = BookModel.objects.filter(user=request.user).aggregate(total=Sum('income'))['total'] or 0
    total_expenses = BookModel.objects.filter(user=request.user).aggregate(total=Sum('expenses'))['total'] or 0
    total_balance = total_income - total_expenses

    #use API
    config_file_path = os.path.join(settings.BASE_DIR,'config.ini')
    config = configparser.ConfigParser()
    config.read(config_file_path)
    api_key = config['API']['key']
    base_currency = 'TWD'
    target_currency = 'JPY'
    exchange_rate = get_exchange_rate(base_currency, target_currency, api_key)
    total_in_target_currency_income = math.ceil(total_income * exchange_rate)
    total_in_target_currency_expenses = math.ceil(total_expenses * exchange_rate)
    total_in_target_currency_balance = math.ceil(total_balance * exchange_rate)


    return render(request, 'ledger.html',{
        'object_list':object_list,
        'username': username,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'total_balance': total_balance,
        'total_in_target_currency_income':total_in_target_currency_income,
        'total_in_target_currency_expenses':total_in_target_currency_expenses,
        'total_in_target_currency_balance':total_in_target_currency_balance,
        })

def recordfn(request):
    record_list = PreviousMonthData.objects.filter(user=request.user)
    return render(request, 'record.html',{'record_list':record_list})


class LedgerCreate(LoginRequiredMixin,CreateView):
    template_name = 'add.html'
    model = BookModel
    fields = ('title', 'income', 'expenses', 'date', 'memo', 'kind')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('ledger')

class LedgerDelete(DeleteView):
    template_name = 'delete.html'
    model = BookModel
    success_url = reverse_lazy('ledger')

def detailfn(request, pk):
    object = get_object_or_404(BookModel, pk=pk)
    return render(request, 'detail.html',{'object':object})

def signupfn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, " ", password)
            return redirect('signin')
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーはすでに登録されています'})
    return render(request, 'signup.html', {'some':100})

def signinfn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ledger')
        else:
            return render(request, 'signin.html', {'context':'ログイン失敗'})
    return render(request, 'signin.html', {'context':'ログイン成功'})

def logoutfn(request):
    logout(request)
    return redirect('signin')

def newledgerfn(request):
    user = request.user
    try:
        previous_month_data = PreviousMonthData.objects.get(user=user)
    except PreviousMonthData.DoesNotExist:

        previous_month_data = PreviousMonthData(user=user, income=0, expenses=0, total=0)


    previous_month_data.income = calculate_previous_month_income(user)
    previous_month_data.expenses = calculate_previous_month_expenses(user)
    previous_month_data.total = previous_month_data.income - previous_month_data.expenses
    previous_month_data.save()
    BookModel.objects.filter(user=request.user).delete()


    return redirect('ledger')


def calculate_previous_month_income(user):
    pre_total_income = BookModel.objects.filter(user=user).aggregate(total=Sum('income'))['total'] or 0
    return pre_total_income

def calculate_previous_month_expenses(user):
    pre_total_expenses = BookModel.objects.filter(user=user).aggregate(total=Sum('expenses'))['total'] or 0
    return pre_total_expenses





