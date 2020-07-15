from chef import Chef
from chef_chinese import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()  # => Inheritance function from Chef
