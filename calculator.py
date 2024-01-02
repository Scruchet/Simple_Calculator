import customtkinter

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.title('Calculator Made By Simon Cruchet')
app.geometry("380x600")
app.configure(bg = '#ffffff')
screen_font = ('Courrier', 55, 'bold')
screen = customtkinter.CTkLabel(app, text="0", font = screen_font)
screen.grid(row=0, column=0, sticky="E", padx=(10,25), pady=(20,30), columnspan=4)

button_size = 35
button_typeface = 'Courrier'
button_orange = '#ff9f0a'
button_grey = '#a5a5a5'
button_dark = '#333333'
button_white = '#000000'
button_black = '#ffffff'
font_button = ('Courrier', 35, 'bold')

zero = customtkinter.CTkButton(app, text="0", width=170, height=75, font = font_button, anchor='w', bg =button_dark ,fg =button_white)
one = customtkinter.CTkButton(app, text="1", width=75, height=75, font = font_button, bg =button_dark ,fg =button_white)
two = customtkinter.CTkButton(app, text="2", width=75, height=75, font = font_button, bg =button_dark ,fg =button_white)
three = customtkinter.CTkButton(app, text="3", width=75, height=75, font = font_button, bg =button_dark ,fg =button_white)
four = customtkinter.CTkButton(app, text="4", width=75, height=75, font = font_button, bg =button_dark ,fg =button_white)
five = customtkinter.CTkButton(app, text="5", width=75, height=75, font = font_button, bg =button_dark ,fg =button_white)
six = customtkinter.CTkButton(app, text="6", width=75, height=75, font = font_button, bg =button_dark ,fg =button_white)
seven = customtkinter.CTkButton(app, text="7", width=75, height=75, font = font_button, bg =button_dark ,fg =button_white)
eight = customtkinter.CTkButton(app, text="8", width=75, height=75, font = font_button, bg =button_dark ,fg =button_white)
nine = customtkinter.CTkButton(app, text="9", width=75, height=75, font = font_button, bg =button_dark ,fg =button_white)
plus = customtkinter.CTkButton(app, text="+", width=75, height=75, font = font_button, bg = button_orange ,fg = button_white)
minus = customtkinter.CTkButton(app, text="-", width=75, height=75, font = font_button, bg = button_orange ,fg = button_white)
divided = customtkinter.CTkButton(app, text="÷", width=75, height=75, font = font_button, bg = button_orange ,fg = button_white)
times = customtkinter.CTkButton(app, text="*", width=75, height=75, font = font_button, bg = button_orange ,fg = button_white)
sqrt = customtkinter.CTkButton(app, text="√", width=75, height=75, font = font_button, bg = button_grey,fg = button_black)
power = customtkinter.CTkButton(app, text="x²", width=75, height=75, font = font_button, bg = button_grey,fg = button_black)
egal = customtkinter.CTkButton(app, text="=", width=75, height=75,font = font_button, bg = button_orange ,fg = button_white)
point = customtkinter.CTkButton(app, text=".", width=75, height=75, font = font_button, bg =button_dark ,fg =button_white)
ac = customtkinter.CTkButton(app, text="AC", width=75, height=75, font = font_button, bg = button_grey,fg = button_black)

zero.grid(row = 5, column = 0, pady=(10,10),   columnspan=2)
one.grid(row = 4, column = 0, padx=(10,10), pady=(10,10))
two.grid(row = 4, column = 1, padx=(10,10), pady=(10,10))
three.grid(row =4, column = 2, padx=(10,10), pady=(10,10))
four.grid(row = 3, column = 0, padx=(10,10), pady=(10,10))
five.grid(row = 3, column = 1, padx=(10,10), pady=(10,10))
six.grid(row = 3, column = 2, padx=(10,10), pady=(10,10))
seven.grid(row = 2, column = 0, padx=(10,10), pady=(10,10))
eight.grid(row = 2, column = 1, padx=(10,10), pady=(10,10))
nine.grid(row = 2, column = 2, padx=(10,10), pady=(10,10))
egal.grid(row = 5, column = 3, padx=(10,10), pady=(10,10))
plus.grid(row = 4, column = 3, padx=(10,10), pady=(10,10))
minus.grid(row = 3, column = 3, padx=(10,10), pady=(10,10))
times.grid(row = 2, column = 3, padx=(10,10), pady=(10,10))
divided.grid(row = 1, column = 3, padx=(10,10), pady=(10,10))
sqrt.grid(row = 1, column = 2, padx=(10,10), pady=(10,10))
power.grid(row = 1, column = 1, padx=(10,10), pady=(10,10))
point.grid(row = 5, column = 2, padx =(10,10), pady=(10,10))
ac.grid(row = 1, column = 0, padx =(10,10), pady=(10,10))

app.mainloop();