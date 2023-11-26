from tkinter import *

import numpy as np

from Model.preparingModels import Models

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
        self.start_increase(10)

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
        model = Models("Model/options.json")
        self.dia_model,self.hea_model,self.hep_model = model.load_models()
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

        hep_button = Button(self.disease_canvas, text="Hepatitis", font=("Arial", 25),command=self.hep_mode)
        hep_button.place(x=50, y=550, width=200, height=45)

    def result_canvas_objects(self):
        self.predict_button = Button(self.result_canvas,text = "Predict", font = ("Arial", 15),command=self.predict)
        self.predict_button.place(x= 800,y = 75)

    def predict(self):
        if self.mode == "Dia":
            self.per_dia()
        elif self.mode == "Hea":
            self.per_hea()

        elif self.mode == "Hep":
            self.per_hep()
    def per_dia(self):
        try:
            sample = np.array([
                float(self.np_entry.get()),
                float(self.pgc_entry.get()),
                float(self.bmi_entry.get()),
                float(self.dpf_entry.get()),
                float(self.age_entry.get())

            ]).reshape(1,-1)

            result = self.dia_model.predict(sample)[0]

            try:
                self.error_label.destroy()
                self.result_label.destroy()
            except:
                pass

            self.result_label = Label(self.result_canvas, text = f"The result is {result}",font = ("Arial", 25))
            self.result_label.place(x = 450 , y= 50,width = 200, height = 30)
        except:
            self.error_label = Label(self.result_canvas,text = "Non integer value entered",font = ("Arial",15))
            self.error_label.place(x = 400 , y=10,width = 250,height = 25)

    def per_hea(self):
        try:
            sample = np.array([
                float(self.age_entry.get()),
                float(self.g_entry.get()),
                float(self.cpt_entry.get()),
                float(self.rbp_entry.get()),
                float(self.c_entry.get()),
                float(self.dia_entry.get()),
                float(self.rer_entry.get()),
                float(self.mhr_entry.get()),
            ]).reshape(1,-1)

            result = self.hea_model.predict(sample)[0]

            try:
                self.error_label.destroy()
                self.result_label.destroy()
            except:
                pass

            self.result_label = Label(self.result_canvas, text = f"The result is {result}",font = ("Arial", 25))
            self.result_label.place(x = 450 , y= 50,width = 200, height = 30)
        except:
            self.error_label = Label(self.result_canvas,text = "Non integer value entered",font = ("Arial",15))
            self.error_label.place(x = 400 , y=10,width = 250,height = 25)

    def per_hep(self):

        sample = np.array([
            float(self.f_entry.get()),
            float(self.a_entry.get()),
            float(self.sp_entry.get()),
            float(self.as_entry.get()),
            float(self.va_entry.get()),
            float(self.b_entry.get()),
            float(self.ap_entry.get()),
            float(self.sg_entry.get()),
            float(self.alb_entry.get()),
            float(self.p_entry.get()),
        ]).reshape(1, -1)

        result = self.hep_model.predict(sample)[0]

        try:
            self.error_label.destroy()
            self.result_label.destroy()
        except:
            pass

        self.result_label = Label(self.result_canvas, text=f"The result is {result}", font=("Arial", 25))
        self.result_label.place(x=450, y=50, width=200, height=30)

            # self.error_label = Label(self.result_canvas, text="Non integer value entered", font=("Arial", 15))
            # self.error_label.place(x=400, y=10, width=250, height=25)

    def check_mode(self):
        try:
            self.error_label.destroy()
            self.result_label.destroy()
        except:
            try:
                self.result_label.destroy()
            except:
                pass
        if self.mode is None:
            self.result_canvas_objects()
        elif self.mode == "Dia":
            self.dist_dia()
        elif self.mode == "Hea":
            self.dist_hea()
        elif self.mode == "Hep":
            self.dist_hep()

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

    def hea_mode(self):
        self.check_mode()
        self.mode = "Hea"
        self.age_label = Label(self.perdit_canvas, text="Age:", font=("Arial", 15))
        self.age_label.place(x=30, y=30, width=50, height=25)

        self.age_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.age_entry.place(x=100, y=30, width=100, height=25)

        self.g_label = Label(self.perdit_canvas, text="Gender:", font=("Arial", 15))
        self.g_label.place(x=30, y=100, width=78, height=25)

        self.g_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.g_entry.place(x=170, y=100, width=100, height=25)

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

        self.g_entry.destroy()
        self.g_label.destroy()

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

    def hep_mode(self):
        self.check_mode()
        self.mode = "Hep"

        self.f_label = Label(self.perdit_canvas,text = "Do you have fatigue:", font=("Arial", 15))
        self.f_label.place(x=30, y=30, width=190, height=25)

        self.f_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.f_entry.place(x=250, y=30, width=100, height=25)

        self.a_label = Label(self.perdit_canvas, text="Do you have anorexia:", font=("Arial", 15))
        self.a_label.place(x=30, y=100, width=190, height=25)

        self.a_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.a_entry.place(x=250, y=100, width=120, height=25)

        self.sp_label = Label(self.perdit_canvas, text="Is your spleen palpable:", font=("Arial", 15))
        self.sp_label.place(x=30, y=170, width=210, height=25)

        self.sp_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.sp_entry.place(x=300, y=170, width=120, height=25)

        self.as_label = Label(self.perdit_canvas, text="Do you have ascites:", font=("Arial", 15))
        self.as_label.place(x=30, y=240, width=180, height=25)

        self.as_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.as_entry.place(x=300, y=240, width=120, height=25)

        self.va_label = Label(self.perdit_canvas, text="Do you have varices:", font=("Arial", 15))
        self.va_label.place(x=30, y=310, width=180, height=25)

        self.va_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.va_entry.place(x=300, y=310, width=120, height=25)

        self.b_label = Label(self.perdit_canvas, text="Do you have bilirubin:", font=("Arial", 15))
        self.b_label.place(x=30, y=380, width=180, height=25)

        self.b_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.b_entry.place(x=300, y=380, width=120, height=25)

        self.ap_label = Label(self.perdit_canvas, text="alk_phosphate:", font=("Arial", 15))
        self.ap_label.place(x=530, y=30, width=180, height=25)

        self.ap_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.ap_entry.place(x=800, y=30, width=120, height=25)

        self.sg_label = Label(self.perdit_canvas, text="sgot:", font=("Arial", 15))
        self.sg_label.place(x=530, y=100, width=100, height=25)

        self.sg_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.sg_entry.place(x=800, y=100, width=120, height=25)

        self.alb_label = Label(self.perdit_canvas, text="albumin:", font=("Arial", 15))
        self.alb_label.place(x=530, y=170, width=100, height=25)

        self.alb_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.alb_entry.place(x=800, y=170, width=120, height=25)

        self.p_label = Label(self.perdit_canvas, text="protime:", font=("Arial", 15))
        self.p_label.place(x=530, y=250, width=100, height=25)

        self.p_entry = Entry(self.perdit_canvas, font=("Arial", 15))
        self.p_entry.place(x=800, y=250, width=120, height=25)

    def dist_hep(self):

        self.f_label.destroy()
        self.f_entry.destroy()

        self.a_entry.destroy()
        self.a_label.destroy()

        self.sp_label.destroy()
        self.sp_entry.destroy()

        self.as_entry.destroy()
        self.as_label.destroy()

        self.ap_label.destroy()
        self.ap_entry.destroy()

        self.sg_entry.destroy()
        self.sg_label.destroy()

        self.alb_label.destroy()
        self.alb_entry.destroy()

        self.p_entry.destroy()
        self.p_label.destroy()

        self.va_label.destroy()
        self.va_entry.destroy()

        self.b_entry.destroy()
        self.b_label.destroy()

if __name__ == "__main__":
    root = Tk()
    loading = Frame(root,width=1800,height = 1000,bg="black")
    main_program = Frame(root,width=1800,height = 1000,bg="white")
    loading_frame = LoadingScreen(main_program,loading)
    loading.pack()
    root.mainloop()