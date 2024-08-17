class Book:
    def __init__(self,cat,id,name,quan) -> None:
        self.cat=cat
        self.id=id
        self.name=name
        self.quan=quan
    
class User:
    def __init__(self,id,name,password) -> None:
        self.id=id
        self.name=name
        self.password=password
        self.borrowedBooks=[]
       

class Library:
    def __init__(self,owner,name) -> None:
        self.owner=owner
        self.name=name
        self.books=[]
        self.users=[]
    
    def addBook(self,cat,id,name,quan):
        book=Book(cat,id,name,quan)
        self.books.append(book)
        print(f"{name} Successfully Added")
    

    def addUser(self,id,name,password):
        user=User(id,name,password)
        self.users.append(user)
        return user

    def borrowBook(self,user,id):
        for book in self.books:
            if book.id==id:
                if book in user.borrowedBooks:
                    print("\n\t Already Borrowed!")
                    return
                elif book.quan<1:
                    print("\n\t Not available!!!")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quan-=1
                    print(f"\n\t {book.name} Successfully Borrowed!!!")
                    return

        print("\n\t Sorry! Book is not Found!!!")




p1=Library("Shaheen","Phitron Library")
admin=p1.addUser(1,"arif","admin1")
# pybook=p1.addBook("sci-fri",15,"dune",5)

run= True
currentUser=admin
while run:
    if currentUser==None:
        print("No logged in user!!")

        option=input("Login? Registration(L/R): ")
        if option=="R":
            id= int(input("\t Enter id: "))
            name=input("\tEnter Name: ")
            password=input("\tEnter Password: ")
            user=p1.addUser(id,name,password)
            currentUser=user

        elif option=="L":
            id= int(input("\t Enter id: "))
            password=input("\tEnter Password: ")

            match=False
            for user in p1.users:
                if user.id==id and user.password==password:
                    currentUser=user
                    match=True
                    break
            if match==False:
                print("No user Found!!")
    else:
        if currentUser==admin:     
            print("Option: \n")
            print("1: Add Book")
            print("2: Show users")
            print("3:Show books")
            print("4:Logout!")
            ch=int(input("Enter Your Choice: "))

            if ch==1:
                cat=input("\tEnter Category: ")
                id=int(input("Enter Id: "))
                name=input("Enter Name: ")
                quantity=int(input("Enter quantity: "))
                p1.addBook(cat,id,name,quantity)
            elif ch==2:
                print(f"The User name is: ",currentUser.name)

            # elif ch==3:
            #     for book in p1.books:
            #         print(p1.addBook)


            elif ch==4:
                currentUser=None
        else:
            print("Option: \n")
            print("1: Borrow Books")
            print("2: Return Books")
            print("3:Show books")
            print("4:Show Borrow Book")
            print("5:Show Return Book")
            print("6:Log Out!!")
            
            ch=int(input("Enter Your Choice: "))
            if ch==6:
                currentUser=None


            
            
