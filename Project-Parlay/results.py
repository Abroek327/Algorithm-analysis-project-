import tkinter as tk
 
# Create our master object to the Application
master = tk.Tk()
master.geometry("1280x720")
 
# Create the text widget
text_widget = tk.Text(master, height=1920, width=1080)
 
# Create a scrollbar
scroll_bar = tk.Scrollbar(master)
 
# Pack the scroll bar
# Place it to the right side, using tk.RIGHT
scroll_bar.pack(side=tk.RIGHT, fill="y", expand=False)
 
# Pack it into our tkinter application
# Place the text widget to the left side
text_widget.pack(side=tk.LEFT, fill="both", expand=True)

#Creates text variable with the output file
long_text = open("ZampleOutput_2.0.txt", 'r').read()
 
# Insert text into the text widget
text_widget.insert(tk.END, long_text)
 
# Start the mainloop
tk.mainloop()