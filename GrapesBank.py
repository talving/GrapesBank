from tkinter import *
import tkinter.messagebox
import random
import os
import sys
import datetime
import time
import os.path




bod = Tk()

username = StringVar()
password = StringVar()
loanamount = StringVar()
sendamount = StringVar()
sendwho = StringVar()

usernameLab = Label(text="Username")
usernameLab.grid(row=1,column=0)



class loginButton:

    # ----------------------------------------------------------------------


    def __init__(self, master):

        self.root = master
        self.root.title("Grapes Bank")
        self.frame = Frame(master)
        self.frame.grid()



        self.usernameEntry = Entry(master, text=username)
        self.usernameEntry.grid(row=1,column=1)          #------------------------------USERNAME ENTRY--------------



        self.printButton = Button(master, text="Login", command = self.printMessage)
        self.printButton.grid(row=4,column=1, sticky=E)   #------------------------------LOGIN BUTTON---------------


        self.quitButton = Button(master, text="Quit", command = master.quit)
        self.quitButton.grid(row=4,column=2, sticky=W)    #------------------------------EXIT BUTTON----------------

        self.logoframe = Frame(master, width=50, height=30)
        self.banklogo = PhotoImage(file="GrapesBank.gif")
        self.banklable = Label(self.logoframe, image=self.banklogo)
        self.banklable.grid()                             #------------------------------LOGO-----------------------
        self.logoframe.grid(row=0, column=1, sticky=N)



    # ----------------------------------------------------------------------


    def printMessage(self):
        global name_txt
        name_txt = username.get() + ".txt"
        name_path = "./" + username.get() + ".txt"        #---------------------------USERNAME TXT-------------------
        PATH = name_path

        pass_txt = password.get() + ".txt"
        pass_path = "./" + password.get() + ".txt"        #---------------------------PASSWORD NOT IN USE-----------
        PATH_P = pass_path



        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            WELCOME_MSG = "LOGGING IN..."
            WELCOME_DURATION = 2000
            top = Toplevel()
            top.title('INFO')
            Message(top, text=WELCOME_MSG, padx=50, pady=50).pack()
            top.after(WELCOME_DURATION, self.openFrame)   #---------------------------POP UP WINDOW 2 SEC------------
            top.after(WELCOME_DURATION, top.destroy)


        elif os.path.isfile(PATH) == False:
            backup_txt = open(name_txt, 'w')
            backup_txt.write("0")
            backup_txt.close()
                                       #--------------------------IF NO ACCOUNT IS FOUND THE PROGRAM WILL MAKE ONE--
            WELCOME_MSG = "Account created.\n  Please log in."
            top = Toplevel()
            top.title('INFO')
            Message(top, text=WELCOME_MSG, padx=50, pady=50).pack()
            okbtn = Button(top,text="Continue", command= top.destroy)
            okbtn.pack()



        with open(name_txt, 'r+') as f:  #----------------Opens the "NAME".txt file and sets as value "balance"------
            self.balance = f.readline()
            balance = int(self.balance)


    # ----------------------------------------------------------------------

    def openFrame(self):

        self.hide()
        self.otherFrame = Toplevel()
        self.otherFrame.title("Menu")            #-------------------------------MENU WINDOW------------------------

        handler = lambda: self.onCloseOtherFrame(self.otherFrame)

        self.logoframe = Frame(self.otherFrame, width=50, height=30)
        self.banklogo = PhotoImage(file="GrapesBank.gif")
        self.banklable = Label(self.logoframe, image=self.banklogo)
        self.banklable.grid()
        self.logoframe.grid(row=0, column=1, sticky=N)


        mover1 = Frame()
        mover1.grid(row=2, column=1)
        mover2 = Frame()
        mover2.grid(row=3, column=1)
        mover3 = Frame()
        mover3.grid(row=4, column=1)


        loan_button= Button(self.otherFrame, text="Loan Money", command=self.loan)
        loan_button.grid(row=2,column=1)                  #-------------------------------LOAN MONEY BUTTON----------

        send_button= Button(self.otherFrame, text="Send Money", command=self.send)
        send_button.grid(row=3,column=1)                  #-------------------------------SEND MONEY BUTTON----------

        lable_bal = Label(self.otherFrame, text= ("You're current Balance is:", self.balance,"SEK"))
        lable_bal.grid(row=5, column=1)                   #-------------------------------BALANCE LABEL--------------

        btn = Button(self.otherFrame, text="Log Out...", command=handler)
        btn.grid(row=6,column=1)                          #-------------------------------LOG OUT BUTTON-------------


    # ----------------------------------------------------------------------

    def loan(self):

        self.hide()
        self.loanframe = Toplevel()                      #-------------------------------Loan window-------------
        self.loanframe.title("Loan")

        loanlable = Label(self.loanframe,text="How much would you like to loan today?")
        loanlable.grid(row=0, column=1)
        self.loanEntry = Entry(self.loanframe, text=loanamount)
        self.loanEntry.grid(row=1, column=1)


        loan_sure_button = Button(self.loanframe, text="Loan Money", command=self.loanenter)
        loan_sure_button.grid(row=2, column=1)
        print(self.balance,"END OF LOAN")



    # ----------------------------------------------------------------------

    def loanenter(self):                                    #-------------------------------LOAN FUNCTION-----------
        self.balance = int(self.balance)
        e = loanamount.get()

        if int(e) == 0:
            zero_MSG = "You can't loan 0SEK.\n Returning to menu..."
            zero_DURATION = 2000
            top = Toplevel()                            #-------------------------------Checks if entry=0------------
            top.title('INFO')
            Message(top, text=zero_MSG, padx=50, pady=50).pack()
            top.after(zero_DURATION, top.destroy)

        elif int(e) >= 0 and int(e) <= 433:
            self.balance += int(e)
            loan_MSG = int(e),"SEK is now added to your account"
            top = Toplevel()
            top.title('INFO')
            Message(top, text=loan_MSG, padx=50, pady=50).pack()
            okbtn = Button(top, text="Continue", command=top.destroy)
            okbtn.pack()

        elif int(e) >= 434 and int(e) <= 999:
            self.balance += int(e)
        elif int(e) >= 1000 and int(e) <= 1498:
            self.balance += int(e)
        elif int(e) >= 1499 and int(e) <= 10000:
            self.balance += int(e)
        elif int(e) >= 10000:
            self.balance += int(e)

        else:print("Invalid value...")#-------------------------------------

        self.onCloseLoanFrame(self.loanframe)
        self.closeotherframeandopen(self.otherFrame)     #--------------------Calls functions to close windows-------



    # ----------------------------------------------------------------------


    def send(self):

        self.hide()
        self.sendframe = Toplevel()                    #-------------------------------Send window-------------
        self.sendframe.title("Send")



        self.sendamountlabel = Label(self.sendframe, text="How much money would you like to send?")
        self.sendamountlabel.grid(row=0, column=1)
        self.sendEntry = Entry(self.sendframe, text=sendamount)
        self.sendEntry.grid(row=1, column=1)

        self.sendwholable = Label(self.sendframe, text="Who would you like to send the money to?")
        self.sendwholable.grid(row=2, column=1)
        self.sendWho = Entry(self.sendframe, text=sendwho)
        self.sendWho.grid(row=3, column=1)


        send_sure_button = Button(self.sendframe, text="Send Money", command=self.sendenter)
        send_sure_button.grid(row=4, column=1)



    # ----------------------------------------------------------------------



    def sendenter(self):                                    #-------------------------------SEND FUNCTION-----------
        self.balance = int(self.balance)

        if int(self.balance) == 0:
            self.erroren()
            self.onCloseSendFrame(self.sendframe)


        if int(sendamount.get()) <= int(self.balance):
            who_path = "./" + sendwho.get() + ".txt"
            PATH2 = who_path
            who_txt = sendwho.get() + ".txt"

            if os.path.isfile(PATH2) and os.access(PATH2,
                                                    #---------Checks if there is a user by that name. if not then abort.
                                                   os.R_OK):


                with open(who_txt,
                          'r+') as r:       #------Inserts the money to the account the user sent it to and removes the amount from users account
                    balance_send = r.readline()
                    balance_send = int(balance_send)

                balance_send += int(sendamount.get())
                balance_send = str(balance_send)
                who_txt_backup = open(who_txt, 'w')
                who_txt_backup.write(balance_send)
                self.balance -= int(sendamount.get())

                SEND_MSG = "SENDING..."  # --------#Checks if user has a account. ELSE make a "NAME".txt file with value 0.
                SEND_DURATION = 1000
                top = Toplevel()
                top.title('SENDING')
                Message(top, text=SEND_MSG, padx=50, pady=50).pack()  # ---------------------------POP UP WINDOW 1 SEC------------
                top.after(SEND_DURATION, top.destroy)


                self.onCloseSendFrame(self.sendframe)
                self.closeotherframeandopen(self.otherFrame)   #--------------------Calls functions to close windows-------



            else:print("ACCOUNT NOT FOUND") #-----------------------------------
        elif int(sendamount.get()) ==0:
            ERROR_MSG = "You can't send 0 SEK"
            top = Toplevel()                    #-------------Checks if user is trying to send 0 SEK, if then error---
            top.title('ERROR')
            Message(top, text=ERROR_MSG, padx=50, pady=50).pack()
            ERRbtn = Button(top, text="Continue", command=top.destroy)
            ERRbtn.pack()

        elif int(sendamount.get()) > int(self.balance):
            self.onCloseSendFrame(self.sendframe)
            self.erroren()





    # ----------------------------------------------------------------------

    def erroren(self):

        ERROR2_MSG = "ERROR"
        top = Toplevel()
        top.title('ERROR')
        Message(top, text=ERROR2_MSG, padx=50, pady=50).pack()
        ERRORbtn = Button(top, text="Continue", command=top.destroy)
        ERRORbtn.pack()

    # ----------------------------------------------------------------------



    def show(self):
        self.root.update()
        self.root.deiconify()

    # ----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
                                                     # ---------------------------LOG OUT FUNCTION------------------
        otherFrame.destroy()
        self.show()
        self.balance = str(self.balance)  ##Converts balance to string then writes the new value to backup file
        backup_txt = open(name_txt, 'w')
        backup_txt.write(self.balance)

    def closeotherframeandopen(self, otherFrame):
        otherFrame.destroy()                         # ----------------------close and reopen menu function---------
        self.openFrame()


    def onCloseSendFrame(self, sendframe):

        sendframe.destroy()                             # ---------------------------Close send FUNCTION------------



    def onCloseLoanFrame(self, loanframe):

        loanframe.destroy()                             # ---------------------------Close loan FUNCTION------------



    # ----------------------------------------------------------------------
    def hide(self):
        self.root.withdraw()



b = loginButton(bod)

bod.mainloop()
