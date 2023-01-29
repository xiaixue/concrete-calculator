import tkinter as tk
import customtkinter as ctk
import numpy as np
from tkinter import messagebox

def isfloat(num):
  try:
    float(num)
    return True
  except ValueError:
    return False

datos_iniciales = {
  "Español": ['Tamaño Máximo del Agregado Grueso','\u03b3 de la Grava Seca Compactada','\u03b3 de la Grava','Humedad de la Grava','Absorción de la Grava','Módulo de finura del Agregado Fino','\u03b3 Compactado de la Arena Seca','\u03b3 de la Arena','Humedad de la Arena','Absorción de la Arena','\u03b3 del Agua','\u03b3 del Cemento'],
  "English": ['Maximum Size of Coarse Aggregate', 'Compacted Dry Gravel S.G \u03b3', 'Gravel S.G \u03b3', 'Gravel Humidity', 'Gravel Absortion', 'Fineness Modulus', 'Compacted Dry Sand S.G \u03b3', 'Sand S.G \u03b3 ', 'Sand Humidity', 'Sand Absortion', 'Water S.G \u03b3', 'Cement \u03b3',],
  "中文": ["砾石的最大尺寸", "压实的干砾石的比重量 \u03b3", "砾石的比重量 \u03b3", "砾石的湿度", "砾石的吸收", "细度模数", "压实的干沙的比重量 \u03b3", "沙的比重量 \u03b3 ", "沙的湿度", "沙的吸收", "水的比重量 \u03b3", "水泥 \u03b3",]}
more = {
    "Español": ["¿Con aire?", "Sí ", "No", "Cemento", "Agua", "Arena", "Grava", "Volumen", "No números negativos"],
    "English": ["With air?", "Yes ", "No", "Cement", "Water", "Sand", "Gravel", "Volume", "Not negative numbers"],
    "中文": ["有空气吗", "是的", "没有", "水泥", "水", "沙", "砾石", "体积", "不要写负数"]}
titles = {
  "English": ["Concrete Calculator - Home", "Concrete Calculator - Initial Data", "Concrete Calculator - Slump", "Concrete Calculator - Results", "Continue"],
  "Español": ["Calculadora de Concreto - Inicio", "Calculadora de Concreto - Datos Iniciales", "Calculadora de Concreto - Revenimiento", "Calculadora de Concreto - Resultados", "Continuar"],
  "中文": ["混凝土的计算器 - Home", "混凝土的计算器 - 初始数据", "混凝土的计算器 - 混凝土的Slump", "混凝土的计算器 - 结果", "下去"]}

datos_iniciales_def = [25.4, 1600, 1500, 3, 0.7, 2, 2100, 1800, 5.5, 1.6, 1000, 1600]
datos_iniciales_uni = ["mm", "kg/m3", "kg/m3", "%", "%", "Mf", "kg/m3", "kg/m3", "%", "%", "kg/m3", "kg/m3"]

revenimiento_datos = { 
  "Español": [("Muros de Cimentación", [8,2], [250, 500]),("Zapatas Reforzadas", [8,2], [200, 300]),("Vigas Reforzadas", [10,2], [150, 250]),("Muros Reforzados", [10,2], [200, 300]),("Columnas para edificios", [10,2], [200, 300]),("Pavimentos y Losas", [8,2], [150, 200]),("Concreto Masivo", [5,2], [200, 500]),],
  "English": [("Foundation Walls", [8,2], [250, 500]),("Reinforced Footing", [8,2], [200, 300]),("Reinforced Beam", [10,2], [150, 250]),("Reinforced Walls", [10,2], [200, 300]),("Columns", [10,2], [200, 300]),("Decks", [8,2], [150, 200]),("Massive Concrete", [5,2], [200, 500]),],
  "中文": [("地基的墙", [8,2], [250, 500]),("基础", [8,2], [200, 300]),("梁", [10,2], [150, 250]),("水泥墙", [10,2], [200, 300]),("柱", [10,2], [200, 300]),("甲板", [8,2], [150, 200]),("水泥的批", [5,2], [200, 500]),],
    }

