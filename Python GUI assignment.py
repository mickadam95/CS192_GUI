import tkinter
import tkinter.messagebox


def dspBox():
  tkinter.messagebox.showinfo('MessageBox', e1.get())

window = tkinter.Tk()

window.title('Unit 5 Submission 1')


e1 = tkinter.Entry(window, bd = 5)
btn = tkinter.Button(window, text = 'Click me', command = dspBox)


e1.pack()
btn.pack()
window.mainloop()
    
