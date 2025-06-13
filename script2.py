class User:
  def __init__(self,username,email,password):
    self.username = username
    self._email = email
    self.password = password
    
  def get_email(self):
    return self._email

  def set_email(self,new_email):
    if "@" in new_email:
      self._email = new_email
  
  def clean_email(self):
    return self._email.lower().strip()
  
  
user1 = User("danthman","Dan@gmail.com","123")

print(user1.clean_email())