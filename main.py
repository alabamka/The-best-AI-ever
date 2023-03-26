from tkinter import *
import customtkinter as ct
from random import randint
from time import sleep
from PIL import ImageTk, Image


num = 0
asked = ''


def WinProperties(win):
    win.geometry("600x300+540+240")
    win.title("I know every thing") 
    win.resizable(False, False) 
    win.iconbitmap('1.ico')


def Answer():
    global num
    global answer
    global asked
    global url
    event = text.get()
    circle1 = ct.CTkButton(master=win, text='', corner_radius=1000,width = 28,
                 fg_color='#989590', state=DISABLED)

    circle2 = ct.CTkButton(master=win, text = '', corner_radius=1000,width = 28,
                 fg_color='#989590', state=DISABLED)

    circle3 = ct.CTkButton(master=win, text = '', corner_radius=1000,width = 28,
                 fg_color='#989590', state=DISABLED)

    circle1.place(relx=0.53, rely=0.91, anchor=CENTER)
    circle2.place(relx=0.47, rely=0.85, anchor=CENTER)
    circle3.place(relx=0.41, rely=0.79, anchor=CENTER)

    if(len(event)>0):
        num = randint(1, 2)
        if (num == 1 and event[len(event) - 1] == '?' and asked != event):
            or try this
    
    
    def get_html():
    url = "https://ru.wikipedia.org/wiki/asled"
    get_page = requests.get(url).text
    return get_page


def get_subcategories():
    page = get_html()
    soup = BeautifulSoup(page, 'lxml')
    subcategories = []
    letters = soup.find('div', class_='toccolours plainlinks center').find('span').find_all('a')
    for letter in letters:
        subcategories.append(letter.get('href'))
    return subcategories


def get_data():
    answer = []
    subcategories = get_subcategories()
    for category in subcategories:
        url = requests.get(category).text
        soup = BeautifulSoup(url, 'lxml')
        names = soup.find(
            'div', class_='mw-content-ltr').find('div', class_='mw-category-group').find_all('a')
        for i in names:
            answer.append(i.text)
    return answer
            sleep(2)
            answer = 'NO'
        if (num == 2 and event[len(event) - 1] == '?' and asked != event):
            or try this
    
    
    def get_html():
    url = "https://ru.wikipedia.org/wiki/asled"
    get_page = requests.get(url).text
    return get_page


def get_subcategories():
    page = get_html()
    soup = BeautifulSoup(page, 'lxml')
    subcategories = []
    letters = soup.find('div', class_='toccolours plainlinks center').find('span').find_all('a')
    for letter in letters:
        subcategories.append(letter.get('href'))
    return subcategories


def get_data():
    answer = []
    subcategories = get_subcategories()
    for category in subcategories:
        url = requests.get(category).text
        soup = BeautifulSoup(url, 'lxml')
        names = soup.find(
            'div', class_='mw-content-ltr').find('div', class_='mw-category-group').find_all('a')
        for i in names:
            answer.append(i.text)
    return answer
            sleep(2)
            answer = 'YES'
        if (event[len(event) - 1] != '?'):
            answer = 'Where is question?'
        if (asked == event):
            answer = 'You already asked it'
    else:
        answer = '*waiting for input*'


    ans = ct.CTkButton(master=win,text=f'{answer}',font=('Cutive Mono Regular', 24), text_color_disabled='black', corner_radius=100,
                 fg_color='#989590', state=DISABLED)
    ans.place(relx=0.28, rely=0.68, anchor=CENTER)
    asked = event
    ans.after(4000, ans.destroy)
    circle1.after(1000, circle1.destroy)
    circle2.after(2000, circle2.destroy)
    circle3.after(3000, circle3.destroy)
    '''
    
    '''


win = ct.CTk()

answer = ct.StringVar()

ct.set_appearance_mode('dark')
WinProperties(win)

ct.CTkLabel(master=win,text='Ask me every thing, but I can answer only \"Yes\" or \"No\"',font=('Cutive Mono Regular', 18), text_color='#5C5CC0').place(relx=0.5, rely=0.05, anchor=CENTER)
text = ct.CTkEntry(master=win,width=500,font=('Cutive Mono Regular', 18), text_color='#5C5C91',placeholder_text='Ask me every thing')
text.place(relx=0.42, rely=0.15, anchor=CENTER)
ct.CTkButton(master=win,text='ASK',font=('Cutive Mono Regular', 24), text_color='#AAA9FF',corner_radius=1000, fg_color = '#5C5CC0',hover_color = '#363670',command=Answer).place(relx=0.13, rely=0.28, anchor=CENTER)
canvas = ct.CTkCanvas(master=win,width=380, height=320, background='#242424', highlightthickness=0)
canvas.place(relx=0.75, rely=0.63, anchor=CENTER)
image = Image.open("img.png")
image = image.resize((300, 300))
image = ImageTk.PhotoImage(image)
imagesprite = canvas.create_image(200, 150, image=image)
win.mainloop()
