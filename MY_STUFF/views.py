from django.shortcuts import render
import sqlite3
import smtplib
import random
from django.contrib import messages
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from soupsieve import select
Uname=""
Umail=""
Utype="user"
con=sqlite3.connect('Users.db',check_same_thread=False)
curs=con.cursor()
curs.execute("create table if not exists User(Name varchar(30),Age varchar(3),Dob varchar(12),Gen varchar(3),country varchar(3),mono varchar(15),Userid varchar(50),password varchar(25),Address varchar(150),oncart varchar(1000),OrderHist varchar(1000))")
curs.execute("create table if not exists Seller(scode varchar(6),Name varchar(30),Age varchar(3),Dob varchar(12),Gen varchar(3),country varchar(3),mono varchar(15),Userid varchar(50),password varchar(25),Address varchar(150),orders varchar(1000),oncart varchar(1000),OrderHist varchar(1000))")
curs.execute("create table if not exists CEO(rachasc vr(6),Name varchar(30),Age varchar(3),Dob varchar(12),Gen varchar(3),country varchar(3),mono varchar(15),Userid varchar(50),password varchar(25),Address varchar(150),orders varchar(1000),oncart varchar(250),OrderHist varchar(1000))")
curs.execute("create table if not exists Grocery(sc varchar(6),Cat varchar(25),Name varchar(30),price varchar(10),description varchar(100),brand varchar(25),pcs varchar(10),quant varchar(10),img varchar(100),onoffer varchar(10))")
curs.execute("create table if not exists Clothes(sc varchar(6),Cat varchar(25),Name varchar(30),price varchar(10),description varchar(100),brand varchar(25),size varchar(10),mat varchar(10),design varchar(25),quant varchar(50),img varchar(100),onoffer varchar(10))")
curs.execute("create table if not exists Accessories(sc varchar(6),Cat varchar(25),Name varchar(30),price varchar(10),description varchar(100),brand varchar(25),quant varchar(10),img varchar(100),onoffer varchar(10))")
curs.execute("create table if not exists Laptop(sc varchar(6),Cat varchar(25),Name varchar(30),price varchar(10),description varchar(100),brand varchar(25),ram varchar(10),proc varchar(25),hdd varchar(10),ssd varchar(10),gprocs varchar(25),batry varchar(15),disp varchar(25),quant varchar(10),img varchar(100),onoffer varchar(10))")
curs.execute("create table if not exists Mobile(sc varchar(6),Cat varchar(25),Name varchar(30),price varchar(10),description varchar(100),brand varchar(25),ram varchar(10),proc varchar(25),rom varchar(10),rc varchar(10),fc varchar(25),batry varchar(15),disp varchar(25),quant varchar(10),img varchar(100),onoffer varchar(10))")
con.commit()
Acc=curs.execute("select * from CEO")
Accs=Acc.fetchall()
if(Accs==[]):
	curs.execute("insert into CEO values('RS01','RishiChaaryS','19','01/09/2003','M','India','9384179855','rishichaary1903@gmail.com','1903king','5/704,162A,kcc nagar,hosur','','','')")
	con.commit()
