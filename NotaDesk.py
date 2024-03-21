import flet as ft
import os
username = os.getlogin()
def main(page: ft.Page):
    page.title = "Flet Notepad"
    def save(e):
        file = open("C://Users//%s//Desktop//%s"%(username,filename.value+".txt"),'w')
        file.write(notepad.value)
        file.close()
    def update(e):
        file = open("C://Users//%s//Desktop//%s"%(username,filename.value+".txt"),'r')
        fileread = file.read()
        notepad.value=fileread
        page.update()
    def on_change(e):
        try:
            save.disabled=False
            update.disabled=False
            filename.error_text =""
            notepad.disabled = False
            file = open("C://Users//%s//Desktop//%s"%(username,filename.value+".txt"),'r')
            fileread = file.read()
            page.add(notepad)
            notepad.value=fileread
            page.update()
        except:
            save.disabled=True
            update.disabled=True
            filename.error_text ="That file doesn't exist!"
            notepad.disabled = True
            page.update()
    page.window_width=1000
    page.window_height=700
    text = ft.Text(value="Create a txt file in dekstop folder and write it's name")
    filename = ft.TextField(label='File name',width=300,on_change=on_change)
    notepad = ft.TextField(hint_text='Write here',border='underline',multiline=True)
    save = ft.ElevatedButton(text='Save',icon=ft.icons.SAVE,on_click=save,disabled=True)
    update = ft.ElevatedButton(text='Update',icon=ft.icons.DOWNLOAD_ROUNDED,on_click=update,disabled=True)
    page.add(text,filename,ft.Row([save,update]))
    page.update()
ft.app(target=main)
