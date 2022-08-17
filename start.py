class book:
    def __init__(self,pageno,price,name):
        self.pagenumber = pageno
        self.rate = price
        self.name = name
    
    def show(self,author):
        print("pages are ",self.pagenumber)
        print("price is ",self.rate)
        print("name is ",self.name)
        print("author is ",author)



v = book(250,800,"hello again")
v.show("bengali")
