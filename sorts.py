""" The sorts functions of the application """
from random import randint

def bubbleSort(array):
	""" Sort the array passed in parameter with the bubble sort """
	length=len(array)
	for i in range(length-1,0,-1):
		isSorted=True
		for j in range(i):
			if array[j+1]<array[j]:
				array.exchangeElements(j+1,j)
				isSorted=False
		if isSorted:
			break

def partition(array,first,last,pivot):
	""" Make a partition in array, by placing all elements lower than array[pivot]
	    before it and the others after """
	array.exchangeElements(pivot,last)
	j=first
	for i in range(first,last):
		if array[i]<=array[last]:
			array.exchangeElements(i,j)
			j+=1
	array.exchangeElements(last,j)
	return j

def quickSort(array,first,last):
	""" Sort the array passed in parameter with the quick sort """
	if first<last:
		pivot=randint(first,last)
		pivot=partition(array,first,last,pivot)
		quickSort(array,first,pivot-1)
		quickSort(array,pivot+1,last)

def combSort(array):
	""" Sort the array passed in parameter with the comb sort """
	length=len(array)
	interval=length
	change=True
	while change or interval>1:
		interval=int(interval/1.3)
		change=False
		for i in range(length-1-interval):
			if array[i+1]<array[i]:
				array.exchangeElements(i+1,i)
				change=True

def selectionSort(array):
	""" Sort the array passed in parameter with the selection sort """
	length=len(array)
	for i in range(length-1):
		mini=i
		for j in range(i+1,length):
			if array[j]<array[mini]:
				mini=j
		if mini!=i:
			array.exchangeElements(i,mini)

def mergeSort(array):
	""" Sort the array passed in parameter with the merge sort """
	length=len(array)
	if length<=1:
		return array
	else:
		m=int(length/2)
		return merge(mergeSort(array[:m]),mergeSort(array[m:]))

def merge(l1,l2):
	""" Merge 2 lists into 1 sorted list """
	if not l1:
		return l2
	elif not l2:
		return l1
	elif l1[0]<=l2[0]:
		return [l1[0]]+merge(l1[1:],l2)
	else:
		return [l2[0]]+merge(l1,l2[1:])

def insertionSort(array):
	""" Sort the array passed in parameter with the insertion sort """
	length=len(array)
	for i in range(1,length):
		x=array[i]
		j=i
		while j>0 and array[j-1]>x:
			array[j]=array[j-1]
			j-=1
		array[j]=x

if __name__ == '__main__':
	l=[1,5,2,13,8,9]
	print(l)
	insertionSort(l)
	print(l)