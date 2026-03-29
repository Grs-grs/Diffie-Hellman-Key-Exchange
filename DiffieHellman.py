import math
from user import Person

class DiffieHellman():
    def generate_public_key(self, private_secret: int, g:int, p:int) -> int:
        public = int(math.pow(g,private_secret) % p)
        return public

    def generate_shared_secret(self, other_user_public_value: int , private_secret:int, p:int):
        shared_secret = int(math.pow(other_user_public_value,private_secret) % p)
        return shared_secret
    

def main():
    diffie = DiffieHellman()
    p = int(input("Enter the public prime number (p): "))
    g = int(input("Enter the public base (g): "))
    user_1 = Person()
    user_2 = Person()
    
    # Set the first user
    user_1.name = input("Enter the first one name's: ")
    user_1.private_secret = (int(input(f"Enter {user_1.name}'s private secret: ")))

    # Set the second user
    user_2.name = input("Enter the second one name's: ")
    user_2.private_secret = (int(input(f"Enter {user_2.name}'s private secret: ")))

    # generating both their public key
    user_1.public_value = diffie.generate_public_key(user_1.private_secret, g,p)
    user_2.public_value = diffie.generate_public_key(user_2.private_secret,g,p)

    # generating both their shared_secret
    user_1.shared_secret = diffie.generate_shared_secret(user_2.public_value, user_1.private_secret, p)
    user_2.shared_secret = diffie.generate_shared_secret(user_1.public_value, user_2.private_secret, p)
    


    print(f"\n{user_1.name}'s public key: {user_1.public_value}")
    print(f"{user_2.name}'s public key: {user_2.public_value}")

    print(f"\n{user_1.name}'s shared secret: {user_1.shared_secret}")
    print(f"{user_2.name}'s shared secret: {user_2.shared_secret}")

    if user_1.shared_secret == user_2.shared_secret:
        print("\nKey exchange successful: both shared secrets match.")
    else:
        print("\nSomething went wrong: the shared secrets do not match.")

if __name__ == '__main__':
    main()