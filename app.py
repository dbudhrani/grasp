import request
from functools import partial
from tkinter import *
from tkinter import ttk

def _request(*args, **kwargs):
  _method = rq_method.get()
  _url = url.get()
  response_area.configure(state="normal")
  rs = request.route(method= _method, url=_url)
  response_area.delete(1.0, END)
  response_area.insert(END, rs)
  response_area.configure(state="disabled")


root = Tk()
root.title("Grasp")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

url = StringVar()
url_entry = ttk.Entry(mainframe, width=70, textvariable=url)
url_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Send", command=_request).grid(column=3, row=1, sticky=W)

Label(mainframe, text="URL").grid(column=1, row=1, sticky=W)

rq_method = StringVar(root)
rq_method.set('GET')
rq_methods = ['GET', 'POST', 'PUT', 'DELETE']

rq_methods_menu = OptionMenu(mainframe, rq_method, *rq_methods)
Label(mainframe, text='Request method').grid(row=2, column=1)
rq_methods_menu.grid(row=2, column=2)

response_area = Text(mainframe, borderwidth=1, relief="sunken")
response_area.grid(column=2, row=3, sticky=(W, E))
response_area.configure(state="disabled")
response_area.bind("<1>", lambda event: response_area.focus_set())

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

url_entry.focus()
root.bind('<Return>', _request)

root.mainloop()

