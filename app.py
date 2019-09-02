import request
from functools import partial
from tkinter import *
from tkinter import ttk

def _request(*args, **kwargs):
  _method = rq_method.get()
  _url = url.get()
  _rq_body = rq_body.get("1.0","end-1c")
  response_area.configure(state="normal")
  rs = request.route(method= _method, url=_url, rq_body=_rq_body)
  response_area.delete(1.0, END)
  response_area.insert(END, rs)
  response_area.configure(state="disabled")

row = 0
root = Tk()
root.title("Grasp")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=row, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

row += 1
url = StringVar()
url_entry = ttk.Entry(mainframe, width=70, textvariable=url)
url_entry.grid(column=2, row=row, sticky=(W, E))

ttk.Button(mainframe, text="Send", command=_request).grid(column=3, row=row, sticky=W)

Label(mainframe, text="URL").grid(column=1, row=row, sticky=W)

rq_method = StringVar(root)
rq_method.set('GET')
rq_methods = ['GET', 'POST', 'PUT', 'DELETE']

row +=1
rq_methods_menu = OptionMenu(mainframe, rq_method, *rq_methods)
Label(mainframe, text='Request method').grid(row=row, column=1)
rq_methods_menu.grid(row=row, column=2)

row += 1
Label(mainframe, text='Request body').grid(row=row, column=1)
rq_body = Text(mainframe, width=70, height=10)
rq_body.grid(column=2, row=row, sticky=(W, E))

row += 1
Label(mainframe, text='Response').grid(row=row, column=1)
response_area = Text(mainframe, height=20, relief="sunken")
response_area.grid(column=2, row=row, sticky=(W, E))
response_area.configure(state="disabled")
response_area.bind("<1>", lambda event: response_area.focus_set())

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

url_entry.focus()
root.bind('<Return>', _request)

root.mainloop()

