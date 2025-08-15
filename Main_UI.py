from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pillow
import subprocess

class Face_Recognation_System:
    def exit_app(self):
        self.root.destroy()

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title("Face Recognation System")
        self.root.attributes('-fullscreen', True)


        # ==================== Background Image ====================
        img_bg = Image.open(r"C:\Users\Asus\OneDrive\Desktop\Acadamic\Final Project\Face Recognation\UI Image\background.jpg")
        img_bg = img_bg.resize((1530, 790), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        bg_image = Label(self.root, image=self.photoimg_bg)
        bg_image.place(x=3, y=0, width=1530, height=790)


        # ==================== Title Label ====================
        title_lbl = Label(bg_image, text="FACE RECOGNATION ATTENDENCE SYSTEM",
                          font=('times new roman', 40, "bold"), bg='white', fg='red')
        title_lbl.place(x=-130, y=0, width=1800, height=100)


        # ==================== Student Button ====================
        import subprocess

        def open_student_details():
            subprocess.Popen(["python", "Student_Details.py"])

        img_student = Image.open(r"C:\Users\Asus\OneDrive\Desktop\Acadamic\Final Project\Face Recognation\UI Image\student.png")
        img_student = img_student.resize((300, 220), Image.LANCZOS)
        self.photoimg_student = ImageTk.PhotoImage(img_student)

        btn_student_img = Button(bg_image, image=self.photoimg_student, cursor='hand2',command=open_student_details)
        btn_student_img.place(x=200, y=150, width=220, height=220)

        btn_student_text = Button(bg_image, text="Student Details", cursor='hand2',
                                  font=('times new roman', 15, "bold"), bg='darkblue', fg='white',
                                  command=open_student_details)
        btn_student_text.place(x=200, y=360, width=220, height=40)


        # ==================== Face Detector Button ====================
        img_face = Image.open(r"C:\Users\Asus\OneDrive\Desktop\Acadamic\Final Project\Face Recognation\UI Image\face_detect.png")
        img_face = img_face.resize((250, 220), Image.LANCZOS)
        self.photoimg_face = ImageTk.PhotoImage(img_face)

        btn_face_img = Button(bg_image, image=self.photoimg_face, cursor='hand2')
        btn_face_img.place(x=500, y=150, width=220, height=220)

        btn_face_text = Button(bg_image, text="Face Detector", cursor='hand2',
                               font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        btn_face_text.place(x=500, y=360, width=220, height=40)


        # ==================== Attendance Button ====================
        img_attendance = Image.open(r"C:\Users\Asus\OneDrive\Desktop\Acadamic\Final Project\Face Recognation\UI Image\attendance.png")
        img_attendance = img_attendance.resize((250, 220), Image.LANCZOS)
        self.photoimg_attendance = ImageTk.PhotoImage(img_attendance)

        btn_attendance_img = Button(bg_image, image=self.photoimg_attendance, cursor='hand2')
        btn_attendance_img.place(x=800, y=150, width=220, height=220)

        btn_attendance_text = Button(bg_image, text="Attendence", cursor='hand2',
                                     font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        btn_attendance_text.place(x=800, y=360, width=220, height=40)


        # ==================== Help Desk Button ====================
        img_help = Image.open(r"C:\Users\Asus\OneDrive\Desktop\Acadamic\Final Project\Face Recognation\UI Image\help.png")
        img_help = img_help.resize((250, 220), Image.LANCZOS)
        self.photoimg_help = ImageTk.PhotoImage(img_help)

        btn_help_img = Button(bg_image, image=self.photoimg_help, cursor='hand2')
        btn_help_img.place(x=1100, y=150, width=220, height=220)

        btn_help_text = Button(bg_image, text="Attendence", cursor='hand2',
                               font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        btn_help_text.place(x=1100, y=360, width=220, height=40)


        # ==================== Train Button ====================
        img_train = Image.open(r"C:\Users\Asus\OneDrive\Desktop\Acadamic\Final Project\Face Recognation\UI Image\train.png")
        img_train = img_train.resize((250, 220), Image.LANCZOS)
        self.photoimg_train = ImageTk.PhotoImage(img_train)

        btn_train_img = Button(bg_image, image=self.photoimg_train, cursor='hand2')
        btn_train_img.place(x=200, y=460, width=220, height=220)

        btn_train_text = Button(bg_image, text="Attendence", cursor='hand2',
                                font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        btn_train_text.place(x=200, y=670, width=220, height=40)


        # ==================== Photos Button ====================
        img_photos = Image.open(r"C:\Users\Asus\OneDrive\Desktop\Acadamic\Final Project\Face Recognation\UI Image\photos.png")
        img_photos = img_photos.resize((250, 220), Image.LANCZOS)
        self.photoimg_photos = ImageTk.PhotoImage(img_photos)

        btn_photos_img = Button(bg_image, image=self.photoimg_photos, cursor='hand2')
        btn_photos_img.place(x=500, y=460, width=220, height=220)

        btn_photos_text = Button(bg_image, text="Attendence", cursor='hand2',
                                 font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        btn_photos_text.place(x=500, y=670, width=220, height=40)
        

        # ==================== Developer Button ====================
        img_dev = Image.open(r"C:\Users\Asus\OneDrive\Desktop\Acadamic\Final Project\Face Recognation\UI Image\developer.png")
        img_dev = img_dev.resize((250, 220), Image.LANCZOS)
        self.photoimg_dev = ImageTk.PhotoImage(img_dev)

        btn_dev_img = Button(bg_image, image=self.photoimg_dev, cursor='hand2')
        btn_dev_img.place(x=800, y=460, width=220, height=220)

        btn_dev_text = Button(bg_image, text="Developer", cursor='hand2',
                              font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        btn_dev_text.place(x=800, y=670, width=220, height=40)


        # ==================== Exit Button ====================
        img_exit = Image.open(r"C:\Users\Asus\OneDrive\Desktop\Acadamic\Final Project\Face Recognation\UI Image\exit.png")
        img_exit = img_exit.resize((250, 220), Image.LANCZOS)
        self.photoimg_exit = ImageTk.PhotoImage(img_exit)

        btn_exit_img = Button(bg_image, image=self.photoimg_exit, cursor='hand2', command=self.exit_app)
        btn_exit_img.place(x=1100, y=460, width=220, height=220)

        btn_exit_text = Button(bg_image, text="Exit", cursor='hand2',
                               font=('times new roman', 15, "bold"), bg='darkblue', fg='white', command=self.exit_app)
        btn_exit_text.place(x=1100, y=670, width=220, height=40)
        
        

# ==================== Run Main Application ====================
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognation_System(root)
    root.mainloop()
