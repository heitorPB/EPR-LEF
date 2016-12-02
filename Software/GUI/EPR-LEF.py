# encoding: utf-8
# Emilio e Heitor

from Tkinter import *
from tkFileDialog import askopenfilename, asksaveasfilename
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.ticker as mtick
import serial
import serial.tools.list_ports
import time
import numpy as np
import struct
import random

global count_max
count_max = 500000

global stop_flag
stop_flag = False

# tempo entre aquisições (em milisegundos)
global delay
delay = 5

global number_of_points
number_of_points = 1

global mean
mean = 1

global x_axis
x_axis = []

global y_axis
y_axis = []

global b_axis
b_axis = []


# descobre qual a porta que o arduino esta conectado
def get_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "Arduino" in p[1] or "tty" in p[1]:
            print("Arduino in", p[0])
            return p[0]
        else:
            return "/dev/ttyUSB0"


def write_display(data, display, decimal):
    format_string = "%." + decimal + "f"
    display.config(state="normal")
    display.delete(1.0, END)
    display.insert(END, format_string % data)
    display.config(state="disabled")


"""def clear_displays():
    display_volts.config(state="normal")
    display_volts.delete(1.0, END)
    display_volts.config(state="disabled")
    display_bits.config(state="normal")
    display_bits.delete(1.0, END)
    display_bits.config(state="disabled")"""


def clear_entries():
    entry_points.delete(0, END)
    entry_mean.delete(0, END)

def read_data():
    global count_max
    sem_dados = True
    count = 0
    x = 0.
    y = 0.
    b = 0.
    connection.write("B")
    #print("B")

    ehlo1   = connection.read(1)
    datalen = connection.read(1)
    data    = connection.read(int(datalen))
    ehlo2   = connection.read(1)
    #print(ehlo1, datalen, data, ehlo2)

    if ehlo1 == b'x' and ehlo2 == b'X':
        dados_x = float(data)
    else:
        dados_x = None

    ehlo1   = connection.read(1)
    datalen = connection.read(2)
    data    = connection.read(int(datalen))
    ehlo2   = connection.read(1)

    #print(ehlo1, datalen, data, ehlo2)
    if ehlo1 == b'y' and ehlo2 == b'Y':
        dados_y = float(data)
    else:
        dados_y = None

    ehlo1   = connection.read(1)
    datalen = connection.read(1)
    data    = connection.read(int(datalen))
    ehlo2   = connection.read(1)
    #print(ehlo1, datalen, data, ehlo2)

    if ehlo1 == b'b' and ehlo2 == b'B':
        dados_b = float(data)
    else:
        dados_b = None

    #print dados_x, dados_y
    #print type(dados_x), type(dados_y)
    return dados_x, dados_y, dados_b