tma_li = [10, 12.5, 20, 25, 40, 50, 100, 150]
contenido_agua_datos = {
  "Sin Aire":{
    3:[205, 200 ,185 ,180 ,160 ,155 ,145, 125],
    5:[205, 200 ,185 ,180 ,160 ,155 ,145, 125],
    8:[225 ,215 ,200, 195 ,175 ,170 ,160 ,140],
    10:[225 ,215 ,200, 195 ,175 ,170 ,160 ,140],
    15:[240, 230, 210, 205, 185, 180, 170, 170],
    18:[240, 230, 210, 205, 185, 180, 170, 170],     },
  "Con Aire":{
    3:[180, 175, 165, 160, 145, 140, 135, 120],
    5:[180, 175, 165, 160, 145, 140, 135, 120],
    8:[200, 190, 180, 175, 160, 155, 150, 135],
    10:[200, 190, 180, 175, 160, 155, 150, 135],
    15:[215, 205, 190, 185, 170, 165, 160, 160],
    18:[215, 205, 190, 185, 170, 165, 160, 160],     }}

res_ref = [175, 210, 245, 280, 315]

water_cement_ratio = {
  0: [0.67, 0.58, 0.51, 0.44, 0.38],
  1: [0.54, 0.46, 0.4, 0.35, 0.3]}

tma_sixth = [10, 12.5, 20, 25, 40, 50]

volume_MAS = {
  2.4: [0.5, 0.59, 0.66, 0.71, 0.76, 0.78],
  2.6: [0.48, 0.57, 0.64, 0.69, 0.74, 0.76],
  2.8: [0.46, 0.55, 0.62, 0.67, 0.72, 0.74],
  3.0: [0.44, 0.53, 0.6, 0.65, 0.7, 0.72]}

class Home():
  def __init__(self, root):
    self.master = root
    self.frame = tk.Frame(self.master, bg = "#F1F1F3")
    self.frame.place(relheight= 1, relwidth= 1, relx= 0, rely= 0)
    self.master.title("Calculador de Concreto - Inicio")
    
    self.word_zh = '混凝土的计算器'
    self.word_en = 'Concrete Calculator'
    self.word_es = 'Calculadora de Concreto'

    self.language = tk.StringVar(); self.language.set("Español")
    self.title_label = ctk.CTkLabel(self.frame, font= ("Consolas", 30), text= "Calculadora de Concreto")
    self.button = ctk.CTkSegmentedButton(master= self.frame, font= ("Consolas", 18), values=["中文", "Español", "English"], command= self.animate_text, variable= self.language)
    self.continuer = ctk.CTkButton(self.frame, font= ("Consolas", 18), text= "Continuar", command= self.go_to)

    self.button.place(relx= 0.3, rely= 0.5, relheight= 0.2, relwidth= 0.4)
    self.continuer.place(relx= 0.39, rely= 0.8, relheight= 0.07, relwidth= 0.2)
    self.title_label.place(relx= 0.3, rely= 0.1, relheight= 0.4, relwidth= 0.4)

  def animate_text(self, e):
    if e == "中文":
      self.title_label.configure(text= self.word_zh)
      self.master.title(titles[self.language.get()][0])
      self.continuer.configure(text= titles[self.language.get()][4])
    elif e == "Español":
      self.title_label.configure(text= self.word_es)
      self.master.title(titles[self.language.get()][0])
      self.continuer.configure(text= titles[self.language.get()][4])
    else:
      self.title_label.configure(text= self.word_en)
      self.master.title(titles[self.language.get()][0])
      self.continuer.configure(text= titles[self.language.get()][4])
    
  def go_to(self):
    self.frame.destroy()
    return Datos_Requeridos(self.master, lang = self.language.get())

