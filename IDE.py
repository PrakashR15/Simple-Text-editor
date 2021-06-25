from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
#set variable for open file name
global open_status_name
open_status_name = False


global selected
selected = False
root = Tk()
root.title('Untitled - TextPad!')
#root.iconbitmap("E:\files")
#w = 300
#ws = root.winfo_screenwidth()
#hs = root.winfo_screenheight()

#x = (ws/2) - (w/2)
#y = (hs/2) - (h/2)
#root.geometry('%dx%d+%d+%d'%(w,h,x,y))
root.maxsize(1200,700)
#Create shorcuts for new file
def new_file_s():
        my_text.delete("1.0", END)
        root.title('Untitled - TextPad!')
        status_bar.config(text="New File         ")
        open_status_name = False

#Create new file function
def new_file(e):
        global open_status_name
        if e:
        	new_file_s()
        else:
        	new_file_s()


#Create a shorcut for open file
def opeen_file_s():
	my_text.delete("1.0", END)
		#Grab file name
	text_file = filedialog.askopenfilename(initialdir="C", title="Open File", filetypes=(("All FIles", "."),("Text Files", ".txt"),("HTML Files", ".html"), ("Python Files", "*.py")))
	if text_file:
		global open_status_name
		open_status_name = text_file
	name = text_file
	status_bar.config(text=f'{name}')
	name = name.replace("C:/Users/PRAKASH", "")
	root.title(f'{name} - TextPad!')

	#open the file
	text_file = open(text_file, 'r')
	stuff = text_file.read()
	my_text.insert(END, stuff)
	text_file.close()


#Create a open file function
def open_file(e):
	if e:
		opeen_file_s()
	else:
		opeen_file_s()
#Save file
def save_file(e):
	global open_status_name
	if e:
		if open_status_name:
			text_file = open(open_status_name, 'w')
			text_file.write(my_text.get(1.0, END))
			text_file.close()
			status_bar.config(text=f'{open_status_name}')
		else:
			save_as_file(e)
	else:
		if open_status_name:
			text_file = open(open_status_name, 'w')
			text_file.write(my_text.get(1.0, END))
			text_file.close()
			status_bar.config(text=f'{open_status_name}')
		else:
			save_as_file(e)
#Create shorcut for save as file
def save_as_file_s():
	text_file = filedialog.asksaveasfilename(defaultextension=".txt", initialdir="C:/Users/PRAKASH", title="Save File", filetypes=(("All Files", "."),("Python FIles","*.py")))
	if text_file:
		name = text_file
		name = name.replace("C:/Users/PRAKASH", "")
		root.title(f'{name} - TextPad!')

		#save the file
		text_file = open(text_file, 'w')
		text_file.write(my_text.get(1.0, END))
		text_file.close()

#Create save ass function
def save_as_file(e):
	if e:
		save_as_file_s()
	else:
		save_as_file_s()

#Cut function
def cut_text(e):
	global selected
	#check to see if we used keyboard shoorcuts
	if e:
		selected = root.clipboard_get()
	else:
		if my_text.selection_get():
			#Grab selected text
			selected = my_text.selection_get()
			#Delete selected text
			my_text.delete("sel.first", "sel.last")
			root.clipboard_clear()
			root.clipboard_append(selected)


#Copy function
def copy_text(e):
	global selected
	#check to see if we used keyboard shoorcuts
	if e:
		selected = root.clipboard_get()
	else:
		if my_text.selection_get():
			#Grab selected text
			selected = my_text.selection_get()
			root.clipboard_clear()
			root.clipboard_append(selected)

#Paste function
def paste_text(e):
	global selected
	global position
	#check to see if we used keyboard shoorcuts
	if e:
		selected = root.clipboard_get()
	#this will grab the position of the cursor
	else:
		if selected:
			selected = my_text.selection_get()
			#Delete selected text
			my_text.delete("sel.first", "sel.last")
			position = my_text.index(INSERT)
			my_text.insert(position, selected)

#Bold TEXT
def bold_it():
	bold_font = font.Font(my_text, my_text.cget("font"))
	bold_font.configure(weight="bold")

	#define current tags
	current_tags = my_text.tag_names("sel.first")
	#configure tag
	my_text.tag_configure("bold", font=bold_font)

	#if statement to see if tag is been set
	if "bold" in current_tags:
		my_text.tag_remove("bold", "sel.first", "sel.last")
	else:
		my_text.tag_add("bold",  "sel.first", "sel.last")
	#Bold TEXT
def italics_it():
	italics_font = font.Font(my_text, my_text.cget("font"))
	italics_font.configure(slant="italic")

	#define current tags
	current_tags = my_text.tag_names("sel.first")
	#configure tag
	my_text.tag_configure("italic", font=italics_font)

	#if statement to see if tag is been set
	if "italic" in current_tags:
		my_text.tag_remove("italic", "sel.first", "sel.last")
	else:
		my_text.tag_add("italic",  "sel.first", "sel.last")



#change selected text color
def text_color():
	#pick a color
	my_color = colorchooser.askcolor()[1]
	if my_color:

		color_font = font.Font(my_text, my_text.cget("font"))

		#define current tags
		current_tags = my_text.tag_names("sel.first")
		#configure tag
		my_text.tag_configure("coloured", font=color_font, foreground=my_color)

		#if statement to see if tag is been set
		if "coloured" in current_tags:
			my_text.tag_remove("coloured", "sel.first", "sel.last")
		else:
			my_text.tag_add("coloured",  "sel.first", "sel.last")

#Change Bg color
def bg_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(bg=my_color)

def all_text_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(fg=my_color)

#Close	
def quit():
	root.destroy()

#Create Tollbar Frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

#Create Main Frame
my_frame = Frame(root)
my_frame.pack()


#Create our Vertical Scrollbar for the text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#craete our hrozontol Scroll bar
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)


#Create Text Box
my_text = Text(my_frame, width=97, height=35, font=("Candara", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

#Configure our scrollbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)
#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: new_file(False))
file_menu.add_command(label="Open", command=lambda: open_file(False))
file_menu.add_command(label="Save", command=lambda: save_file(False))
file_menu.add_command(label="Save As", command=lambda: save_as_file(False))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)


#Add Edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False),  accelerator="Ctrl+C")
edit_menu.add_command(label="Paste              ", command=lambda: paste_text(False), accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="Ctrl+Y")


#BBG color mneu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected Text", command=text_color)
color_menu.add_separator()
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)


#add satusbar bottom
status_bar = Label(root, text='Ready      ',bd=1, relief=SUNKEN,  anchor=W)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)




#Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

root.bind('<Control-Key-n>', new_file)
root.bind('<Control-Key-o>', open_file)
root.bind('<Control-Key-s>', save_file)
root.bind('<Control-Key-k>', save_as_file)

#Bold Button
bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5)

#Italic Button
italic_button = Button(toolbar_frame, text="Italics", command=italics_it)
italic_button.grid(row=0, column=1, padx=5)

#UNDO/REDO buttons
#ubdo Button
undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5)

#redo Button
redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)

#textColor
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5)



root.mainloop()
