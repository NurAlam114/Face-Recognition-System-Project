from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pillow



class Student_Details:
    def exit_app(self):
        self.root.destroy()

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title("Face Recognation System")
        #self.root.attributes('-fullscreen', True)

        # ==================== Background Image ====================
        img_bg = Image.open(r"C:\Users\Asus\OneDrive\Desktop\Acadamic\Final Project\Face Recognation\UI Image\background.jpg")
        img_bg = img_bg.resize((1530, 790), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        bg_image = Label(self.root, image=self.photoimg_bg)
        bg_image.place(x=3, y=0, width=1530, height=790)


        # ==================== Title Label ====================
        title_lbl = Label(bg_image, text="STUDENT MANAGEMENT SYSTEM",
                          font=('times new roman', 40, "bold"), bg='white', fg='darkgreen')
        title_lbl.place(x=-130, y=0, width=1800, height=100)


        # frame
        main_frame = LabelFrame( bg_image,bd=10,relief=RIDGE,text="Stdent Details",font=('times new roman',12,'bold'))
        main_frame.place(x=255,y=185,width=1000,height=500)

        # Current course
        Current_Course_frame = LabelFrame( bg_image,bd=5,relief=RIDGE,text="Current course",font=('times new roman',12,'bold'))
        Current_Course_frame.place(x=300,y=220,width=900,height=150)


        # ---------- Department ----------
        dep_label = Label(Current_Course_frame, text="Select Department:", font=("Times New Roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=20, pady=20, sticky=W)

        dep_combo = ttk.Combobox(Current_Course_frame, font=("Times New Roman", 12), state="readonly", width=25)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical", "EEE", "BBA")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=20, pady=20, sticky=W)

        # ---------- Semester ----------
        sem_label = Label(Current_Course_frame, text="Select Semester:", font=("Times New Roman", 12, "bold"), bg="white")
        sem_label.grid(row=0, column=2, padx=20, pady=20, sticky=W)

        sem_combo = ttk.Combobox(Current_Course_frame, font=("Times New Roman", 12), state="readonly", width=20)
        sem_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        sem_combo.current(0)
        sem_combo.grid(row=0, column=3, padx=20, pady=20, sticky=W)

        # ---------- Course ----------
        course_label = Label(Current_Course_frame, text="Select Course:", font=("Times New Roman", 12, "bold"), bg="white")
        course_label.grid(row=1, column=0, padx=20, pady=10, sticky=W)

        course_combo = ttk.Combobox(Current_Course_frame, font=("Times New Roman", 12), state="readonly", width=25)
        course_combo["values"] = ("Select Course", "Python", "Data Structures", "Math", "AI", "DBMS", "Networking")
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=20, pady=10, sticky=W)

        # ---------- Year ----------
        year_label = Label(Current_Course_frame, text="Select Year:", font=("Times New Roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=2, padx=20, pady=10, sticky=W)

        year_combo = ttk.Combobox(Current_Course_frame, font=("Times New Roman", 12), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020", "2021", "2022", "2023", "2024", "2025")
        year_combo.current(0)
        year_combo.grid(row=1, column=3, padx=20, pady=10, sticky=W)






        # ==================== Run Main Application ====================
if __name__ == "__main__":
    root = Tk()
    obj = Student_Details(root)
    root.mainloop()