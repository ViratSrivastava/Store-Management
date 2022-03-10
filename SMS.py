import pickle
import random as r
import os
import time as t
class productlist(object):
    def __int__(l):
        #seller
        l.sno=0
        l.prodno=0
        l.prodname=""
        l.prodtype=""
        l.qnt=0
        l.price=0
        #buyer
        l.buyer=""
        l.tprice=0
        l.buyqnt=0
        l.date=0
        l.address=""
    #Seller
    def add_prod(l):
        l.sno=r.randint(0,999)
        l.prodno=r.randint(10000,99999)
        print("Your Serial No. is : ",l.sno)
        print("product No. is : ",l.prodno) 
        l.prodname=input("Type Product Name : ")
        l.prodtype=input("Type Product Type : ")
        l.qnt=int(input("Type Product Quantity : "))
        l.price=int(input("Type Product Price : "))
    def display_all(l):        
        print("%-4s"%l.sno,"%-7s"%l.prodno,"%-35s"%l.prodname,"%-12s"%l.prodtype,"%-8s"%l.qnt,"%-5s"%l.price)
    def display_prod(l):
        print("Serial No. : ",l.sno)
        print("Product No. : ",l.prodno)
        print("Product Name. : ",l.prodname)
        print("Product Type : ",l.prodtype)
        print("Product Quantity : ",l.qnt)
        print("Product Price : ",l.price)
        #Buyer
    def cancel_prod(l):
        l.buyer=l.buyer
        l.address=l.address
        l.buyqnt=l.buyqnt
        l.date=l.date
        l.tprice=l.tprice
    def buy_prod(l):
        l.sno=l.sno
        l.prodno=l.prodno
        l.price=l.price
        l.prodname=l.prodname
        l.prodtype=l.prodtype
        l.buyer=input("Type Customer Name : ")
        qnt=int(input("How Much Quantity You Want To Buy : "))
        if(l.qnt==0):
            print("Currently Product Not Available")
        elif(qnt<=l.qnt):
            l.qnt-=qnt
            l.buyqnt=qnt
            
        else:
            print("You Cannot Buy More Than ",l.qnt," Quantity")
        l.address=input("Type Customer Address : ")
        l.tprice=l.price*l.buyqnt
        l.date=t.ctime()
        print("Your Total Price is : ",l.tprice)
        print("Date/Time : ",l.date)
    def check_prod(l):
        try:
            l.buyer=l.buyer
            print("Serial No. : ",l.sno)
            print("Product No. : ",l.prodno)                
            print("Customer Name : ",l.buyer)
            print("Product Name. : ",l.prodname)
            print("Product Type : ",l.prodtype)
            print("Product Quantity : ",l.buyqnt)
            print("Day/Date/Time : ",l.date)
            print("Product Price : ",l.price)
            print("Total Price : ",l.tprice)
            print("Customer Address : ",l.address)
        except AttributeError:
            print("Product Not Buyed Yet")
    def display_buyer(l):
        try:
            if not(l.buyer==""):
                print("%-3s"%l.sno,"%-5s"%l.prodno,"%-10s"%l.buyer,"%-10s"%l.prodname,"%-10s"%l.prodtype,"%-3s"%l.buyqnt,"%-20s"%l.date,"%-7s"%l.price,"%-7s"%l.tprice,"%-40s"%l.address)
                print(20*"~~~~")
        except AttributeError:
            pass
    
    def display_prodtype(l):
        try:
            if(l.prodtype in l.prodtype):
                print("%-10s"%l.prodtype)
        except AttributeError:
            pass
    def modify_prod_data(l):
        try:
            l.prodname=input("Type Product Name : ")
            l.prodtype=input("Type Product Type : ")
            l.qnt=int(input("Type Product Quantity : "))
            l.price=int(input("Type Product Price : "))
        except AttributeError:
            pass
    