# TODO fazer a porra do texto pro eixo x
def plot_received_data(collected_points):

    if collected_points == 0:
        from_AD_x, from_AD_y, from_AD_b = read_data()
        while True:
            aux, aux2, aux3 = read_data()
            if abs(from_AD_x - aux) > 0.0002:
                break

    global stop_flag

    if not stop_flag:
        from_AD_x, from_AD_y, from_AD_b = read_data()
        while from_AD_x == None or from_AD_y == None:
            from_AD_x, from_AD_y, from_AD_b = read_data()

        #write_display(from_AD_y, display_bits, "0")
        #write_display(5.0 * from_AD_y / 1023.0, display_volts, "2")

        global x_axis, y_axis, b_axis
        try:
            if abs(from_AD_x * 10000. - x_axis[len(x_axis) - 1]) < 100.:
                x_axis.append(from_AD_x * 10000.)
                y_axis.append(from_AD_y)
                b_axis.append(from_AD_b)
                try:
                    graph.lines[0].remove()
                except IndexError:
                    pass

                graph.plot(x_axis, y_axis, color="red",
                    linestyle="solid", linewidth="2.5")
            else:
                stop_flag = True
		# graph.plot (x_axis, y_axis, "r-", lw="2.5")
		# graph.plot (y_axis, "r-", lw="2.5")
		# line, = graph.plot (x_axis, y_axis, color="red", linestyle="solid", linewidth="2.5")
		# escala automatica para o eixo y
            #graph.set_ylim(min(y_axis) * .9, max(y_axis) * 1.1)
            graph.set_xlim(min(x_axis) * .99, max(x_axis) * 1.01)
            canvas.draw()

        except IndexError:
            if collected_points == 0:
                x_axis.append(from_AD_x * 10000)
                y_axis.append(from_AD_y)
                b_axis.append(from_AD_b)
            else:
                pass

        global delay
        window.after(delay, plot_received_data, collected_points + 1)

    else:
        bt_on.config(state="normal")
        bt_off.config(state="disabled")
        print len(x_axis), len(b_axis)
        (b, b0), cov = np.polyfit(x_axis, b_axis, 1, cov = True)
        #print b, b0
        B_axis = []
        for x_iten in x_axis:
            B_axis.append(10000. * ((x_iten * b) + b0))
        #print B_axis
        graph.lines[0].remove()
        canvas.draw()
        graph.plot(B_axis, y_axis, color="red", linestyle="solid", linewidth="2.5")
        graph.set_xlim(min(B_axis) * .99, max(B_axis) * 1.01)
        canvas.draw()

        print "Fim da coleta"


def start_reading():
    global mean

    #number_of_points = int(entry_points.get())
    graph.set_xlim(0, number_of_points)
    canvas.draw()

    #mean = entry_mean.get()
    tp = tempo.get()
    cp = campo.get()
    #print type(tp), tp
    #print type(cp), cp
    
    connection.write("T")
    connection.write(str(tp))
    time.sleep(0.1)
    echo1_tp = connection.read(1)
    echo2_tp = connection.read(len(str(tp)))
    echo3_tp = connection.read(1)
    if echo1_tp == b't' and echo3_tp == b'T':
        print str(echo2_tp)
        
    #time.sleep(0.01)
    
    connection.write("D")
    connection.write(str(cp))
    time.sleep(0.1)
    echo1_cp = connection.read(1)
    echo2_cp = connection.read(len(str(cp)))
    echo3_cp = connection.read(1)
    if echo1_cp == b'd' and echo3_cp == b'D':
        print str(echo2_cp)
    #time.sleep(0.01)
    
    
    #time.sleep(0.01)
    
    mean = '5'
    #print mean
    connection.write("A")
    time.sleep(0.01)
    connection.write(mean)
    time.sleep(0.1)

    try:
        graph.lines[0].remove()
    except IndexError:
        pass

    global x_axis, y_axis
    x_axis = []
    y_axis = []
    b_axis = []

    global stop_flag
    stop_flag = False

    bt_on.config(state="disabled")
    bt_off.config(state="normal")
    connection.write("I")
    plot_received_data(0)

def stop_reading():
    global stop_flag
    stop_flag = True
    connection.write("P");


def plot_file():
    global number_of_points, mean

    cores = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'g'] #no more white
    # recebe o nome do arquivo a ser lido
    file_name = askopenfilename()
    # Le o arquivo em uma linha e retorna uma matriz com os dados
    data = np.loadtxt(file_name)

    # limpa a área gráfica (opcional)
    #try:
    #    graph.lines[0].remove()
    #except IndexError:
    #    pass
    # separa a matriz de dados em vetores para X e Y
    x_axis = data[:, 0]
    y_axis = data[:, 1]
    # grafica
    graph.plot(x_axis, y_axis, "k-", lw="1.5", color = cores[random.randint(0, len(cores)-1)])
    graph.autoscale()
    # desenha
    canvas.draw()


