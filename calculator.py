from math import *
import customtkinter

error = False
op = False
nb_max_on_screen = 11
curent_nb = False
MAX_RESULT = 99999999999
stack_screen = []
button_size = 35
button_typeface = 'Courrier'
button_orange = '#ff9f0a'
button_grey = '#a5a5a5'
button_dark = '#333333'
button_white = '#ffffff'
button_black = '#000000'

def _get_nb_as_text_from_stack():
    text = ''
    for num in stack_screen:
        text += str(num)
    return text

def _get_nb_from_stack():
    text = _get_nb_as_text_from_stack()
    if '.' in stack_screen:
        return float(text)
    else:
        return int(text)


def update_screen(value=False):
    if value:
        screen.configure(text=value[0:nb_max_on_screen])
    else:
        screen.configure(text="0")


def print_result():
    fl = curent_nb - floor(curent_nb)
    if error:
        update_screen("Error")
    else:
        if fl > 0:
            update_screen(str(curent_nb))
        else:
            update_screen(str(floor(curent_nb)))

def execute_operation(operation):
    global curent_nb,error
    if operation:
        nb2= _get_nb_from_stack()
        result = 0
        if operation == 'PLUS':
            result = nb2 + curent_nb
        elif operation == 'MINUS':
            result = curent_nb - nb2
            print(result)
        elif operation == 'TIMES':
            result = nb2 * curent_nb
            print(result)
        elif operation == 'DIVIDED':
            if curent_nb == 0:
                error = True
            else:
                result = curent_nb / nb2
                print(result)
        if result > MAX_RESULT:
            error = True
        if not error:
            curent_nb = result
        stack_screen.clear()
        print_result()
                

def execute_number_key(key):
    if len(stack_screen) < nb_max_on_screen:
        if key == '.' and '.' in stack_screen:
            return
        stack_screen.append(key)
        update_screen(_get_nb_as_text_from_stack())

def execute_symbol_key(operation):
    global curent_nb, op
    if curent_nb and op:
        execute_operation(op)
        op = False
    if not curent_nb:
        curent_nb = _get_nb_from_stack()
    op = operation
    stack_screen.clear()
     
def execute_reset_key():
    stack_screen.clear()
    global curent_nb, op,error
    curent_nb = False
    op= False
    error = False
    curent_nb = 0
    update_screen()

def execute_equal_key():
    global curent_nb, op
    if curent_nb and op:
        execute_current_operation()
        op = False
        curent_nb = False

def execute_current_operation():
    global op
    if curent_nb is not False and op:
        execute_operation(op)
        op = False

def execute_pow_key(pow):
    global curent_nb
    curent_nb = _get_nb_from_stack()
    if pow == "POW":
        print(str(curent_nb))
        result = curent_nb **2
    elif pow == "SQRT":
        print(str(curent_nb))
        result = sqrt(curent_nb)
    stack_screen.clear()
    curent_nb = result
    print_result()

def pressed_key(key):
    if key in ['0','1','2','3','4','5','6','7','8','9','.']:
        execute_number_key(key)
    elif key in ['PLUS','MINUS','TIMES','DIVIDED']:
        execute_symbol_key(key)
    elif key in ['SQRT','POW']:
        execute_pow_key(key)
    elif key == "EQUAL":
        execute_equal_key()
    elif key == 'AC':
        execute_reset_key()




font_button = (button_typeface, button_size, 'bold')
customtkinter.set_appearance_mode('dark')

app = customtkinter.CTk()
app.title('Calculator Made By Simon Cruchet')
app.geometry("380x600")

screen_font = ('Courrier', 55, 'bold')
screen = customtkinter.CTkLabel(app, text="0", font = screen_font)
screen.grid(row=0, column=0, sticky="E", padx=(10,28), pady=(20,30), columnspan=4)

zero = customtkinter.CTkButton(app, text="0", width=170, height=75, font = font_button, anchor='w', fg_color =button_dark ,text_color =button_white, command= lambda : pressed_key('0'))
one = customtkinter.CTkButton(app, text="1", width=75, height=75, font = font_button, fg_color =button_dark ,text_color =button_white, command= lambda : pressed_key('1'))
two = customtkinter.CTkButton(app, text="2", width=75, height=75, font = font_button, fg_color =button_dark ,text_color =button_white, command= lambda : pressed_key('2'))
three = customtkinter.CTkButton(app, text="3", width=75, height=75, font = font_button, fg_color =button_dark ,text_color =button_white, command= lambda : pressed_key('3'))
four = customtkinter.CTkButton(app, text="4", width=75, height=75, font = font_button, fg_color =button_dark ,text_color =button_white, command= lambda : pressed_key('4'))
five = customtkinter.CTkButton(app, text="5", width=75, height=75, font = font_button, fg_color =button_dark ,text_color =button_white, command= lambda : pressed_key('5'))
six = customtkinter.CTkButton(app, text="6", width=75, height=75, font = font_button, fg_color =button_dark ,text_color =button_white, command= lambda : pressed_key('6'))
seven = customtkinter.CTkButton(app, text="7", width=75, height=75, font = font_button, fg_color =button_dark ,text_color =button_white, command= lambda : pressed_key('7'))
eight = customtkinter.CTkButton(app, text="8", width=75, height=75, font = font_button, fg_color =button_dark ,text_color =button_white, command= lambda : pressed_key('8'))
nine = customtkinter.CTkButton(app, text="9", width=75, height=75, font = font_button, fg_color =button_dark ,text_color =button_white, command= lambda : pressed_key('9'))
plus = customtkinter.CTkButton(app, text="+", width=75, height=75, font = font_button, fg_color = button_orange ,text_color = button_white, command= lambda : pressed_key('PLUS'))
minus = customtkinter.CTkButton(app, text="-", width=75, height=75, font = font_button, fg_color = button_orange ,text_color = button_white, command= lambda : pressed_key('MINUS'))
divided = customtkinter.CTkButton(app, text="÷", width=75, height=75, font = font_button, fg_color = button_orange ,text_color = button_white, command= lambda : pressed_key('DIVIDED'))
times = customtkinter.CTkButton(app, text="*", width=75, height=75, font = font_button, fg_color = button_orange ,text_color = button_white, command= lambda : pressed_key('TIMES'))
sqrt_button = customtkinter.CTkButton(app, text="√", width=75, height=75, font = font_button, fg_color = button_grey,text_color = button_black, command= lambda : pressed_key('SQRT'))
power = customtkinter.CTkButton(app, text="x²", width=75, height=75, font = font_button, fg_color = button_grey,text_color = button_black, command= lambda : pressed_key('POW'))
egal = customtkinter.CTkButton(app, text="=", width=75, height=75,font = font_button, fg_color = button_orange ,text_color = button_white, command= lambda : pressed_key('EQUAL'))
point = customtkinter.CTkButton(app, text=".", width=75, height=75, font = font_button, fg_color =button_dark ,text_color =button_white, command= lambda : pressed_key('.'))
ac = customtkinter.CTkButton(app, text="AC", width=75, height=75, font = font_button, fg_color = button_grey,text_color = button_black, command= lambda : pressed_key('AC'))

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
sqrt_button.grid(row = 1, column = 2, padx=(10,10), pady=(10,10))
power.grid(row = 1, column = 1, padx=(10,10), pady=(10,10))
point.grid(row = 5, column = 2, padx =(10,10), pady=(10,10))
ac.grid(row = 1, column = 0, padx =(10,10), pady=(10,10))

app.mainloop();