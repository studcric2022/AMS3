from django.shortcuts import render,HttpResponse
import mysql.connector as sql
fn=""
ln=""
s=""
em=""
pwd=""

def register(request):
    global fn,ln,s,em,pwd
    if request.method=='POST':
        m= sql.connect(host="localhost", user="root", passwd='rohit@12356',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='firstname':
                fn=value
            if key=='lastname':
                ln=value
            if key=='sex':
                s=value        
            if key=='email':
                em=value
            if key=='password':
                pwd=value 
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()         
    return render(request,'cse/register.html')