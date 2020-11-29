
import pandas as pd
import main
import os
HEIGHT = 700
WIDTH = 800


def test(pow,ti,tp,tl,tr,al,gam,w, woj,osoby, ur, um, dead):
    main.gsca(pow,ti,tp,tl,tr,al,gam,w, woj,osoby, ur, um, dead)
    os.system('python gui_img.py')



from tkinter import *
root = Tk()

canvas = Canvas(root, height=850, width=1200, bg='white')
canvas.pack()

tekst = 'Modelowanie rozprzestrzeniania się epidemii '
intro = Label(root, text=tekst, bg='white', bd=2, font=('Helvetica',25, 'bold'))
intro.place(relx=0.5, rely=0.0, relwidth=0.9, relheight=0.06, anchor='n')
tekst2 = 'z użyciem globalnego automatu komórkowego'
intro2 = Label(root, text=tekst2, bg='white', bd=2, font=('Helvetica',25,'bold'))
intro2.place(relx=0.5, rely=0.055, relwidth=0.9, relheight=0.06, anchor='n')
tekst3 = 'Poniższy model jest przykładem globalnego automatu komórkowego symulującego rozprzestrzenianie się zakaźnej choroby w środowisku heterogenicznym. '
intro3 = Label(root, text=tekst3, bg='white', bd=2, font=('Helvetica',10))
intro3.place(relx=0.5, rely=0.11, relwidth=0.9, relheight=0.04, anchor='n')
tekst4 = 'Model bazuje na dostępnych rozwiązaniach w postaci modeli SIR, wprowadzając stochastyczne i przestrzenne parametry umożliwia analizę dynamiki choroby. '
intro4 = Label(root, text=tekst4, bg='white', bd=2, font=('Helvetica',10))
intro4.place(relx=0.5, rely=0.14, relwidth=0.9, relheight=0.04, anchor='n')
tekst5 = 'Rezultaty symulacji wizualizują tempo rozprzestrzenienia się choroby i mogą być wykorzystywane do opisania możliwych działań zapobiegawczych.'
intro5 = Label(root, text=tekst5, bg='white', bd=2, font=('Helvetica',10))
intro5.place(relx=0.5, rely=0.17, relwidth=0.9, relheight=0.04, anchor='n')

frame = Frame(root, bg='white', bd=1)
frame.place(relx=0.77, rely=0.215, relwidth=0.42, relheight=0.65, anchor='n')

frame2 = Frame(root, bg='white', bd=1)
frame2.place(relx=0.77, rely=0.835, relwidth=0.42, relheight=0.1, anchor='n')

tekst_1 = 'Możesz wybrać jeden z wprowadzonych scenariuszy przenoszenia choroby:'
label_1 = Label(frame, text=tekst_1, bg='white', bd=1, font=('Helvetica',10))
label_1.place(relx=0, rely=0, relheight=0.05)
r= IntVar()
tekst_6 = 'Lub stworzyć swój własny:'
label_6 = Label(frame, text=tekst_6, bg='white', bd=1, font=('Helvetica',10))
label_6.place(relx=0, rely=0.13, relheight=0.05)
tekst_7 = '_______________________________________________________________________________________'
label_7 = Label(frame, text=tekst_7, bg='white', bd=1, font=('Helvetica',7))
label_7.place(relx=0, rely=0.17, relheight=0.018)

