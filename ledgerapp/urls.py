

from django.urls import path
from .views import ledgerfn, LedgerCreate, detailfn, LedgerDelete, signinfn, signupfn, logoutfn, recordfn, newledgerfn


urlpatterns = [
    path('ledger/', ledgerfn, name="ledger"),
    path('add/', LedgerCreate.as_view(), name="add"),
    path('delete/<int:pk>', LedgerDelete.as_view(), name="delete"),
    path('detail/<int:pk>', detailfn, name="detail"),
    path('signin/', signinfn, name="signin"),
    path('signup/', signupfn, name="signup"),
    path('logout/', logoutfn, name="logout"),
    path('record/', recordfn, name="record"),
    path('new/', newledgerfn, name="new"),



]

