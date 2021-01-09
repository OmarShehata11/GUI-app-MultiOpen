from tkinter import *
from tkinter import filedialog, Text
import os


if __name__ == '__main__':
    main = Tk()
    main.geometry("900x700")
    main.title("first GUI program i have made ")


def checkPass():
    if password_box.get() == "omar ahmed":
        play_apps()

    else:
        label = Label(main, text=f"the password is wrong bitch !")
        label.pack()


pass_label = Label(main, text="enter the password to open the program ")
password_box = Entry(main, width=20)
submit_button = Button(main, text="confirm", command=checkPass)

pass_label.pack()
password_box.pack()
submit_button.pack()


def play_apps():
    main.geometry("900x900")
    for widget in main.winfo_children():
        widget.destroy()

    body = Canvas(main, height=700, width=900, bg='lightblue')
    body.pack()
    main.title("GUI first app")
    apps = []  # empty list

    if os.path.isfile("save.txt"):
        with open('save.txt', "r") as g:
            tempFiles = g.read()
            tempFiles = tempFiles.split(',')
            apps = [x for x in tempFiles if x.strip()]

    def deleteApps():
        pass

    def addFiles():
        for widget in frame.winfo_children():
            widget.destroy()

        fileName = filedialog.askopenfilename(initialdir="D:", title="select the fucken file",
                                              filetypes=(("all files", "*.*"), ("exe", "*.exe")))
        apps.append(fileName)
        print(fileName)
        for app in apps:
            label = Label(frame, text=app, bg="red")
            label.pack()

    def runFiles():
        for app in apps:
            os.startfile(app)

    frame = Frame(body, bg="lightgreen")

    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    openFile = Button(main, text="open file", padx=10, pady=5, fg="white", bg="black", command=addFiles)
    runApps = Button(main, text="run the apps", padx=10, pady=7, fg="white", bg="black", command=runFiles)

    openFile.pack()
    runApps.pack()

    for app in apps:
        label = Label(frame, text=app)
        label.pack()

    with open('save.txt', 'w') as f:
        for app in apps:
            f.write(app + "\n")


main.mainloop()

# add new button for deleting the apps the user want
# by also using a delete button contain the letter "x" in front of all the apps
