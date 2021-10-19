This tutorial will cover some of the basic OOPs(object oriented programming) concept in brief. If you want to learn it in more detail 
I would suggest you take time to also look into other tutorials

This tutorial will not reiterate the definitions. This tutorial will only help you to understand concepts by using examples.

### Class:
This is one of the fundamental concept of OOPs. You will be using class to group similar items, properties of a thing.


**example:** Take for instance Mercedes Benz(car manfacturing company) as a thing. Now ask yourself, what will you look before buying a Mercedes Benz?

You will likely look into color(eg: blue, black etc.), model(s-class, c-class, g-class etc), shape(sedan, SUV, hatchback etc.), horsepower etc.
Now color, model etc will be called as properties of the car(in our case Mercedes).

Now write down the properties.
* color.
* model.
* shape.
You can add more properties if you wish to.

now 


**example:** Take a Car as a thing. Now ask yourself, how will you differentiate between different each car? 
You will likely look at the brand of the car(eg: Mercedes Benz, Rolls Royce, Toyota etc.), each car might have different color (eg: blue, black etc.), and each car will be classified into Sedan, SUV, hatchback etc. and every car will have different shape.
So the properties of the car are as follows:
* brand.
* color.
* classification.
* shape

So now you will have to group the common properties under a class.
So the way you define a class in python could be so.

```python
class Car:
    def __init__(self, color="red"):
        self.color = color
        self.category = "sedan"
        self.brand = "Mercedes Benz"
    
    def set_brand(self, brand):
        self.brand = brand
    
    def set_categoty(self, category):
        self.category = category
car1 = Car("black")
car1.set_brand("Toyota")
print(car1.brand) # op: Toyota
```

> Note: functions inside the classes are called methods.
When you create an instance/object by calling the class like Car() each c