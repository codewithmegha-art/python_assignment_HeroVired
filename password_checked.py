import re 

def check_password(password):
     """
    Checks if the password meets the following criteria:
    - At least 8 characters long
    - Contains both uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character
    """
    
     errors = []
     
     if len(password) < 8 :
         errors.append("❌ Password must be at least 8 characters long.")
     if not re.search(r'[A-Z]' , password):
           errors.append("❌ Password must contain at least one uppercase letter.")
     if not re.search(r'[a-z]' , password):
          errors.append("❌ Password must contain at least one lowercase letter.")
     if not re.search(r'\d' , password):
         errors.append("❌ Password must contain at least one digit.")
     if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("❌ Password must contain at least one special character.") 
        
     if errors : 
         for error in errors:
             print(error)
         return False 
     
     
     return True 
 
 
#  Script Excution 

if __name__  == "__main__":
    user_password = input("Enter your password : ")
    
    if check_password(user_password):
         print("✅ Password is strong!")
         
    else : 
         print("⚠️ Please try again with a stronger password.")
        
        
        
    
   
    
    