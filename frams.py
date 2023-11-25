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
        self.mode = "Dia"
        age_lable = Label(self.perdit_canvas,text = "Age:",font = ("Arial", 15))
        age_lable.place(x = 30,y=30,width=50,height = 25)

        age_entry = Entry(self.perdit_canvas,font = ("Arial", 15))
        age_entry.place(x = 100,y = 30,width=100,height = 25)

        np_label = Label(self.perdit_canvas,text = "No of times pregnant:",font = ("Arial",15))
        np_label.place(x = 30,y=100,width = 195,height = 25)

        np_entry = Entry(self.perdit_canvas,font = ("Arial", 15))
        np_entry.place(x = 250,y = 100,width=100,height = 25)

        pgc_label = Label(self.perdit_canvas, text="Plasma glucose concentration:", font=("Arial", 15))
        pgc_label.place(x=30, y=170, width=274, height=25)

        pgc_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        pgc_entry.place(x=330, y=170, width=100, height=25)

        bmi_label = Label(self.perdit_canvas,text = "Body mass index:", font=("Arial", 15))
        bmi_label.place(x = 30,y=240,width = 161,height = 25)

        bmi_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        bmi_entry.place(x=220, y=240, width=100, height=25)

        dpf_label = Label(self.perdit_canvas,text = "Diabetes pedigree function:", font=("Arial", 15))
        dpf_label.place(x = 30,y=310, width=244, height=25)

        dpf_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        dpf_entry.place(x = 300, y=310, width=100, height=25)

        def dist():
            age_lable.destroy()
            age_entry.destroy()

            np_label.destroy()
            np_entry.destroy()

            pgc_label.destroy()
            pgc_entry.destroy()

            bmi_label.destroy()
            bmi_entry.destroy()

            dpf_label.destroy()
            dpf_entry.destroy()

    def check_mode(self):
        if self.mode is None:
            pass
        elif self.mode == "Dia":
            self.dia_mode.dist()

    def hea_mode(self):
        """
        fasting blood sugar > 120 mg/dl
        resting electrocardiographic results
        maximum heart rate achieved
        exercise induced angina
        oldpeak
        slope of peak
        number of major vessels
        thal
        :return:
        """
        self.mode = "Hea"
        age_lable = Label(self.perdit_canvas, text="Age:", font=("Arial", 15))
        age_lable.place(x=30, y=30, width=50, height=25)

        age_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        age_entry.place(x=100, y=30, width=100, height=25)

        sex_label = Label(self.perdit_canvas, text="Sex:", font=("Arial", 15))
        sex_label.place(x=30, y=100, width=50, height=25)

        sex_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        sex_entry.place(x=100, y=100, width=100, height=25)

        cpt_label = Label(self.perdit_canvas, text="chest pain type:", font=("Arial", 15))
        cpt_label.place(x=30, y=170, width=274, height=25)

        cpt_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        cpt_entry.place(x=330, y=170, width=100, height=25)

        rbp_label = Label(self.perdit_canvas, text="resting blood pressure:", font=("Arial", 15))
        rbp_label.place(x=30, y=240, width=161, height=25)

        rbp_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        rbp_entry.place(x=220, y=240, width=100, height=25)

        c_label = Label(self.perdit_canvas, text="cholestoral:", font=("Arial", 15))
        c_label.place(x=30, y=310, width=244, height=25)

        c_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        c_entry.place(x=300, y=310, width=100, height=25)

        dia_label = Label(self.perdit_canvas,text="diabetes", font=("Arial", 15))
        dia_label.place(x=30, y=380, width=244, height=25)


if __name__ == "__main__":
    root = Tk()
    loading = Frame(root,width=1800,height = 1000,bg="black")
    main_program = Frame(root,width=1800,height = 1000,bg="white")
    loading_frame = LoadingScreen(main_program,loading)
    loading.pack()
    root.mainloop()