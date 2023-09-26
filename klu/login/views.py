from django.shortcuts import render,HttpResponse
import mysql.connector as sql

em=""
pwd=""

def login(request):
    global em,pwd
    if request.method=='POST':
        m= sql.connect(host="localhost", user="root", passwd='rohit@12356',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():      
            if key=='email':
                em=value
            if key=='password':
                pwd=value 
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall()) 
        if t==():
            return render(request,'cse/login.html')
        else:
            return render(request,'cse/intro.html')
    return render(request,'cse/login.html')