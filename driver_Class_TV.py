from Class_TV import TV 
import tkinter as tk
import sys
class TVDriver:
    def TVTest(self):
        #Imports two TV sets
        first_tv=TV()
        second_TV=TV()
        #TV 1's properties
        first_tv.tv_on()
        first_tv.know_tv_channel()
        first_tv.tv_channel(30)
        first_tv.tv_volume(3)

        #second TV's properties
        second_TV.tv_on()
        second_TV.know_tv_channel()
        second_TV.tv_channel(3)
        second_TV.tv_volume(2)

        window=tk.Tk()
        #Print TV 1's properties
        window.title("TV Properties")
        window.minsize(300,500)
        lbl=tk.Label(text="TV 1's channel is "+ str(first_tv.know_tv_channel()) + " and the volume is " + str(first_tv.know_tv_volume()))
        lbl.pack()
        lbl2=tk.Label(text="TV 2's channel is " + str(second_TV.know_tv_channel()) + " and the volume is " + str(second_TV.know_tv_volume()))
        lbl2.pack()
        button=tk.Button(text="Exit", command=window.quit())
        button.pack()
        window.mainloop()

driver=TVDriver()
driver.TVTest()