#Seller
e=open("prodlist.dat","ab")
e.close()
pass
def seller():
    #main
    #Add Product
    def new_prod():
        os.system("cls")
        print(40*"~~~~","\n\n")
        print("              Add Products\n")
        print(40*"~~~~","\n")
        try:
            prod=productlist()
            file=open("prodlist.dat","ab")
            prod.add_prod()
            pickle.dump(prod,file)
            file.close()
            print("Product Added Successfully")
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except:
            pass

    def remove_prod():
        z=0
        try:
            n=int(input("Type Searial No. Or Product No. : "))
            file=open("prodlist.dat","rb")
            temp=open("temp.dat","wb")
            while True:
                prod=pickle.load(file)
                if((prod.sno==n)or(prod.prodno==n)):
                    z=1
                    print("Product Found")
                    prod.display_prod()
                    print("\n\nProduct Removed Successfuly")
                else:
                    pickle.dump(prod,temp)
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except EOFError:
            file.close()
            temp.close()
            if(z==0):
                print("Product Not Found")
        except IOError:
            print("File Not Found")
        os.remove("prodlist.dat")
        os.rename("temp.dat","prodlist.dat")
        input("Press Enter To Continue...")
#Remove All Products
    def remove():
        os.system("cls")
        print(40*"~~~~","\n\n")
        print("        Remove All Products")
        print(40*"~~~~","\n")
        try:
            a=input("Are You Realy Want To Remove All Products...[Y/N] : ")
            
            b=open("temp.dat","wb")
            if(a=='y' or a=='Y'):
                os.remove("prodlist.dat")
                b.close()
                os.rename("temp.dat","prodlist.dat")
                print("All Products Removed Successfuly")
            else:        
                b.close()
                os.remove("temp.dat")
                print("Remove All Products Unsuccessful")
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except:
            pass
        
#Display All Products
    def disp_all():
        os.system("cls")
        print(40*"~~~~","\n\n")
        print("                             All Products\n")
        print(40*"~~~~","\n")
        try:
            file=open("prodlist.dat","rb")
            print("%-3s"%"Sno.","%-5s"%"ProdNo.","%-35s"%"Name","%-12s"%"Type","%-3s"%"Quantity","%-7s"%"Price")
            print(20*"~~~~")
            while True:
                
                prod=pickle.load(file)
                prod.display_all()
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except EOFError:
            file.close()
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except IOError:
            print("File Not Found")
#search Product
    def disp_prod():
        os.system("cls")
        print(40*"~~~~","\n\n")
        print("              Search By Name\n")
        print(40*"~~~~","\n")
        try:
            z=0
            pl=int(input("Type Product Name : "))
            file=open("prodlist.dat","rb")
            while True:
                prod=pickle.load(file)
                if(prod.prodname==pl):
                    z=1
                    prod.display_prod()
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except EOFError:
            file.close()
            if(z==0):
                print("Product Not Available")
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except IOError:
            print("File Not Found")
#All Buyers
    def disp_buyer():
        os.system("cls")
        print(40*"~~~~","\n\n")
        print("                                 All Buyers\n")
        print(40*"~~~~","\n")
        try:
            file=open("prodlist.dat","rb")
            while True:
                prod=pickle.load(file)
                prod.display_buyer()
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except EOFError:
            file.close()
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except IOError:
            print("File Not Found")
        

    while True:
        os.system("cls")
        print(40*"~~~~","\n\n")
        print("                             Grossary Management\n")
        print(40*"~~~~","\n")
        print("""
1.  Add Product
2.  Display All Products
3.  Display Buyers
4.  Search Products
5.  Search Product By Catagory Type
6.  Display Catagory Type
7.  Modify Product Details
8.  Remove Product
9.  Remove All Products
10. Exit
    """)
        try:
            ch=int(input("Type Your Choice : "))
            if(ch==1):
                new_prod()
            elif(ch==2):
                disp_all()
            elif(ch==3):
                disp_buyer()
            elif(ch==4):
                disp_prod()
            elif(ch==5):
                disp_type()
            elif(ch==6):
                display_type()
            elif(ch==7):
                modify_prod()
            elif(ch==8):
                remove_prod()
            elif(ch==9):
                remove()
            elif(ch==10):
                break
            else:
                print("INVALID CHOICE")
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        

