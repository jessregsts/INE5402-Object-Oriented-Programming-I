from tkinter import*
from tkinter import ttk
from webbrowser import get
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class SistemaLocadora:
    def __init__(self,root):
        self.root=root
        self.root.title("Mikan Video")
        self.root.geometry("1550x800+0+0")

        # = Variaveis =
        self.member_var=StringVar()
        self.cad_var=StringVar()
        self.idcpf_var=StringVar()
        self.name_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.phonenumber_var=StringVar()
        self.dvdid_var=StringVar()
        self.director_var=StringVar()
        self.date1_var=StringVar()
        self.date2_var=StringVar()
        self.date3_var=StringVar()
        self.latedays_var=StringVar()
        self.finalprice_var=StringVar()

        # = Titulo =
        lbltitle=Label(self.root,text="Mikan Video",bg="palegreen",fg="darkorange",bd=10,relief=RIDGE,font=("comic sans ms",30,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        # = Caixa 1 =
        frame=Frame(self.root,bd=7,relief=RIDGE,padx=20,bg="peachpuff")
        frame.place(x=0,y=90,width=1366,height=400)
        # = Caixa 1 esquerda  =
        DataFrameLeft=LabelFrame(frame,text="Insira seus Dados",bg="peachpuff",fg="darkorange",bd=12,relief=RIDGE,font=("comic sans ms",12))
        DataFrameLeft.place(x=0,y=5,width=800,height=350)

        lblMember=Label(DataFrameLeft,bg="peachpuff",text="Membro: 🧙",font=("comic sans ms",15),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        
        from tkinter import ttk
        comMember=ttk.Combobox(DataFrameLeft,font=("comic sans ms",14),width=17,state="readonly",textvariable=self.member_var)
        comMember["value"]=("Jedi Padawan", "Jedi Master", "Jedi Grandmaster")
        comMember.grid(row=0,column=1)

        lblCadastro=Label(DataFrameLeft,bg="peachpuff",text="Nº Cadastro:",font=("comic sans ms",14),padx=2,pady=6)
        lblCadastro.grid(row=1,column=0,sticky=W)
        txtCadastro=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.cad_var,width=17)
        txtCadastro.grid(row=1,column=1)

        lblIDCPF=Label(DataFrameLeft,bg="peachpuff",text="Nº ID/CPF:",font=("comic sans ms",14),padx=2,pady=6)
        lblIDCPF.grid(row=2,column=0,sticky=W)
        txtIDCPF=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.idcpf_var,width=17)
        txtIDCPF.grid(row=2,column=1)

        lblName=Label(DataFrameLeft,bg="peachpuff",text="Nome: ☺️",font=("comic sans ms",14),padx=2,pady=6)
        lblName.grid(row=3,column=0,sticky=W)
        txtName=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.name_var,width=17)
        txtName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="peachpuff",text="Sobrenome:",font=("comic sans ms",14),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.lastname_var,width=17)
        txtLastName.grid(row=4,column=1)

        lblAddress=Label(DataFrameLeft,bg="peachpuff",text="Endereço:",font=("comic sans ms",14),padx=2,pady=6)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.address_var,width=17)
        txtAddress.grid(row=5,column=1)

        lblPhoneNumber=Label(DataFrameLeft,bg="peachpuff",text="Telefone: ☎️",font=("comic sans ms",14),padx=2,pady=6)
        lblPhoneNumber.grid(row=6,column=0,sticky=W)
        txtPhoneNumber=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.phonenumber_var,width=17)
        txtPhoneNumber.grid(row=6,column=1)

        lblIdDvd=Label(DataFrameLeft,bg="peachpuff",text="ID Dvd:",font=("comic sans ms",14),padx=2,pady=6)
        lblIdDvd.grid(row=0,column=2,sticky=W)
        txtIdDvd=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.dvdid_var,width=17)
        txtIdDvd.grid(row=0,column=3)

        lblDirector=Label(DataFrameLeft,bg="peachpuff",text="Direção: 🎞️",font=("comic sans ms",14),padx=2,pady=6)
        lblDirector.grid(row=1,column=2,sticky=W)
        txtDirector=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.director_var,width=17)
        txtDirector.grid(row=1,column=3)

        lblDate1=Label(DataFrameLeft,bg="peachpuff",text="Data Empréstimo:",font=("comic sans ms",14),padx=2,pady=6)
        lblDate1.grid(row=2,column=2,sticky=W)
        txtDate1=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.date1_var,width=17)
        txtDate1.grid(row=2,column=3)

        lblData2=Label(DataFrameLeft,bg="peachpuff",text="Data Devolução 1:",font=("comic sans ms",14),padx=2,pady=6)
        lblData2.grid(row=3,column=2,sticky=W)
        txtData2=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.date2_var,width=17)
        txtData2.grid(row=3,column=3)

        lblData3=Label(DataFrameLeft,bg="peachpuff",text="Data Devolução 2:",font=("comic sans ms",14),padx=2,pady=6)
        lblData3.grid(row=4,column=2,sticky=W)
        txtData3=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.date3_var,width=17)
        txtData3.grid(row=4,column=3)

        lblLate=Label(DataFrameLeft,bg="peachpuff",text="Dias em Atraso:",font=("comic sans ms",14),padx=2,pady=6)
        lblLate.grid(row=5,column=2,sticky=W)
        txtLate=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.latedays_var,width=17)
        txtLate.grid(row=5,column=3)

        lblFP=Label(DataFrameLeft,bg="peachpuff",text="Preço Final:",font=("comic sans ms",14),padx=2,pady=6)
        lblFP.grid(row=6,column=2,sticky=W)
        txtFP=Entry(DataFrameLeft,font=("comic sans ms",14),textvariable=self.finalprice_var,width=17)
        txtFP.grid(row=6,column=3)

        # = Caixa 1 direita =
        DataFrameRight=LabelFrame(frame,text="Detalhes do Produto",bg="peachpuff",fg="darkorange",bd=12,relief=RIDGE,font=("comic sans ms",12))
        DataFrameRight.place(x=810,y=5,width=500,height=350)

        self.txtBox=Text(DataFrameRight,font=("comic sans ms",12),width=23,height=12,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        
        listMovies=['Carrie','Amelie','Old Boy','Pulp Fiction','Alien','Burning','Paprika','The Evil Dead','Split','After Yang','In The Mood For Love','Mulan','The Witch','Happy Together','Falen Angels','My Neighbor Totoro','Umma','Chungking Express','Columbus','Drive My Car','Spirited Away','Princess Mononoke','Turning Red','The Batman','Executive Order','500 Days of Summer','Black Swan','The Handmaiden','Blade Runner','Aquarius','Melancholia','A Ghost Story','Licorice Pizza','Before Sunset','Madame Satã','The Sword in The Stone','Before Sunrise','High Life','The Green Knight','Dead Poets Society','Coda','X','As Tears Go By','2046','Titane','Seven Samurai','Perfect Blue','Uncut Gems','Millenium Actress','Men','Evil Dead 2','Mad God','Fantastic Mr. Fox','Tokyo Story','Cha Cha Real Smooth','The Edge of Seventeen','Millenium Mambo','Farewell My Concubine','The Tree Of Life','Thor Love and Thunder','Last Night In Soho','Whiplash']
        
        def SelectMovie(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Carrie"):
                self.dvdid_var.set("BTS00001")
                self.director_var.set("Brian De Palma")
                
                d1=datetime.datetime.today()
                self.date1_var.set(d1)
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date2_var.set(d3)
                d4=datetime.timedelta(days=20)
                d5=d1+d4
                self.date3_var.set(d5)
                ld=("5 dias")
                self.latedays_var.set(ld)
                fp=("R$9.50")
                self.finalprice_var.set(fp)
            elif (x=="Amelie"):
                self.dvdid_var.set("BTS00002")
                self.director_var.set("Jean-Pierre Jeunet")
                
                d1=datetime.datetime.today()
                self.date1_var.set(d1)
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date2_var.set(d3)
                d4=datetime.timedelta(days=2)
                d5=d1+d4
                self.date3_var.set(d5)
                ld=("0 dias")
                self.latedays_var.set(ld)
                fp=("R$7.00")
                self.finalprice_var.set(fp)
            elif (x=="Old Boy"):
                self.dvdid_var.set("BTS00003")
                self.director_var.set("Park Chan-wook")
                
                d1=datetime.datetime.today()
                self.date1_var.set(d1)
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date2_var.set(d3)
                d4=datetime.timedelta(days=16)
                d5=d1+d4
                self.date3_var.set(d5)
                ld=("1 dia")
                self.latedays_var.set(ld)
                fp=("R$7.50")
                self.finalprice_var.set(fp)
            elif (x=="Pulp Fiction"):
                self.dvdid_var.set("BTS00004")
                self.director_var.set("Quentin Tarantino")
                
                d1=datetime.datetime.today()
                self.date1_var.set(d1)
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date2_var.set(d3)
                d4=datetime.timedelta(days=18)
                d5=d1+d4
                self.date3_var.set(d5)
                ld=("3 dias")
                self.latedays_var.set(ld)
                fp=("R$8.50")
                self.finalprice_var.set(fp)
            elif (x=="Alien"):
                self.dvdid_var.set("BTS00005")
                self.director_var.set("Ridley Scott")
                
                d1=datetime.datetime.today()
                self.date1_var.set(d1)
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date2_var.set(d3)
                d4=datetime.timedelta(days=0)
                d5=d1+d4
                self.date3_var.set(d5)
                ld=("0 dias")
                self.latedays_var.set(ld)
                fp=("R$7.00")
                self.finalprice_var.set(fp)
            elif (x=="Burning"):
                self.dvdid_var.set("BTS00006")
                self.director_var.set("Lee Chang-dong")
                
                d1=datetime.datetime.today()
                self.date1_var.set(d1)
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date2_var.set(d3)
                d4=datetime.timedelta(days=30)
                d5=d1+d4
                self.date3_var.set(d5)
                ld=("15 dias")
                self.latedays_var.set(ld)
                fp=("R$14.50")
                self.finalprice_var.set(fp)
            


        listBox=Listbox(DataFrameRight,font=("comic sans ms",12),width=20,height=12)
        listBox.grid(row=0,column=0,padx=4)
        listBox.bind("<<ListboxSelect>>",SelectMovie)
        listScrollbar.config(command=listBox.yview)
        

        for item in listMovies:
            listBox.insert(END,item)

        # = Caixa 2 =
        FrameButton=Frame(self.root,bd=7,relief=RIDGE,padx=20,bg="peachpuff")
        FrameButton.place(x=0,y=495,width=1366,height=55)

        btnAddButton=Button(FrameButton,command=self.adda_data,text="Add. Dados",font=("comic sans ms",12),width=21,bg="mediumaquamarine",fg="white")
        btnAddButton.grid(row=0,column=0)

        btnAddButton=Button(FrameButton,command=self.showData,text="Mostrar Dados",font=("comic sans ms",12),width=21,bg="mediumaquamarine",fg="white")
        btnAddButton.grid(row=0,column=1)

        btnAddButton=Button(FrameButton,command=self.update,text="Atualizar",font=("comic sans ms",12),width=21,bg="mediumaquamarine",fg="white")
        btnAddButton.grid(row=0,column=2)

        btnAddButton=Button(FrameButton,command=self.delete,text="Deletar",font=("comic sans ms",12),width=21,bg="mediumaquamarine",fg="white")
        btnAddButton.grid(row=0,column=3)

        btnAddButton=Button(FrameButton,command=self.reset,text="Resetar",font=("comic sans ms",12),width=21,bg="mediumaquamarine",fg="white")
        btnAddButton.grid(row=0,column=4)

        btnAddButton=Button(FrameButton,command=self.iExit,text="Sair",font=("comic sans ms",12),width=21,bg="mediumaquamarine",fg="white")
        btnAddButton.grid(row=0,column=5)

        # = Caixa 3 =
        FrameDetails=Frame(self.root,bd=7,relief=RIDGE,padx=20,bg="peachpuff")
        FrameDetails.place(x=0,y=570,width=1366,height=130)

        TableFrame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="peachpuff")
        TableFrame.place(x=0,y=2,width=1310,height=112)

        
        xscroll=ttk.Scrollbar(TableFrame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(TableFrame,orient=VERTICAL )
        self.mikan_table=ttk.Treeview(TableFrame,column=("member","cad","idcpf","name","lastname","address","phonenumber","dvdid","director","date1","date2","date3","latedays","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.mikan_table.xview)
        yscroll.config(command=self.mikan_table.yview)

        self.mikan_table.heading("member",text="Membro")
        self.mikan_table.heading("cad",text="Nº Cadastro")
        self.mikan_table.heading("idcpf",text="Nº ID/CPF")
        self.mikan_table.heading("name",text="Nome")
        self.mikan_table.heading("lastname",text="Sobrenome")
        self.mikan_table.heading("address",text="Endereço")
        self.mikan_table.heading("phonenumber",text="Telefone")
        self.mikan_table.heading("dvdid",text="ID DVD")
        self.mikan_table.heading("director",text="Direção")
        self.mikan_table.heading("date1",text="Data Empréstimo")
        self.mikan_table.heading("date2",text="Data Devolução 1")
        self.mikan_table.heading("date3",text="Data Devolução 2")
        self.mikan_table.heading("latedays",text="Dias em Atraso")
        self.mikan_table.heading("finalprice",text="Preço Final")

        self.mikan_table["show"]="headings"
        self.mikan_table.pack(fill=BOTH,expand=1)

        self.mikan_table.column("member",width=100)
        self.mikan_table.column("cad",width=100)
        self.mikan_table.column("idcpf",width=100)
        self.mikan_table.column("name",width=100)
        self.mikan_table.column("lastname",width=100)
        self.mikan_table.column("address",width=100)
        self.mikan_table.column("phonenumber",width=100)
        self.mikan_table.column("dvdid",width=100)
        self.mikan_table.column("director",width=100)
        self.mikan_table.column("date1",width=100)
        self.mikan_table.column("date2",width=100)
        self.mikan_table.column("date3",width=100)
        self.mikan_table.column("latedays",width=100)
        self.mikan_table.column("finalprice",width=100)

        self.fatch_data()
        self.mikan_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="32462584",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into mikanvideo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.member_var.get(),self.cad_var.get(),self.idcpf_var.get(),self.name_var.get(),self.lastname_var.get(),self.address_var.get(),self.phonenumber_var.get(),self.dvdid_var.get(),self.director_var.get(),self.date1_var.get(),self.date2_var.get(),self.date3_var.get(),self.latedays_var.get(),self.finalprice_var.get()))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Sucesso","Membro inserido com sucesso")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="32462584",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update mikanvideo set member=%s,cad=%s,idcpf=%s,name=%s,lastname=%s,address=%s,phonenumber=%s,dvdid=%s,director=%s,date1=%s,date2=%s,date3=%s,latedays=%s where cad=%s",(self.member_var.get(),self.cad_var.get(),self.idcpf_var.get(),self.name_var.get(),self.lastname_var.get(),self.address_var.get(),self.phonenumber_var.get(),self.dvdid_var.get(),self.director_var.get(),self.date1_var.get(),self.date2_var.get(),self.date3_var.get(),self.latedays_var.get(),self.finalprice_var.get(),))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Sucesso","Cadastro atualizado")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="32462584",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from mikanvideo")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.mikan_table.delete(*self.mikan_table.get_children())
            for i in rows:
                self.mikan_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.mikan_table.focus()
        content=self.mikan_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.cad_var.set(row[1]),
        self.idcpf_var.set(row[2]),
        self.name_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address_var.set(row[5]),
        self.phonenumber_var.set(row[6]),
        self.dvdid_var.set(row[7]),
        self.director_var.set(row[8]),
        self.date1_var.set(row[9]),
        self.date2_var.set(row[10]),
        self.date3_var.set(row[11]),
        self.latedays_var.set(row[12]),
        self.finalprice_var.set(row[13]),

    def showData(self):
        self.txtBox.insert(END,"Membro\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"Nº Cadastro\t\t"+ self.cad_var.get() + "\n")
        self.txtBox.insert(END,"Nº ID/CPF\t\t"+ self.idcpf_var.get() + "\n")
        self.txtBox.insert(END,"Nome\t\t"+ self.name_var.get() + "\n")
        self.txtBox.insert(END,"Sobrenome\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Endereço\t\t"+ self.address_var.get() + "\n")
        self.txtBox.insert(END,"Telefone\t\t"+ self.phonenumber_var.get() + "\n")
        self.txtBox.insert(END,"ID DVD\t\t"+ self.dvdid_var.get() + "\n")
        self.txtBox.insert(END,"Direção\t\t"+ self.director_var.get() + "\n")
        self.txtBox.insert(END,"Data Empréstimo \t\t"+ self.date1_var.get() + "\n")
        self.txtBox.insert(END,"Data Devolução 1\t\t"+ self.date2_var.get() + "\n")
        self.txtBox.insert(END,"Dias Devolução 2\t\t"+ self.date3_var.get() + "\n")
        self.txtBox.insert(END,"Dias em Atraso\t\t"+ self.latedays_var.get() + "\n")
        self.txtBox.insert(END,"Preço Final\t\t"+ self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.cad_var.set(""),
        self.idcpf_var.set(""),
        self.name_var.set(""),
        self.lastname_var.set(""),
        self.address_var.set(""),
        self.phonenumber_var.set(""),
        self.dvdid_var.set(""),
        self.director_var.set(""),
        self.date1_var.set(""),
        self.date2_var.set(""),
        self.date3_var.set(""),
        self.latedays_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0", END)
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Sistema Mikan Video", "Sair da página?")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="32462584",database="mydata")
            my_cursor=conn.cursor()
            query="delete from mikanvideo where cad=%s"
            value=(self.cad_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Sucesso","Membro Deletado")


if __name__ == "__main__":
    root=Tk()
    obj=SistemaLocadora(root)
    root.mainloop()
