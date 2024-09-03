class Notebook:
    def __init__(self):
        self.pages = 100  
        self.size = 'a4'  
        self.spacing = 'college'  
        
        # Additional attributes
        self.cover_color = 'blue
        self.is_hardcover = False   
        self.has_bookmark = True   
        self.owner = None           

    def add_owner(self, name):
        
        self.owner = name


journal = Notebook()
journal.add_owner("Alex")
print(journal)
