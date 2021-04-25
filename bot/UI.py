from tkinter import *
from tkinter import ttk

root = Tk() #画面の作成

bot_flag=[False,False,False,False,False,False]

root.title('Twitter reply Bot') # タイトル
root.geometry("400x280")

root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

label1 = ttk.Label(frame1, text='Username   @', padding=(5, 2))
label1.grid(row=0, column=0, sticky=E)

label2 = ttk.Label(text='Botを選択してください')
label2.place(x=60, y=70)
#label2.grid(row=0, column=0, sticky=E)


def put_button(username, bin1, bin2, bin3, bin4, bin5, bin6):
    print("ユーザ名；", username.get())

    # チェックされているか？
    if bin1.get():
        bot_flag[0]=True
    else:
        bot_flag[0]=False

    if bin2.get():
        bot_flag[1]=True
    else:
        bot_flag[1]=False

    if bin3.get():
        bot_flag[2]=True
    else:
        bot_flag[2]=False

    if bin4.get():
        bot_flag[3]=True
    else:
        bot_flag[3]=False

    if bin5.get():
        bot_flag[4]=True
    else:
        bot_flag[4]=False

    if bin6.get():
        bot_flag[5]=True
    else:
        bot_flag[5]=False

    print("選択ボット：", bot_flag)

    root.destroy()
    root.quit()



def Get_infomation():
    # Username Entry
    username = StringVar()
    username_entry = ttk.Entry(
        frame1,
        textvariable=username,
        width=30)
    username_entry.grid(row=0, column=1)

    frame2 = ttk.Frame(frame1, padding=(0, 5))
    frame2.grid(row=2, column=1, sticky=W)


    # チェックON・OFF変数
    bin1 = BooleanVar()
    bin1.set(False)
    chk1 = ttk.Checkbutton(root,variable=bin1, text='bot1(画像リプライ)')
    chk1.place(x=70, y=90)

    bin2 = BooleanVar()
    bin2.set(False)
    chk2 = ttk.Checkbutton(root,variable=bin2, text='bot2(対話ボット)')
    chk2.place(x=70, y=110)

    bin3 = BooleanVar()
    bin3.set(False)
    chk3 = ttk.Checkbutton(root,variable=bin3, text='bot3(クソリプ)')
    chk3.place(x=70, y=130)
    
    bin4 = BooleanVar()
    bin4.set(False)
    chk4 = ttk.Checkbutton(root,variable=bin4, text='bot4(しりとり)')
    chk4.place(x=70, y=150)
    
    bin5 = BooleanVar()
    bin5.set(False)
    chk5 = ttk.Checkbutton(root,variable=bin5, text='bot5(励まし)')
    chk5.place(x=70, y=170)
    
    bin6 = BooleanVar()
    bin6.set(False)
    chk6 = ttk.Checkbutton(root,variable=bin6, text='bot6(あいさつ)')
    chk6.place(x=70, y=190)


    # OK.Chancelボタン
    button1 = ttk.Button(text='OK',command=lambda: put_button(username, bin1, bin2, bin3, bin4, bin5, bin6))
    button1.place(x=220,y=250)
    button2 = ttk.Button(text='Cancel', command=quit)
    button2.place(x=310,y=250)

    root.mainloop()
    
    return [username.get()], bot_flag


if __name__ == '__main__':
    Get_infomation()
    
