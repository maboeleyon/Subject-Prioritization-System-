import tkinter as tk
from tkinter import ttk, messagebox

class SubjectPrioritizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Subject Prioritization System")
        self.subjects = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Input Frame
        input_frame = ttk.LabelFrame(main_frame, text="Add New Subject", padding=10)
        input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        # Subject Name
        ttk.Label(input_frame, text="Subject Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Final Exam Grade
        ttk.Label(input_frame, text="Final Exam Grade:").grid(row=1, column=0, sticky="w")
        self.final_grade_entry = ttk.Entry(input_frame)
        self.final_grade_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Classwork %
        ttk.Label(input_frame, text="Classwork %:").grid(row=2, column=0, sticky="w")
        self.classwork_entry = ttk.Entry(input_frame)
        self.classwork_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Days Before Exam
        ttk.Label(input_frame, text="Days Before Exam:").grid(row=3, column=0, sticky="w")
        self.days_entry = ttk.Entry(input_frame)
        self.days_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Remaining Content %
        ttk.Label(input_frame, text="Remaining Content %:").grid(row=4, column=0, sticky="w")
        self.remaining_content_entry = ttk.Entry(input_frame)
        self.remaining_content_entry.grid(row=4, column=1, padx=5, pady=5)
        
        # Buttons
        ttk.Button(input_frame, text="Add Subject", command=self.add_subject).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(input_frame, text="Prioritize", command=self.prioritize).grid(row=6, column=0, columnspan=2, pady=5)
        ttk.Button(input_frame, text="Clear All", command=self.clear_all).grid(row=7, column=0, columnspan=2, pady=5)
        
        # Preview Frame
        preview_frame = ttk.LabelFrame(main_frame, text="Entered Subjects (Preview)", padding=10)
        preview_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        self.preview_tree = ttk.Treeview(preview_frame, columns=("Subject", "Final", "Classwork", "Days", "Remaining"), show="headings", height=8)
        
        # Configure preview headings
        self.preview_tree.heading("Subject", text="Subject")
        self.preview_tree.heading("Final", text="Final Grade")
        self.preview_tree.heading("Classwork", text="Classwork %")
        self.preview_tree.heading("Days", text="Days Left")
        self.preview_tree.heading("Remaining", text="Remaining %")
        
        # Configure preview columns
        self.preview_tree.column("Subject", width=120)
        self.preview_tree.column("Final", width=70, anchor="center")
        self.preview_tree.column("Classwork", width=80, anchor="center")
        self.preview_tree.column("Days", width=70, anchor="center")
        self.preview_tree.column("Remaining", width=80, anchor="center")
        
        self.preview_tree.pack(expand=True, fill="both")
        
        # Results Frame
        results_frame = ttk.LabelFrame(main_frame, text="Prioritized Results", padding=10)
        results_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        
        self.results_tree = ttk.Treeview(results_frame, columns=("No.", "Subject", "Final", "Classwork", "Days", "Remaining", "Total"), show="headings")
        
        # Configure results headings
        self.results_tree.heading("No.", text="No.")
        self.results_tree.heading("Subject", text="Subject")
        self.results_tree.heading("Final", text="Final Grade")
        self.results_tree.heading("Classwork", text="Classwork %")
        self.results_tree.heading("Days", text="Days Left")
        self.results_tree.heading("Remaining", text="Remaining %")
        self.results_tree.heading("Total", text="Total Score")
        
        # Configure results columns
        self.results_tree.column("No.", width=40, anchor="center")
        self.results_tree.column("Subject", width=120)
        self.results_tree.column("Final", width=70, anchor="center")
        self.results_tree.column("Classwork", width=80, anchor="center")
        self.results_tree.column("Days", width=70, anchor="center")
        self.results_tree.column("Remaining", width=80, anchor="center")
        self.results_tree.column("Total", width=70, anchor="center")
        
        self.results_tree.pack(expand=True, fill="both")
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
    
    def calculate_weights(self, subject):
       # Final exam weight
       final_grade = int(subject['final_grade'])
       if final_grade >= 90:
           w_final = 5
       elif final_grade >= 75:
           w_final = 4
       elif final_grade >= 60:
           w_final = 3
       elif final_grade >= 50:
           w_final = 2
       elif final_grade == 0:
           w_final = 0
           messagebox.showinfo("Note", f"{subject['name']} has no final exam.")
       else:
           w_final = 1
       
       # Classwork weight
       classwork = float(subject['classwork'])
       if classwork >= 90:
           w_class = 1
       elif 85 <= classwork < 90:
           w_class = 2
       elif 75 <= classwork < 85:
           w_class = 3
       elif 70 <= classwork < 75:
           w_class = 4
       else:
           w_class = 5
       
       # Days weight
       days = int(subject['days'])
       if days <= 2:
           w_days = 5
       elif days == 3:
           w_days = 4
       elif days == 4:
           w_days = 3
       else:
           w_days = 2
       
       # Remaining content weight
       rc = int(subject['remaining_content'])
       if rc >= 50:
           w_content = 6
       elif 40 <= rc < 50:
           w_content = 5
       elif 30 <= rc < 40:
           w_content = 4
       elif 20 <= rc < 30:
           w_content = 3
       elif 10 <= rc < 20:  
           w_content = 2
       else:
           w_content = 1
       
       return w_final + w_class + w_days + w_content
    
    def add_subject(self):
        try:
            subject = {
                'name': self.name_entry.get(),
                'final_grade': self.final_grade_entry.get(),
                'classwork': self.classwork_entry.get(),
                'days': self.days_entry.get(),
                'remaining_content': self.remaining_content_entry.get()
            }
            
            if not subject['name']:
                messagebox.showerror("Error", "Subject name cannot be empty")
                return
                
            if int(subject['days']) == 0:
                messagebox.showerror("Error", "You can't prioritize a subject on the same day as the exam.")
                return
                
            self.subjects.append(subject)
            self.update_preview()
            messagebox.showinfo("Success", "Subject added successfully!")
            self.clear_entries()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields")
    
    def update_preview(self):
        # Clear previous preview
        for item in self.preview_tree.get_children():
            self.preview_tree.delete(item)
            
        # Add current subjects to preview
        for subject in self.subjects:
            self.preview_tree.insert("", "end", 
                                  values=(subject['name'],
                                          subject['final_grade'],
                                          f"{subject['classwork']}%",
                                          subject['days'],
                                          f"{subject['remaining_content']}%"))
    
    def prioritize(self):
        if not self.subjects:
            messagebox.showwarning("Warning", "No subjects to prioritize")
            return
            
        # Clear previous results
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
            
        # Calculate weights and sort
        for subject in self.subjects:
            subject['total'] = self.calculate_weights(subject)
            
        sorted_subjects = sorted(self.subjects, key=lambda x: x['total'], reverse=True)
            
        # Add sorted subjects to results treeview with numbering
        for i, subject in enumerate(sorted_subjects, 1):
            self.results_tree.insert("", "end", 
                                   values=(i,
                                           subject['name'],
                                           subject['final_grade'],
                                           f"{subject['classwork']}%",
                                           subject['days'],
                                           f"{subject['remaining_content']}%",
                                           subject['total']))
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.final_grade_entry.delete(0, tk.END)
        self.classwork_entry.delete(0, tk.END)
        self.days_entry.delete(0, tk.END)
        self.remaining_content_entry.delete(0, tk.END)
    
    def clear_all(self):
        self.clear_entries()
        self.subjects = []
        for item in self.preview_tree.get_children():
            self.preview_tree.delete(item)
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        messagebox.showinfo("Cleared", "All data has been cleared")

if __name__ == "__main__":
    root = tk.Tk()
    app = SubjectPrioritizationApp(root)
    root.mainloop()