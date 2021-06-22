import webbrowser
from tkinter import ttk
from tkinter import *






def rickity():
    site = 'youtube.com/watch?v=dQw4w9WgXcQ'
    visit = "http://{}".format(site)
    webbrowser.open(visit)


root = Tk()


root.geometry('597x369')
root.configure(background='#F0F8FF')
root.title('Rickety Browser')


Label(root, text='Rickety Browser', bg='#F0F8FF', font=('arial', 20, 'bold')).place(x=206, y=11)



URL=ttk.Entry(root, width=60)
URL.place(x=66, y=130)




Button(root, text='Search', bg='#F0F8FF', font=('arial', 15, 'bold'), command=rickity).place(x=450, y=115)









if __name__ == "__main__":
    root.mainloop()