def clicked(value):
    if value == 1:
        var1,var2, var3, var4, var5, var6, var7, var8, var10, var11, var12, var13 = StringVar(root), StringVar(root), StringVar(root), StringVar(
            root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root)
        var1.set('Granice województw')
        parm1.config(textvariable=var1)
        var2.set("5")
        parm2.config(textvariable=var2)
        var3.set("3")
        parm3.config(textvariable=var3)
        var4.set("10")
        parm4.config(textvariable=var4)
        var5.set("90")
        parm5.config(textvariable=var5)
        var6.set("0.07")
        parm6.config(textvariable=var6)
        var7.set("0.1")
        parm7.config(textvariable=var7)
        var8.set("0.3")
        parm8.config(textvariable=var8)
        var10.set("150")
        parm10.config(textvariable=var10)
        var11.set("0.000027")
        parm11.config(textvariable=var11)
        var12.set("0.000029")
        parm12.config(textvariable=var12)
        var13.set("0.00005")
        parm13.config(textvariable=var13)

    if value == 2:
        var1,var2, var3, var4, var5, var6, var7, var8, var10, var11, var12, var13 = StringVar(root), StringVar(root), StringVar(root), StringVar(
            root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root)
        var1.set('Drogi krajowe')
        parm1.config(textvariable=var1)
        var2.set("5")
        parm2.config(textvariable=var2)
        var3.set("3")
        parm3.config(textvariable=var3)
        var4.set("10")
        parm4.config(textvariable=var4)
        var5.set("90")
        parm5.config(textvariable=var5)
        var6.set("0.07")
        parm6.config(textvariable=var6)
        var7.set("0.1")
        parm7.config(textvariable=var7)
        var8.set("0.3")
        parm8.config(textvariable=var8)
        var10.set("150")
        parm10.config(textvariable=var10)
        var11.set("0.000027")
        parm11.config(textvariable=var11)
        var12.set("0.000029")
        parm12.config(textvariable=var12)
        var13.set("0.00005")
        parm13.config(textvariable=var13)

    if value == 3:
        var1,var2, var3, var4, var5, var6, var7, var8, var10, var11, var12, var13 = StringVar(root), StringVar(root), StringVar(root), StringVar(
            root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root)
        var1.set('Porty lotnicze')
        parm1.config(textvariable=var1)
        var2.set("5")
        parm2.config(textvariable=var2)
        var3.set("3")
        parm3.config(textvariable=var3)
        var4.set("10")
        parm4.config(textvariable=var4)
        var5.set("90")
        parm5.config(textvariable=var5)
        var6.set("0.07")
        parm6.config(textvariable=var6)
        var7.set("0.1")
        parm7.config(textvariable=var7)
        var8.set("0.3")
        parm8.config(textvariable=var8)
        var10.set("150")
        parm10.config(textvariable=var10)
        var11.set("0.000027")
        parm11.config(textvariable=var11)
        var12.set("0.000029")
        parm12.config(textvariable=var12)
        var13.set("0.00005")
        parm13.config(textvariable=var13)

    if value == 4:
        var1,var2, var3, var4, var5, var6, var7, var8, var10, var11, var12, var13 = StringVar(root), StringVar(root), StringVar(root), StringVar(
            root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root), StringVar(root)
        var1.set('Transport kolejowy')
        parm1.config(textvariable=var1)
        var2.set("5")
        parm2.config(textvariable=var2)
        var3.set("3")
        parm3.config(textvariable=var3)
        var4.set("10")
        parm4.config(textvariable=var4)
        var5.set("90")
        parm5.config(textvariable=var5)
        var6.set("0.07")
        parm6.config(textvariable=var6)
        var7.set("0.1")
        parm7.config(textvariable=var7)
        var8.set("0.3")
        parm8.config(textvariable=var8)
        var10.set("150")
        parm10.config(textvariable=var10)
        var11.set("0.000027")
        parm11.config(textvariable=var11)
        var12.set("0.000029")
        parm12.config(textvariable=var12)
        var13.set("0.00005")
        parm13.config(textvariable=var13)


t1 = 'Droga przenoszenia choroby:'
l1 = Label(frame, text=t1, bg='white', bd=1, font=('Helvetica',10))
l1.place(relx=0.02, rely=0.2, relwidth=0.4, relheight=0.05)
t2 = 'Czas inkubacji choroby:'
l2 = Label(frame, text=t2, bg='white', bd=1, font=('Helvetica',10))
l2.place(relx=0.49, rely=0.2, relwidth=0.4, relheight=0.05)

parm1 = Spinbox(frame, values=('Granice województw','Drogi krajowe','Transport kolejowy'), font=('Helvetica',10))
parm1.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.06  )
parm2 = Spinbox(frame, from_=1, to=8, increment=1, font=('Helvetica',10))
parm2.place(relx=0.55, rely=0.25, relwidth=0.4, relheight=0.06)