class Datos_Requeridos:
  def __init__(self, root, lang= None):
    self.master = root
    self.font = ("Consolas", 18)
    self.frame = tk.Frame(self.master, bg = "#F1F1F3")
    self.frame.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
    self.datos_iniciales_var = list()
    self.bg_color = "#EFF9FF"
    self.language = lang
    self.master.title(titles[self.language][1])

    for k, i in enumerate(datos_iniciales[self.language]):
      self.datos_iniciales_var.append(tk.StringVar())
      self.datos_iniciales_var[k].set(datos_iniciales_def[k])
      label = tk.Label(self.frame, font= self.font, text= i, anchor="w")
      units = tk.Label(self.frame, font= self.font, text= datos_iniciales_uni[k], anchor="w")
      entry = ctk.CTkEntry(self.frame, font= self.font, fg_color= self.bg_color, text_color= "black", textvariable= self.datos_iniciales_var[k])
      entry.place(relx= 0.42, rely= 0.1 + 0.06 * k, relwidth= 0.15, relheight= 0.04)
      label.place(relx= 0.1, rely= 0.1 + 0.06 * k, relwidth= 0.3, relheight= 0.04)
      units.place(relx= 0.6, rely= 0.1 + 0.06 * k, relwidth= 0.15, relheight= 0.04)
      entry.bind("<KeyRelease>", lambda event, k= k: self.checker(k))
    
    self.continue_button = ctk.CTkButton(self.frame, fg_color = "gray", border_color = "black", text_color = "white", text = "→", font = self.font, hover = True, command = lambda: self.continuer())
    self.continue_button.place(relx= 0.85, rely = 0.87, relwidth= 0.1, relheight= 0.05)

    self.button_back = ctk.CTkButton(self.frame, fg_color = "gray", border_color = "black", text_color = "white", text = "←", font = self.font, hover = True, command = self.go_back)
    self.button_back.place(relx= 0.02, rely= 0.02, relwidth= 0.05, relheight= 0.05)

  def checker(self, k, event= None):
    numero = self.datos_iniciales_var[k].get()
    if isfloat(numero) or numero.isdigit():
      numero = float(numero)
      if k in (3, 4, 8, 9) and not 0 <= numero <= 100: 
        self.datos_iniciales_var[k].set(datos_iniciales_def[k])
      elif k not in (3, 4, 8, 9) and not 0 <= numero:
        self.datos_iniciales_var[k].set(datos_iniciales_def[k])
    else: self.datos_iniciales_var[k].set(datos_iniciales_def[k])
    return

  def continuer(self):
    datos_i = []
    for j, i in enumerate(self.datos_iniciales_var):
      datos_i.append(float(i.get()))
    return Revenimiento(self.master, datos_i= datos_i, lang= self.language)

  def go_back(self):
    self.frame.destroy()
    return Home(self.master)

