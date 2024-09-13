# class Training:
#     def __init__(self, participants, duration):
#         self.__participants = participants
#         self.__duration = duration

#     def set_duration(self, a):
#         self.__duration = a  

#     def set_participants(self, a):
#         self.__participants = a  

#     def get_participants(self):
#         return self.__participants  

#     def get_duration(self):
#         return self.__duration  

#     def Which_conduct_training(self):
#         return f"Trainig is conduct"

# class FootballTraining(Training):
#     def __init__(self, participants, duration, conduct_training):
#         super().__init__(participants, duration)
#         self.conduct_training = conduct_training

#     def Which_conduct_training(self):
#         return f"Football is {self.conduct_training}"


# class BasketballTraining(Training):
#     def __init__(self, participants, duration, conduct_training):
#         super().__init__(participants, duration)
#         self.conduct_training = conduct_training

#     def Which_conduct_training(self):
#         return f"Basketball is  {self.conduct_training}"


# class TennisTraining(Training):
#     def __init__(self, participants, duration, conduct_training):
#         super().__init__(participants, duration)
#         self.conduct_training = conduct_training

#     def Which_conduct_training(self):
#         return f"Tennis is{self.conduct_training}"

# football=FootballTraining(12,120,'conduct')
# basketball=BasketballTraining(12,120,'conduct')
# tennis=TennisTraining(2,60,' not conduct')
# print(football.Which_conduct_training())
# print(basketball.Which_conduct_training())
# print(tennis.Which_conduct_training())

# print(football.get_duration())
# football.set_duration(60)
# print(football.get_duration())


#  Bank


class BankAccount:
    def __init__(self, balance):
        self._balance = balance 
    
    def deposit(self, a):
        self._balance += a
        print('Счет пополнен')
    
    def withdraw(self, a):
        if self._balance < a:
            print('У вас недостаточно средств')
        else:
            self._balance -= a
            print('Транзакция успешно выполнена')
    
    def get_balance(self):
        return self._balance

class CurrentAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)


    def withdraw(self, a):
        self._balance -= a
        print('Транзакция успешно выполнена')


bank = CurrentAccount(100)
bank.withdraw(200)  
print(bank.get_balance())  
bank.deposit(200)   
print(bank.get_balance()) 