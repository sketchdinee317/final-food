#Admin will have the following functionalities:
def processOrder(quantity, item_list):
    global total
    if quantity > item_list[2]:
        print("There is not enough stock!")
        pass
    else:
        total += item_list[1] * quantity
        item_list[2] -= quantity


total = 0
A = ["Burger", int(150), 50], ["juice", int(50), 200], ["pizaa", int(200), 20]

print("Welcome to McDonald's")
print("[1]", A[0][0:2],
      "\n[2]", A[1][0:2],
      "\n[3]", A[2][0:2])

order = []
more_items = 'yes'
while more_items == 'yes':
    choice, quantity = int((input("\nWhat would you like?\n"))), int(input("\nHow many quantity like?\n"))
    if 1 <= choice <= 3:
        processOrder(quantity, A[choice - 1])
        order.append([choice-1, quantity]) # added - append the order with the current position
    more_items = (input("Do you want to order more items?")).lower()
print("Thank you for ordering!\nYour total cost is: $" + str(total))
print('Order list:')
for el in order:
    print(f'Position: {A[el[0]][0]}, quantity: {el[1]}, cost: {A[el[0]][1]*el[1]}')

# Log in to the application
class user:
    user_id = 2911
    users = []
    
    def __init__(self,full_name,phone,email,address,password):
        self.id = user.user_id
        self.full_name = full_name
        self.phone = phone
        
# The user will see 3 options:
       # 🔴 Place New Order
        #🔴 Order History
        #🔴 Update Profile
        
class user:
    user_id = 2911
    users = []
    
    def __init(self,full_name,phone,email,address,password):
        self.id = user.user_id
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.address = address
        self.password = password
        user.users.append(self)
        user.user_id += 1
        
        user1 = user("dinesh",78908541,"dinesh@gmail.com","banglore","otp")
        user2 = user("kumar",89064214,"kumar@gmail.com","chennai","pto")
        
        print(user1.id)
        print(user1.full_name)
        print(user1.phone)
        print(user1.email)
        print(user1.address)
        print(user1.password)
        
        
#Once the items are selected user should see the list of all the items selected. The user will also get an option to place an order.
        def new_order(food_items):
            food_item_id = [int(x) for x in input("Enter a list food id(2:3): ").split()]
            selected_food_items = [food_item_id - 1] for food_item_id in food_item_id]
           print("selected food items:")
           for i,food_item in enumerate(selected_food_items):
               print(f"{i +1}.{food_item.name} ({food_item.quantity}) {food_item.price}]")
               
               confirm_order = input("place order" (y/n): ")
                if confirm_order.lower() =="y":
                    order = order(selected_food_items)
                    return order
                else:
                    return none
                
                order = new_order(food_item)
                if order is not none:
                    print("order place:" order.food_items)
                else:
                    print("order is cancelled.")
#Order History should show a list of all the previous orders
class user:
    def __init__(self,name,phone_number,email,address,password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order = []
        
        def new_order(self,order):
            self.order.append(order)
            
      def view_order_history(self):
          print("order is history")
          for i,order in enumerate(self.order):
              print(f" order {i +1}: {order.food_items})
                
                    
            user = user("dinesh","987665424","dinesh@gmail.com","banglore","otp")
            order = order([food_items[0], food_items[2]])
            user.place_order(order)
            user.view_order_history()
            
  # Update Profile: the user should be able to update their profile.
  class user:
      def __init__(self,name,phone_number,email,address,password):
          self.name = name
          self.phone_number = phone_number
          self.email = email
          self.address = address
          self.password = password
          self.order = []
          
          def new_order(self,order):
              self.order.append(order)
              
        def view_order_history(self):
            print("order is history")