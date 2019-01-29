from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color,Rectangle
from kivy.animation import Animation
from constants import *
from time import sleep

class Array(Widget):
	"""An array containing objects of type SquareOfArray and a list of its values """

	def __init__(self,values,**kwargs):
		super(Array, self).__init__(**kwargs)
		self.values=values
		self.size_hint=(None,None)
		with self.canvas:
			Color(1., 0, 0)
			self.squares=[SquareOfArray(x,pos=(WIDTH_CASE*i,10),size=(WIDTH_CASE,HEIGHT_CASE),size_hint=(None,None)) 
			for i,x in enumerate(values)]

	def update_rect(self, *args):
		self.squares[i].pos = self.pos
		self.rect.size = self.size

	def __getitem__(self,i):
		return self.values[i]

	def __setitem__(self,i,x):
		self.values[i]=x

	def __len__(self):
		return len(self.values)

	def animationExchangeElements(self,square,d,y,k):
		"""Move a square of the array self"""
		animation=Animation(pos=square.pos,t='out_bounce')
		animation+=Animation(pos=(square.pos[0]+d,square.pos[1]+y),t='out_bounce')
		animation+=Animation(pos=self.squares[k].pos,t='out_bounce')
		animation.start(square)

	def exchangeElements(self,i,j):
		"""Exchange the elements of indexes i and j of the list self.values"""
		radiusRotation=(i+j)*WIDTH_CASE/2
		print(radiusRotation)
		self.values[i],self.values[j]=self.values[j],self.values[i]
		#self.animationExchangeElements(self.squares[i],radiusRotation,50,j)
		#self.animationExchangeElements(self.squares[j],-radiusRotation,50,i)
		k=self.squares[i].pos[0]
		self.squares[i].pos=(self.squares[j].pos[0],self.squares[i].pos[1])
		self.squares[j].pos=(k,self.squares[j].pos[1])
		print("---------------------",i," ",j)
		for x  in self.squares:
			print("x:",x.pos[0]," y:",x.pos[1])
		print(self.values)


class SquareOfArray(Widget):
	"""A square of array (present in Array.squares)"""

	def __init__(self,value,**kwargs):
		super(SquareOfArray, self).__init__(**kwargs)
		self.value=value
		with self.canvas:
			Color(1,1,1,1)
			self.border=Rectangle(pos=self.pos,size=self.size)
			Color(1,0,0,1)
			self.rect=Rectangle(pos=(self.pos[0]+2,self.pos[1]+2),size=(self.width*0.9,self.height*0.9))
			self.labelValue=Label(text=str(value),pos=self.rect.pos,size=self.size,markup=True)
			self.bind(pos=self.update_square,size=self.update_square)

	def update_square(self, *args):
		self.border.pos=self.pos
		self.rect.pos=(self.pos[0]+2,self.pos[1]+2)
		self.labelValue.pos=self.rect.pos