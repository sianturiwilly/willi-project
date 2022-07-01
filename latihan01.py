# Python Pertemuan ke-34
# Willi Sianturi

import PySimpleGUI as sg
import pandas as pd

# a
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

fig = matplotlib.figure.Figure(figsize=(5, 3), dpi=100)

data = {
  "pengalaman": [1, 1, 2, 2, 1],
  "gaji": [7.2, 7.1, 8.3, 7.9, 7.3],
}

df = pd.DataFrame(data)

headings = list(data)
values = df.values.tolist()

# a
# 1 baris 1 kolom
# plt.title("Pengalaman")
fig.add_subplot(111).scatter(
  df['pengalaman'], 
  df['gaji'],
  label="Gaji Karyawan"
)

# a
def gambar_plot(canvas, figure):
  figure_canvas = FigureCanvasTkAgg(figure, canvas)
  figure_canvas.draw()
  figure_canvas.get_tk_widget().pack(expand=2)
  return figure_canvas

sg.set_options(font=("Courier New", 10))
sg.theme("default")

menu_def = [['File', ['Open', 'Cek Hasil', 'Exit',]],
            ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
            ['Help', 'About...'],]

layout = [
  [sg.Menu(menu_def)],
  [sg.Text("Masukan nama:")],
  [sg.InputText(key="TXT-NAME", expand_x=True)], # a
  [sg.Text("Hasil:")],
  [sg.InputText(key="TXT-RESULT", readonly=True, expand_x=True)], # a
  [sg.Text("Tabel:")],
  [
    sg.Table(values=values, headings=headings, expand_x=True, expand_y=True), # a 
    sg.Canvas(key="CANVAS", expand_y=True)], # a
  [sg.Button('Ok', key="BTN-OK", expand_x=True), sg.Button('Cancel', expand_x=True)]
]

window = sg.Window("Program Willi", layout, finalize=True) # a
fig_canvas_agg = gambar_plot(window['CANVAS'].TKCanvas, fig) # a
txt_result = window['TXT-RESULT'] 

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
    break
  if event == 'BTN-OK':
    txt_result.update(value=values['TXT-NAME'].upper())
  elif event == 'Open':
    print("Menu open dibuka!")
  elif event == 'Cek Hasil':
    txt_result.update(value=values['TXT-NAME'].lower())

window.close()