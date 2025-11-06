from datetime import datetime

class Account:
    """Класс пользователя с основными методами списаний, пополнений, проверки баланса и проверкой истории операций"""

    #конструктор
    def __init__(self, name, balance, currency):
        #ниже все атрибуты экземпляра
        self.name = name
        self.balance = balance
        self.currency = currency
        self.transactions = []
        self.created_at = datetime.now()

    #метод пополнения
    def deposit(self, amount, description=""):
        transaction_data = {
            "type":"deposit",
            "amount":amount,
            "description":description,
            "date":datetime.now(),
        }
        
        if amount <= 0:
            transaction_data["status"] = "ERROR"
            transaction_data["error"] = "Сумма должна быть положительной"
            self.transactions.append(transaction_data)
            return False 
        else:
            self.balance += amount
            transaction_data["status"] = "SUCCESS"
            transaction_data["new_balance"] = self.balance
            self.transactions.append(transaction_data)
            return True

    #метод списаний    
    def withdraw(self, amount, description=""):
        transaction_data = {
            "type":"withdraw",
            "amount":amount,
            "description":description,
            "date":datetime.now(),
        }
        
        if amount <= 0:
            transaction_data["status"] = "ERROR"
            transaction_data["error"] = "Сумма должна быть положительной"
            self.transactions.append(transaction_data)
            return False
        elif self.balance < amount:
            transaction_data["status"] = "ERROR"
            transaction_data["error"] = "Недостаточно средств"
            transaction_data["current_balance"] = self.balance
            self.transactions.append(transaction_data)
            return False
        else:
            self.balance -= amount
            transaction_data["status"] = "SUCCESS"
            transaction_data["new_balance"] = self.balance
            self.transactions.append(transaction_data)
            return True
    
    #метод получения баланса
    def get_balance(self):
        return self.balance
     
    #метод получения истории операций
    def get_transaction_history(self):
        return self.transactions


#for i, tx in enumerate(test.get_transaction_history(), 1):
#    status = "✅" if tx["status"] == "SUCCESS" else "❌"
#    print(f"{i}. {status} {tx['type']}: {tx['amount']} - {tx['description']}")
#    if tx["status"] == "ERROR":
#        print(f"   Ошибка: {tx['error']}")