#Modify Product
def modify_prod():
    os.system("cls")
    try:
        z=0
        n=int(input("Type Searial No. Or Product No. : "))
        file=open("prodlist.dat","rb")
        temp=open("temp.dat","wb")
        while True:               
            prod=pickle.load(file)
            if((prod.sno==n)or(prod.prodno==n)):
                z=1
                print("Product Found")
                
                print("Enter New Data")
                prod.modify_prod_data()
                pickle.dump(prod,temp)
                print("Product Modified Successfuly")
            else:
                pickle.dump(prod,temp)
    except ValueError:
        print("Please Type Integer Number")
        input("Press Enter To Continue...")
    except EOFError:
        file.close()
        temp.close()
        if(z==0):
            print("Productt Not Available")
    except IOError:
        print("File Not Found")
    os.remove("prodlist.dat")
    os.rename("temp.dat","prodlist.dat")
    input("Press Enter To Continue...")



#Display Product By Type
def disp_type():
    os.system("cls")
    print(40*"~~~~","\n\n")
    print("              Search By Product Catagory Type\n")
    print(40*"~~~~","\n")
    try:
        z=0
        pl=input("Type Product Type : ")
        file=open("prodlist.dat","rb")
        while True:
            prod=pickle.load(file)
            if(prod.prodtype.lower()==pl):
                z=1
                prod.display_all()
    except ValueError:
        print("Please Type Integer Number")
        input("Press Enter To Continue...")        
    except EOFError:
        file.close()
        if(z==0):
            print("Product Not Available")
        print(40*"~~~~")
        input("Press Enter To Continue...")
    except IOError:
        print("File Not Found")
#Display Product Type

def display_type():
    os.system("cls")
    print(40*"~~~~","\n\n")
    print("              Product Catagory Type\n")
    print(40*"~~~~","\n")
    try:
        z=0
        file=open("prodlist.dat","rb")
        while True:
            prod=pickle.load(file)
            z=1
            
            prod.display_prodtype()
    except ValueError:
        print("Please Type Integer Number")
        input("Press Enter To Continue...")        
    except EOFError:
        file.close()
        if(z==0):
            print("Product Not Available")
        print(40*"~~~~")
        input("Press Enter To Continue...")
    except IOError:
        print("File Not Found")


def buyer():
    def prod_buy():
        os.system("cls")
        print(40*"~~~~","\n\n")
        print("                                    Buy Product\n")
        print(40*"~~~~","\n")
        try:
            z=0
            pl=int(input("Type Product Serial No. or Product No. : "))
            file=open("prodlist.dat","rb")
            temp=open("temp.dat","wb")
            while True:
                prod=pickle.load(file)
                if((prod.sno==pl) or (prod.prodno==pl)):
                    z=1
                    print("Product Found")
                    prod.display_prod()
                    prod.buy_prod()
                    pickle.dump(prod,temp)
                else:
                    pickle.dump(prod,temp)
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except EOFError:
            file.close()
            temp.close()
            if(z==0):
                print("Product Not Found")
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except IOError:
            print("File Not Found")
        os.remove("prodlist.dat")
        os.rename("temp.dat","prodlist.dat")