global final
global final1
global final2
global final3
global final4
curs.execute("select * from Mobile where onoffer =='on'")
dit={}
final=[]
ad=curs.fetchall()
for i in range(0,len(ad)):
	sc1=ad[i][0]
	ct1=ad[i][1]
	nm1=ad[i][2]
	em1=ad[i][3]
	sb1=ad[i][5]
	bd1=ad[i][13]
	dit={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
	final.append(dit)
curs.execute("select * from Laptop where onoffer =='on'")
dit1={}
final1=[]
ad=curs.fetchall()
for i in range(0,len(ad)):
	sc1=ad[i][0]
	ct1=ad[i][1]
	nm1=ad[i][2]
	em1=ad[i][3]
	sb1=ad[i][5]
	bd1=ad[i][14]
	dit1={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
	final1.append(dit1)
curs.execute("select * from Accessories where onoffer =='on'")
dit2={}
final2=[]
ad=curs.fetchall()
for i in range(0,len(ad)):
	sc1=ad[i][0]
	ct1=ad[i][1]
	nm1=ad[i][2]
	em1=ad[i][3]
	sb1=ad[i][5]
	bd1=ad[i][7]
	dit2={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
	final2.append(dit2)
curs.execute("select * from Clothes where onoffer =='on'")
dit3={}
final3=[]
ad=curs.fetchall()
for i in range(0,len(ad)):
	sc1=ad[i][0]
	ct1=ad[i][1]
	nm1=ad[i][2]
	em1=ad[i][3]
	sb1=ad[i][5]
	bd1=ad[i][10]
	dit3={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
	final3.append(dit3)
curs.execute("select * from Grocery where onoffer =='on'")
dit4={}
final4=[]
ad=curs.fetchall()
for i in range(0,len(ad)):
	sc1=ad[i][0]
	ct1=ad[i][1]
	nm1=ad[i][2]
	em1=ad[i][3]
	sb1=ad[i][5]
	bd1=ad[i][8]
	dit4={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
	final4.append(dit4)
def Home(request):
	test=curs.execute("select oncart from ceo")
	teres=test.fetchall()
	Name=str(request.POST.get("Home"))
	if request.method=="POST":
		Lgcred=Name.split(',')
		curs.execute("select * from Mobile where onoffer =='on'")
		dit={}
		final=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][13]
			dit={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final.append(dit)
		curs.execute("select * from Laptop where onoffer =='on'")
		dit1={}
		final1=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][14]
			dit1={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final1.append(dit1)
		curs.execute("select * from Accessories where onoffer =='on'")
		dit2={}
		final2=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][7]
			dit2={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final2.append(dit2)
		curs.execute("select * from Clothes where onoffer =='on'")
		dit3={}
		final3=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][10]
			dit3={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final3.append(dit3)
		curs.execute("select * from Grocery where onoffer =='on'")
		dit4={}
		final4=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][8]
			dit4={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final4.append(dit4)
		return render(request, 'Home.html',{ "Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2],'Details':final,'Details1':final1,'Details2':final2,'Details3':final3,'Details4':final4})
	else:
		curs.execute("select * from Mobile where onoffer =='on'")
		dit={}
		final=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][13]
			dit={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final.append(dit)
		curs.execute("select * from Laptop where onoffer =='on'")
		dit1={}
		final1=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][14]
			dit1={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final1.append(dit1)
		curs.execute("select * from Accessories where onoffer =='on'")
		dit2={}
		final2=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][7]
			dit2={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final2.append(dit2)
		curs.execute("select * from Clothes where onoffer =='on'")
		dit3={}
		final3=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][10]
			dit3={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final3.append(dit3)
		curs.execute("select * from Grocery where onoffer =='on'")
		dit4={}
		final4=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][8]
			dit4={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final4.append(dit4)
		return render(request, 'Home.html',{"Name":"1",'Details':final,'Details1':final1,'Details2':final2,'Details3':final3,'Details4':final4})
def Mobile(request):
	global final
	global final1
	global final2
	global final3
	global final4
	final=[]
	final1=[]
	final2=[]
	final3=[]
	final4=[]
	Name=str(request.POST.get("Home"))
	if request.method=="POST":
		Lgcred=Name.split(',')
		B={'Name':[],'Brand':[],"Img":[]}
		for i in Accs:
			B['Name'].append(i[1])
			B['Brand'].append(i[4])
			B['Img'].append(i[-3])
		A=open("Lsav.txt","r")
		Ac=A.read()
		Acl=Ac.split(" ")
		if(Acl==['']):
			Uname=''
			Umail=''
			Utype=''
		else:
			Uname=Acl[0]
			Umail=Acl[1]
			Utype=Acl[2]
		curs.execute("select * from Mobile")
		ditmob={}
		nm=[]
		em=[]
		sb=[]
		bd=[]
		dt=[]
		finalmob=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][13]
			ditmob={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			finalmob.append(ditmob)
		return render(request, 'Home.html',{ "Name":Lgcred[0],"User":Lgcred[1],"languages":["Ate","Bat","Cat"],"Type":Lgcred[2],"prd":B,'Page':"Mobile",'Details':finalmob,})
	else:
		return render(request, 'Home.html',{"Name":"1",'Page':"Mobile"})
def Laptop(request):
	global final
	global final1
	global final2
	global final3
	global final4
	Acc=curs.execute("select * from mobile")
	Accs=Acc.fetchall()
	B={'Name':[],'Brand':[],"Img":[]}
	for i in Accs:
		B['Name'].append(i[1])
		B['Brand'].append(i[4])
		B['Img'].append(i[-3])
	A=open("Lsav.txt","r")
	Ac=A.read()
	Acl=Ac.split(" ")
	if(Acl==['']):
		Uname=''
		Umail=''
		Utype=''
	else:
		Uname=Acl[0]
		Umail=Acl[1]
		Utype=Acl[2]
	curs.execute("select * from Laptop")
	ditlap={}
	nm=[]
	em=[]
	sb=[]
	bd=[]
	dt=[]
	finallap=[]
	ad=curs.fetchall()
	for i in range(0,len(ad)):
		sc1=ad[i][0]
		ct1=ad[i][1]
		nm1=ad[i][2]
		em1=ad[i][3]
		sb1=ad[i][5]
		bd1=ad[i][14]
		ditlap={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
		finallap.append(ditlap)
	return render(request,'Home.html',{"Name":Uname,"User":Umail,"languages":["Ate","Bat","Cat"],"Type":Utype,"prd":B,'Page':"Laptop",'Details':finallap,})
def Accessories(request):
	global final
	global final1
	global final2
	global final3
	global final4
	Acc=curs.execute("select * from mobile")
	Accs=Acc.fetchall()
	B={'Name':[],'Brand':[],"Img":[]}
	for i in Accs:
		B['Name'].append(i[1])
		B['Brand'].append(i[4])
		B['Img'].append(i[-3])
	A=open("Lsav.txt","r")
	Ac=A.read()
	Acl=Ac.split(" ")
	if(Acl==['']):
		Uname=''
		Umail=''
		Utype=''
	else:
		Uname=Acl[0]
		Umail=Acl[1]
		Utype=Acl[2]
	curs.execute("select * from Accessories")
	ditacc={}
	nm=[]
	em=[]
	sb=[]
	bd=[]
	dt=[]
	finalacc=[]
	ad=curs.fetchall()
	for i in range(0,len(ad)):
		sc1=ad[i][0]
		ct1=ad[i][1]
		nm1=ad[i][2]
		em1=ad[i][3]
		sb1=ad[i][5]
		bd1=ad[i][7]
		ditacc={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
		finalacc.append(ditacc)
	return render(request,'Home.html',{"Name":Uname,"User":Umail,"languages":["Ate","Bat","Cat"],"Type":Utype,"prd":B,'Page':"Accessories",'Details':finalacc,})
def Clothes(request):
	global final
	global final1
	global final2
	global final3
	global final4
	Acc=curs.execute("select * from mobile")
	Accs=Acc.fetchall()
	B={'Name':[],'Brand':[],"Img":[]}
	for i in Accs:
		B['Name'].append(i[1])
		B['Brand'].append(i[4])
		B['Img'].append(i[-3])
	A=open("Lsav.txt","r")
	Ac=A.read()
	Acl=Ac.split(" ")
	if(Acl==['']):
		Uname=''
		Umail=''
		Utype=''
	else:
		Uname=Acl[0]
		Umail=Acl[1]
		Utype=Acl[2]
	curs.execute("select * from Clothes")
	ditclo={}
	nm=[]
	em=[]
	sb=[]
	bd=[]
	dt=[]
	finalclo=[]
	ad=curs.fetchall()
	for i in range(0,len(ad)):
		sc1=ad[i][0]
		ct1=ad[i][1]
		nm1=ad[i][2]
		em1=ad[i][3]
		sb1=ad[i][5]
		bd1=ad[i][10]
		ditclo={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
		finalclo.append(ditclo)
	return render(request,'Home.html',{"Name":Uname,"User":Umail,"languages":["Ate","Bat","Cat"],"Type":Utype,"prd":B,'Page':"Clothes",'Details':finalclo,})
def Grocery(request):
	global final
	global final1
	global final2
	global final3
	global final4
	Acc=curs.execute("select * from mobile")
	Accs=Acc.fetchall()
	B={'Name':[],'Brand':[],"Img":[]}
	for i in Accs:
		B['Name'].append(i[1])
		B['Brand'].append(i[4])
		B['Img'].append(i[-3])
	A=open("Lsav.txt","r")
	Ac=A.read()
	Acl=Ac.split(" ")
	if(Acl==['']):
		Uname=''
		Umail=''
		Utype=''
	else:
		Uname=Acl[0]
		Umail=Acl[1]
		Utype=Acl[2]
	curs.execute("select * from Grocery")
	ditgro={}
	nm=[]
	em=[]
	sb=[]
	bd=[]
	dt=[]
	finalgro=[]
	ad=curs.fetchall()
	for i in range(0,len(ad)):
		sc1=ad[i][0]
		ct1=ad[i][1]
		nm1=ad[i][2]
		em1=ad[i][3]
		sb1=ad[i][5]
		bd1=ad[i][8]
		ditgro={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
		finalgro.append(ditgro)
	return render(request,'Home.html',{"Name":Uname,"User":Umail,"languages":["Ate","Bat","Cat"],"Type":Utype,"prd":B,'Page':"Grocery",'Details':finalgro,})
def Oa(request):
	if request.method=="POST":
		Orderrs=[]
		Userdet=str(request.POST.get("Home"))
		Userr=Userdet.split(",")
		if(Userr[2]=="ceo"):
			curs.execute("select orderhist from ceo")
			deta=curs.fetchall()
			detadata=deta[0][0].split("|")
			for i in range(0,len(detadata)-1):
				b=detadata[i].split(",")
				if(b[1]=="MOBILE"):
					curs.execute("select * from MOBILE where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="LAPTOP"):
					curs.execute("select * from LAPTOP where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="GROCERY"):
					curs.execute("select * from GROCERY where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][8],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="CLOTHES"):
					curs.execute("select * from CLOTHES where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][10],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="ACCESSORIES"):
					curs.execute("select * from ACCESSORIES where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][7],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
		elif(Userr[2]=="seller"):
			curs.execute("select orderhist from seller")
			deta=curs.fetchall()
			detadata=deta[0][0].split("|")
			for i in range(0,len(detadata)-1):
				b=detadata[i].split(",")
				if(b[1]=="MOBILE"):
					curs.execute("select * from MOBILE where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="LAPTOP"):
					curs.execute("select * from LAPTOP where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="GROCERY"):
					curs.execute("select * from GROCERY where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][8],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="CLOTHES"):
					curs.execute("select * from CLOTHES where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][10],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="ACCESSORIES"):
					curs.execute("select * from ACCESSORIES where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][7],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
		elif(Userr[2]=="user"):
			curs.execute("select orderhist from user")
			deta=curs.fetchall()
			detadata=deta[0][0].split("|")
			for i in range(0,len(detadata)-1):
				b=detadata[i].split(",")
				if(b[1]=="MOBILE"):
					curs.execute("select * from MOBILE where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="LAPTOP"):
					curs.execute("select * from LAPTOP where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="GROCERY"):
					curs.execute("select * from GROCERY where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][8],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="CLOTHES"):
					curs.execute("select * from CLOTHES where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][10],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
				elif(b[1]=="ACCESSORIES"):
					curs.execute("select * from ACCESSORIES where name='{}' and sc='{}'".format(b[2],b[0]))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][7],"Seller":delt[0][0],"Cata":delt[0][1]}
					Orderrs.append(ordit)
		return render(request,'Home.html',{"Name":Userr[0],"User":Userr[1],"Type":Userr[2],'Page':"OA",'Details':Orderrs})
	else:
		return render(request,'Home.html',{"Name":Userr[0],"User":Userr[1],"Type":Userr[2],'Page':"OA",'Details':Orderrs})
def Sr(request):
	Results=[]
	if request.method=="POST":
		Userdet=str(request.POST.get("Home"))
		SrchReq=str(request.POST.get("ser"))
		Userr=Userdet.split(",")
		curs.execute("select * from GROCERY")
		Grocery=curs.fetchall()
		curs.execute("select * from CLOTHES")
		Clothes=curs.fetchall()
		curs.execute("select * from ACCESSORIES")
		Accessories=curs.fetchall()
		curs.execute("select * from MOBILE")
		Mobile=curs.fetchall()
		curs.execute("select * from LAPTOP")
		Laptop=curs.fetchall()
		if(len(Grocery)!=0):
			for i in range(0,len(Grocery)):
				if(SrchReq==Grocery[i][2]):
					curs.execute("select * from GROCERY where name='{}'".format(SrchReq))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][8],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
		if(len(Clothes)!=0):
			for i in range(0,len(Clothes)):
				if(SrchReq==Clothes[i][2]):
					curs.execute("select * from CLOTHES where name='{}'".format(SrchReq))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][10],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
		if(len(Accessories)!=0):
			for i in range(0,len(Accessories)):
				if(SrchReq==Accessories[i][2]):
					curs.execute("select * from ACCESSORIES where name='{}'".format(SrchReq))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][7],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
		if(len(Mobile)!=0):
			for i in range(0,len(Mobile)):
				print(SrchReq,Mobile[i][2])
				if(SrchReq==Mobile[i][2]):
					curs.execute("select * from MOBILE where name='{}'".format(SrchReq))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					print(ordit)
					Results.append(ordit)
		if(len(Laptop)!=0):
			for i in range(0,len(Laptop)):
				if(SrchReq==Laptop[i][2]):
					curs.execute("select * from LAPTOP where name='{}'".format(SrchReq))
					delt=curs.fetchall()
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
		if(Results==[]):
			return render(request,'Home.html',{"Name":Userr[0],"User":Userr[1],"Res":"No","Type":Userr[2],'Page':"SR",'Details':Results})
		else:
			return render(request,'Home.html',{"Name":Userr[0],"User":Userr[1],"Res":"Yes","Type":Userr[2],'Page':"SR",'Details':Results})
	else:
		return render(request,'Home.html',{"Name":Userr[0],"User":Userr[1],"Type":Userr[2],'Page':"SR",'Details':Results})
def View(request,product=""):
	product=str(request.POST.get("Prdname"))
	if request.method=="POST":
		products=product.split(',')
		if(products[1]=="GROCERY"):
			curs.execute("select * from {} where sc=='{}' and Name=='{}'".format(products[1],products[0],products[2]))
			finalgro1=[]
			finalgro=[]
			ad=curs.fetchall()
			for i in range(0,len(ad)):
				sc1=ad[i][0]
				ct1=ad[i][1]
				nm1=ad[i][2]
				em1=ad[i][3]
				fd1=ad[i][4]
				sb1=ad[i][5]
				fg1=ad[i][6]
				dg1=ad[i][7]
				bd1=ad[i][8]
				ditgro1={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Quant':fg1,'Brand':sb1,'Details':fd1,'Image':bd1}
				finalgro1.append(ditgro1)
			curs.execute("select * from Grocery")
			ad=curs.fetchall()
			for i in range(0,len(ad)):
				sc1=ad[i][0]
				ct1=ad[i][1]
				nm1=ad[i][2]
				em1=ad[i][3]
				sb1=ad[i][5]
				bd1=ad[i][8]
				ditgro={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
				finalgro.append(ditgro)
		elif(products[1]=="CLOTHES"):
			finalgro=[]
			curs.execute("select * from Clothes")
			ad=curs.fetchall()
			ditclo={}
			nm=[]
			em=[]
			sb=[]
			bd=[]
			dt=[]
			for i in range(0,len(ad)):
				sc1=ad[i][0]
				ct1=ad[i][1]
				nm1=ad[i][2]
				em1=ad[i][3]
				sb1=ad[i][5]
				bd1=ad[i][10]
				ditclo={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
				finalgro.append(ditclo)
			curs.execute("select * from {} where sc=='{}' and Name=='{}'".format(products[1],products[0],products[2]))
			finalgro1=[]
			ad=curs.fetchall()
			for i in range(0,len(ad)):
				sc1=ad[i][0]
				ct1=ad[i][1]
				nm1=ad[i][2]
				em1=ad[i][3]
				fd1=ad[i][4]
				sb1=ad[i][5]
				fg1=ad[i][6]
				dg1=ad[i][7]
				de1=ad[i][8]
				bd1=ad[i][10]
				ditgro1={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Size':fg1,'Mat':dg1,'Des':de1,'Brand':sb1,'Details':fd1,'Image':bd1}
				finalgro1.append(ditgro1)
		elif(products[1]=="ACCESSORIES"):
			curs.execute("select * from Accessories")
			ditacc={}
			nm=[]
			em=[]
			sb=[]
			bd=[]
			dt=[]
			finalgro=[]
			ad=curs.fetchall()
			for i in range(0,len(ad)):
				sc1=ad[i][0]
				ct1=ad[i][1]
				nm1=ad[i][2]
				em1=ad[i][3]
				sb1=ad[i][5]
				bd1=ad[i][7]
				ditacc={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
				finalgro.append(ditacc)
			curs.execute("select * from {} where sc=='{}' and Name=='{}'".format(products[1],products[0],products[2]))
			finalgro1=[]
			ad=curs.fetchall()
			for i in range(0,len(ad)):
				sc1=ad[i][0]
				ct1=ad[i][1]
				nm1=ad[i][2]
				em1=ad[i][3]
				fd1=ad[i][4]
				sb1=ad[i][5]
				bd1=ad[i][7]
				ditgro1={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Details':fd1,'Image':bd1}
				finalgro1.append(ditgro1)
		elif(products[1]=="MOBILE"):
			curs.execute("select * from Mobile")
			ditmob={}
			nm=[]
			em=[]
			sb=[]
			bd=[]
			dt=[]
			finalgro=[]
			ad=curs.fetchall()
			for i in range(0,len(ad)):
				sc1=ad[i][0]
				ct1=ad[i][1]
				nm1=ad[i][2]
				em1=ad[i][3]
				sb1=ad[i][5]
				bd1=ad[i][13]
				ditmob={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
				finalgro.append(ditmob)
			curs.execute("select * from {} where sc=='{}' and Name=='{}'".format(products[1],products[0],products[2]))
			finalgro1=[]
			ad=curs.fetchall()
			for i in range(0,len(ad)):
				sc1=ad[i][0]
				ct1=ad[i][1]
				nm1=ad[i][2]
				em1=ad[i][3]
				fd1=ad[i][4]
				sb1=ad[i][5]
				fg1=ad[i][6]
				dg1=ad[i][7]
				de1=ad[i][8]
				rc1=ad[i][9]
				fc1=ad[i][10]
				ba1=ad[i][11]
				dp1=ad[i][12]
				bd1=ad[i][13]
				ditgro1={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Details':fd1,'Ram':fg1,'Proc':de1,'Rom':dg1,'Rc':rc1,'Fc':fc1,'Bat':ba1,'Dp':dp1,'Image':bd1}
				finalgro1.append(ditgro1)
		elif(products[1]=="LAPTOP"):
			curs.execute("select * from Laptop")
			ditlap={}
			nm=[]
			em=[]
			sb=[]
			bd=[]
			dt=[]
			finalgro=[]
			ad=curs.fetchall()
			for i in range(0,len(ad)):
				sc1=ad[i][0]
				ct1=ad[i][1]
				nm1=ad[i][2]
				em1=ad[i][3]
				sb1=ad[i][5]
				bd1=ad[i][14]
				ditlap={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
				finalgro.append(ditlap)
			curs.execute("select * from {} where sc=='{}' and Name=='{}'".format(products[1],products[0],products[2]))
			finalgro1=[]
			ad=curs.fetchall()
			for i in range(0,len(ad)):
				sc1=ad[i][0]
				ct1=ad[i][1]
				nm1=ad[i][2]
				em1=ad[i][3]
				fd1=ad[i][4]
				sb1=ad[i][5]
				fg1=ad[i][6]
				dg1=ad[i][7]
				de1=ad[i][8]
				rc1=ad[i][9]
				fc1=ad[i][10]
				ba1=ad[i][11]
				dp1=ad[i][12]
				bd1=ad[i][14]
				ditgro1={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Details':fd1,'Ram':fg1,'Proc':de1,'Hdd':dg1,'Ssd':rc1,'Gproc':fc1,'Bat':ba1,'Dp':dp1,'Image':bd1}
				finalgro1.append(ditgro1)
		return render(request,"View.html",{"Name":Uname,"User":Umail,"Type":Utype,"Product":finalgro1,"Prd":finalgro})
	else:
		return render(request,"View.html",{"Product":product})
def Orders(request):
	Name=str(request.POST.get("Order"))
	Lgcred=Name.split(',')
	final=[]
	if request.method=="POST":
		if(Lgcred[2]=="seller"):
			curs.execute("select orders from seller where Name='{}' and Userid='{}'".format(Lgcred[0],Lgcred[1]))
			imp=curs.fetchall()
			impdet=imp[0][0].split("|")
			if(len(impdet)==1):
				ste="Empty"
			else:
				ste="NotEmpty"
			for i in range (0,len(impdet)-1):
				impp=impdet[i].split(",")
				ad=impp[6:len(impp)-2]
				addres=''
				for jk in range(0,len(ad)):
					if(jk!=len(ad)-1):
						addres=addres+str(ad[jk])+","
					else:
						addres=addres+str(ad[jk])
				if(impp[1]=="GROCERY"):
					curs.execute("select * from grocery where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][8],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="CLOTHES"):
					curs.execute("select * from clothes where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][10],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="MOBILE"):
					curs.execute("select * from mobile where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][13],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="LAPTOP"):
					curs.execute("select * from laptop where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][14],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="ACCESSORIES"):
					curs.execute("select * from accessories where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][7],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
			return render(request, 'Orders.html',{"Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2],"State":ste,"Prds":final})
		elif(Lgcred[2]=="ceo"):
			curs.execute("select orders from ceo where Name='{}' and Userid='{}'".format(Lgcred[0],Lgcred[1]))
			imp=curs.fetchall()
			impdet=imp[0][0].split("|")
			if(len(impdet)==1):
				ste="Empty"
			else:
				ste="NotEmpty"
			for i in range (0,len(impdet)-1):
				impp=impdet[i].split(",")
				ad=impp[6:len(impp)-2]
				addres=''
				for jk in range(0,len(ad)):
					if(jk!=len(ad)-1):
						addres=addres+str(ad[jk])+","
					else:
						addres=addres+str(ad[jk])
				if(impp[1]=="GROCERY"):
					curs.execute("select * from grocery where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][8],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="CLOTHES"):
					curs.execute("select * from clothes where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][10],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="MOBILE"):
					curs.execute("select * from mobile where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][13],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="LAPTOP"):
					curs.execute("select * from laptop where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][14],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="ACCESSORIES"):
					curs.execute("select * from accessories where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][7],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
			return render(request, 'Orders.html',{"Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2],"State":ste,"Prds":final})
		return render(request, 'Orders.html',{"Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2]})
	else:
		return render(request,'Orders.html',{})
def Cart(request):
	if request.method=="POST":
		Name=str(request.POST.get("Cart"))
		Lgcred=Name.split(',')
		curs.execute("select * from user")
		usr=curs.fetchall()
		curs.execute("select * from Seller")
		slr=curs.fetchall()
		curs.execute("select * from CEO")
		co=curs.fetchall()
		curs.execute("select * from grocery")
		gro=curs.fetchall()
		if(str(Lgcred[0])=='n'or Lgcred[1]=='n'or Lgcred[2]=='n'):
			pass
		else:
			qt=str(request.POST.get("Qnty"))
			if(int(qt)<10):
				oncrt=str(Lgcred[0])+","+str(Lgcred[1])+","+str(Lgcred[2])+",0"+str(qt)+"|"
			else:
				oncrt=str(Lgcred[0])+","+str(Lgcred[1])+","+str(Lgcred[2])+","+str(qt)+"|"
			onorders=str(Lgcred[0])+","+str(Lgcred[1])+","+str(Lgcred[2])+","+str(qt)+","+str(Lgcred[3])+","+str(Lgcred[4])+"|"
			if(Lgcred[5]=="user"):
				for i in range (0,len(usr)):
					if(usr[i][0]==Lgcred[3] and usr[i][6]==Lgcred[4]):
						curs.execute("select oncart from user where Name='{}' and Userid='{}'".format(Lgcred[3],Lgcred[4]))
						b=curs.fetchall()
						curs.execute("update user set oncart='{}' where Name='{}' and Userid='{}'".format(str(b[0][0])+oncrt,Lgcred[3],Lgcred[4]))
						con.commit()
			elif(Lgcred[5]=="seller"):
				for i in range (0,len(slr)):
					if(slr[i][1]==Lgcred[3] and slr[i][7]==Lgcred[4]):
						curs.execute("select oncart from seller where Name='{}' and Userid='{}'".format(Lgcred[3],Lgcred[4]))
						b=curs.fetchall()
						curs.execute("update seller set oncart='{}' where Name='{}' and Userid='{}'".format(str(b[0][0])+oncrt,Lgcred[3],Lgcred[4]))
						con.commit()
			elif(co[0][1]==Lgcred[3] and co[0][7]==Lgcred[4]):
				curs.execute("select oncart from ceo where Name='{}' and Userid='{}'".format(Lgcred[3],Lgcred[4]))
				b=curs.fetchall()
				curs.execute("update ceo set oncart='{}' where Name='{}' and Userid='{}'".format(str(b[0][0])+oncrt,Lgcred[3],Lgcred[4]))
				con.commit()
		final=[]
		if(Lgcred[5]=="user"):
			for i in range (0,len(usr)):
				if(usr[i][0]==Lgcred[3] and usr[i][6]==Lgcred[4]):
					curs.execute("select oncart from user where Name='{}' and Userid='{}'".format(Lgcred[3],Lgcred[4]))
					imp=curs.fetchall()
					impdet=imp[0][0].split("|")
					if(len(impdet)==1):
						ste="Empty"
					else:
						ste="NotEmpty"
					for i in range (0,len(impdet)-1):
						impp=impdet[i].split(",")
						if(impp[1]=="GROCERY"):
							curs.execute("select * from grocery where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][8]}
							final.append(res)
						elif(impp[1]=="CLOTHES"):
							curs.execute("select * from clothes where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][10]}
							final.append(res)
						elif(impp[1]=="MOBILE"):
							curs.execute("select * from mobile where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][13]}
							final.append(res)
						elif(impp[1]=="LAPTOP"):
							curs.execute("select * from laptop where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][14]}
							final.append(res)
						elif(impp[1]=="ACCESSORIES"):
							curs.execute("select * from accessories where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][7]}
							final.append(res)
					return render(request, 'Cart.html',{"Name":Lgcred[3],"User":Lgcred[4],"Type":Lgcred[5],"State":ste,"Prds":final})
		elif(Lgcred[5]=="seller"):
			for i in range (0,len(usr)):
				if(usr[i][0]==Lgcred[3] and usr[i][6]==Lgcred[4]):
					curs.execute("select oncart from seller where Name='{}' and Userid='{}'".format(Lgcred[3],Lgcred[4]))
					imp=curs.fetchall()
					impdet=imp[0][0].split("|")
					if(len(impdet)==1):
						ste="Empty"
					else:
						ste="NotEmpty"
					for i in range (0,len(impdet)-1):
						impp=impdet[i].split(",")
						if(impp[1]=="GROCERY"):
							curs.execute("select * from grocery where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][8]}
							final.append(res)
						elif(impp[1]=="CLOTHES"):
							curs.execute("select * from clothes where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][10]}
							final.append(res)
						elif(impp[1]=="MOBILE"):
							curs.execute("select * from mobile where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][13]}
							final.append(res)
						elif(impp[1]=="LAPTOP"):
							curs.execute("select * from laptop where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][14]}
							final.append(res)
						elif(impp[1]=="ACCESSORIES"):
							curs.execute("select * from accessories where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][7]}
							final.append(res)
					return render(request, 'Cart.html',{"Name":Lgcred[3],"User":Lgcred[4],"Type":Lgcred[5],"State":ste,"Prds":final})
		elif(co[0][1]==Lgcred[3] and co[0][7]==Lgcred[4]):
			curs.execute("select oncart from ceo where Name='{}' and Userid='{}'".format(Lgcred[3],Lgcred[4]))
			imp=curs.fetchall()
			impdet=imp[0][0].split("|")
			if(len(impdet)==1):
				ste="Empty"
			else:
				ste="NotEmpty"
			for i in range (0,len(impdet)-1):
				impp=impdet[i].split(",")
				if(impp[1]=="GROCERY"):
					curs.execute("select * from grocery where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][8]}
					final.append(res)
				elif(impp[1]=="CLOTHES"):
					curs.execute("select * from clothes where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][10]}
					final.append(res)
				elif(impp[1]=="MOBILE"):
					curs.execute("select * from mobile where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][13]}
					final.append(res)
				elif(impp[1]=="LAPTOP"):
					curs.execute("select * from laptop where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][14]}
					final.append(res)
				elif(impp[1]=="ACCESSORIES"):
					curs.execute("select * from accessories where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][7]}
					final.append(res)
			return render(request, 'Cart.html',{"Name":Lgcred[3],"User":Lgcred[4],"Type":Lgcred[5],"State":ste,"Prds":final})
		return render(request, 'Cart.html',{"Name":Lgcred[3],"User":Lgcred[4],"Type":Lgcred[5]})
	else:
		return render(request,'Cart.html',{})
def Product(request):
	Name=str(request.POST.get("Addp"))
	if request.method=="POST":
		Lgcred=Name.split(',')
		return render(request, 'AddProduct.html',{"Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2]})
	else:
		return render(request, 'AddProduct.html',{})
def AddProduct(request,):
	Name=str(request.POST.get("opu"))
	if request.method=="POST":
		Lgcred=Name.split(',')
		SC=str(request.POST.get("Sellcd"))
		CT=str(request.POST.get("cat"))
		if(CT=="GROCERY"):
			Pn=str(request.POST.get("Pn"))
			Pp=str(request.POST.get("Pp"))
			Pd=str(request.POST.get("Pd"))
			Pb=str(request.POST.get("Pb"))
			P1=str(request.POST.get("P1"))
			quant=str(request.POST.get("Qs"))
			myfile = request.FILES['Po']
			fs = FileSystemStorage()
			fnme=myfile.name.split(".")
			file=SC+Pn+" "+fnme[0]+"."+fnme[1]
			filename = fs.save(file, myfile)
			uploaded_file_url = fs.url(filename)
			curs.execute("insert into Grocery values('{}','{}','{}','{}','{}','{}','{}','{}','{}','on')".format(SC,CT,Pn,Pp,Pd,Pb,P1,quant,file))
			con.commit()
			return render(request, 'AddProduct.html',{"Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2]})
		elif(CT=="CLOTHES"):
			Pn=str(request.POST.get("Pn"))
			Pp=str(request.POST.get("Pp"))
			Pd=str(request.POST.get("Pd"))
			Pb=str(request.POST.get("Pb"))
			P1=str(request.POST.get("P1"))
			P2=str(request.POST.get("P2"))
			P3=str(request.POST.get("P3"))
			Size1=str(request.POST.get("Sz1"))
			Size2=str(request.POST.get("Sz2"))
			Size3=str(request.POST.get("Sz3"))
			Size4=str(request.POST.get("Sz4"))
			Size5=str(request.POST.get("Sz5"))
			Quant1=str(request.POST.get("Qs1"))
			Quant2=str(request.POST.get("Qs2"))
			Quant3=str(request.POST.get("Qs3"))
			Quant4=str(request.POST.get("Qs4"))
			Quant5=str(request.POST.get("Qs5"))
			quant=Size1+":"+Quant1+","+Size2+":"+Quant2+","+Size3+":"+Quant3+","+Size4+":"+Quant4+","+Size5+":"+Quant5
			myfile = request.FILES['Po']
			fs = FileSystemStorage()
			fnme=myfile.name.split(".")
			file=SC+Pn+" "+fnme[0]+"."+fnme[1]
			filename = fs.save(file, myfile)
			uploaded_file_url = fs.url(filename)
			curs.execute("insert into clothes values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','on')".format(SC,CT,Pn,Pp,Pd,Pb,P1,P2,P3,quant,file))
			con.commit()
			return render(request, 'AddProduct.html',{"Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2]})
		elif(CT=="ACCESSORIES"):
			Pn=str(request.POST.get("Pn"))
			Pp=str(request.POST.get("Pp"))
			Pd=str(request.POST.get("Pd"))
			Pb=str(request.POST.get("Pb1"))
			quant=str(request.POST.get("Qs"))
			myfile = request.FILES['Po']
			fs = FileSystemStorage()
			fnme=myfile.name.split(".")
			file=SC+Pn+" "+fnme[0]+"."+fnme[1]
			filename = fs.save(file, myfile)
			uploaded_file_url = fs.url(filename)
			curs.execute("insert into Accessories values('{}','{}','{}','{}','{}','{}','{}','{}','on')".format(SC,CT,Pn,Pp,Pd,Pb,quant,file))
			con.commit()
			return render(request, 'AddProduct.html',{"Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2]})
		elif(CT=="MOBILE"):
			Pn=str(request.POST.get("Pn"))
			Pp=str(request.POST.get("Pp"))
			Pd=str(request.POST.get("Pd"))
			Pb=str(request.POST.get("Pb1"))
			quant=str(request.POST.get("Qs"))
			P1=str(request.POST.get("P1"))
			P2=str(request.POST.get("P2"))
			P3=str(request.POST.get("P3"))
			P4=str(request.POST.get("P4"))
			P5=str(request.POST.get("P5"))
			P6=str(request.POST.get("P6"))
			P7=str(request.POST.get("P7"))
			myfile = request.FILES['Po']
			fs = FileSystemStorage()
			fnme=myfile.name.split(".")
			file=SC+Pn+" "+fnme[0]+"."+fnme[1]
			filename = fs.save(file, myfile)
			uploaded_file_url = fs.url(filename)
			curs.execute("insert into Mobile values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','on')".format(SC,CT,Pn,Pp,Pd,Pb,P1,P2,P3,P4,P5,P6,P7,uploaded_file_url,quant))
			con.commit()
			return render(request, 'AddProduct.html',{"Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2]})
		elif(CT=="LAPTOP"):
			Pn=str(request.POST.get("Pn"))
			Pp=str(request.POST.get("Pp"))
			Pd=str(request.POST.get("Pd"))
			Pb=str(request.POST.get("Pb1"))
			P1=str(request.POST.get("P1"))
			P2=str(request.POST.get("P2"))
			P3=str(request.POST.get("P3"))
			P4=str(request.POST.get("P4"))
			P5=str(request.POST.get("P5"))
			P6=str(request.POST.get("P6"))
			P7=str(request.POST.get("P7"))
			quant=str(request.POST.get("Qs"))
			myfile = request.FILES['Po']
			fs = FileSystemStorage()
			fnme=myfile.name.split(".")
			file=SC+Pn+" "+fnme[0]+"."+fnme[1]
			filename = fs.save(file, myfile)
			uploaded_file_url = fs.url(filename)
			curs.execute("insert into Laptop values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','on')".format(SC,CT,Pn,Pp,Pd,Pb,P2,P3,P1,P4,P5,P6,P7,quant,file))
			con.commit()
			return render(request, 'AddProduct.html',{"Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2]})
		else:
			pass
	else:
		return render(request, 'AddProduct.html',{})
def User(request):
	Name=str(request.POST.get("Addu"))
	if request.method=="POST":
		Lgcred=Name.split(',')
		return render(request, 'AddUser.html',{"Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2]})
	else:
		return render(request, 'AddUser.html',{})
def AddUser(request):
	global Fn
	global Ln
	global Age
	global Dob
	global Gen
	global Cunt
	global Mob
	global Mail
	global Password
	global otp6
	global otp
	global capt
	global Adrs
	Name=str(request.POST.get("Addu"))
	Fn=str(request.POST.get("FirNme"))
	Ln=str(request.POST.get("LstNme"))
	Age=str(request.POST.get("Age"))
	Dob=str(request.POST.get("Dob"))
	Gen=str(request.POST.get("Gen"))
	Cunt=str(request.POST.get("country"))
	Mob=str(request.POST.get("Mob"))
	Mail=str(request.POST.get("Mil"))
	Adrs=str(request.POST.get("address"))
	Password=str(request.POST.get("pas"))
	otp6=random.randint(100000,999999)
	capt=random.randint(100000,999999)
	Acc=curs.execute("select * from seller")
	Accs=Acc.fetchall()
	Lgcred=Name.split(',')
	if request.method=="POST":
		if("@" in Mail):
			if(Accs==[]):
				messages.info(request, 'OTP is Sent To Your Mail.')
				with smtplib.SMTP('smtp.gmail.com',587) as smtp:
					smtp.starttls()
					smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
					sub='LADEN VERIFICATION'
					bod='WELCOME!! Use '+str(otp6)+" as your OTP to Get your LADEN account Validated. Your are one-step away from the Whole New World Of Exitements. Here you can explore things you expect at price you don't ecpect. Happy Shopping :)."
					msg=f"subject:{sub}\n\n{bod}"
					smtp.sendmail('manageladen01@gmail.com','rishichaary1903@gmail.com',msg)
				return render(request, 'Validation.html',{"cp":capt,"otp":otp6,"Res":""})
			else:
				for i in range(0,len(Accs)):
					if(Accs[i][6]==Mail):
						return render(request, 'Signup.html',{"Mv":1})
					else:
						if(i==len(Accs)-1):
							messages.info(request, 'OTP is Sent To Your Mail.')
							with smtplib.SMTP('smtp.gmail.com',587) as smtp:
								smtp.starttls()
								smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
								sub='LADEN VERIFICATION'
								bod='WELCOME!! Use '+str(otp6)+" as your OTP to Get your LADEN SELLER account Validated. Your are one-step away from the Whole New World Of Exitements. Here you can explore things you expect at price you don't ecpect. Happy Shopping :)."
								msg=f"subject:{sub}\n\n{bod}"
								smtp.sendmail('manageladen01@gmail.com','rishichaary1903@gmail.com',msg)
							return render(request, 'Validation.html',{"cp":capt,"otp":otp6,"Res":""})
		else:
			pass
	else:
		return render(request, 'AddUser.html',{"Name":Lgcred[0],"User":Lgcred[1],"Type":Lgcred[2]})
def Validation(request):
	Etp=str(request.POST.get("otp"))
	Cap=str(request.POST.get("cap"))
	Acc=curs.execute("select * from seller")
	Accs=Acc.fetchall()
	if request.method=="POST":
		if(len(Etp)==6):
			if(Etp==str(otp6) and Cap==str(capt)):
				if(Accs==[]):
					curs.execute("insert into Seller values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','','','')".format(Fn[0]+Ln[0]+str(len(Accs)),Fn+Ln,Age,Dob,Gen,Cunt,Mob,Mail,Password,Adrs))
					con.commit()
					with smtplib.SMTP('smtp.gmail.com',587) as smtp:
						smtp.starttls()
						smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
						sub='LADEN WELLCOMES YOU PARTNER!!!'
						bod="WELCOME PARTNER!! "+Fn[0]+Ln[0]+str(len(Accs))+" is your seller code. You Have Entered The Whole New World Of Exitements. Here you can explore and Sell your things you expect at price you don't ecpect. Happy Selling & Shopping :)."
						msg=f"subject:{sub}\n\n{bod}"
						smtp.sendmail('manageladen01@gmail.com',Mail,msg)
					return render(request, 'Home.html',{ "Name":"","User":"",})
				else:
					curs.execute("insert into Seller values('{}','{}','{}','{}','{}','{}','{}','{}','{}','','','','')".format(Fn[0]+Ln[0]+str(len(Accs)),Fn+Ln,Age,Dob,Gen,Cunt,Mob,Mail,Password,Adrs))
					con.commit()
					with smtplib.SMTP('smtp.gmail.com',587) as smtp:
						smtp.starttls()
						smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
						sub='LADEN WELLCOMES YOU PARTNER!!!'
						bod="WELCOME PARTNER!! "+Fn[0]+Ln[0]+str(len(Accs))+" is your seller code. You Have Entered The Whole New World Of Exitements. Here you can explore and Sell your things you expect at price you don't ecpect. Happy Selling & Shopping :)."
						msg=f"subject:{sub}\n\n{bod}"
						smtp.sendmail('manageladen01@gmail.com',Mail,msg)
					return render(request, 'Home.html',{ "Name":"","User":"",})
			else:
				messages.error(request, 'Inavlid Credentials.')
				return render(request, 'Validation.html',{"cp":capt,"otp":otp6,"Res":"Inavlid Credentials"})
		else:
			if(Etp==str(otp) and Cap==str(capt)):
				curs.execute("insert into User values('{}','{}','{}','{}','{}','{}','{}','{}','','','')".format(Fn+Ln,Age,Dob,Gen,Cunt,Mob,Mail,Password,Adrs))
				con.commit()
				with smtplib.SMTP('smtp.gmail.com',587) as smtp:
					smtp.starttls()
					smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
					sub='LADEN WELLCOMES YOU!!!'
					bod="WELCOME!! You Have Entered The Whole New World Of Exitements. Here you can explore things you expect at price you don't ecpect. Happy Shopping :)."
					msg=f"subject:{sub}\n\n{bod}"
					smtp.sendmail('manageladen01@gmail.com',Mail,msg)
				return render(request, 'Home.html',{ "Name":"","User":"",})
			else:
				messages.error(request, 'Inavlid Credentials.')
				return render(request, 'Validation.html',{"cp":capt,"otp":otp,"Res":"Inavlid Credentials"})
	else:
		return render(request, 'Validation.html',{"cp":capt,"otp":otp,"Res":""})
def Signin(request):
	global Fn
	global Ln
	global Age
	global Dob
	global Gen
	global Cunt
	global Mob
	global Mail
	global Password
	global otp
	global capt
	global Adrs
	Fn=str(request.POST.get("FirNme"))
	Ln=str(request.POST.get("LstNme"))
	Age=str(request.POST.get("Age"))
	Dob=str(request.POST.get("Dob"))
	Gen=str(request.POST.get("Gen"))
	Cunt=str(request.POST.get("country"))
	Mob=str(request.POST.get("Mob"))
	Mail=str(request.POST.get("Mil"))
	Password=str(request.POST.get("pas"))
	Adrs=str(request.POST.get("address"))
	otp=random.randint(1000,9999)
	capt=random.randint(100000,999999)
	Acc=curs.execute("select * from User")
	Accs=Acc.fetchall()
	if request.method=="POST":
		if("@" in Mail):
			if(Accs==[]):
				messages.info(request, 'OTP is Sent To Your Mail.')
				with smtplib.SMTP('smtp.gmail.com',587) as smtp:
					smtp.starttls()
					smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
					sub='LADEN VERIFICATION'
					bod='WELCOME!! Use '+str(otp)+" as your OTP to Get your LADEN account Validated. Your are one-step away from the Whole New World Of Exitements. Here you can explore things you expect at price you don't ecpect. Happy Shopping :)."
					msg=f"subject:{sub}\n\n{bod}"
					smtp.sendmail('manageladen01@gmail.com',Mail,msg)
				return render(request, 'Validation.html',{"cp":capt,"otp":otp,"Res":""})
			else:
				for i in range(0,len(Accs)):
					if(Accs[i][6]==Mail):
						return render(request, 'Signup.html',{"Mv":1})
					else:
						if(i==len(Accs)-1):
							messages.info(request, 'OTP is Sent To Your Mail.')
							with smtplib.SMTP('smtp.gmail.com',587) as smtp:
								smtp.starttls()
								smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
								sub='LADEN VERIFICATION'
								bod='WELCOME!! Use '+str(otp)+" as your OTP to Get your LADEN account Validated. Your are one-step away from the Whole New World Of Exitements. Here you can explore things you expect at price you don't ecpect. Happy Shopping :)."
								msg=f"subject:{sub}\n\n{bod}"
								smtp.sendmail('manageladen01@gmail.com',Mail,msg)
							return render(request, 'Validation.html',{"cp":capt,"otp":otp,"Res":""})
		else:
			pass
	else:
		return render(request, 'Signup.html',{"Mv":0})
def Login(request):
	test=curs.execute("select oncart from ceo")
	teres=test.fetchall()
	Name=str(request.POST.get("Home"))
	if request.method=="POST":
		Lgcred=Name.split(',')
		curs.execute("select * from Mobile where onoffer =='on'")
		dit={}
		final=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][13]
			dit={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final.append(dit)
		curs.execute("select * from Laptop where onoffer =='on'")
		dit1={}
		final1=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][14]
			dit1={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final1.append(dit1)
		curs.execute("select * from Accessories where onoffer =='on'")
		dit2={}
		final2=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][7]
			dit2={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final2.append(dit2)
		curs.execute("select * from Clothes where onoffer =='on'")
		dit3={}
		final3=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][10]
			dit3={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final3.append(dit3)
		curs.execute("select * from Grocery where onoffer =='on'")
		dit4={}
		final4=[]
		ad=curs.fetchall()
		for i in range(0,len(ad)):
			sc1=ad[i][0]
			ct1=ad[i][1]
			nm1=ad[i][2]
			em1=ad[i][3]
			sb1=ad[i][5]
			bd1=ad[i][8]
			dit4={'Seller':sc1,'Cata':ct1,'Name':nm1,'Price':em1,'Brand':sb1,'Image':bd1}
			final4.append(dit4)
	global Usr
	global Uname
	global Umail
	global Utype
	Usr=str(request.POST.get("Userid"))
	Pass=str(request.POST.get("Pass"))
	Acc=curs.execute("select * from User")
	Accs=Acc.fetchall()
	Acc1=curs.execute("select * from Seller")
	Accs1=Acc1.fetchall()
	Acc2=curs.execute("select * from CEO")
	Accs2=Acc2.fetchall()
	if request.method=="POST":
		for i in range(0,len(Accs2)):
			if(Accs2[i][7]==Usr and Accs2[i][8]==Pass):
				Uname=Accs2[i][1]
				Umail=Accs2[i][7]
				Utype="ceo"
				user="Authenticated"
				Lsv=open("Lsav.txt","w")
				Lsv.write(Accs2[i][1]+" "+Accs2[i][7]+" "+"ceo")
				Lsv.close()
				return render(request, 'Home.html',{ "Name":Uname,"User":Umail,"languages":["Ate","Bat","Cat"],"Type":Utype,'Details':final,'Details1':final1,'Details2':final2,'Details3':final3,'Details4':final4})
			elif(Usr==None or Pass==None):
				user="Empty"
				UName=""
				UEmail=""
				return render(request, 'Login.html',{"User":user,})
			else:
				if(i==len(Accs2)-1):
					if(Accs1==[]):
						for i in range(0,len(Accs)):
							if(Accs[i][6]==Usr and Accs[i][7]==Pass):
								Uname=Accs[i][0]
								Umail=Accs[i][6]
								Utype="user"
								user="Authenticated"
								Lsv=open("Lsav.txt","w")
								Lsv.write(Accs[i][0]+" "+Accs[i][6]+" user")
								Lsv.close()
								return render(request, 'Home.html',{ "Name":Uname,"User":Umail,"languages":["Ate","Bat","Cat"],"Type":Utype,'Details':final,'Details1':final1,'Details2':final2,'Details3':final3,'Details4':final4})
								break
							elif(Usr==None or Pass==None):
								user="Empty"
								UName=""
								UEmail=""
								return render(request, 'Login.html',{"User":user,})
								break
							else:
								if(i==len(Accs)-1):
									UName=""
									UEmail=""
									messages.add_message(request, messages.INFO, 'Inavlid Credentials')
									messages.error(request, 'Inavlid Credentials.')
									user="NotAuthenticated"
									return render(request, 'Login.html',{"User":user,})
									break
					else:
						for i in range(0,len(Accs1)):
							if(Accs1[i][7]==Usr and Accs1[i][8]==Pass):				
								Uname=Accs1[i][1]
								Umail=Accs1[i][7]
								Utype="seller"
								user="Authenticated"
								Lsv=open("Lsav.txt","w")
								Lsv.write(Accs1[i][1]+" "+Accs1[i][7]+" seller")
								Lsv.close()
								return render(request, 'Home.html',{ "Name":Uname,"User":Umail,"languages":["Ate","Bat","Cat"],"Type":Utype,'Details':final,'Details1':final1,'Details2':final2,'Details3':final3,'Details4':final4})
								break
							elif(Usr==None or Pass==None):
								user="Empty"
								UName=""
								UEmail=""
								return render(request, 'Login.html',{"User":user,})
								break
							else:
								if(i==len(Accs1)-1):
									for i in range(0,len(Accs)):
										if(Accs[i][6]==Usr and Accs[i][7]==Pass):
											Uname=Accs[i][0]
											Umail=Accs[i][6]
											Utype="user"
											user="Authenticated"
											Lsv=open("Lsav.txt","w")
											Lsv.write(Accs[i][0]+" "+Accs[i][6]+" user")
											Lsv.close()
											return render(request, 'Home.html',{ "Name":Uname,"User":Umail,"languages":["Ate","Bat","Cat"],"Type":Utype,'Details':final,'Details1':final1,'Details2':final2,'Details3':final3,'Details4':final4})
											break
										elif(Usr==None or Pass==None):
											user="Empty"
											UName=""
											UEmail=""
											return render(request, 'Login.html',{"User":user,})
											break
										else:
											if(i==len(Accs)-1):
												UName=""
												UEmail=""
												messages.add_message(request, messages.INFO, 'Inavlid Credentials')
												messages.error(request, 'Inavlid Credentials.')
												user="NotAuthenticated"
												return render(request, 'Login.html',{"User":user,})
											else:
												pass
	else:
		pass
	return render(request, 'Login.html',{})
def FogPas(request):
	Acc=curs.execute("select * from User")
	Accs=Acc.fetchall()
	Acc1=curs.execute("select * from Seller")
	Accs1=Acc1.fetchall()
	Acc2=curs.execute("select * from CEO")
	Accs2=Acc2.fetchall()
	for i in range(0,len(Accs)):
		if(Accs[i][6]==Usr):
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.starttls()
				smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
				sub='LADEN PASSWORD'
				bod='Here is your LADEN account Password: '+Accs[i][7]+' You are made free from resetting pasword process by LADEN. Happy Shopping :).'
				msg=f"subject:{sub}\n\n{bod}"
				smtp.sendmail('manageladen01@gmail.com',Usr,msg)
				return render(request, 'Home.html',{ "Name":"1","User":"1",'Details':final,'Details1':final1,'Details2':final2,'Details3':final3,'Details4':final4})
		else:
			if(i==len(Accs)-1):
				for j in range(0,len(Accs1)):
					if(Accs1[j][7]==Usr):
						with smtplib.SMTP('smtp.gmail.com',587) as smtp:
							smtp.starttls()
							smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
							sub='LADEN PASSWORD'
							bod='Here is your LADEN account Password: '+Accs1[i][8]+' You are made free from resetting pasword process by LADEN. Happy Shopping :).'
							msg=f"subject:{sub}\n\n{bod}"
							smtp.sendmail('manageladen01@gmail.com',Usr,msg)
							return render(request, 'Home.html',{ "Name":"1","User":"1",'Details':final,'Details1':final1,'Details2':final2,'Details3':final3,'Details4':final4})
					else:
						if(j==len(Accs1)-1):
							for k in range(0,len(Accs2)):
								if(Accs2[k][7]==Usr):
									with smtplib.SMTP('smtp.gmail.com',587) as smtp:
										smtp.starttls()
										smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
										sub='LADEN PASSWORD'
										bod='Here is your LADEN account Password: '+Accs2[i][8]+' You are made free from resetting pasword process by LADEN. Happy Shopping :).'
										msg=f"subject:{sub}\n\n{bod}"
										smtp.sendmail('manageladen01@gmail.com',Usr,msg)
										return render(request, 'Home.html',{ "Name":"1","User":"1",'Details':final,'Details1':final1,'Details2':final2,'Details3':final3,'Details4':final4})
								else:
									if(k==len(Accs2)-1):
										return render(request, 'Login.html',{"User":"NotAuthenticated",})
def LGout(request):
	return render(request, 'Home.html',{"Name":"1","User":"1",'Details':final,'Details1':final1,'Details2':final2,'Details3':final3,'Details4':final4})
def Remove(request):
	curs.execute("select * from user")
	usr=curs.fetchall()
	curs.execute("select * from Seller")
	slr=curs.fetchall()
	curs.execute("select * from CEO")
	co=curs.fetchall()
	final=[]
	if request.method=="POST":
		Data=str(request.POST.get("Remdet"))
		Split_Data=Data.split(",")
		if(Split_Data[2]=="ceo"):
			curs.execute("select oncart from ceo where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			imp=curs.fetchall()
			impdet=imp[0][0].split("|")
			for i in range (0,len(impdet)-1):
				if((Split_Data[3] in impdet[i]) and (Split_Data[5] in impdet[i]) and (Split_Data[6] in impdet[i])):
					impdet.remove(impdet[i])
					B="|".join(impdet)
					curs.execute("update ceo set oncart='{}' where Name='{}' and Userid='{}'".format(str(B),Split_Data[0],Split_Data[1]))
					con.commit()
					break
			curs.execute("select oncart from ceo where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			imp=curs.fetchall()
			impdet=imp[0][0].split("|")
			if(len(impdet)==1):
				ste="Empty"
			else:
				ste="NotEmpty"
			for i in range (0,len(impdet)-1):
				impp=impdet[i].split(",")
				if(impp[1]=="GROCERY"):
					curs.execute("select * from grocery where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][8]}
					final.append(res)
				elif(impp[1]=="CLOTHES"):
					curs.execute("select * from clothes where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][10]}
					final.append(res)
				elif(impp[1]=="MOBILE"):
					curs.execute("select * from mobile where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][13]}
					final.append(res)
				elif(impp[1]=="LAPTOP"):
					curs.execute("select * from laptop where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][14]}
					final.append(res)
				elif(impp[1]=="ACCESSORIES"):
					curs.execute("select * from accessories where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][7]}
					final.append(res)
			return render(request, 'Cart.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"State":ste,"Prds":final})
		elif(Split_Data[2]=="seller"):
			curs.execute("select oncart from seller where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			imp=curs.fetchall()
			impdet=imp[0][0].split("|")
			for i in range (0,len(impdet)-1):
				if((Split_Data[3] in impdet[i]) and (Split_Data[5] in impdet[i]) and (Split_Data[6] in impdet[i])):
					impdet.remove(impdet[i])
					B="|".join(impdet)
					curs.execute("update seller set oncart='{}' where Name='{}' and Userid='{}'".format(str(B),Split_Data[0],Split_Data[1]))
					con.commit()
					break
			for i in range (0,len(usr)):
				if(usr[i][0]==Lgcred[3] and usr[i][6]==Lgcred[4]):
					curs.execute("select oncart from seller where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
					imp=curs.fetchall()
					impdet=imp[0][0].split("|")
					if(len(impdet)==1):
						ste="Empty"
					else:
						ste="NotEmpty"
					for i in range (0,len(impdet)-1):
						impp=impdet[i].split(",")
						if(impp[1]=="GROCERY"):
							curs.execute("select * from grocery where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][8]}
							final.append(res)
						elif(impp[1]=="CLOTHES"):
							curs.execute("select * from clothes where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][10]}
							final.append(res)
						elif(impp[1]=="MOBILE"):
							curs.execute("select * from mobile where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][13]}
							final.append(res)
						elif(impp[1]=="LAPTOP"):
							curs.execute("select * from laptop where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][14]}
							final.append(res)
						elif(impp[1]=="ACCESSORIES"):
							curs.execute("select * from accessories where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][7]}
							final.append(res)
					return render(request, 'Cart.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"State":ste,"Prds":final})
		elif(Split_Data[2]=="user"):
			curs.execute("select oncart from seller where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			imp=curs.fetchall()
			impdet=imp[0][0].split("|")
			for i in range (0,len(impdet)-1):
				if((Split_Data[3] in impdet[i]) and (Split_Data[5] in impdet[i]) and (Split_Data[6] in impdet[i])):
					impdet.remove(impdet[i])
					B="|".join(impdet)
					curs.execute("update user set oncart='{}' where Name='{}' and Userid='{}'".format(str(B),Split_Data[0],Split_Data[1]))
					con.commit()
					break
			for i in range (0,len(usr)):
				if(usr[i][0]==Lgcred[3] and usr[i][6]==Lgcred[4]):
					curs.execute("select oncart from user where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
					imp=curs.fetchall()
					impdet=imp[0][0].split("|")
					if(len(impdet)==1):
						ste="Empty"
					else:
						ste="NotEmpty"
					for i in range (0,len(impdet)-1):
						impp=impdet[i].split(",")
						if(impp[1]=="GROCERY"):
							curs.execute("select * from grocery where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][8]}
							final.append(res)
						elif(impp[1]=="CLOTHES"):
							curs.execute("select * from clothes where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][10]}
							final.append(res)
						elif(impp[1]=="MOBILE"):
							curs.execute("select * from mobile where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][13]}
							final.append(res)
						elif(impp[1]=="LAPTOP"):
							curs.execute("select * from laptop where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][14]}
							final.append(res)
						elif(impp[1]=="ACCESSORIES"):
							curs.execute("select * from accessories where sc='{}' and Name='{}'".format(impp[0],impp[2]))
							det=curs.fetchall()
							res={"Name":det[0][2],"Seller":det[0][0],"Quant":impp[3],"TP":int(impp[3])*int(det[0][3]),"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][7]}
							final.append(res)
					return render(request, 'Cart.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"State":ste,"Prds":final})
	else:
		return render(request,'Cart.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"State":"Empty"})
def CheckOut(request):
	if request.method=="POST":
		Data=str(request.POST.get("Check"))
		Split_Data=Data.split(",")
		if(Split_Data[2]=="ceo"):
			curs.execute("select address from ceo where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			adres=curs.fetchall()
			curs.execute("select mono from ceo where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			mobile=curs.fetchall()
			curs.execute("select oncart from ceo where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			imp=curs.fetchall()
			curs.execute("update ceo set OrderHist='{}' where Name='{}' and Userid='{}'".format(imp[0][0],Split_Data[0],Split_Data[1]))
			con.commit()
			impdet=imp[0][0].split("|")
			for i in range(0,len(impdet)-1):
				impprd=impdet[i].split(",")
				onorders=str(impprd[0])+","+str(impprd[1])+","+str(impprd[2])+","+str(impprd[3])+","+str(Split_Data[0])+","+str(Split_Data[1])+","+str(adres[0][0])+","+str(mobile[0][0])+"|"
				curs.execute("select scode from seller")
				fig=curs.fetchall()
				for k in range (0,len(fig)):
					if(fig[k][0]==impprd[0]):
						curs.execute("select orders from seller where scode='{}'".format(impprd[0]))
						h=curs.fetchall()
						curs.execute("select Userid from seller where scode='{}'".format(impprd[0]))
						Reciver=curs.fetchall()
						curs.execute("update seller set orders='{}' where scode='{}'".format(str(h[0][0])+onorders,impprd[0]))
						con.commit()
				curs.execute("select rachasc from ceo")
				figg=curs.fetchall()
				if(impprd[0]==figg[0][0]):
						curs.execute("select orders from ceo where rachasc='{}'".format(impprd[0]))
						h=curs.fetchall()
						curs.execute("select Userid from ceo where rachasc='{}'".format(impprd[0]))
						Reciver=curs.fetchall()
						curs.execute("update ceo set orders='{}' where rachasc='{}'".format(str(str(h[0][0])+str(onorders)),impprd[0]))
						con.commit()
			curs.execute("update ceo set oncart='' where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			con.commit()
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.starttls()
				smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
				sub='LADEN ORDER SUCCESS'
				bod='Thank You For Shopping. Your Order Has Been Successfully Placed. Seller you ordered will be taking over your order from now. Further Details regarding delivery will be intimated by your Seller.'
				msg=f"subject:{sub}\n\n{bod}"
				smtp.sendmail('manageladen01@gmail.com',Split_Data[1],msg)
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.starttls()
				smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
				sub='NEW INCOMMING ORDER'
				bod='You have recived a order from '+str(Split_Data[0])+"( "+str(Split_Data[1])+" ). Check Your Orders In LADEN website. Happy Business."
				msg=f"subject:{sub}\n\n{bod}"
				smtp.sendmail('manageladen01@gmail.com',Reciver[0][0],msg)
		elif(Split_Data[2]=="seller"):
			curs.execute("select address from seller where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			adres=curs.fetchall()
			curs.execute("select mono from seller where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			mobile=curs.fetchall()
			curs.execute("select oncart from seller where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			imp=curs.fetchall()
			curs.execute("update seller set OrderHist='{}' where Name='{}' and Userid='{}'".format(imp[0][0],Split_Data[0],Split_Data[1]))
			con.commit()
			impdet=imp[0][0].split("|")
			for i in range(0,len(impdet)-1):
				impprd=impdet[i].split(",")
				onorders=str(impprd[0])+","+str(impprd[1])+","+str(impprd[2])+","+str(impprd[3])+","+str(Split_Data[0])+","+str(Split_Data[1])+","+str(adres[0][0])+","+str(mobile[0][0])+"|"
				curs.execute("select scode from seller")
				fig=curs.fetchall()
				for k in range (0,len(fig)):
					if(fig[k][0]==impprd[0]):
						curs.execute("select orders from seller where scode='{}'".format(impprd[0]))
						h=curs.fetchall()
						curs.execute("select Userid from seller where scode='{}'".format(impprd[0]))
						Reciver=curs.fetchall()
						curs.execute("update seller set orders='{}' where scode='{}'".format(str(h[0][0])+onorders,impprd[0]))
						con.commit()
				curs.execute("select rachasc from ceo")
				figg=curs.fetchall()
				if(impprd[0]==figg[0][0]):
						curs.execute("select orders from ceo where rachasc='{}'".format(impprd[0]))
						h=curs.fetchall()
						curs.execute("select Userid from ceo where rachasc='{}'".format(impprd[0]))
						Reciver=curs.fetchall()
						curs.execute("update ceo set orders='{}' where rachasc='{}'".format(str(h[0][0])+onorders,impprd[0]))
						con.commit()
			curs.execute("update seller set oncart='' where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			con.commit()
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.starttls()
				smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
				sub='LADEN ORDER SUCCESS'
				bod='Thank You For Shopping. Your Order Has Been Successfully Placed. Seller you ordered will be taking over your order from now. Further Details regarding delivery will be intimated by your Seller.'
				msg=f"subject:{sub}\n\n{bod}"
				smtp.sendmail('manageladen01@gmail.com',Split_Data[1],msg)
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.starttls()
				smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
				sub='NEW INCOMMING ORDER'
				bod='You have recived a order from '+str(Split_Data[0])+"( "+str(Split_Data[1])+" ). Check Your Orders In LADEN website. Happy Business."
				msg=f"subject:{sub}\n\n{bod}"
				smtp.sendmail('manageladen01@gmail.com',Reciver[0][0],msg)	
		elif(Split_Data[2]=="user"):
			curs.execute("select address from user where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			adres=curs.fetchall()
			curs.execute("select mono from user where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			mobile=curs.fetchall()
			curs.execute("select oncart from user where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			imp=curs.fetchall()
			curs.execute("update user set OrderHist='{}' where Name='{}' and Userid='{}'".format(imp[0][0],Split_Data[0],Split_Data[1]))
			con.commit()
			impdet=imp[0][0].split("|")
			for i in range(0,len(impdet)-1):
				impprd=impdet[i].split(",")
				onorders=str(impprd[0])+","+str(impprd[1])+","+str(impprd[2])+","+str(impprd[3])+","+str(Split_Data[0])+","+str(Split_Data[1])+","+str(adres[0][0])+","+str(mobile[0][0])+"|"
				curs.execute("select scode from seller")
				fig=curs.fetchall()
				for k in range (0,len(fig)):
					if(fig[k][0]==impprd[0]):
						curs.execute("select orders from seller where scode='{}'".format(impprd[0]))
						h=curs.fetchall()
						curs.execute("select Userid from seller where scode='{}'".format(impprd[0]))
						Reciver=curs.fetchall()
						curs.execute("update seller set orders='{}' where scode='{}'".format(str(h[0][0])+onorders,impprd[0]))
						con.commit()
				curs.execute("select rachasc from ceo")
				figg=curs.fetchall()
				if(impprd[0]==figg[0][0]):
						curs.execute("select orders from ceo where rachasc='{}'".format(impprd[0]))
						h=curs.fetchall()
						curs.execute("select Userid from ceo where rachasc='{}'".format(impprd[0]))
						Reciver=curs.fetchall()
						curs.execute("update ceo set orders='{}' where rachasc='{}'".format(str(h[0][0])+onorders,impprd[0]))
						con.commit()
			curs.execute("update user set oncart='' where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			con.commit()
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.starttls()
				smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
				sub='LADEN ORDER SUCCESS'
				bod='Thank You For Shopping. Your Order Has Been Successfully Placed. Seller you ordered will be taking over your order from now. Further Details regarding delivery will be intimated by your Seller.'
				msg=f"subject:{sub}\n\n{bod}"
				smtp.sendmail('manageladen01@gmail.com',Split_Data[1],msg)
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.starttls()
				smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
				sub='NEW INCOMMING ORDER'
				bod='You have recived a order from '+str(Split_Data[0])+"( "+str(Split_Data[1])+" ). Check Your Orders In LADEN website. Happy Business."
				msg=f"subject:{sub}\n\n{bod}"
				smtp.sendmail('manageladen01@gmail.com',Reciver[0][0],msg)
		return render(request,'Cart.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"State":"Ordered"})
	else:
		return render(request,'Cart.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"State":"Ordered"})
def Deliver(request):
	if request.method=="POST":
		Data=str(request.POST.get("Del"))
		Split_Data=Data.split(",")
		if(Split_Data[2]=="ceo"):
			curs.execute("select orders from ceo where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			ord=curs.fetchall()
			orddet=ord[0][0].split("|")
			for i in range(0,len(orddet)-1):
				if((Split_Data[3] in orddet[i]) and (Split_Data[4] in orddet[i])and (Split_Data[5] in orddet[i])and (Split_Data[6] in orddet[i])and (Split_Data[7] in orddet[i])):
					orddet.remove(orddet[i])
					B="|".join(orddet)
					curs.execute("update ceo set orders='{}' where Name='{}' and Userid='{}'".format(str(B),Split_Data[0],Split_Data[1]))
					con.commit()
					break
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.starttls()
				smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
				sub='DELIVERY UPDATE'
				bod='We have handed over your order to our delivery partner. Our delivery partner will be contacting to from now for further updates.'
				msg=f"subject:{sub}\n\n{bod}"
				smtp.sendmail('manageladen01@gmail.com',Split_Data[4],msg)
			curs.execute("select orders from ceo where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			imp=curs.fetchall()
			impdet=imp[0][0].split("|")
			if(len(impdet)==1):
				ste="Empty"
			else:
				ste="NotEmpty"
			for i in range (0,len(impdet)-1):
				impp=impdet[i].split(",")
				ad=impp[6:len(impp)-2]
				addres=''
				for jk in range(0,len(ad)):
					if(jk!=len(ad)-1):
						addres=addres+str(ad[jk])+","
					else:
						addres=addres+str(ad[jk])
				if(impp[1]=="GROCERY"):
					curs.execute("select * from grocery where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][8],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="CLOTHES"):
					curs.execute("select * from clothes where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][10],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="MOBILE"):
					curs.execute("select * from mobile where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][13],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="LAPTOP"):
					curs.execute("select * from laptop where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][14],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="ACCESSORIES"):
					curs.execute("select * from accessories where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][7],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
			return render(request, 'Orders.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"State":ste,"Prds":final})
		elif(Split_Data[2]=="seller"):
			curs.execute("select orders from seller where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			ord=curs.fetchall()
			orddet=ord[0][0].split("|")
			for i in range(0,len(orddet)-1):
				if((Split_Data[3] in orddet[i]) and (Split_Data[4] in orddet[i])and (Split_Data[5] in orddet[i])and (Split_Data[6] in orddet[i])and (Split_Data[7] in orddet[i])):
					orddet.remove(orddet[i])
					B="|".join(orddet)
					curs.execute("update seller set orders='{}' where Name='{}' and Userid='{}'".format(str(B),Split_Data[0],Split_Data[1]))
					con.commit()
					break
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.starttls()
				smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
				sub='DELIVERY UPDATE'
				bod='We have handed over your order to our delivery partner. Our delivery partner will be contacting to from now for further updates.'
				msg=f"subject:{sub}\n\n{bod}"
				smtp.sendmail('manageladen01@gmail.com',Split_Data[4],msg)
			curs.execute("select orders from seller where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			ord=curs.fetchall()
			orddet=ord[0][0].split("|")
			for i in range(0,len(orddet)-1):
				if((Split_Data[3] in orddet[i]) and (Split_Data[4] in orddet[i])and (Split_Data[5] in orddet[i])and (Split_Data[6] in orddet[i])and (Split_Data[7] in orddet[i])):
					orddet.remove(orddet[i])
					B="|".join(orddet)
					curs.execute("update seller set orders='{}' where Name='{}' and Userid='{}'".format(str(B),Split_Data[0],Split_Data[1]))
					con.commit()
					break
			curs.execute("select orders from seller where Name='{}' and Userid='{}'".format(Split_Data[0],Split_Data[1]))
			imp=curs.fetchall()
			impdet=imp[0][0].split("|")
			if(len(impdet)==1):
				ste="Empty"
			else:
				ste="NotEmpty"
			for i in range (0,len(impdet)-1):
				impp=impdet[i].split(",")
				ad=impp[6:len(impp)-2]
				addres=''
				for jk in range(0,len(ad)):
					if(jk!=len(ad)-1):
						addres=addres+str(ad[jk])+","
					else:
						addres=addres+str(ad[jk])
				if(impp[1]=="GROCERY"):
					curs.execute("select * from grocery where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][8],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="CLOTHES"):
					curs.execute("select * from clothes where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][10],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="MOBILE"):
					curs.execute("select * from mobile where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][13],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="LAPTOP"):
					curs.execute("select * from laptop where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][14],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
				elif(impp[1]=="ACCESSORIES"):
					curs.execute("select * from accessories where sc='{}' and Name='{}'".format(impp[0],impp[2]))
					det=curs.fetchall()
					res={"Name":det[0][2],"Seller":det[0][0],"Cata":det[0][1],"Brand":det[0][5],"Price":det[0][3],"Image":det[0][7],"Quant":impp[3],"TP":str(int(impp[3])*int(det[0][3])),"FrmU":impp[4],"FrmE":impp[5],"FrmA":addres,"FrmM":impp[len(impp)-1]}
					final.append(res)
			return render(request, 'Orders.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"State":ste,"Prds":final})
	else:
		return render(request,'Orders.html',{})
def More(request):
	Results=[]
	if request.method=="POST":
		Data=str(request.POST.get("Mre"))
		Split_Data=Data.split(",")
		if(Split_Data[2]=="ceo"):
			curs.execute("select rachasc from ceo where name='{}' and userid='{}'".format(Split_Data[0],Split_Data[1]))
			sc=curs.fetchall()
			curs.execute("select * from GROCERY where sc='{}'".format(sc[0][0]))
			Grocery=curs.fetchall()
			curs.execute("select * from CLOTHES where sc='{}'".format(sc[0][0]))
			Clothes=curs.fetchall()
			curs.execute("select * from ACCESSORIES where sc='{}'".format(sc[0][0]))
			Accessories=curs.fetchall()
			curs.execute("select * from MOBILE where sc='{}'".format(sc[0][0]))
			Mobile=curs.fetchall()
			curs.execute("select * from LAPTOP where sc='{}'".format(sc[0][0]))
			Laptop=curs.fetchall()
			if(len(Grocery)!=0):
				for i in range(0,len(Grocery)):
					delt=Grocery
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][9],"Image":delt[0][8],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Clothes)!=0):
				for i in range(0,len(Clothes)):
					delt=Clothes
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][11],"Image":delt[0][10],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Accessories)!=0):
				for i in range(0,len(Accessories)):
					delt=Accessories
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][8],"Image":delt[0][7],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Mobile)!=0):
				for i in range(0,len(Mobile)):
					delt=Mobile
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					print(ordit)
					Results.append(ordit)
			if(len(Laptop)!=0):
				for i in range(0,len(Laptop)):
					delt=Laptop
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
		elif(Split_Data[2]=="seller"):
			curs.execute("select scode from seller where name='{}' and userid='{}'".format(Split_Data[0],Split_Data[1]))
			sc=curs.fetchall()
			curs.execute("select * from GROCERY where sc='{}'".format(sc[0][0]))
			Grocery=curs.fetchall()
			curs.execute("select * from CLOTHES where sc='{}'".format(sc[0][0]))
			Clothes=curs.fetchall()
			curs.execute("select * from ACCESSORIES where sc='{}'".format(sc[0][0]))
			Accessories=curs.fetchall()
			curs.execute("select * from MOBILE where sc='{}'".format(sc[0][0]))
			Mobile=curs.fetchall()
			curs.execute("select * from LAPTOP where sc='{}'".format(sc[0][0]))
			Laptop=curs.fetchall()
			if(len(Grocery)!=0):
				for i in range(0,len(Grocery)):
					delt=Grocery
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][9],"Image":delt[0][8],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Clothes)!=0):
				for i in range(0,len(Clothes)):
					delt=Clothes
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][11],"Image":delt[0][10],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Accessories)!=0):
				for i in range(0,len(Accessories)):
					delt=Accessories
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][8],"Image":delt[0][7],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Mobile)!=0):
				for i in range(0,len(Mobile)):
					delt=Mobile
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					print(ordit)
					Results.append(ordit)
			if(len(Laptop)!=0):
				for i in range(0,len(Laptop)):
					delt=Laptop
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
		return render(request,'More.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"P":Results})
def DelUsr(request):
	Results=[]
	if request.method=="POST":
		Data=str(request.POST.get("More"))
		Split_Data=Data.split(",")
		Delusr=str(request.POST.get("Delus"))
		curs.execute("select userid from seller")
		usrs=curs.fetchall()
		for i in range(0,len(usrs[0])):
			if(Delusr==usrs[0][i]):
				rf="Success"
				curs.execute("delete from seller where userid='{}'".format(usrs[0][i]))
				with smtplib.SMTP('smtp.gmail.com',587) as smtp:
					smtp.starttls()
					smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
					sub='SELLER DELETED'
					bod=str(usrs[0][i])+' Has been Successfuly removed from Sellers list.'
					msg=f"subject:{sub}\n\n{bod}"
					smtp.sendmail('manageladen01@gmail.com',Split_Data[1],msg)
				with smtplib.SMTP('smtp.gmail.com',587) as smtp:
					smtp.starttls()
					smtp.login('manageladen01@gmail.com','ckbjwjcgtddjdadc')
					sub='YOU HAVE BEEN REMOVED'
					bod="You Have been removed from LADEN sellers list. Thank you for you Service."
					msg=f"subject:{sub}\n\n{bod}"
					smtp.sendmail('manageladen01@gmail.com',usrs[0][i],msg)
		if(Split_Data[2]=="ceo"):
			curs.execute("select rachasc from ceo where name='{}' and userid='{}'".format(Split_Data[0],Split_Data[1]))
			sc=curs.fetchall()
			curs.execute("select * from GROCERY where sc='{}'".format(sc[0][0]))
			Grocery=curs.fetchall()
			curs.execute("select * from CLOTHES where sc='{}'".format(sc[0][0]))
			Clothes=curs.fetchall()
			curs.execute("select * from ACCESSORIES where sc='{}'".format(sc[0][0]))
			Accessories=curs.fetchall()
			curs.execute("select * from MOBILE where sc='{}'".format(sc[0][0]))
			Mobile=curs.fetchall()
			curs.execute("select * from LAPTOP where sc='{}'".format(sc[0][0]))
			Laptop=curs.fetchall()
			if(len(Grocery)!=0):
				for i in range(0,len(Grocery)):
					delt=Grocery
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][9],"Image":delt[0][8],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Clothes)!=0):
				for i in range(0,len(Clothes)):
					delt=Clothes
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][11],"Image":delt[0][10],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Accessories)!=0):
				for i in range(0,len(Accessories)):
					delt=Accessories
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][8],"Image":delt[0][7],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Mobile)!=0):
				for i in range(0,len(Mobile)):
					delt=Mobile
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					print(ordit)
					Results.append(ordit)
			if(len(Laptop)!=0):
				for i in range(0,len(Laptop)):
					delt=Laptop
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
	return render(request,'More.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"P":Results})
def DelPrd(request):
	Results=[]
	if request.method=="POST":
		Data=str(request.POST.get("Dp"))
		Split_Data=Data.split(",")
		if(Split_Data[4]=="GROCERY"):
			curs.execute("delete from grocery where sc='{}' and name='{}'".format(Split_Data[5],Split_Data[3]))
			con.commit()
		elif(Split_Data[4]=="CLOTHES"):
			curs.execute("delete from clothes where sc='{}' and name='{}'".format(Split_Data[5],Split_Data[3]))
			con.commit()
		elif(Split_Data[4]=="ACCESSORIES"):
			curs.execute("delete from ACCESSORIES where sc='{}' and name='{}'".format(Split_Data[5],Split_Data[3]))
			con.commit()
		elif(Split_Data[4]=="MOBILE"):
			curs.execute("delete from mobile where sc='{}' and name='{}'".format(Split_Data[5],Split_Data[3]))
			con.commit()
		elif(Split_Data[4]=="LAPTOP"):
			curs.execute("delete from laptop where sc='{}' and name='{}'".format(Split_Data[5],Split_Data[3]))
			con.commit()
		if(Split_Data[2]=="ceo"):
			curs.execute("select rachasc from ceo where name='{}' and userid='{}'".format(Split_Data[0],Split_Data[1]))
			sc=curs.fetchall()
			curs.execute("select * from GROCERY where sc='{}'".format(sc[0][0]))
			Grocery=curs.fetchall()
			curs.execute("select * from CLOTHES where sc='{}'".format(sc[0][0]))
			Clothes=curs.fetchall()
			curs.execute("select * from ACCESSORIES where sc='{}'".format(sc[0][0]))
			Accessories=curs.fetchall()
			curs.execute("select * from MOBILE where sc='{}'".format(sc[0][0]))
			Mobile=curs.fetchall()
			curs.execute("select * from LAPTOP where sc='{}'".format(sc[0][0]))
			Laptop=curs.fetchall()
			if(len(Grocery)!=0):
				for i in range(0,len(Grocery)):
					delt=Grocery
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][9],"Image":delt[0][8],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Clothes)!=0):
				for i in range(0,len(Clothes)):
					delt=Clothes
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][11],"Image":delt[0][10],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Accessories)!=0):
				for i in range(0,len(Accessories)):
					delt=Accessories
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][8],"Image":delt[0][7],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Mobile)!=0):
				for i in range(0,len(Mobile)):
					delt=Mobile
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					print(ordit)
					Results.append(ordit)
			if(len(Laptop)!=0):
				for i in range(0,len(Laptop)):
					delt=Laptop
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
		elif(Split_Data[2]=="seller"):
			curs.execute("select scode from seller where name='{}' and userid='{}'".format(Split_Data[0],Split_Data[1]))
			sc=curs.fetchall()
			curs.execute("select * from GROCERY where sc='{}'".format(sc[0][0]))
			Grocery=curs.fetchall()
			curs.execute("select * from CLOTHES where sc='{}'".format(sc[0][0]))
			Clothes=curs.fetchall()
			curs.execute("select * from ACCESSORIES where sc='{}'".format(sc[0][0]))
			Accessories=curs.fetchall()
			curs.execute("select * from MOBILE where sc='{}'".format(sc[0][0]))
			Mobile=curs.fetchall()
			curs.execute("select * from LAPTOP where sc='{}'".format(sc[0][0]))
			Laptop=curs.fetchall()
			if(len(Grocery)!=0):
				for i in range(0,len(Grocery)):
					delt=Grocery
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][9],"Image":delt[0][8],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Clothes)!=0):
				for i in range(0,len(Clothes)):
					delt=Clothes
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][11],"Image":delt[0][10],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Accessories)!=0):
				for i in range(0,len(Accessories)):
					delt=Accessories
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][8],"Image":delt[0][7],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Mobile)!=0):
				for i in range(0,len(Mobile)):
					delt=Mobile
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					print(ordit)
					Results.append(ordit)
			if(len(Laptop)!=0):
				for i in range(0,len(Laptop)):
					delt=Laptop
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
		return render(request,'More.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"P":Results})
	else:
		return render(request,'More.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"P":Results})
def UpPrd(request):
	Results=[]
	if request.method=="POST":
		Data=str(request.POST.get("Up"))
		Split_Data=Data.split(",")
		Pr=str(request.POST.get("nup"))
		onf=str(request.POST.get("Onoff"+str(Split_Data[3])))
		if(Split_Data[4]=="GROCERY"):
			curs.execute("update grocery set price='{}',onoffer='{}' where sc='{}' and name='{}'".format(Pr,onf,Split_Data[5],Split_Data[3]))
			con.commit()
		elif(Split_Data[4]=="CLOTHES"):
			curs.execute("update clothes set price='{}',onoffer='{}' where sc='{}' and name='{}'".format(Pr,onf,Split_Data[5],Split_Data[3]))
			con.commit()
		elif(Split_Data[4]=="ACCESSORIES"):
			curs.execute("update accessories set price='{}',onoffer='{}' where sc='{}' and name='{}'".format(Pr,onf,Split_Data[5],Split_Data[3]))
			con.commit()
		elif(Split_Data[4]=="MOBILE"):
			curs.execute("update mobile set price='{}',onoffer='{}' where sc='{}' and name='{}'".format(Pr,onf,Split_Data[5],Split_Data[3]))
			con.commit()
		elif(Split_Data[4]=="LAPTOP"):
			curs.execute("update laptop set price='{}',onoffer='{}' where sc='{}' and name='{}'".format(Pr,onf,Split_Data[5],Split_Data[3]))
			con.commit()
		if(Split_Data[2]=="ceo"):
			curs.execute("select rachasc from ceo where name='{}' and userid='{}'".format(Split_Data[0],Split_Data[1]))
			sc=curs.fetchall()
			curs.execute("select * from GROCERY where sc='{}'".format(sc[0][0]))
			Grocery=curs.fetchall()
			curs.execute("select * from CLOTHES where sc='{}'".format(sc[0][0]))
			Clothes=curs.fetchall()
			curs.execute("select * from ACCESSORIES where sc='{}'".format(sc[0][0]))
			Accessories=curs.fetchall()
			curs.execute("select * from MOBILE where sc='{}'".format(sc[0][0]))
			Mobile=curs.fetchall()
			curs.execute("select * from LAPTOP where sc='{}'".format(sc[0][0]))
			Laptop=curs.fetchall()
			if(len(Grocery)!=0):
				for i in range(0,len(Grocery)):
					delt=Grocery
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][9],"Image":delt[0][8],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Clothes)!=0):
				for i in range(0,len(Clothes)):
					delt=Clothes
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][11],"Image":delt[0][10],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Accessories)!=0):
				for i in range(0,len(Accessories)):
					delt=Accessories
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][8],"Image":delt[0][7],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Mobile)!=0):
				for i in range(0,len(Mobile)):
					delt=Mobile
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					print(ordit)
					Results.append(ordit)
			if(len(Laptop)!=0):
				for i in range(0,len(Laptop)):
					delt=Laptop
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
		elif(Split_Data[2]=="seller"):
			curs.execute("select scode from seller where name='{}' and userid='{}'".format(Split_Data[0],Split_Data[1]))
			sc=curs.fetchall()
			curs.execute("select * from GROCERY where sc='{}'".format(sc[0][0]))
			Grocery=curs.fetchall()
			curs.execute("select * from CLOTHES where sc='{}'".format(sc[0][0]))
			Clothes=curs.fetchall()
			curs.execute("select * from ACCESSORIES where sc='{}'".format(sc[0][0]))
			Accessories=curs.fetchall()
			curs.execute("select * from MOBILE where sc='{}'".format(sc[0][0]))
			Mobile=curs.fetchall()
			curs.execute("select * from LAPTOP where sc='{}'".format(sc[0][0]))
			Laptop=curs.fetchall()
			if(len(Grocery)!=0):
				for i in range(0,len(Grocery)):
					delt=Grocery
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][9],"Image":delt[0][8],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Clothes)!=0):
				for i in range(0,len(Clothes)):
					delt=Clothes
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][11],"Image":delt[0][10],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Accessories)!=0):
				for i in range(0,len(Accessories)):
					delt=Accessories
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][8],"Image":delt[0][7],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
			if(len(Mobile)!=0):
				for i in range(0,len(Mobile)):
					delt=Mobile
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					print(ordit)
					Results.append(ordit)
			if(len(Laptop)!=0):
				for i in range(0,len(Laptop)):
					delt=Laptop
					ordit={"Brand":delt[0][5],"Name":delt[0][2],"Price":delt[0][3],"Offersts":delt[0][15],"Image":delt[0][13],"Seller":delt[0][0],"Cata":delt[0][1]}
					Results.append(ordit)
		return render(request,'More.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"P":Results})
	else:
		return render(request,'More.html',{"Name":Split_Data[0],"User":Split_Data[1],"Type":Split_Data[2],"P":Results})