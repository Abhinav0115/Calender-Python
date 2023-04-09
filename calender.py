from tkinter import *

import calendar


def showCal():
    new_gui = Tk()

    new_gui.config(background="white")

    new_gui.title("CALENDAR")

    new_gui.geometry("550x600")

    fetch_year = int(year_field.get())

    cal_content = calendar.calendar(fetch_year)

    cal_year = Label(new_gui, text=cal_content, font=("Consolas", 10, "bold"))

    cal_year.grid(row=5, column=1, padx=20)

    new_gui.mainloop()


# Driver Code
if __name__ == "__main__":
    gui = Tk()

    gui.config(
        background="white",
        padx=15,
    )

    gui.title("CALENDAR")

    gui.geometry("250x250")

    cal = Label(gui, text="CALENDAR", bg="dark gray", font=("times", 28, "bold"))

    year = Label(gui, text="Enter Year", bg="light green")
    blank = Label(gui, text="", bg="white", pady=0)
    blank2 = Label(gui, text="", bg="white")

    year_field = Entry(gui)

    Show = Button(
        gui,
        text="Show Calendar",
        fg="Black",
        bg="yellow",
        font=("times", 10, "bold"),
        command=showCal,
    )

    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

    cal.grid(row=1, column=1)

    blank.grid(row=2, column=1)
    year.grid(row=3, column=1)

    year_field.grid(row=4, column=1)

    blank2.grid(row=5, column=1)
    Show.grid(row=6, column=1)

    Exit.grid(row=7, column=1)

    gui.mainloop()
