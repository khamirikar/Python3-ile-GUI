#!/usr/bin/env python
# coding: utf-8

# In[26]:


from tkinter import *
from tkcalendar import DateEntry

Window = Tk()
canvas = Canvas(Window, height=450, width=750 )
canvas.pack()

frame_ust = Frame(Window, bg='#808080')
frame_ust.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)

frame_alt_sol = Frame(Window, bg='#808080')
frame_alt_sol.place(relx=0.1, rely=0.21, relheight=0.5, relwidth=0.23)

frame_alt_sag = Frame(Window, bg='#808080')
frame_alt_sag.place(relx=0.34, rely=0.21, relheight=0.5, relwidth=0.56)

Yazi_hatirlatma = Label(frame_ust, bg='#808080', text="Hatirlatma yazi", font="Verdana 12 bold" )
Yazi_hatirlatma.pack(padx=10, pady=10, side=LEFT)

Yazi_hatirlatma_ops = StringVar(frame_ust)
Yazi_hatirlatma_ops.set("Opsiyon secin")
Yazi_hatirlatma_acilirmenu = OptionMenu(frame_ust,
                                        Yazi_hatirlatma_ops,
                                        "Dogum gunu",
                                        "alisveris",
                                        "Odeme"
                                       )
Yazi_hatirlatma_acilirmenu.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarih = DateEntry(frame_ust, width=12, background = "orange", foreground = "black",
                             borderwidth=1,locale="de_De" )
hatirlatma_tarih._top_cal.overrideredirect(False)
hatirlatma_tarih.pack(padx=10, pady=10, side=RIGHT)
#codetyper NmK
Yazi_hatirlatma_tarih = Label(frame_ust, bg='#808080', text="Hatirlatma Tarihi", font="Verdana 12 bold" )
Yazi_hatirlatma_tarih.pack(padx=10, pady=10, side=RIGHT)

Yazi_yontem = Label(frame_alt_sol, bg='#808080', text="Hatirlatma yontemi", font="Verdana 10 bold" )
Yazi_yontem.pack(padx=10, pady=10, anchor=NW)

var = IntVar()
b1 = Radiobutton(frame_alt_sol, text='Sisteme kaydet', variable=var, value=1, bg='#808080',
                 font='Verdana 8'
                  )
b1.pack(anchor=NW, pady=5, padx=15)

b2 = Radiobutton(frame_alt_sol, text='Eposata gonder', variable=var, value=2, bg='#808080',
                 font='Verdana 8'
                  )
b2.pack(anchor=NW, pady=5, padx=15)

var1 = IntVar()
c1 = Checkbutton(frame_alt_sol, text="Bir hafta once", variable=var1, onvalue=1, offvalue=0, bg='#808080',
                 font='Verdana 8')
c1.pack(ancho=NW, pady=2, padx=25)

var2 = IntVar()
c2 = Checkbutton(frame_alt_sol, text="Bir gun once", variable=var2, onvalue=1, offvalue=0, bg='#808080',
                 font='Verdana 8')
c2.pack(ancho=NW, pady=2, padx=25)

var3 = IntVar()
c3 = Checkbutton(frame_alt_sol, text="ayni gun", variable=var3, onvalue=1, offvalue=0, bg='#808080',
                 font='Verdana 8')
c3.pack(ancho=NW, pady=2, padx=25)

from tkinter import messagebox
def gonder():#codingNmK
    son_mesaj = ""
    try:
        
        if var.get():
            if var.get() == 1:
                son_mesaj += "Veri basariyla sisteme kaydedildi"
            
                tip = Yazi_hatirlatma_ops.get() if Yazi_hatirlatma_ops.get()== '' else "Genel"
                tarih = hatirlatma_tarih.get()
                mesaj = YourText.get("1.0", "end")
                
            
                with open("HatirlatmaMeti.txt","w", encoding="utf-8") as dosya:
                    dosya.write('{} kategorisi , {} tarihinde , {} mesaji'.format(tip, tarih, mesaj))
            
            elif var.get() == 2:
                son_mesaj += "e-posta ile sisteme kaydedildi"
            messagebox.showinfo("islem basarili", son_mesaj)
        else:
            son_mesaj += "Gerekli alanlar doldurulmadi"
            messagebox.showwarning("Bilgi yetersiz", son_mesaj)
    except:
        son_mesaj += "islem basarisiz oldu "
        messagebox.showerror("basarisiz islem ", son_mesaj)
    
    finally:
        Window.destroy()


Label(frame_alt_sag, bg='#808080', text="Hatirlatma Mesaji", font="Verdana 10 bold" ).pack(padx=10, pady=10)

YourText = Text(frame_alt_sag, height=9, width=50)
YourText.tag_configure("RENKLENDIRME", foreground="black",font="Verdana 8 bold")
YourText.pack()
#CodedwithNmK
YourText_bos = "Buraya Mesajini Ekle..."
YourText.insert(END, YourText_bos,'RENKLENDIRME')



YourText_button = Button(frame_alt_sag, text="GONDER", command=gonder)
YourText_button.pack(anchor=S)



Window.mainloop()


# In[ ]:




