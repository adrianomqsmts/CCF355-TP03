from tkinter import *
import view.login as vl
import view.singin as vs
import view.album as al
import view.figura as fg
import view.offer as of
import view.anunciar as va
import view.trade as vt
import controller.client as clt


class Interface:
    def __init__(self, master=None):
        # FONT AND FRAMES
        self.font = ("Comic Sans MS", "12")
        self.frame = Frame(root, bg="#565656")
        self.frame.pack()
        self.frame2 = Frame(root, bg="#565656")
        self.frame2.pack()
        self.frame3 = Frame(root, bg="#565656")
        self.frame3.pack()
        self.frame4 = Frame(root, bg="#565656")
        self.frame4.pack()
        # MENU 1
        self.mylabel = Label(self.frame, text="Menu", font=("Comic Sans MS", 15, "bold"), pady=10, fg="white",
                             bg="#565656")
        self.login = Button(self.frame, text="Login",
                            font=self.font, pady=10,
                            width=30, command=self.menuLogin,
                            bg="#f4a259")
        self.singin = Button(self.frame, text="Criar Conta",
                             font=self.font, pady=10,
                             width=30, command=lambda: self.menuSingin(),
                             bg="#ffd166")
        self.exit = Button(self.frame, text="Sair",
                           font=self.font, pady=10,
                           width=30, command=root.quit,
                           bg="#ff5c5c")
        self.openMenu1()
        # MENU 2
        self.usernametext = Label(self.frame, text="Username",
                                  font=("Comic Sans MS", 13), pady=10,
                                  fg="#dad7cd", bg="#565656")
        self.usernameinput = Entry(self.frame, width=30, font=("Arial", "12"))
        self.passwordtext = Label(self.frame2, text="Senha",
                                  font=("Comic Sans MS", 13), pady=10,
                                  fg="#dad7cd", bg="#565656")
        self.passwordinput = Entry(self.frame2, width=30, font=("Arial", "12"))
        self.loginsubmit = Button(self.frame3, text="Login",
                                  font=self.font, pady=10,
                                  width=10, command=lambda: self.submitLogin(),
                                  bg="#f4a259")
        self.back = Button(self.frame3, text="Voltar",
                           font=self.font, pady=10,
                           width=10, command=lambda: self.openMenu1(),
                           bg="#ff5c5c")
        self.msgerro = Label(self.frame4, text="Username ou Senha Inválidos", fg="red", font=self.font, bg="#565656")
        # MENU 3
        self.mylabel = Label(self.frame, text="Menu", font=("Comic Sans MS", 15, "bold"), pady=10, fg="white",
                             bg="#565656")
        self.album = Button(self.frame, text="Ver Album",
                            font=self.font, pady=10,
                            width=30, command=self.albumview,
                            bg="#5b8e7d")
        self.buy = Button(self.frame, text="Comprar Figuras",
                          font=self.font, pady=10,
                          width=30, command=self.buyview,
                          bg="#c1ddeb")
        self.sell = Button(self.frame, text="Vender Figuras",
                           font=self.font, pady=10,
                           width=30, command=self.sellview,
                           bg="#8cb369")
        self.trade = Button(self.frame, text="Trocar Figuras",
                            font=self.font, pady=10,
                            width=30, command=self.tradeview,
                            bg="#f5be51")
        self.back2 = Button(self.frame, text="Sair",
                            font=self.font, pady=10,
                            width=30, command=lambda: self.openMenu1(),
                            bg="#ff5c5c")
        # MENU 4
        self.usernametext2 = Label(self.frame, text="Username",
                                  font=("Comic Sans MS", 13), pady=10,
                                  fg="#dad7cd", bg="#565656")
        self.usernameinput2 = Entry(self.frame, width=30, font=("Arial", "12"))
        self.passwordtext2 = Label(self.frame2, text="Senha",
                                  font=("Comic Sans MS", 13), pady=10,
                                  fg="#dad7cd", bg="#565656")
        self.passwordinput2 = Entry(self.frame2, width=30, font=("Arial", "12"))
        self.singinsubmit = Button(self.frame3, text="Cadastrar",
                                   font=self.font, pady=10,
                                   width=10, command=lambda: self.submitSingin(),
                                   bg="#f4a259")
        self.msgerro2 = Label(self.frame4, text="Username ja cadastrado.", fg="red", font=self.font, bg="#565656")
        self.msgerro3 = Label(self.frame4, text="Não deixe os campos em branco.", fg="red", font=self.font, bg="#565656")
        self.msgaccept = Label(self.frame4, text="Usuário cadastrado com sucesso.", fg="green", font=self.font, bg="#565656")

    def menuLogin(self):
        self.openMenu2()

    def menuSingin(self):
        self.openMenu4()

    def albumview(self):
        pass

    def buyview(self):
        pass

    def sellview(self):
        pass

    def tradeview(self):
        pass

    def openMenu1(self):
        self.clearMenu()
        self.mylabel.pack(pady=10)
        self.login.pack(pady=10)
        self.singin.pack(pady=10)
        self.exit.pack(pady=10)

    def openMenu2(self):
        self.clearMenu()
        self.mylabel.pack(pady=10)
        self.usernametext.pack(padx=5, side="left")
        self.usernameinput.pack(padx=5, side="right", ipady=5)
        self.passwordtext.pack(padx=20, side="left")
        self.passwordinput.pack(padx=5, side="right", ipady=5)
        self.loginsubmit.pack(pady=20, ipadx=10, side="right")
        self.back.pack(padx=50, ipadx=10, side="left")

    def openMenu3(self, response):
        self.clearMenu()
        name = response['name']
        welcome = Label(self.frame, text="Bem-vindo " + name, fg="white",
                        font=("Comic Sans MS", 15, "bold"), bg="#565656")
        welcome.pack()
        self.album.pack(pady=10)
        self.buy.pack(pady=10)
        self.sell.pack(pady=10)
        self.trade.pack(pady=10)
        self.back2.pack(pady=10)

    def openMenu4(self):
        self.clearMenu()
        self.mylabel.pack(pady=10)
        self.usernametext2.pack(padx=5, side="left")
        self.usernameinput2.pack(padx=5, side="right", ipady=5)
        self.passwordtext2.pack(padx=20, side="left")
        self.passwordinput2.pack(padx=5, side="right", ipady=5)
        self.singinsubmit.pack(pady=20, ipadx=10, side="right")
        self.back.pack(padx=50, ipadx=10, side="left")

    def submitLogin(self):
        name = self.usernameinput.get()
        password = self.passwordinput.get()
        self.processLogin(name, password)

    def submitSingin(self):
        name = self.usernameinput2.get()
        password = self.passwordinput2.get()
        self.processSingin(name, password)

    def processLogin(self, name, password):
        if self.msgerro or self.msgerro3:
            self.msgerro.pack_forget()
            self.msgerro3.pack_forget()
        if (name == '') or (password == ''):
            self.msgerro3.pack(pady=10)
        else:
            response = vl.loginview(name, password)
            if response:
                if response:
                    self.openMenu3(response)
            else:
                self.msgerro.pack(pady=10)

    def processSingin(self, name, password):
        if self.msgerro2 or self.msgerro3 or self.msgaccept:
            self.msgerro2.pack_forget()
            self.msgerro3.pack_forget()
            self.msgaccept.pack_forget()
        if (name == '') or (password == ''):
            self.msgerro3.pack(pady=10)
        else:
            response = vs.singinview(name, password)
            if response:
                self.msgaccept.pack(pady=10)
            else:
                self.msgerro2.pack(pady=10)

    def clearMenu(self):
        for widgets in self.frame.winfo_children():
            widgets.pack_forget()
        for widgets in self.frame2.winfo_children():
            widgets.pack_forget()
        for widgets in self.frame3.winfo_children():
            widgets.pack_forget()
        for widgets in self.frame4.winfo_children():
            widgets.pack_forget()


root = Tk()
root.geometry("600x500+250+100")
photo = PhotoImage(file='view/img/icon.png')
root.iconphoto(False, photo)
root.configure(bg="#565656")
root.title("One Figure")
Interface(root)
root.mainloop()
