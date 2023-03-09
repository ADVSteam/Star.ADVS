#设计基本框架
import tkinter as tk
import tkinter.messagebox
win = tk.Tk()
win.title("Star账号获取系统")
win.geometry("500x260")
#进行设定功能代码
tk_name = tk.StringVar()
tk_name.set("Star.ADVS TEAM")
tk_pwd = tk.StringVar()
tk_pwd.set("")
#处理函数模块
def login():
    name = tk_name.get()
    pwd = tk_pwd.get()
    if name == "Star.ADVS TEAM"  and pwd == "Star.20230309":
        tk.messagebox.showinfo(title = '获取成功',message = '文件地址:https://h5.icodee.com/gui/share?pid=VRb5BX6Y1D&bellcode_env=pro')
    else:
        tk.messagebox.showinfo(title = '获取失败',message = '失败原因:可能由于密码输入错误 ; 如果您没有获取到密码请咨询zparty.cn@outlook.com')

def cancel():
    tk_pwd.set('')
    tk_name.set("Star.ADVS TEAM")
    
def _quit():
    win.quit()
    win.destroy()

#设计标签页
labzparty =  tk.Label(win,text = 'Star账号获取系统',width = 250)
labzs = tk.Label(win,text='#如果您没有获取到密码请到zparty.cn@outlook.com获取，输入”20230309“即可获取。',width = 150)
labname = tk.Label(win,text='账号:',width = 150)
labpwd = tk.Label(win,text='密码:',width = 150)

#设计输入框
entname = tk.Entry(win, width = 100,textvariable = tk_name)
entpwd = tk.Entry(win, show = '*', width = 100,textvariable = tk_pwd)

#设计按钮
ok = tk.Button(win,text = "下一步",command = login)
_quit = tk.Button(win,text = "退出",command = _quit)
cancel = tk.Button(win,text = "重置",command = cancel)

#窗口位置
labzparty.place(x = 50,y = 0,width = 400,height = 50)
labzs.place(x = 10,y = 200,width = 500,height = 30)
labname.place(x =120  ,y = 60 ,width =80,height =20 )
labpwd.place(x =120  ,y =100  ,width = 80,height =20 )
entname.place(x =  200,y = 60 ,width = 150,height = 20)
entpwd.place(x = 200,y = 100 ,width = 150,height =20 )
ok.place(x =290  ,y = 150 ,width = 50,height = 20)
_quit.place(x = 150 ,y =  150,width = 50,height = 20)
cancel.place(x = 220 ,y =  150,width =50 ,height =20 )

#结束
win.mainloop()



        
        
