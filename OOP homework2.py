class House:
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color
        
    def build_expansion(self, added_size):
       
        self.size += added_size


home = House(2000)
print(home.size) 
home.build_expansion(500)
print(home.size) 
