class BankAccount:
	ROI = 10.5;
	def __init__(self, Name, Amount):
		self.Name =Name;
		self.Amount =Amount;

	def Deposit(self,value):
		self.Amount = self.Amount + value;

	def Withdraw(self,value):
		self.Amount = self.Amount - value;
	
	def CalculateIntrest(self):
		print("Intrest is : ",self.Amount*BankAccount.ROI)

	def Display(self):
		print(self.Name);
		print(self.Amount);	
		print()

def main():
	obj1 = BankAccount("Amar",2000);
	obj1.Display()
	obj1.CalculateIntrest()

	obj2 = BankAccount("Sagar",5000);
	obj2.Display()
	obj2.CalculateIntrest()
	
	obj1.Deposit(500);
	obj2.Deposit(500);
	obj1.Display()
	obj2.Display()

	obj1.Withdraw(200);
	obj2.Withdraw(300);
	obj1.Display()
	obj2.Display()

if __name__ == "__main__":
	main();