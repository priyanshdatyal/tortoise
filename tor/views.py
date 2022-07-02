import datetime
from http.client import HTTPResponse
from random import random
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import BrandPlans, CustomerGoals

# Create your views here.


def index(request):
    return render(request,'home.html')
def brand(request):
    pn = BrandPlans.objects.all()
    data = {
        "pn":pn,
    }
    return render(request,'brand.html',data)


def customers(request):
    pn = CustomerGoals.objects.all()
    data = {
        "pn":pn,
    }
    return render(request,'customers.html',data)

def user(request):
    pn = BrandPlans.objects.all()
    data = {
        "pn":pn,
    }
    return render(request,'user.html',data)

def addCust(request):
    if(request.method=="POST"):
        planid=request.POST.get('planidcst')
        userName=request.POST.get('custName')
        plantype=request.POST.get('plantypecst')
        promoOffer=request.POST.get('promoOffer')
        plan=BrandPlans.objects.get(planid=request.POST.get("planidcst"))
        if(promoOffer==str("YES")):
            if(plantype==str(1)):
                promoPercent=plan.lpromPrcnt
                amount=plan.lowam
                tenure=plan.lowtn
                bptype=plan.ltype
            elif(plantype==str(2)):
                promoPercent=plan.mpromPrcnt
                amount=plan.midam
                tenure=plan.midtn
                bptype=plan.mtype
            else:
                promoPercent=plan.hpromPrcnt
                amount=plan.hiam
                tenure=plan.hightn
                bptype=plan.htype
        else:
            if(plantype==str(1)):
                promoPercent=plan.lbp
                amount=plan.lowam
                tenure=plan.lowtn
                bptype=plan.ltype
            elif(plantype==str(2)):
                promoPercent=plan.mbp
                amount=plan.midam
                tenure=plan.midtn
                bptype=plan.mtype
            else:
                promoPercent=plan.hbp
                amount=plan.hiam
                tenure=plan.hightn
                bptype=plan.htype
        userid = userName.replace(" ","_")+str(random()).replace(",","")

        if(promoOffer==str("YES")):
            today = datetime.date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
            print(f"---------------------------------------\n{today<=plan.enDate}\n-----------------------------")
            if(plan.quota > 0 and today<=plan.enDate ):
                data=CustomerGoals(userid=userid,planid=planid,userName=userName,benefitPercentage=promoPercent,depositedAmount=amount,selectedAmount=amount,selectedTenure=tenure,benefitType=bptype)
                data.save()
        else:
            data=CustomerGoals(userid=userid,planid=planid,userName=userName,benefitPercentage=promoPercent,depositedAmount=amount,selectedAmount=amount,selectedTenure=tenure,benefitType=bptype)
            data.save()
    
    return redirect("/user/")

    
def updatePlanBP(request):
    if(request.method=="POST"):
        BrandPlans.objects.filter(planid=request.POST.get("planid")).update(endDate=request.POST.get('endDate'))
        BrandPlans.objects.filter(planid=request.POST.get("planid")).update(quota=request.POST.get('quota'))
        BrandPlans.objects.filter(planid=request.POST.get("planid")).update(ltype=request.POST.get("ltype"))
        BrandPlans.objects.filter(planid=request.POST.get("planid")).update(mtype=request.POST.get("mtype"))
        BrandPlans.objects.filter(planid=request.POST.get("planid")).update(htype=request.POST.get("htype"))
        BrandPlans.objects.filter(planid=request.POST.get("planid")).update(lpromPrcnt=request.POST.get("lbenefitPercent"))
        BrandPlans.objects.filter(planid=request.POST.get("planid")).update(mpromPrcnt=request.POST.get("mbenefitPercent"))
        BrandPlans.objects.filter(planid=request.POST.get("planid")).update(hpromPrcnt=request.POST.get("hbenefitPercent")) 


    return redirect("/brand/")

def addPlan(request):
    if(request.method=="POST"):
        planid=request.POST.get('planid')
        planname=request.POST.get('planname')
        lowtn=request.POST.get('lowtn')
        midtn=request.POST.get('midtn')
        hightn=request.POST.get('hightn')
        lbp=request.POST.get('lbp')
        mbp=request.POST.get('mbp')
        hbp=request.POST.get('hbp')
        lowam=request.POST.get('lowam')
        midam=request.POST.get('midam')
        hiam=request.POST.get('hiam')
        data = BrandPlans(planid=planid,planname=planname,lowtn=lowtn,midtn=midtn,hightn=hightn,lbp=lbp,mbp=mbp,hbp=hbp,lowam=lowam,midam=midam,hiam=hiam)
        data.save()
        
    pn = BrandPlans.objects.all()
    data = {
        "pn":pn,
    }
    return redirect('/brand/')