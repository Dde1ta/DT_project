from tkinter import *

class LoadingScreen:
    def __init__(self,root,master = None):
        self.master = master
        self.root = root
        self.objects()

    def objects(self):
        self.label_increase = Label(self.master,bg = "cyan")
        self.label_increase.place(x = 450,y = 500,width=50,height=20)
        loading_name = Label(self.master,text = "LOADING",font = ("Arial", 65),bg = "black",fg="white")
        loading_name.place(x = 575,y = 250,width=400,height=150)
        button_start = Button(self.master,text = "Clike me to start loading",
                                   command=lambda :self.start_increase(10))
        button_start.place(x = 100,y = 200,width = 50,
                                   height = 100,)

    def increase_to(self,r):
        if r> 600:
            self.master.after(100,self.distroy)
        else:
            self.label_increase.place(x = 450,y = 500,width=50+r,height=20)
            self.master.update()
            self.start_increase(r+1)

    def start_increase(self,r):
        self.master.after(1,lambda:self.increase_to(r))

    def distroy(self):
        main_ = MainFrame(self.root)
        self.root.pack()
        self.master.destroy()

class MainFrame:
    def __init__(self,master = None):
        self.mode = None
        self.master = master
        self.canvass()

    def canvass(self):
        self.disease_canvas = Canvas(self.master,width=300,height = 1000,bg = "blue",borderwidth=0)
        self.disease_canvas.place(x = 0,y=0)
        self.disease_canvas_objects()

        self.perdit_canvas = Canvas(self.master,width=1500,height = 700,borderwidth=0)
        self.perdit_canvas.place(x = 300,y=0)

        self.result_canvas = Canvas(self.master,width = 1500,height = 250,bg = "green")
        self.result_canvas.place(x = 300, y=600)

    def disease_canvas_objects(self):
        dia_button = Button(self.disease_canvas,text = "Diabetes",font = ("Arial", 20),command=self.dia_mode)
        dia_button.place(x = 50,y = 150,width=200,height = 45)

        heart_button = Button(self.disease_canvas, text="Heart Attack Chance", font=("Arial", 20),command=self.hea_mode)
        heart_button.place(x=20, y=350, width=270, height=45)

        hep_button = Button(self.disease_canvas, text="Hepatitis", font=("Arial", 25))
        hep_button.place(x=50, y=550, width=200, height=45)

    def dia_mode(self):
        self.check_mode()
        self.mode = "Dia"
        self.age_label = Label(self.perdit_canvas,text = "Age:",font = ("Arial", 15))
        self.age_label.place(x = 30,y=30,width=50,height = 25)

        self.age_entry = Entry(self.perdit_canvas,font = ("Arial", 15))
        self.age_entry.place(x = 100,y = 30,width=100,height = 25)

        self.np_label = Label(self.perdit_canvas,text = "No of times pregnant:",font = ("Arial",15))
        self.np_label.place(x = 30,y=100,width = 195,height = 25)

        self.np_entry = Entry(self.perdit_canvas,font = ("Arial", 15))
        self.np_entry.place(x = 250,y = 100,width=100,height = 25)

        self.pgc_label = Label(self.perdit_canvas, text="Plasma glucose concentration:", font=("Arial", 15))
        self.pgc_label.place(x=30, y=170, width=274, height=25)

        self.pgc_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.pgc_entry.place(x=330, y=170, width=100, height=25)

        self.bmi_label = Label(self.perdit_canvas,text = "Body mass index:", font=("Arial", 15))
        self.bmi_label.place(x = 30,y=240,width = 161,height = 25)

        self.bmi_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.bmi_entry.place(x=220, y=240, width=100, height=25)

        self.dpf_label = Label(self.perdit_canvas,text = "Diabetes pedigree function:", font=("Arial", 15))
        self.dpf_label.place(x = 30,y=310, width=244, height=25)

        self.dpf_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.dpf_entry.place(x = 300, y=310, width=100, height=25)

    def dist_dia(self):
        self.age_label.destroy()
        self.age_entry.destroy()

        self.np_label.destroy()
        self.np_entry.destroy()

        self.pgc_label.destroy()
        self.pgc_entry.destroy()

        self.bmi_label.destroy()
        self.bmi_entry.destroy()

        self.dpf_label.destroy()
        self.dpf_entry.destroy()

    def check_mode(self):
        if self.mode is None:
            pass
        elif self.mode == "Dia":
            self.dist_dia()
        elif self.mode == "Hea":
            self.dist_hea()

    def hea_mode(self):
        self.check_mode()
        self.mode = "Hea"
        self.age_label = Label(self.perdit_canvas, text="Age:", font=("Arial", 15))
        self.age_label.place(x=30, y=30, width=50, height=25)

        self.age_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.age_entry.place(x=100, y=30, width=100, height=25)

        self.sex_label = Label(self.perdit_canvas, text="Sex:", font=("Arial", 15))
        self.sex_label.place(x=30, y=100, width=50, height=25)

        self.sex_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.sex_entry.place(x=100, y=100, width=100, height=25)

        self.cpt_label = Label(self.perdit_canvas, text="Chest pain type:", font=("Arial", 15))
        self.cpt_label.place(x=30, y=170, width=160, height=25)

        self.cpt_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.cpt_entry.place(x=200, y=170, width=100, height=25)

        self.rbp_label = Label(self.perdit_canvas, text="Resting blood pressure:", font=("Arial", 15))
        self.rbp_label.place(x=30, y=240, width=221, height=25)

        self.rbp_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.rbp_entry.place(x=250, y=240, width=100, height=25)

        self.c_label = Label(self.perdit_canvas, text="Cholestoral:", font=("Arial", 15))
        self.c_label.place(x=30, y=310, width=120, height=25)

        self.c_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.c_entry.place(x=170, y=310, width=100, height=25)

        self.dia_label = Label(self.perdit_canvas,text="Fasting blood sugar:", font=("Arial", 15))
        self.dia_label.place(x=30, y=380, width=195, height=25)

        self.dia_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.dia_entry.place(x=250, y=380, width=195, height=25)

        self.rer_label = Label(self.perdit_canvas, text="Resting electrocardiographic results:", font=("Arial", 15))
        self.rer_label.place(x=30, y=450, width=340, height=25)

        self.rer_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.rer_entry.place(x=400, y=450, width=195, height=25)

        self.mhr_label = Label(self.perdit_canvas, text="Maximum heart rate achieved:", font=("Arial", 15))
        self.mhr_label.place(x=30, y=520, width=290, height=25)

        self.mhr_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.mhr_entry.place(x=350, y=520, width=195, height=25)

    def dist_hea(self):
        self.age_label.destroy()
        self.age_entry.destroy()

        self.sex_entry.destroy()
        self.sex_label.destroy()

        self.cpt_label.destroy()
        self.cpt_entry.destroy()

        self.rbp_label.destroy()
        self.rbp_entry.destroy()

        self.c_label.destroy()
        self.c_entry.destroy()

        self.dia_label.destroy()
        self.dia_entry.destroy()

        self.rer_entry.destroy()
        self.rer_label.destroy()

        self.mhr_entry.destroy()
        self.mhr_label.destroy()


if __name__ == "__main__":
    root = Tk()
    loading = Frame(root,width=1800,height = 1000,bg="black")
    main_program = Frame(root,width=1800,height = 1000,bg="white")
    loading_frame = LoadingScreen(main_program,loading)
    loading.pack()
    root.mainloop()