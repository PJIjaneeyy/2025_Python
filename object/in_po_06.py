import tkinter as tk
from tkinter import ttk

class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

class Duck(Animal):
    def speak(self):
        return "꽥꽥!"

def make_sound(animal_class):
    animal = animal_class()
    result_label.config(text=animal.speak())

root = tk.Tk()
root.title("동물 소리 듣기") 




...



root.mainloop()