def write_data():
    global mean
    global x_axis, y_axis

    # recebe o nome do arquivo a ser salvo
    file_name = asksaveasfilename()
    print file_name + "!!!!!"
    header = "Arquivo: " + file_name + "\n"
    header = header + "Numero de pontos: " + str(len(x_axis)) + "\n"
    header = header + "Numero de medias: " + str(mean)

    print header
    # salva os dados
    np.savetxt(file_name, np.transpose(
        [x_axis, y_axis]), delimiter='\t', header=header, comments='# ')


def clear_plot():
    global x_axis, y_axis
    x_axis = []
    y_axis = []
    # remove o gráfico feito
    graph.lines[0].remove()
    # reseta os limites do gráfico
    graph.set_xlim(0, 1)
    graph.set_ylim(0, 1050)
    # redesenha
    canvas.draw()


def on_closing():
    print("Adios")
    # manda o comando C pro arduino resetar
    connection.write("C")
    connection.close()
    window.destroy()


# checa se os campos de numero e medias estao preenchidos
def field_check(*args):
    #str1 = stringvar1.get()
    #str2 = stringvar2.get()
    if str2:
        bt_on.config(state='normal')
    else:
        bt_on.config(state='disabled')


connection = serial.Serial(get_arduino_port(), 115200, timeout = 2)
time.sleep(1)
print("Foi")

window = Tk()
window.minsize(width=900,height=600)
window.title("EPR - LEF - FisComp")
window.state("normal")

#### TÍTULO ####
title_area = Frame(window)
title_area.pack(side="top", fill="y")

#### GRÁFICO ####
graph_area = Frame(window)
graph_area.pack(side="top", fill="both", expand=True)

#### INTERAÇÃO COM USUÁRIO ####
user_area = Frame(window)
user_area.pack(side="bottom", fill="x")

# TÍTULO
title = Label(title_area, text="EPR - LEF",
              font="arial 14 bold")
title.pack(side="top", fill="x", expand=True)


# GRÁFICO

fig = Figure()

canvas = FigureCanvasTkAgg(fig, graph_area)
canvas.draw()
canvas.get_tk_widget().pack(side="bottom", fill="both", expand=True)

graph = fig.add_subplot(1, 1, 1)
graph.grid()
graph.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
graph.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
graph.set_ylabel("Sinal (Volts)", size=18)
graph.set_xlabel("B (Gauss)", size=18)
graph.autoscale(True, "y", False)
#graph.set_ylim(-20, 20)

toolbar = NavigationToolbar2TkAgg(canvas, graph_area)
toolbar.update()
toolbar.pack(side="left")


# USUÁRIO

# Botões
# adicionamos agora mais três botões: ler de arquivo, salvar em arquivo e
# limpar gráfico

user_buttons = Frame(user_area)
user_buttons.pack(side="right", fill="y", expand=True)

# grid 2x3 (duas colunas e três linhas)
user_buttons.columnconfigure(0, weight=1)
user_buttons.columnconfigure(1, weight=1)
for i in range(0, 3):
    user_buttons.rowconfigure(i, weight=1)

bt_on = Button(user_buttons, text="Ler conversor",
               font="Arial 12 bold", width=10, command=start_reading)
bt_on.grid(row=0, column=0, pady=3)

bt_off = Button(user_buttons, text="Parar leitura", font="Arial 12 bold",
                width=10, state="disabled", command=stop_reading)
bt_off.grid(row=1, column=0, pady=3)

bt_write = Button(user_buttons, text="Salvar",
                  font="Arial 12 bold", width=10, command=write_data)
bt_write.grid(row=0, column=1, pady=3)

bt_read = Button(user_buttons, text="Ler",
                 font="Arial 12 bold", width=10, command=plot_file)
bt_read.grid(row=1, column=1, pady=3)

bt_clear = Button(user_buttons, text="Limpar",
                  font="Arial 12 bold", width=10, command=clear_plot)
