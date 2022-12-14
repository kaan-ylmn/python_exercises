import time

class Computer():
    def __init__(self,user_name = "user ",state = "close", sound = 0 ,apps = []):
        self.user_name = user_name
        self.state = state
        self.sound = sound
        self.apps = apps

    def closing_pc(self):
        if self.state == "close":
            return "The computer system is already closed"
        else:
            time.sleep(2)
            return f"The computer system is closing ...\nGoodbye {self.user_name}!"

    def opening_pc(self):            
        if self.state == "close":
            return "The computer system is already open"
        else:
            time.sleep(2)
            return f"The computer is opening...\nWelcome {self.user_name}!"

    def enter_username(self,username):
        self.user_name = username
        return f"Your username is {self.user_name}"

    def show_username(self):
        return self.user_name

    def volume(self, process):
        if process == "+":
            if self.sound < 100:
                self.sound += 5
                return f"Volume {self.sound}"
            else:
                return "The volume is maximum 100"

        if process == "-":
            if self.sound > 0:
                self.sound -= 5
                return f"Volume {self.sound}"
            else:
                return "The volume is minimum 0"                

    def show_volume(self):
        return self.sound

    def showing_apps(self):
        return self.apps

    def adding_apps(self,new_app):
        print("New apps are adding...\nIt takes a few time...\n")
        for app in new_app:
            self.apps.append(app)
        time.sleep(2)
        for added_app in self.apps:
            print(f"{added_app} is added...")

    def removing_app(self,app_name):
        if len(self.apps) == 0:
            return "There is no apps in the computer system. First add app please!.."
        
        else:
            print(f"{app_name} is removing...\n It takes a few time...")
            self.apps.remove(app_name)
            time.sleep(2)
            return f"Process is successfully done..."    

computer = Computer()

print("""
    Welcome to Computer Program

1- Open computer

2- Close computer

3- Entering username

4- Show username
 
5- Volume settings

6- Show apps

7- Add apps

8- Delete app
""")

while True:
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        print(computer.opening_pc())
    elif choice == 2:
        print(computer.closing_pc())
        break   
    elif choice == 3:
        username = input("Enter a username: ")
        print(computer.enter_username(username))
    elif choice == 4:
        print(computer.show_username())
    elif choice == 5:
        print("Press q to exit from this panel...")
        while True:
            volume = input(f"\nCurrent volume is {computer.show_volume()}\nWould you like to increase or decrease volume: ")
            if not(volume == "q"):
                print(computer.volume(volume))
            else:
                print("Volume Settings are closing...")
                time.sleep(1)
                break
    elif choice == 6:                    
        print(f"Current apps in the computer system {computer.showing_apps()}")
    elif choice == 7:     
        app_list = list(map(str,input("Enter apps: ").split()))
        computer.adding_apps(app_list)
    elif choice == 8: 
        while True:
            print("Press q for leave this menu")
            remove_app = input(f"Current apps in the computer system {computer.showing_apps()}\nEnter a app which one you want to delete: ")
            if remove_app == "q":
                break
            else:
                print(f"Are you sure about deleting {remove_app} app ?")
                confirm = input("YES/NO : ")
                if confirm == "YES":
                    print(computer.removing_app(remove_app))
                else:
                    break
    else:                                 
        print("Invalid transaction")                             
    