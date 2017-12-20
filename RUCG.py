#Made by Sournav Sekhar Bhattacharya
from tkinter import *
import praw
cnt=0;
client_id_user=''
client_s_user=''
name_user=''
pwd=''
search_user=''

def window0():

    window0=Tk();
    window0.title("Subreddit Analsys for Mods")
    window0.minsize(width=400, height=400)
    def click():
        global client_id_user
        client_id_user=textentry.get()
        global client_s_user
        client_s_user=textentry2.get()
        global name_user
        name_user=textentry3.get()
        global pwd
        pwd=textentry4.get()
        global search_user
        search_user=textentry5.get()
        window0.destroy()
    Label(window0,text="Client ID:  ").grid(row=0)
    textentry = Entry(window0,width=20, bg="white")
    textentry.grid(row=0,column=1,sticky=W)
    Label(window0,text="Client Secret:  ").grid(row=1)
    textentry2= Entry(window0,width=20, bg="white")
    textentry2.grid(row=1,column=1,sticky=W)
    Label(window0,text="Username:  ").grid(row=2)
    textentry3= Entry(window0,width=20, bg="white")
    textentry3.grid(row=2,column=1,sticky=W)
    Label(window0,text="Password:  ").grid(row=3)
    textentry4= Entry(window0,width=20, bg="white")
    textentry4.config(show="*")
    textentry4.grid(row=3,column=1,sticky=W)
    Label(window0,text="Searchuser:  ").grid(row=4)
    textentry5= Entry(window0,width=20, bg="white")
    textentry5.grid(row=4,column=1,sticky=W)
    #Button 1
    button1=Button(window0,text="SUBMIT",width=6, command=click)
    button1.grid(row=5,column=1,sticky=W,pady=4)
    text=open('login_info.txt').read().splitlines();
    mainloop()
window0()
reddit=praw.Reddit(client_id=client_id_user,
                       client_secret=client_s_user,
                       username=name_user,
                       password=pwd,
                       user_agent='bob1')
        
for comment in reddit.redditor(search_user).comments.new(limit=None):
  try:
    f = open('store.txt', 'a')
    f.write('\n')
    f.write(comment.body)
    f.write('\n')
    f.close()
    print(comment.body)
  except Exception as e:
    pass