# Cancel Product
    def remove_buyer():
        z=0
        try:
            n=int(input("Type Searial No. Or Product No. : "))
            name=input("Type Customer Name : ")
            file=open("prodlist.dat","rb")
            temp=open("temp.dat","wb")
            while True:
                
                prod=pickle.load(file)
                if(((prod.sno==n)or(prod.prodno==n))and(prod.buyer==name)):
                    z=1
                    print("Product Found")
                    prod.cancel_prod()
                    
                else:
                    pickle.dump(prod,temp)
                    
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except EOFError:
            file.close()
            temp.close()
            print("\n\nOrder Canceled Successfuly")
            if(z==0):
                print("Order Not Found")
        except IOError:
            print("File Not Found")
        os.remove("prodlist.dat")
        os.rename("temp.dat","prodlist.dat")
        input("Press Enter To Continue...")

#Display all Products For Buyer
    def buy_all():
        os.system("cls")
        print(40*"~~~~","\n\n")
        print("                                         All Products\n")
        print(40*"~~~~","\n")
        try:
            file=open("prodlist.dat","rb")
            print("%-3s"%"Sno.","%-5s"%"ProdNo.","%-35s"%"Name","%-12s"%"Type","%-3s"%"Quantity","%-7s"%"Price")
            print(20*"~~~~")
            while True:
                prod=pickle.load(file)
                prod.display_all()
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except EOFError:
            file.close()
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except IOError:
            print("File Not Found")
#search Product
    def prod_disp():
        os.system("cls")
        print(40*"~~~~","\n\n")
        print("                                 Search Orders By Searial No. or Product No.\n")
        print(40*"~~~~","\n")
        try:
            z=0
            pl=int(input("Type Product Serial No. or Product No. : "))
            file=open("prodlist.dat","rb")
            while True:
                prod=pickle.load(file)
                if((prod.sno==pl) or (prod.prodno==pl)):
                    z=1
                    prod.check_prod()
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except EOFError:
            file.close()
            if(z==0):
                print("No Orders Available")
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except IOError:
            print("File Not Found")
    #search Product
    def search_prod():
        os.system("cls")
        print(40*"~~~~","\n\n")
        print("                                   Search By Name\n")
        print(40*"~~~~","\n")
        try:
            z=0
            pl=input("Type Product Name : ")
            file=open("prodlist.dat","rb")
            while True:
                prod=pickle.load(file)
                if(prod.prodname==pl):
                    z=1
                    prod.display_prod()
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except EOFError:
            file.close()
            if(z==0):
                print("Product Not Available")
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except IOError:
            print("File Not Found")


    while True:
        os.system("cls")
        print(40*"~~~~","\n\n")
        print("                                  Stack Management System\n")
        print("                                  Dev. By TRios\n")
        print(40*"~~~~","\n")
        print("""
1. Buy Product
2. Display All Products
3. Orders
4. Search Products
5. Search Product By Type
6. Display Product Type
7. Exit
    """)
        try:
            ch=int(input("Type Your Choice : "))
            if(ch==1):
                prod_buy()
            elif(ch==2):
                buy_all()
            elif(ch==4):
                search_prod()
            elif(ch==3):
                prod_disp()
            elif(ch==5):
                disp_type()
            elif(ch==6):
                display_type()
            elif(ch==7):
                print(40*"~~~~")
                print("                           Thank You For Using My Program         ")
                print(40*"~~~~")
                break
            else:
                print("INVALID CHOICE")
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        

while True:
    os.system("title Program Made By TRios")
    os.system("cls")
    print(40*"~~~~","\n\n")
    print("                             Please Choose Your Catagory\n")
    print(40*"~~~~","\n")
    print("""
1. Seller
2. Buyer
3. Exit""")
    try:
        ch=int(input("Type Your Choice : "))
        if(ch==1):
            cc=input("Type Seller Password : ")
            if(cc=="1234"):
                seller()
            else:
                print("You are Not Allowed To Seller's Area")
                input("Press Enter To Continue...")
                buyer()
        elif(ch==2):
            buyer()
        elif(ch==3):
            print(40*"~~~~")
            print("                                   Thank You For Using My Program         ")
            print(40*"~~~~")
            break
        else:
            print("INVALID CHOICE")
    except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")