class Revenimiento():
  def __init__(self, root, datos_i, lang= None):
    self.master = root
    self.font = ("Consolas", 18)
    self.font_entry = ("Consolas", 18)
    self.frame = tk.Frame(self.master, bg = "#F1F1F3")
    self.frame.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
    self.bg_color = "#EFF9FF"
    self.datos_iniciales = datos_i
    self.language = lang
    self.master.title(titles[self.language][2])
    
    self.revenimiento_var = list()
    self.min_rev = list()
    self.max_rev = list()
    self.type = tk.IntVar()

    id_min = tk.StringVar(); id_min.set("min")
    id_max = tk.StringVar(); id_max.set("max")
    indicador_min = ctk.CTkEntry(
      self.frame, 
      font= self.font, 
      fg_color= self.bg_color, 
      text_color= "black", 
      state="disabled", 
      textvariable= id_min, 
      corner_radius=0)
    indicador_max = ctk.CTkEntry(
      self.frame, 
      font= self.font, 
      fg_color= self.bg_color, 
      text_color= "black", 
      state="disabled", 
      textvariable= id_max, 
      corner_radius=0)
    indicador_min.place(
      relx= 0.75, rely= 0.05, 
      relwidth= 0.05, relheight= 0.04)
    indicador_max.place(
      relx= 0.79, rely= 0.05, 
      relwidth= 0.04, relheight= 0.04)

    for k, i in enumerate(revenimiento_datos[self.language]):
      self.revenimiento_var.append(tk.StringVar())
      self.min_rev.append(tk.StringVar())
      self.max_rev.append(tk.StringVar())
      self.min_rev[k].set(revenimiento_datos[self.language][k][1][1])
      self.max_rev[k].set(revenimiento_datos[self.language][k][1][0])
      self.revenimiento_var[k].set((revenimiento_datos[self.language][k][1][0])/2 + (revenimiento_datos[self.language][k][1][1])/2)
      label = ctk.CTkRadioButton(self.frame, font= self.font, text_color= "black", text= i[0], variable= self.type, value= k)

      units = ctk.CTkLabel(self.frame, font= self.font, text= "cm", anchor="w")

      entry = ctk.CTkEntry(self.frame, font= self.font_entry, fg_color= self.bg_color, text_color= "black", textvariable= self.revenimiento_var[k])
      entry.bind("<KeyRelease>", lambda wtf, option= k: self.checker(option))

      entry_sugg_min = ctk.CTkEntry(self.frame, font= self.font_entry, fg_color= self.bg_color, text_color= "black", textvariable= self.min_rev[k], state= "disabled", corner_radius= 0)
      entry_sugg_max = ctk.CTkEntry(self.frame, font= self.font_entry, fg_color= self.bg_color, text_color= "black", textvariable= self.max_rev[k], state= "disabled", corner_radius= 0)
      entry_sugg_min.place(relx= 0.75, rely= 0.1 + 0.07 * k, relwidth= 0.05, relheight= 0.05)
      entry_sugg_max.place(relx= 0.79, rely= 0.1 + 0.07 * k, relwidth= 0.04, relheight= 0.05)

      entry.place(relx= 0.42, rely= 0.1 + 0.07 * k, relwidth= 0.15, relheight= 0.05)
      label.place(relx= 0.1, rely= 0.1 + 0.07 * k, relwidth= 0.30, relheight= 0.05)
      units.place(relx= 0.6, rely= 0.1 + 0.07 * k, relwidth= 0.15, relheight= 0.05)
      entry.bind("<KeyRelease>", lambda event, k= k: self.checker(k))

    self.continue_button = ctk.CTkButton(self.frame, fg_color = "gray", border_color = "white", text_color = "white", text = "→", font = self.font, hover = True, command = lambda: self.continuer())
    self.continue_button.place(relx= 0.85, rely = 0.87, relwidth= 0.1, relheight= 0.05)

    self.f_c = tk.StringVar(); self.f_c.set(250)
    self.f_c_entry = ctk.CTkEntry(self.frame, font= self.font_entry, fg_color= self.bg_color, text_color= "black", textvariable= self.f_c)
    self.f_c_entry.place(relx= 0.11, rely= 0.85, relwidth= 0.1, relheight= 0.05)
    self.f_c_label = tk.Label(self.frame, font= ("Consolas", 18), text= "f'c=", anchor="w").place(relx= 0.05, rely= 0.85, relwidth= 0.05, relheight= 0.05)
    self.f_c_entry.bind("<KeyRelease>", self.checker_Fc)

    self.aire = tk.IntVar(); self.aire.set(0)
    self.aire_check_si = ctk.CTkRadioButton(self.frame, font= self.font_entry, text_color= "black", text= more[self.language][1], variable= self.aire, value= 1, command= self.air_function)
    self.aire_check_no = ctk.CTkRadioButton(self.frame, font= self.font_entry, text_color= "black", text= more[self.language][2], variable= self.aire, value= 0, command= self.air_function)
    self.aire_label = tk.Label(self.frame, font= ("Consolas", 16), text= more[self.language][0], anchor="w").place(relx= 0.05, rely= 0.75, relwidth= 0.1, relheight= 0.05)
    self.aire_check_no.place(relx= 0.05 + 0.2, rely= 0.75, relwidth= 0.1, relheight= 0.05)
    self.aire_check_si.place(relx= 0.17 + 0.2, rely= 0.75, relwidth= 0.1, relheight= 0.05)

    self.button_back = ctk.CTkButton(self.frame, fg_color = "gray", border_color = "black", text_color = "white", text = "←", font = self.font, hover = True, command = self.go_back)
    self.button_back.place(relx= 0.02, rely= 0.02, relwidth= 0.05, relheight= 0.05)

  def air_function(self):
    aire = self.aire.get()
    if aire == 1:
      self.porcentaje_aire = tk.StringVar(); self.porcentaje_aire.set(2)
      self.porcentaje_aire_entry = ctk.CTkEntry(self.frame, font= self.font_entry, fg_color= self.bg_color, text_color= "black", textvariable= self.porcentaje_aire)
      self.porcentaje_aire_label = tk.Label(self.frame, font= ("Consolas", 16), text= "%", anchor="w")
      self.porcentaje_aire_entry.bind("<KeyRelease>", lambda e, k=3: self.air_checker(k= k))
      self.porcentaje_aire_label.place(relx= 0.66, rely= 0.75, relwidth= 0.1, relheight= 0.05)
      self.porcentaje_aire_entry.place(relx= 0.55, rely= 0.75, relwidth= 0.1, relheight= 0.05)
    else:
      try:
        self.porcentaje_aire_entry.destroy()
        self.porcentaje_aire_label.destroy()
      except:
        pass
  
  def air_checker(self, k, event= None):
    numero = self.porcentaje_aire.get()
    if isfloat(numero) or numero.isdigit():
      numero = float(numero)
      if k in (3, 4, 8, 9) and not 0 <= numero <= 100: 
        self.porcentaje_aire.set(2)
      elif k not in (3, 4, 8, 9) and not 0 <= numero:
        self.porcentaje_aire.set(2)
    else: self.porcentaje_aire.set(2)
    return

  def checker(self, k, event= None):
    numero = self.revenimiento_var[k].get()
    if isfloat(numero) or numero.isdigit():
      numero = float(numero)
      if numero < 0: self.revenimiento_var[k].set((revenimiento_datos[self.language][k][1][0])/2 + (revenimiento_datos[self.language][k][1][1])/2)
    else:     
      self.revenimiento_var[k].set((revenimiento_datos[self.language][k][1][0])/2 + (revenimiento_datos[self.language][k][1][1])/2)
    return

  def checker_Fc(self, event):
    numero = self.f_c.get()
    if isfloat(numero):
      numero = float(numero)
      if numero < 0: self.f_c.set(250)
    else:     
      self.f_c.set(250)
    return

  def continuer(self):
    k = self.type.get()
    rev = float(self.revenimiento_var[k].get())
    fc = float(self.f_c.get())
    aire = self.aire.get()
    tma = self.datos_iniciales[0]
    if aire == 0:
      to_iter = contenido_agua_datos["Sin Aire"]
      air_con = 0
    else: 
      to_iter = contenido_agua_datos["Con Aire"]
      air_con = float(self.porcentaje_aire.get())
    for i, (j, k) in enumerate(to_iter.items()):
      if rev == float(j):
        c_a = to_iter[j]
        break
      elif 5 < rev < 8:
        down = np.array(to_iter[5])
        uppr = np.array(to_iter[8])
        delt = ( uppr - down ) * (rev - 5) / 3 
        c_a = down + delt
        break
      elif 8 <= rev <= 10:
        c_a = to_iter[8]
        break
      elif 10 < rev < 15:
        down = np.array(to_iter[10])
        uppr = np.array(to_iter[15])
        delt = ( uppr - down ) * (rev - 10) / 5 
        c_a = down + delt
        break
      elif rev <= 5:
        c_a = to_iter[3]
        break
      else:
        c_a = to_iter[18]
        break
    fit = np.polyfit(tma_li, np.log(c_a), 1)
    a = np.exp(fit[1])
    b = fit[0]
    cont_agua = a * np.exp(b * tma)
    w_c_fit = np.polyfit(np.log(res_ref), water_cement_ratio[aire], 1)
    w_c_ratio = np.log(fc) * w_c_fit[0] + w_c_fit[1]
    cement_weight = cont_agua / w_c_ratio

    mf = self.datos_iniciales[5]
    for ind, (k, kl) in enumerate(volume_MAS.items()):
      residuo = k % mf
      if mf < k and ind == 0:
        volumen = np.array(kl)
        delta_m = residuo * 0.1
        volumen = volumen + delta_m
        break
      elif mf < k:
        volumen = np.array(kl)
        delta_m = - residuo * 0.1
        volumen = volumen + delta_m
        break
    else:
      volumen = np.array(kl)
      delta_m = - (mf - 3) * 0.1
      volumen = volumen + delta_m

    volume_gravel = np.interp([tma], tma_sixth, volumen) 
    gravel_w = volume_gravel * self.datos_iniciales[1]
    gravel_v = gravel_w / self.datos_iniciales[2]
    alpha = air_con / 100
    sand_w = self.datos_iniciales[7] * (1 -  cont_agua/self.datos_iniciales[10] - cement_weight/self.datos_iniciales[11] - gravel_v / (gravel_w/gravel_v) - alpha)
    
    gravel_w_fix = gravel_w * (1 + 0.01 * (self.datos_iniciales[4] - self.datos_iniciales[3]))
    sand_w_fix = sand_w * ( 1 + 0.01 * (self.datos_iniciales[9] - self.datos_iniciales[8]))
    water_w_fix = cont_agua + gravel_w * 0.01 * (self.datos_iniciales[4] - self.datos_iniciales[3]) + sand_w * 0.01 * (self.datos_iniciales[9] - self.datos_iniciales[8])

    return Results(self.master, {"cement":cement_weight, "water": water_w_fix, "sand": sand_w_fix, "gravel": gravel_w_fix}, lang= self.language, datos_i = self.datos_iniciales)

  def go_back(self):
      self.frame.destroy()
      return Datos_Requeridos(self.master, lang= self.language)

