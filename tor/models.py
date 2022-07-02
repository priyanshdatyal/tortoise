from pickle import TRUE
from django.db import models
import datetime
# Create your models here.

class BrandPlans(models.Model):
    planid=models.CharField(max_length=50,primary_key=TRUE)
    planname=models.CharField(max_length=50)
    lowtn=models.CharField(max_length=50)
    midtn=models.CharField(max_length=50)
    hightn=models.CharField(max_length=50)
    lbp=models.CharField(max_length=50)
    mbp=models.CharField(max_length=50)
    hbp=models.CharField(max_length=50)
    lowam=models.CharField(max_length=50)
    midam=models.CharField(max_length=50)
    hiam=models.CharField(max_length=50)
    quota=models.CharField(max_length=50)
    endDate=models.CharField(max_length=50)
    lpromPrcnt=models.CharField(max_length=50,default="0")
    mpromPrcnt=models.CharField(max_length=50,default="0")
    hpromPrcnt=models.CharField(max_length=50,default="0")
    ltype=models.CharField(max_length=50,default="0")
    mtype=models.CharField(max_length=50,default="0")
    htype=models.CharField(max_length=50,default="0")
    date = datetime.date(datetime.date.today().year + 100, datetime.date.today().month, datetime.date.today().day)
    quota=models.CharField(max_length=50,default=10000000000000)
    endDate=models.DateField(max_length=50,default=date)

class CustomerGoals(models.Model):
    userid=models.CharField(max_length=50,primary_key=TRUE)
    planid=models.CharField(max_length=50)
    userName=models.CharField(max_length=50)
    selectedAmount=models.CharField(max_length=50)
    selectedTenure=models.CharField(max_length=50)
    startedDate=models.CharField(max_length=50,default=datetime.date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day))
    depositedAmount=models.CharField(max_length=50)
    benefitPercentage=models.CharField(max_length=50)
    benefitType=models.CharField(max_length=50)