t3 = 'Czas zakażania:'
l3 = Label(frame, text=t3, bg='white', font=('Helvetica',10))
l3.place(relx=0., rely=0.32, relwidth=0.3, relheight=0.05)
t4 = 'Czas zdrowienia:'
l4 = Label(frame, text=t4, bg='white', bd=1, font=('Helvetica',10))
l4.place(relx=0.5, rely=0.32, relwidth=0.3, relheight=0.05)

parm3 = Spinbox(frame, from_=1, to=10, increment=1, font=('Helvetica',10))
parm3.place(relx=0.05, rely=0.37, relwidth=0.4, relheight=0.06)
parm4 = Spinbox(frame, from_=1, to=14, increment=1, font=('Helvetica',10))
parm4.place(relx=0.55, rely=0.37, relwidth=0.4, relheight=0.06)

t5 = 'Czas odporności:'
l5 = Label(frame, text=t5, bg='white', bd=1, font=('Helvetica',10))
l5.place(relx=0., rely=0.44, relwidth=0.3, relheight=0.05)
t6 = 'Współczynnik kontaktów:'
l6 = Label(frame, text=t6, bg='white', bd=1, font=('Helvetica',10))
l6.place(relx=0.55, rely=0.44, relwidth=0.3, relheight=0.05)

parm5 = Spinbox(frame, from_=60, to=120, increment=2, font=('Helvetica',10))
parm5.place(relx=0.05, rely=0.49, relwidth=0.4, relheight=0.06)
parm6 = Spinbox(frame, from_=0.05, to=0.13, increment=0.001, font=('Helvetica',10))
parm6.place(relx=0.55, rely=0.49, relwidth=0.4, relheight=0.06)

t7 = 'Współczynnik wyzdrowień:'
l7 = Label(frame, text=t7, bg='white', bd=1, font=('Helvetica',10))
l7.place(relx=0.01, rely=0.56, relwidth=0.4, relheight=0.05)
t8 = 'Stopień izolacji:'
l8 = Label(frame, text=t8, bg='white', bd=1, font=('Helvetica',10))
l8.place(relx=0.42, rely=0.56, relwidth=0.45, relheight=0.05)

parm7 = Spinbox(frame, from_=0.08, to=0.15, increment=0.001, font=('Helvetica',10))
parm7.place(relx=0.05, rely=0.61, relwidth=0.4, relheight=0.06)
parm8 = Spinbox(frame, from_=0, to=1.0, increment=0.1, font=('Helvetica',10))
parm8.place(relx=0.55, rely=0.61, relwidth=0.4, relheight=0.06)

t9 = 'Województwo z pierwszymi przypadkami:'
l9 = Label(frame, text=t9, bg='white', bd=1, font=('Helvetica',10))
l9.place(relx=-0.1, rely=0.69, relwidth=0.7, relheight=0.05)
t10 = 'Początkowa ilość zainfekowanych:'
l10 = Label(frame, text=t10, bg='white', bd=1, font=('Helvetica',10))
l10.place(relx=0.53, rely=0.69, relwidth=0.45, relheight=0.05)

woj = ['Dolnośląskie', 'Kujawsko-pomorskie', 'Lubelskie','Lubuskie','Łódzkie', 'Małopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Śląskie', 'Świętokrzyskie', 'Warmińsko-mazurskie', 'Wielkopolskie', 'Zachodniopomorskie']
parm9 = Spinbox(frame, values=woj, font=('Helvetica',10))
parm9.place(relx=0.05, rely=0.74, relwidth=0.4, relheight=0.06)
parm10 = Spinbox(frame, from_=150, to=2000, increment=20, font=('Helvetica',10))
parm10.place(relx=0.55, rely=0.74, relwidth=0.4, relheight=0.06)

t11 = 'Współczynnik narodzin:'
l11 = Label(frame, text=t11, bg='white', bd=1, font=('Helvetica',10))
l11.place(relx=-0.001, rely=0.82, relwidth=0.4, relheight=0.05)
t12 = 'Współczynnik umieralności:'
l12 = Label(frame, text=t12, bg='white', bd=1, font=('Helvetica',10))
l12.place(relx=0.49, rely=0.82, relwidth=0.45, relheight=0.05)

