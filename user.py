class User:
   '''
   Class that generates new instances of users
   '''
   user_list = [] #Empty user list

#    def __init__(self,first_name , last_name):
#        '''
#        init method to create instances of the user class
#        Args:
#            first_name: New User.first_name
#            last_name: New user.last_name
#        '''
#        self.first_name = first_name
#        self.last_name = last_name

   def save_user(self):
       '''
       save_user method to save new users into user_list
       '''
       User.user_list.append(self)

   def delete_user(self):
       '''
       delete method to delete saved user from the user list
       '''
       User.user_list.remove(self)

   @classmethod
   def display_users(cls):
       '''
       method that returns the user list
       '''
       return cls.user_list
       main()