class Results():
  def __init__(self, root, results, lang= None, datos_i= None):
    self.master = root
    self.font = ("Consolas", 18)
    self.font_entry = ("Consolas", 18)
    self.frame = tk.Frame(self.master, bg = "#F1F1F3")
    self.frame.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
    self.bg_color = "#EFF9FF"
    self.results = results
    self.language = lang
    self.datos_iniciales = datos_i
    self.master.title(titles[self.language][3])

    self.results_lis = list()
    for i, (k, j) in enumerate(self.results.items()):
      self.results_lis.append(tk.StringVar())
      self.results_lis[i].set(round(float(j),3))
      units = tk.Label(self.frame, font= self.font, bg = "#F1F1F3", text= more[self.language][3 + i], anchor="w")
      units_ = tk.Label(self.frame, font= self.font, bg = "#F1F1F3", text= "kg", anchor="w")
      entry = ctk.CTkEntry(self.frame, font= self.font_entry, fg_color= self.bg_color, text_color= "black", textvariable= self.results_lis[i], state= "disabled")

      entry.place(relx= 0.25, rely= 0.1 + 0.07 * i, relwidth= 0.15, relheight= 0.05)
      units.place(relx= 0.1, rely= 0.1 + 0.07 * i, relwidth= 0.15, relheight= 0.05)
      units_.place(relx= 0.42, rely= 0.1 + 0.07 * i, relwidth= 0.15, relheight= 0.05)
    
    self.required_vol_var = tk.StringVar(); self.required_vol_var.set(1)
    self.required_vol_var_l = tk.StringVar(); self.required_vol_var_l.set(1000)

    required_vol = ctk.CTkEntry(self.frame, font= self.font_entry, fg_color= self.bg_color, text_color= "black", textvariable= self.required_vol_var)
    required_vol_un = tk.Label(self.frame, font= self.font, bg = "#F1F1F3", text= "m3", anchor="w")
    required_vol.place(relx= 0.25, rely= 0.8, relwidth= 0.15, relheight= 0.05)
    required_vol_un.place(relx= 0.42, rely= 0.8, relwidth= 0.15, relheight= 0.05)
    required_vol.bind("<KeyRelease>", self.update)
    vol_m = tk.Label(self.frame, font= self.font, bg = "#F1F1F3", text= more[self.language][7], anchor="w")
    vol_m.place(relx= 0.1, rely= 0.8, relwidth= 0.15, relheight= 0.05)

    required_vol_un_l = tk.Label(self.frame, font= self.font, bg = "#F1F1F3", text= "l", anchor="w")
    required_vol_l = ctk.CTkEntry(self.frame, font= self.font_entry, fg_color= self.bg_color, text_color= "black", textvariable= self.required_vol_var_l)
    required_vol_l.place(relx= 0.25, rely= 0.7, relwidth= 0.15, relheight= 0.05)
    required_vol_un_l.place(relx= 0.42, rely= 0.7, relwidth= 0.15, relheight= 0.05)
    required_vol_l.bind("<KeyRelease>", self.update_l)
    vol_l = tk.Label(self.frame, font= self.font, bg = "#F1F1F3", text= more[self.language][7], anchor="w")
    vol_l.place(relx= 0.1, rely= 0.7, relwidth= 0.15, relheight= 0.05)

    self.button_back = ctk.CTkButton(self.frame, fg_color = "gray", border_color = "black", text_color = "white", text = "←", font = self.font, hover = True, command = self.go_back)
    self.button_back.place(relx= 0.02, rely= 0.02, relwidth= 0.05, relheight= 0.05)
  
  def update(self, w):
    vol = self.required_vol_var.get()
    if isfloat(vol) == True:
      vol = float(vol)
      if vol < 0:
        self.required_vol_var.set(1)
        self.required_vol_var_l.set(1000)
        for k, m in enumerate(self.results.keys()):
          self.results_lis[k].set(round(float(self.results[m]),3))
        return messagebox.showinfo("Warning", more[self.language][8]) 
      else:
        for k, m in enumerate(self.results.keys()):
          self.results_lis[k].set(round(float(self.results[m]) * vol,3) )
        self.required_vol_var_l.set(vol * 1000)
    else:
      self.required_vol_var.set(1)
      self.required_vol_var_l.set(1000)
      for k, m in enumerate(self.results.keys()):
        self.results_lis[k].set(round(float(self.results[m]),3))
    return
  
  def update_l(self, w):
    vol = self.required_vol_var_l.get()
    if isfloat(vol) == True:
      vol = float(vol)
      if vol < 0:
        self.required_vol_var_l.set(1)
        self.required_vol_var.set(1000)
        for k, m in enumerate(self.results.keys()):
          self.results_lis[k].set(round(float(self.results[m]),3))
        return messagebox.showinfo("Warning", more[self.language][8]) 
      else:
        for k, m in enumerate(self.results.keys()):
          self.results_lis[k].set(round(float(self.results[m]) * vol / 1000,3) )
        self.required_vol_var.set(vol / 1000)
    else:
      self.required_vol_var_l.set(1000)
      self.required_vol_var.set(1)
      for k, m in enumerate(self.results.keys()):
        self.results_lis[k].set(round(float(self.results[m]),3))
    return

  def go_back(self):
      self.frame.destroy()
      return Revenimiento(self.master, datos_i = self.datos_iniciales, lang= self.language)
        
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.minsize(width=600/2, height= 400/2)
root.geometry("1000x600")
a = Home(root)

root.mainloop()