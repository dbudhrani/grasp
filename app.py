import request
from functools import partial
from tkinter import *
from tkinter import ttk

def _request(*args, **kwargs):
  _url = url.get()
  rs = request._get(url=_url)
  response_area.delete(1.0, END)
  response_area.insert(END, rs)


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

ttk.Label(mainframe, text="URL: ").grid(column=1, row=1, sticky=W)

response_area = Text(mainframe, borderwidth=3, relief="sunken")
response_area.grid(column=2, row=2, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

url_entry.focus()
root.bind('<Return>', _request)

root.mainloop()

