# coding: utf-8
class Node():
  def __init__(self,key,value):
    self.key = key
    self.value = value
    self.passNum = ''
  
  def __eq__(self,other):
    return self.key == other.key and self.value == other.value
 	
  def __gt__(self,other):
    return self.key > other.key
 	
  def __lt__(self,other):
    return self.key < other.key

class Heap:
  def __init__(self, HeapType='min'):
    self._elements = []
    self._HeapType = HeapType
    self._count = 0

  def __len__(self):
    return self._count

  def is_empty(self):
    if len(self)==0:
      return True
    return False 

  def add(self, key, value):
    self._elements.append((key, value))
    self._count += 1
    self._UpSort(self._count - 1) 

  def delete(self):
    if self.is_empty():
      print "You cannot delete from empty heap."
    else:
      value = self._elements[0]
      self._count -= 1
      self._elements[0] = self._elements[self._count]
      self._DownSort(0)
      return value

  def _UpSort(self, index):
    if index > 0:
      parent = index // 2
      if self._HeapType != 'min':
        if self._elements[index][0] > self._elements[parent][0]:
          temp = self._elements[index]
          self._elements[index] = self._elements[parent]
          self._elements[parent] = temp
          self._UpSort(parent)
      else:
        if self._elements[index][0] > self._elements[parent][0]:
          temp = self._elements[index]
          self._elements[index] = self._elements[parent]
          self._elements[parent] = temp
          self._UpSort(parent)	

  def _DownSort(self, index):
    left = 2 * index + 1
    right = 2 * index + 2
    if self._HeapType != 'min':
      maxVal = index
      if left < self._count and self._elements[left][0] >= self._elements[maxVal][0]:
        maxVal = left
      elif right < self._count and self._elements[right][0] >= self._elements[maxVal][0]:
        maxVal = right
        if maxVal != index:
          temp = self._elements[maxVal]
          self._elements[maxVal] = self._elements[index]
          self._elements[index] = temp
          self._DownSort(maxVal)
    else:
      maxVal = index
      if left < self._count and self._elements[left][0] >= self._elements[maxVal][0]:
        maxVal = left
      elif right < self._count and self._elements[right][0] >= self._elements[maxVal][0]:
        maxVal = right
        if maxVal != index:
          temp = self._elements[maxVal]
          self._elements[maxVal] = self._elements[index]
          self._elements[index] = temp
          self._DownSort(maxVal)

def findMax(self):
  assert self._HeapType != "min"
  return self._L[0]

def findMin(self):
  assert self._HeapType == "min"
  return self._L[0]