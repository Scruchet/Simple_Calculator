import customtkinter

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.title('Calculator Made By Simon Cruchet')
app.geometry("380x600")

screen_font = ('Courrier', 55, 'bold')
screen = customtkinter.CTkLabel(app, text="0", font = screen_font)
screen.grid(row=0, column=0, sticky="E", padx=(10,25), pady=(20,30), columnspan=4)

button_size = 35
button_typeface = 'Courrier'

font_button = ('Courrier', 35, 'bold')

zero = customtkinter.CTkButton(app, text="0", width=170, height=75, font = font_button, anchor='w', bg = ,fg = )
one = customtkinter.CTkButton(app, text="1", width=75, height=75, font = font_button, bg = ,fg = )
two = customtkinter.CTkButton(app, text="2", width=75, height=75, font = font_button, bg = ,fg = )
three = customtkinter.CTkButton(app, text="3", width=75, height=75, font = font_button, bg = ,fg = )
four = customtkinter.CTkButton(app, text="4", width=75, height=75, font = font_button, bg = ,fg = )
five = customtkinter.CTkButton(app, text="5", width=75, height=75, font = font_button, bg = ,fg = )
six = customtkinter.CTkButton(app, text="6", width=75, height=75, font = font_button, bg = ,fg = )
seven = customtkinter.CTkButton(app, text="7", width=75, height=75, font = font_button, bg = ,fg = )
eight = customtkinter.CTkButton(app, text="8", width=75, height=75, font = font_button, bg = ,fg = )
nine = customtkinter.CTkButton(app, text="9", width=75, height=75, font = font_button, bg = ,fg = )
plus = customtkinter.CTkButton(app, text="+", width=75, height=75, font = font_button, bg = ,fg = )
minus = customtkinter.CTkButton(app, text="-", width=75, height=75, font = font_button, bg = ,fg = )
divided = customtkinter.CTkButton(app, text="÷", width=75, height=75, font = font_button, bg = ,fg = )
times = customtkinter.CTkButton(app, text="*", width=75, height=75, font = font_button, bg = ,fg = )
sqrt = customtkinter.CTkButton(app, text="√", width=75, height=75, font = font_button, bg = ,fg = )
power = customtkinter.CTkButton(app, text="x²", width=75, height=75, font = font_button, bg = ,fg = )
egal = customtkinter.CTkButton(app, text="=", width=75, height=75,font = font_button, bg = ,fg = )
point = customtkinter.CTkButton(app, text=",", width=75, height=75, font = font_button, bg = ,fg = )
ac = customtkinter.CTkButton(app, text="AC", width=75, height=75, font = font_button, bg = ,fg = )

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