parm11 = Spinbox(frame, from_=0.000017, to=0.00003, format='%10.7f', increment=0.0000001, font=('Helvetica',10))
parm11.place(relx=0.05, rely=0.87, relwidth=0.4, relheight=0.06)
parm12 = Spinbox(frame,  from_=0.000017, to=0.00003, format='%10.7f', increment=0.0000001, font=('Helvetica',10))
parm12.place(relx=0.55, rely=0.87, relwidth=0.4, relheight=0.06)

t13 = 'Śmiertelność choroby:'
l13 = Label(frame2, text=t13, bg='white', bd=1, font=('Helvetica',10))
l13.place(relx=-0.07, rely=0 , relwidth=0.5, relheight=0.4)
parm13 = Spinbox(frame2, from_=0.000017, to=0.00003, format='%10.7f', increment=0.0000001, font=('Helvetica',10))
parm13.place(relx=0.05, rely=0.4, relwidth=0.4, relheight=0.4)

varr = IntVar(root)
varr.set(4)

rb1 = Radiobutton(frame, bg='white', text='Granice województw', variable=r, value=1, font=('Helvetica',10),command = lambda:clicked(r.get()))
rb1.place(relx=0.15, rely=0.045, relwidth=0.35, relheight=0.04)

rb2= Radiobutton(frame, bg='white',text='Drogi krajowe', variable=r, value=2,font=('Helvetica',10), command = lambda:clicked(r.get()))
rb2.place(relx=0.57, rely=0.045, relwidth=0.35, relheight=0.04)
rb3= Radiobutton(frame,bg='white', text='Porty lotnicze', variable=r, value=3, font=('Helvetica',10),command = lambda:clicked(r.get()))
rb3.place(relx=0.112, rely=0.09, relwidth=0.35, relheight=0.04)
rb4= Radiobutton(frame,bg='white', text='Transport kolejowy', variable=r, value=4, font=('Helvetica',10),command = lambda:clicked(r.get()))
rb4.place(relx=0.6, rely=0.09, relwidth=0.35, relheight=0.04)

lower_frame = Frame(root, bg='white', bd=10)
lower_frame.place(relx=0.55, rely=0.26, relwidth=0.5, relheight=0.6, anchor='ne')

down_frame = Frame(root, bg='white')
down_frame.place(relx=0.55, rely=0.75, relwidth=0.5, relheight=0.15, anchor='ne')

dl1 = 'Populacja:'
dlabel1 = Label(down_frame,text=dl1, bg='white', font=('Helvetica',10))
dlabel1.place(relx=0.085, rely=0, relwidth=0.2, relheight=0.2)
dl11 = '38 422 373'
dlabel11 = Label(down_frame,text=dl11, bg='white', font=('Helvetica',10))
dlabel11.place(relx=0.4, rely=0, relwidth=0.2, relheight=0.2)

dl2 = 'Podatni na chorobę:'
dlabel2 = Label(down_frame,text=dl2, bg='white', font=('Helvetica',10))
dlabel2.place(relx=0.131, rely=0.22, relwidth=0.2, relheight=0.2)
dl22 = '38 422 373'
dlabel22 = Label(down_frame,text=dl22, bg='white', font=('Helvetica',10))
dlabel22.place(relx=0.4, rely=0.22, relwidth=0.2, relheight=0.2)

dl3 = 'Zainfekowani:'
dlabel3 = Label(down_frame,text=dl3, bg='white', font=('Helvetica',10))
dlabel3.place(relx=0.1, rely=0.45, relwidth=0.2, relheight=0.2)
dl33 = '0'
dlabel33 = Label(down_frame,text=dl33, bg='white', font=('Helvetica',10))
dlabel33.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.2)

dl4 = 'Tymczasowo odporni:'
dlabel4 = Label(down_frame,text=dl4, bg='white', font=('Helvetica',10))
dlabel4.place(relx=0.088, rely=0.68, relwidth=0.3, relheight=0.2)
dl44 = '0'
dlabel44 = Label(down_frame,text=dl44, bg='white', font=('Helvetica',10))
dlabel44.place(relx=0.4, rely=0.68, relwidth=0.2, relheight=0.2)

from PIL import ImageTk, Image

img = Image.open('{0}_disease.png'.format(0))
resized = img.resize((500,375), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)

