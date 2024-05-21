


from tkinter import *
import random
import pyperclip



uppercase_chars = "ABCDEFGHIJKLMNOPRSTUVZ"
lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
symbol_chars = "!@#$%=:?';.\/|~,>*()<"
number_chars = "0123456789"

#okno s pomocjo tkinterja, z naslovom random pass gen.
root = Tk ()
root.geometry("400x300+100+100")



#napis generated password, ki mu lahko spreminjamo font velikost in barvo
length_pass = Label(root, text = "Password length:" )
length_pass.pack()
#vrstica za vpis dolzine kode
length_entry = Entry(root,width = 5)
length_entry.insert(1,24)
length_entry.pack()



passwordLabel = Label(root, text = "Generated password")
passwordLabel.pack()

#vrstica, kjer se izpise nakljucno generirano geslo
password_field = Entry(root, width=28, justify='center')
password_field.pack()


#checkbox za uporabo stevilk
include_numbers = BooleanVar()
numbers_checkbox = Checkbutton(root, text="Include Numbers", variable=include_numbers)
numbers_checkbox.pack()

#checkbox za uporabo simbolov
include_symbols = BooleanVar()
symbols_checkbox = Checkbutton(root, text="Include Symbols", variable=include_symbols)
symbols_checkbox.pack()


n_length = 40

def generate_password():
   chars = uppercase_chars + lowercase_chars
   length = int((length_entry.get()))
   if length > n_length:
      length = n_length
 
   if include_numbers.get():
      chars += number_chars
   if include_symbols.get():
      chars += symbol_chars
   
   
   password = ''.join(random.choice(chars)for _ in range(length))
   password_field.delete(0,END)  # pobrise polje od zacetka do konca
   password_field.insert(0, password)  # prikaze kodo v polju

generate_button = Button(root,text="Generate Password",command=generate_password)
generate_button.pack()

def copy_password():
      password = password_field.get()
      if password:
         pyperclip.copy(password)
copy_button = Button(root,text="Copy Password",command=copy_password)
copy_button.pack()

root.mainloop()



