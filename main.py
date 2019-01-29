"""The main program """
from classes import *
from sorts import *
from kivy.app import App
from random import shuffle,randint
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

class GraphicSorts(App):
    def build(self):
        myList=[1,13,58,9,65,1,2,7]
        root=Window(Array(myList))
        return root
    
class Window(BoxLayout):

    def __init__(self,array,**kwargs):
        super(Window, self).__init__(**kwargs)
        self.orientation="horizontal"
        leftBar=BoxLayout(orientation="vertical",size_hint_x=None)
        self.array=array
        self.array.pos=self.pos
        self.nbEltsArray=None
        self.currentSort=None
        self.namesSorts={"Tri rapide":quickSort,"Tri fusion":mergeSort,"Tri par insertion":insertionSort,
        "Tri a bulles":bubbleSort,"Tri par selection":selectionSort,"Tri comb":combSort}
        btnNewArray=Button(text="Nouveau tableau",on_press=self.createNewArray,
            size_hint_y=None,height=44)
        creationArray=BoxLayout(pos=self.pos,orientation="horizontal")
        self.inputNbElts=TextInput(text="Nombre d'elements",multiline=False,
            on_text_validate=self.on_enter,size_hint_y=None,height=0)
        self.randomArray=ToggleButton(text='Aleatoire', group='kind of array',
            state='down',size_hint_y=None,height=0)
        self.manualArray=ToggleButton(text='Saisir manuellement',
            group='kind of array',size_hint_y=None,height=0)
        self.validateArray=Button(text="Valider",
            on_press=self.validateCreationArray,size_hint_y=None,height=0)
        widgets=[self.inputNbElts,self.randomArray,self.manualArray,self.validateArray]
        for widget in widgets:
            creationArray.add_widget(widget) 
        btnShuffle=Button(text="Melanger le tableau",on_press=self.shuffleArray,size_hint_y=None,height=44)
        listOfSorts=DropDown()
        for sort in self.namesSorts:
            btn=Button(text=sort,size_hint_y=None,height=35)
            btn.bind(on_release=lambda btn: listOfSorts.select(btn.text))
            listOfSorts.add_widget(btn)
        btnChooseSort=Button(text="Type de tri",on_release=listOfSorts.open,size_hint_y=None,height=44)
        btnSort=Button(text="Trier le tableau",on_press=self.sortArray)
        listOfSorts.bind(on_select=lambda instance, x: self.setCurrentSort(x))
        #add widgets in the window
        widgets=[btnNewArray,creationArray,btnShuffle,btnChooseSort,btnSort]
        for widget in widgets:
            leftBar.add_widget(widget)
        self.add_widget(leftBar)
        self.add_widget(array)

    def setCurrentSort(self,sort):
        self.currentSort=self.namesSorts[sort]
        print("tri courant "+sort)

    def on_enter(instance,value):
        try:
            self.nbEltsArray=int(value.text)
        except:
            value.text="Le nombre d'éléments du tableau doit etre 1 entier."

    def createNewArray(self,instance):
        """ Create a new array which can be a random array or a manual entry and update self.array """
        for widget in [self.inputNbElts,self.randomArray,self.manualArray,self.validateArray]:
            widget.height=10
            widget.size_hint_y=0.2

    def validateCreationArray(self,instance):
        print("ok")

    def shuffleArray(self,instance):
        """ Shuffle the current array self.array """
        newValues=sorted(self.array.values)
        self.array.values=newValues

    def sortArray(self,instance):
        """ Sort the current array self.array according to the value of self.currentSort """ 
        if not self.currentSort:
            print("Choisir 1 tri!")
        else:
            if self.currentSort.__name__=="quickSort":
                self.currentSort(self.array,0,len(self.array)-1)
            else:
                self.currentSort(self.array)
            print(self.array.values)

if __name__=="__main__":
	GraphicSorts().run()