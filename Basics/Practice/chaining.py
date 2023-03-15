class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0 

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)

# !!!!To make prettier, i can do print(f"(key, ex. First Name:) {self.(key, ex: first_name)}"")
# EXAMPLE:  print(f"First Name: {self.first_name}")


    def enroll(self):
        # BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.
# SOLUTION IS FROM SOLUTIONS VIDEO, I'M USING IT TO LEARN AND DON'T PASS THIS AS MY OWN CODE
#       if self.is_rewards_member:
            # print("User already member")
            # return false
        self.is_reward_member = True
        self.gold_card_points = 200



    def spend_points(self, gold_card_points, amount):
# SOLUTION IS FROM SOLUTIONS VIDEO, I'M USING IT TO LEARN AND DON'T PASS THIS AS MY OWN CODE
# BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.
#       if self.gold_card_points < amount:
            # print("Unable to process")
        self.gold_card_points = (gold_card_points - amount)
        print(self.gold_card_points)

# Should do:
# def spend_points(self, amount):
#     self.gold_card_points = self.gold_card_points - amount, or -= amount


Sonia = User("Sonia", "M", "sonia.m@gmail.com", 33)
Sonia.display_info().enroll().is_reward_member().gold_card_points()

Sam = User("Sam", "Smith", "s.smith@gmail.com", 33)
Sam.display_info().enroll().is_reward_member().gold_card_points().spend_points(200,50)


Abby = User("Abby", "Reyes", "abby.reyes@gmail.com", 35)
Abby.display_info().enroll().is_reward_member().gold_card_points().spend_points(200,80)


https://login.codingdojo.com/m/506/12458/87326

