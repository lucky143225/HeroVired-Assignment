"""importing Regular expression operations"""
import re

def check_password_strength(password):
    """
    Checks the strength of the password based on given criteria:
    - Minimum length of 8 characters
    - Contains both uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character
    """
    missing_criteria = []
    
    if len(password) < 8:   
        missing_criteria.append("Minimum length of 8 characters")
    if not re.search(r"[A-Z]", password):    #searching for upper case 
        missing_criteria.append("At least one uppercase letter")
    if not re.search(r"[a-z]", password):    #searching for Lower case 
        missing_criteria.append("At least one lowercase letter")
    if not re.search(r"\d", password):  #searching for single sigit
        missing_criteria.append("At least one digit")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):    #searching for special character 
        missing_criteria.append("At least one special character")
    
    is_strong = len(missing_criteria) == 0
    return is_strong, missing_criteria

def main():
    password = input("Enter your password to check its strength: ")
    
    is_strong, missing_criteria = check_password_strength(password)
    
    if is_strong:
        print("Your password is strong.")
    else:
        print("Your password is not strong enough.")
        print("The following criteria are missing:")
        for criteria in missing_criteria:
            print(f"- {criteria}")

if __name__ == "__main__":
    main()