panel = Label(lower_frame, image=new_pic)
panel.pack(pady=8)

def update(i):
    img2 = Image.open('charts\{0}_disease.png'.format(i))
    resize = img2.resize((500, 375), Image.ANTIALIAS)
    new_pic2 = ImageTk.PhotoImage(resize)
    panel.configure(image=new_pic2)
    panel.image = new_pic2

    data = pd.read_csv(r'C:\Users\PC\PycharmProjects\GSCA\SIR.csv')
    data1 = str(round(data['S'][i]))
    data2 = str(round(data['I'][i]))
    data3 = str(round(data['R'][i]))
    data4 = str(round(data['P'][i]))
    data1 = data1[0:2]+' '+ data1[2:5] +' '+ data1[5:]
    data4 = data4[0:2] + ' ' + data4[2:5] + ' ' + data4[5:]
    if len(data2) >= 6:
        if len(data2) == 7:
            data2 = data2[0]+' '+ data2[1:4] + ' ' + data2[4:]
        elif len(data2) == 8:
            data2 = data2[0:2] + ' ' + data2[2:5] + ' ' + data2[5:]
        else:
            data2 = data2[0:3] + ' ' + data2[3:]
    if len(data2) < 6:
        if len(data2) == 5:
            data2 = data2[0:2] + ' ' + data2[2:]
        elif len(data2) == 4:
            data2 = data2[0] + ' ' + data2[1:]
        else:
            data2 = data2
    if len(data3) >= 6:
        if len(data3) == 7:
            data3 = data3[0]+' '+ data3[1:4] + ' ' + data3[4:]
        elif len(data3) == 8:
            data3 = data3[0:2] + ' ' + data3[2:5] + ' ' + data3[5:]
        else:
            data3 = data3[0:3] + ' ' + data3[3:]
    if len(data3) < 6:
        if len(data3) == 5:
            data3 = data3[0:2] + ' ' + data3[2:]
        elif len(data3) == 4:
            data3 = data3[0] + ' ' + data3[1:]
        else:
            data3 = data3

    dlabel11.configure(text=data4)
    dlabel22.configure(text=data1)
    dlabel33.configure(text=data2)
    dlabel44.configure(text=data3)
    i += 5
    if i == 195:
        return
    root.after(500, update, i)

def grab():
    wojewodztwa = {
        "Dolnośląskie": 0,
        "Kujawsko-pomorskie": 1,
        "Lubelskie": 2,
        "Lubuskie": 3,
        "Łódzkie": 4,
        "Małopolskie": 5,
        "Mazowieckie": 6,
        "Opolskie": 7,
        "Podkarpackie": 8,
        "Podlaskie": 9,
        "Pomorskie": 10,
        "Śląskie": 11,
        "Świętokrzystkie": 12,
        "Warmińsko-mazurskie": 13,
        "Wielkopolskie": 14,
        "Zachodniopomorskie": 15
    }
    powiazanie = {
        'Granice województw': 'brak',
        'Transport kolejowy' : 'kolej',
        'Drogi krajowe' : 'drogi',
        'Porty lotnicze' : 'lotnictwo'
    }

    pow = powiazanie[parm1.get()]
    ti, tp, tl, tr = int(parm2.get()), int(parm3.get()), int(parm4.get()), int(parm5.get())
    al, gam = float(parm6.get()), float(parm7.get())
    w = float(parm8.get())
    woj = int(wojewodztwa[parm9.get()])
    osoby = int(parm10.get())
    ur = float(parm11.get())
    um = float(parm12.get())
    dead = float(parm13.get())
    print(pow, ti, tp, tl, tr, al, gam, w, woj, osoby, ur, um, dead)
    test(pow,ti,tp,tl,tr,al,gam,w, woj, osoby, ur, um, dead)
    root.after(0, update, 0)

warning = Label(frame, bg='white', bd=1, font=('Helvetica', 10))
warning.place(relx=0.15, rely=0.92, relwidth=0.8, relheight=0)

button = Button(frame2, bg='skyBlue', bd=3 ,text="Rozpocznij symulacje", font=('Helvetica',12), command=lambda :grab())
button.place(relx=0.57,rely=0.4 ,relheight=0.5, relwidth=0.35)




root.mainloop()
