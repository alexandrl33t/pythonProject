from tkinter import *
from threading import Thread
import prime_generator
import encryptor

global window
global window2


class Window(Tk):
    p = None
    q = None
    d_sender = None
    e_sender = None
    n_sender = None
    d_receiver = None
    e_receiver = None
    n_receiver = None

    def __init__(self, title=""):
        super().__init__()
        self.title(title)
        self.geometry('1200x800')
        self.label1 = Label(self, text="Простые числа", font=("Arial bold", 14), width=80, anchor="w")
        self.label1.grid(row=0, column=0, ipady=10)
        self.label2 = Label(self, text="P: ", font=("Arial", 13), justify=LEFT, width=80, anchor="w")
        self.label2.grid(row=1, column=0)
        self.label3 = Label(self, text="Q: ", font=("Arial", 13), justify=LEFT, width=80, anchor="w")
        self.label3.grid(row=2, column=0)
        self.label4 = Label(self, text="Для подписи", font=("Arial bold", 14), justify=LEFT, width=80, anchor="w")
        self.label4.grid(row=3, column=0, ipady=10)
        self.labelOpenKeySender = Label(self, text="Открытый ключ ", font=("Arial bold", 13), justify=LEFT, width=80,
                                        anchor="w")
        self.labelOpenKeySender.grid(row=4, column=0)
        self.labelNSender = Label(self, text="N: ", font=("Arial bold", 13), justify=LEFT, width=80, anchor="w")
        self.labelNSender.grid(row=5, column=0)
        self.labelESender = Label(self, text="E: ", font=("Arial bold", 13), justify=LEFT, width=80, anchor="w")
        self.labelESender.grid(row=6, column=0)
        self.label7 = Label(self, text="Для сообщения", font=("Arial bold", 14), justify=LEFT, width=80, anchor="w")
        self.label7.grid(row=7, column=0, ipady=10)
        self.labelOpenKeyReciver = Label(self, text="Открытый ключ ", font=("Arial bold", 13), width=80, anchor="w")
        self.labelOpenKeyReciver.grid(row=8, column=0)
        self.labelNReciver = Label(self, text="N: ", font=("Arial bold", 13), justify=LEFT, width=80, anchor="w")
        self.labelNReciver.grid(row=9, column=0)
        self.labelEReciver = Label(self, text="E: ", font=("Arial bold", 13), justify=LEFT, width=80, anchor="w")
        self.labelEReciver.grid(row=10, column=0)
        self.label9 = Label(self, text="Сообщение", font=("Arial bold", 13), justify=LEFT, width=80, anchor="w")
        self.label9.grid(row=11, column=0, ipady=10)
        self.editor = Text(self)
        self.editor.insert("1.0", "")
        self.editor.grid(row=12, column=0, padx=20, pady=20)
        b1 = Button(self, text="Сгенерировать P и Q", activeforeground="blue", activebackground="pink",
                    pady=10, width=40, command=self.generate)
        b1.grid(row=0, column=1)
        b2 = Button(self, text="Проверка на простоту", activeforeground="blue", activebackground="pink",
                    pady=10, width=40, command=self.checkPrime)
        b2.grid(row=1, column=1)
        b3 = Button(self, text="Сформировать ключи", activeforeground="blue", activebackground="pink",
                    pady=10, width=40, command=self.generateKeys)
        b3.grid(row=2, column=1)
        if self.title() == "Отправитель":
            b5 = Button(self, text="Закодировать и подписаться сообщение", activeforeground="blue",
                        activebackground="pink",
                        pady=10, width=40, command=self.encrypt)
            b5.grid(row=3, column=1)
            b6 = Button(self, text="Отправить сообщение", activeforeground="blue", activebackground="pink",
                        pady=10, width=40, command=self.send_message)
            b6.grid(row=4, column=1)
        else:
            b4 = Button(self, text="Отправить ключи", activeforeground="blue", activebackground="pink",
                        pady=10, width=40, command=self.exchangeKeys)
            b4.grid(row=3, column=1)
            b7 = Button(self, text="Проверить подпись", activeforeground="blue", activebackground="pink",
                        pady=10, width=20, command=self.decrypt)
            b7.grid(row=4, column=1)

    def generate(self, n=16):
        generator = prime_generator.PrimeGenerator(n)
        self.p = generator.generate()
        self.q = generator.generate()
        self.label2['text'] = f"P: {self.p}"
        self.label3['text'] = f"Q: {self.q}"

    def checkPrime(self):
        self.editor.delete("1.0", END)
        if self.p and self.q:
            if prime_generator.PrimeGenerator.isMillerRabinPassed(
                    self.q) and prime_generator.PrimeGenerator.isMillerRabinPassed(self.p):
                self.editor.insert("1.0", "Числа простые")
            else:
                self.editor.insert("1.0", "Числа не простые")
        else:
            self.editor.insert("1.0", "Сгенерируйте пару простых чисел")

    def generateKeys(self):
        self.editor.delete("1.0", END)
        if self.p and self.q:
            if self.title() == "Отправитель":
                window.labelNReciver['text'] = "N: "
                window.labelEReciver['text'] = "E: "
                window.e_sender = encryptor.generate_key_pair(self.p, self.q)[0][0]
                window.d_sender = encryptor.generate_key_pair(self.p, self.q)[1][0]
                window.n_sender = encryptor.generate_key_pair(self.p, self.q)[0][1]
                window.labelNSender['text'] += str(self.n_sender)
                window.labelESender['text'] += str(self.e_sender)
                if self.n_receiver and self.e_receiver:
                    window.labelNReciver['text'] += str(self.n_receiver)
                    window.labelEReciver['text'] += str(self.e_receiver)
            else:
                window2.labelNReciver['text'] = "N: "
                window2.labelEReciver['text'] = "E: "
                window2.e_receiver = encryptor.generate_key_pair(self.p, self.q)[0][0]
                window2.d_receiver = encryptor.generate_key_pair(self.p, self.q)[1][0]
                window2.n_receiver = encryptor.generate_key_pair(self.p, self.q)[0][1]
                window2.labelNReciver['text'] += str(self.n_receiver)
                window2.labelEReciver['text'] += str(self.e_receiver)
        else:
            self.editor.insert("1.0", "Сгенерируйте пару простых чисел")

    def exchangeKeys(self):
        self.editor.delete("1.0", END)
        if self.title() == "Отправитель":
            if self.n_sender and self.e_sender:
                window2.n_sender = self.n_sender
                window2.e_sender = self.e_sender
                window2.labelNSender['text'] = "N: "
                window2.labelESender['text'] = "E: "
                window2.labelNSender['text'] += str(self.n_sender)
                window2.labelESender['text'] += str(self.e_sender)
        else:
            if self.n_receiver and self.e_receiver:
                window.n_receiver = self.n_receiver
                window.e_receiver = self.e_receiver
                window.labelNReciver['text'] = "N: "
                window.labelEReciver['text'] = "E: "
                window.labelNReciver['text'] += str(self.n_receiver)
                window.labelEReciver['text'] += str(self.e_receiver)

    def encrypt(self):
        if self.n_sender and self.e_sender:
            if len(self.editor.get("1.0", END)) > 1:
                encrypted_text = encryptor.encrypt((self.d_sender, window2.n_receiver), self.editor.get("1.0", END))
                self.editor.delete("1.0", END)
                self.editor.insert("1.0", encrypted_text)
            else:
                self.editor.delete("1.0", END)
                self.editor.insert("1.0", "Напишите сообщение для кодирования")
        else:
            self.editor.delete("1.0", END)
            self.editor.insert("1.0", "Сформируйте ключи")

    def send_message(self):
        if self.n_sender and self.e_sender:
            if len(self.editor.get("1.0", END)) > 1:
                text = self.editor.get("1.0", END)
                window2.editor.delete("1.0", END)
                window2.editor.insert("1.0", text)
                window2.n_sender = self.n_sender
                window2.e_sender = self.e_sender
                window2.labelNSender['text'] = f"N: {self.n_sender}"
                window2.labelESender['text'] = f"E: {self.e_sender}"
            else:
                self.editor.delete("1.0", END)
                self.editor.insert("1.0", "Напишите сообщение для кодирования")
        else:
            self.editor.delete("1.0", END)
            self.editor.insert("1.0", "Сформируйте ключи")

    def decrypt(self):
        if len(self.editor.get("1.0", END)) > 1:
            encrypted_text = self.editor.get("1.0", END)
            encrypted_text = "".join(encrypted_text.split())
            decrypted_text = encryptor.decrypt((self.d_sender, window.n_sender), encrypted_text)
            print(encrypted_text)
            self.editor.insert("1.0", decrypted_text)
        else:
            self.editor.delete("1.0", END)
            self.editor.insert("1.0", "У вас нет")


class Window2(Window):
    def __init__(self, title):
        super().__init__(title)


window = Window("Отправитель")
window2 = Window2("Получатель")

window.mainloop()
window2.mainloop()
