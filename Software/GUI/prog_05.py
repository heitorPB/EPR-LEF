# encoding: utf-8
# Emilio e Heitor

# TODO import TKinter as tk to be compatible to python3
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

global count_max
count_max = 500000

global stop_flag
stop_flag = False

# tempo entre aquisições (em milisegundos)
global delay
delay = 10

global number_of_points
number_of_points = 1

global mean
mean = 1

global x_axis
x_axis = []

global y_axis
y_axis = []


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

# TODO ARRUMAR ESSA BOSTA DE FUNCAO IMBECIL
def read_data():
    global count_max
    sem_dados = True
    count = 0
    x = 0.
    y = 0.

    # TODO FIXME checar se datalen vai sempre ser 1 char!!!!!!!
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


    #print dados_x, dados_y
    #print type(dados_x), type(dados_y)
    return dados_x, dados_y


# TODO fazer a porra do texto pro eixo x
def plot_received_data(collected_points):
	
	if collected_points == 0:
		from_AD_x, from_AD_y = read_data()
		while True:
			aux, aux2 = read_data()
			if abs(from_AD_x - aux) > 0.0002:
				break
	
	global stop_flag, number_of_points
    
	if (not stop_flag) and (collected_points < number_of_points):
		from_AD_x, from_AD_y = read_data()
		while from_AD_x == None or from_AD_y == None:
			from_AD_x, from_AD_y = read_data()

        #write_display(from_AD_y, display_bits, "0")
        #write_display(5.0 * from_AD_y / 1023.0, display_volts, "2")

		global x_axis, y_axis
		x_axis.append(from_AD_x)
		y_axis.append(from_AD_y)
		
		try:
			graph.lines[0].remove()
		except IndexError:
			pass
			
		graph.plot(x_axis, y_axis, color="red",
				linestyle="solid", linewidth="2.5")
		# graph.plot (x_axis, y_axis, "r-", lw="2.5")
		# graph.plot (y_axis, "r-", lw="2.5")
		# line, = graph.plot (x_axis, y_axis, color="red", linestyle="solid", linewidth="2.5")
		# escala automatica para o eixo y
		graph.set_ylim(min(y_axis) * .9, max(y_axis) * 1.1)
		graph.set_xlim(min(x_axis) * .99, max(x_axis) * 1.01)
		canvas.draw()
        
		global delay
		window.after(delay, plot_received_data, collected_points + 1)
	
	else:
		bt_on.config(state="normal")
		bt_off.config(state="disabled")
		print "Fim da coleta"


def start_reading():
    global number_of_points, mean

    number_of_points = int(entry_points.get())
    graph.set_xlim(0, number_of_points)
    canvas.draw()

    mean = entry_mean.get()
    connection.write("A")
    time.sleep(0.1)
    connection.write(mean)
    time.sleep(0.1)

    try:
        graph.lines[0].remove()
    except IndexError:
        pass

    global x_axis, y_axis
    x_axis = []
    y_axis = []

    global stop_flag
    stop_flag = False

    bt_on.config(state="disabled")
    bt_off.config(state="normal")

    plot_received_data(0)


def stop_reading():
    global stop_flag
    stop_flag = True


def plot_file():
    global number_of_points, mean

    # recebe o nome do arquivo a ser lido
    file_name = askopenfilename()
    # Le o arquivo em uma linha e retorna uma matriz com os dados
    data = np.loadtxt(file_name)

    # limpa a área gráfica (opcional)
    try:
        graph.lines[0].remove()
    except IndexError:
        pass
    # separa a matriz de dados em vetores para X e Y
    x_axis = data[:, 0]
    y_axis = data[:, 1]
    # grafica
    graph.plot(x_axis, y_axis, "k-", lw="1.5")
    graph.autoscale()
    # desenha
    canvas.draw()


def write_data():
    global number_of_points, mean
    global x_axis, y_axis

    # recebe o nome do arquivo a ser salvo
    file_name = asksaveasfilename()
    print file_name + "!!!!!"
    header = "Arquivo: " + file_name + "\n"
    header = header + "Numero de pontos: " + str(number_of_points) + "\n"
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
    str1 = stringvar1.get()
    str2 = stringvar2.get()
    if str1 and str2:
        bt_on.config(state='normal')
    else:
        bt_on.config(state='disabled')


connection = serial.Serial(get_arduino_port(), 9600, timeout = 2)
time.sleep(1)
print("Foi")

window = Tk()
window.minsize(width=900,height=800)
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
graph.set_xlabel("$\Delta V \approx \Delta B$", size=18)
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


# Entradas
user_entries = Frame(user_area)
user_entries.pack(side="left", fill="y", expand=True)

for i in range(0, 2):
    user_entries.columnconfigure(i, weight=1)
    user_entries.rowconfigure(i, weight=1)

label_points = Label(user_entries, text="Número de pontos:", font="arial 12")
label_points.grid(row=0, column=0)

stringvar1 = StringVar(user_entries)
stringvar2 = StringVar(user_entries)
stringvar1.trace("w", field_check)
stringvar2.trace("w", field_check)

entry_points = Entry(user_entries, width=8, textvariable=stringvar1)
entry_points.insert(END, "205")
entry_points.grid(row=0, column=1)

label_mean = Label(user_entries, text="Número de médias:", font="arial 12")
label_mean.grid(row=1, column=0)
entry_mean = Entry(user_entries, width=8, textvariable=stringvar2)
entry_mean.insert(END, "5")
entry_mean.grid(row=1, column=1)


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
