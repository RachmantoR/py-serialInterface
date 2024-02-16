import tkinter as gui

colorlcd = "#81cf09"

app = gui.Tk()

img = gui.PhotoImage(file="/asset/img/lcd_screen.png")
panel = gui.PhotoImage(file="/asset/img/panel.jpg")
app.geometry("1000x1000")

app.configure(bg="lightblue")
app.resizable(width=False, height=False)

# lcd = gui.Label(app, image=img, width=img.width(), height=img.height())
# lcd.grid(row = 0, column= 0)

panel = gui.Label(app, image=panel, width=panel.width(), height=panel.height())
panel.grid(row = 0, column= 0)

app.mainloop()