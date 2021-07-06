
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import font, messagebox, ttk

import requests
from ttkthemes import ThemedStyle
from ttkwidgets.autocomplete import AutocompleteCombobox

api_key="YOUR-API-KEY"
respons = requests.get('https://v6.exchangerate-api.com/v6/YOUR-API-KEY/codes')#To fetch the currency codes
code=[]#list for currency code
name=[]#list for currency name
currency_dict={}

#Making list of currency and its code
for i in range(160):
    code.append(respons.json()['supported_codes'][i][0])
    name.append(respons.json()['supported_codes'][i][1])

#Converting above list to dictionary 
for key in name:
    for value in code:
        currency_dict[key] = value
        code.remove(value)
        break  



#GUI
#-----------------------------------------------------------------------------------------
win=tk.Tk()
win.title('Currency Exchange')
win.resizable(False,False)#resizable(x-dim,y-dim)
win.config(bg="#1a1b26")
Font_tuple = ("Geneva",'15' ,'bold')
style=ThemedStyle(win)
style.set_theme("equilux")

#label 1
ttk.Label(win,text='Enter amount',background='#1a1b26',foreground='orange',font=Font_tuple).grid(column=0)

#label 2
ttk.Label(win,text='Enter currency',background='#1a1b26',foreground='orange',font=Font_tuple).grid(column=2,row=0)

def currency_exchange():
    try:
        response= requests.get('https://v6.exchangerate-api.com/v6/'+api_key+'/pair/'+currency_dict[base_currency_name.get()] +'/'+currency_dict[target_currency_name.get()]+'/'+ base_currency.get("1.0",'end-1c'))
        target_currency.insert(tk.INSERT,response.json()['conversion_result'])
    except:
            messagebox.showerror("showerror", "Currency not supported")

def clear_text():
    base_currency.delete("1.0", "end")
    target_currency.delete("1.0", "end")
#Entry box 1
#base_var=tk.DoubleVar()
base_currency=st.ScrolledText(win,width=12,height=1,font = ("Helvetica",20))
base_currency.grid(column=0,row=1,padx=10,pady=10)
base_currency.focus()
base_currency.config(bg='#1a1b26',fg='orange')
#Entry box 2
#target_var=tk.DoubleVar()
target_currency=st.ScrolledText(win,width=12,height=1,font = ("Helvetica",20))
target_currency.grid(column=0,row=2,padx=10,pady=10)
target_currency.config(bg='#1a1b26',fg='orange')
#Drop down base
base_currency_name_var=tk.StringVar()
base_currency_values=name
base_currency_name=AutocompleteCombobox(win,width=20,textvariable=base_currency_name_var,completevalues=base_currency_values,font=Font_tuple)
base_currency_name.grid(column=2,row=1,padx=10,pady=10)
base_currency_name.current()
#Drop down target

target_currency_name_var=tk.StringVar()
target_currency_values=name
target_currency_name=AutocompleteCombobox(win,width=20,textvariable=target_currency_name_var,completevalues=target_currency_values,font=Font_tuple)
target_currency_name.grid(column=2,row=2,padx=10,pady=10)
target_currency_name.current()
#Button
action=ttk.Button(win,text='Exchange',command=currency_exchange,width=11)
action.grid(column=2,pady=10)

clear=ttk.Button(win,text='Clear',command=clear_text)
clear.grid(column=0,row=3,pady=10)
win.mainloop()
#-----------------------------------------------------------------------------------------