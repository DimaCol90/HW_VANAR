class FruitBox:
    def __init__(self,apples,oranges):
        if isinstance(apples,int) and isinstance(oranges,int):
            if apples + oranges>50:
                print("limit is 50")
            else:
                self.apples = apples
                self.oranges = oranges
        else:
            print("not integer")
        
    def __add__(self, other_box):
        return FruitBox(self.apples + other_box.apples, self.oranges + other_box.oranges)
  
b1=FruitBox(5,10)    
b2=FruitBox(10,20)
b3= b1 + b2
print(b3.apples)
print(b3.oranges)

print(b3)