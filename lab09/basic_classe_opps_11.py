# TASK Lab 09
# Using the expenseTracker Class continue with the task:
# CREATE A CSV FIle for Expense/Income
# load the CSV File and populate the dictionary of the expenseTracker class
# find the total expense and income

# Additional Task
# Using the concept of menu driven programming,
# Show the menu options to add new transaction [expense/income]
# export the updated dictionary to the file

class expenseTracker:
    def __init__(self):
        self.transactionDetails={"details":[]}

    def retrieveTransactions(self):
        for i in open("G:\github\MScDSA-MDS171-23122038-stuty\lab09\data.csv","r+").readlines():
            line=i.split(",")
            if line[1]!="Expense Category":
                transaction={"type":line[0],"category":line[1],"amount":line[2],"description":line[3],"date":line[4]}
                self.transactionDetails["details"].append(transaction)

    def calculateTotal(self):
        totalIncome=0
        totalExpense=0
        for i in self.transactionDetails["details"]:
            if i["type"]=="Income":
                totalIncome+=int(i["amount"])
            else:
                totalExpense+=int(i["amount"])
        return totalIncome,totalExpense
    
    def addTransaction(self,type,category,amount,description,date):
        transaction={"type":type,"category":category,"amount":amount,"description":description,"date":date}
        self.transactionDetails["details"].append(transaction)
    
    def writeTransactions(self):
        file=open("G:\github\MScDSA-MDS171-23122038-stuty\lab09\data.csv","w+")
        file.write("Type,Expense Category,Amount,Description,Date\n")
        for i in self.transactionDetails["details"]:
            date=str(i["date"]).strip()
            file.write(i["type"]+","+i["category"]+","+i["amount"]+","+i["description"]+","+date+"\n")
        file.close()


order=expenseTracker()
order.retrieveTransactions()
while True:
    print("1.Add New Transaction\n2.Calculate Total Income and Expense\n3.Exit")
    choice=int(input("Select your action:"))
    if choice==1:
        type=input("Enter the type of transaction (Income/Expense):")
        category=input("Enter the category:")
        amount=input("Enter the amount:")
        description=input("Enter the description of transaction:")
        date=input("Enter the date mm/dd/yyyy:")
        order.addTransaction(type,category,amount,description,date)
    elif choice==2:
        totalIncome,totalExpense=order.calculateTotal()
        print("Total Income=",totalIncome,"\nTotal Expense=",totalExpense)
        order.writeTransactions()
    elif choice==3:
        order.writeTransactions()
        exit()