bt_clear.grid(row=2, column=1, pady=3)


# Displays
#user_displays = Frame(user_area)
#user_displays.pack(side="right", fill="y", expand=True)

#for i in range(0, 2):
#    user_displays.rowconfigure(i, weight=1)
#    user_displays.columnconfigure(i, weight=1)

#label_volts = Label(user_displays, text="Tensão (0 - 5V):", font="arial 12")
#label_volts.grid(row=0, column=0)
#display_volts = Text(user_displays, font="arial 12 bold",
 #                    width=8, height=1, state="disabled")
#display_volts.grid(row=0, column=1)

#label_bits = Label(
#    user_displays, text="Tensão (0 -1023 bits):", font="arial 12")
#label_bits.grid(row=1, column=0)
#display_bits = Text(user_displays, font="arial 12 bold",
#                    width=8, height=1, state="disabled")
#display_bits.grid(row=1, column=1)

#Radio buttons, para tempo e escale de varredura
radio_buttons = Frame(user_area)
radio_buttons.pack(side="left", fill="y", expand=True)

radio_buttons.columnconfigure(0, weight=1)
radio_buttons.columnconfigure(1, weight=1)

for i in range(0, 5):
    radio_buttons.rowconfigure(i, weight=1)

tempo = IntVar()
titulo_tempo = Button(radio_buttons, text="Tempo", font="Arial 12 bold",width=10)
titulo_tempo.grid(row = 0, column = 0)

tempo30RB = Radiobutton(radio_buttons, text = "30 segundos", variable = tempo, value = '0')
tempo30RB.grid(row = 1, column = 0)

tempo60RB = Radiobutton(radio_buttons, text = "60 segundos", variable = tempo, value = '1')
tempo60RB.grid(row = 2, column = 0)

tempo3mRB = Radiobutton(radio_buttons, text = "3  minutos", variable = tempo, value = '2')
tempo3mRB.grid(row = 3, column = 0)

tempo5mRB = Radiobutton(radio_buttons, text = "5 minutos", variable = tempo, value = '3')
tempo5mRB.grid(row = 4, column = 0)

campo = IntVar()
titulo_campo = Button(radio_buttons, text="Campo", font="Arial 12 bold",width=10)
titulo_campo.grid(row = 0, column = 1)

campo50G = Radiobutton(radio_buttons, text = "50 Gauss", variable = campo, value = '0')
campo50G.grid(row = 1, column = 1)

campo100G = Radiobutton(radio_buttons, text = "100 Gauss", variable = campo, value = '1')
campo100G.grid(row = 2, column = 1)

campo500G = Radiobutton(radio_buttons, text = "500 Gauss", variable = campo, value = '2')
campo500G.grid(row = 3, column = 1)

campo1000G = Radiobutton(radio_buttons, text = "1000 Gauss", variable = campo, value = '3')
campo1000G.grid(row = 4, column = 1)

# Entradas
user_entries = Frame(user_area)
user_entries.pack(side="left", fill="y", expand=True)

for i in range(0, 2):
    user_entries.columnconfigure(i, weight=1)
    user_entries.rowconfigure(i, weight=1)

#label_points = Label(user_entries, text="Número de pontos:", font="arial 12")
#label_points.grid(row=0, column=0)

#stringvar1 = StringVar(user_entries)
#stringvar2 = StringVar(user_entries)
#stringvar1.trace("w", field_check)
#stringvar2.trace("w", field_check)

#entry_points = Entry(user_entries, width=8, textvariable=stringvar1)
#entry_points.insert(END, "205")
#entry_points.grid(row=0, column=1)

#label_mean = Label(user_entries, text="Tempo de varredura:", font="arial 12")
#label_mean.grid(row=0, column=0)
#entry_mean = Entry(user_entries, width=8, textvariable=stringvar2)
#entry_mean.insert(END, "5")
#entry_mean.grid(row=0, column=1)


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
