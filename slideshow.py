
import glob
from logging import root
import PySimpleGUI as sg
import tkinter as tk 
from tkinter import*
from PIL import Image
from PIL import ImageTk
import random
import shutil
import os






def Alll():
    def parse_folder(path):
        images = glob.glob(f'{path}/*.jpg') + glob.glob(f'{path}/*.png')
        return images

    def load_image(path, window):

        try:
            image = Image.open(path)
            image.thumbnail((400, 400))
            photo_img = ImageTk.PhotoImage(image)
            window["image"].update(data=photo_img)
        except:
            print(f"Unable to open {path}!")
    def main():
        elements = [
            [sg.Image(key="image")],
            [
                sg.Text("Image File"),
                sg.Input(size=(25, 1), enable_events=True, key="file"),
                sg.FolderBrowse(),
            ],
            [
                sg.Button("Prev"),
                sg.Button("Next"),
                sg.Button("Exit"),
                sg.Button("Save"),
                
                sg.Button("slider")
            ]
        ]
        window = sg.Window("Image Viewer", elements, size=(550, 500))
        images = []
        location = 0
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED: 
                if 1+1==2:
                    break

            if event == "file":
                images = parse_folder(values["file"])
                if images:
                    load_image(images[0], window)
            if event == "Next" and images:
                if location == len(images) - 1:
                    location = 0
                else:
                    location += 1
                load_image(images[location], window)
            #if event == "Slider":
               
                
            if event == "Prev" and images:
                if location == 0:
                    location = len(images) - 1
                else:
                    location -= 1
                load_image(images[location], window)
            if event == "Save" and images:
                if True:
                    src_dir = images[location]
                    dst_dir = "/Users/spn/Desktop/pngs"
                    for jpgfile in glob.iglob(os.path.join(src_dir)):
                        shutil.copy(jpgfile, dst_dir) 
                else:
                    print("Breaking ")
            if event == "slider":
                print("working on it ")                
        window.close()
    if __name__ == "__main__":
        main() 

Alll()










