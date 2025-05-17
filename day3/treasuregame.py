print("""     _            _.,----,
   __  _.-._ / '-.        -  ,._  \) 
  |  `-)_   '-.   \       / < _ )/" }
  /__    '-.   \   '-, ___(c-(6)=(6)
   , `'.    `._ '.  _,'   >\    "  )
   :;;,,'-._   '---' (  ( "/`. -='/
  ;:;;:;;,  '..__    ,`-.`)'- '--'
  ;';:;;;;;'-._ /'._|   Y/   _/' \\
        '''"._ F    |  _/ _.'._   `\\
               L    \   \/     '._  \\
        .-,-,_ |     `.  `'---,  \_ _|
        //    'L    /  \,   ("--',=`)7
       | `._       : _,  \  /'`-._L,_'-._
       '--' '-.\__/ _L   .`'         './/
                   [ (  /
                    ) `{
         snd        \__)
""")
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
user_input = input("left or right? ")
if user_input == "left":
    user_input = input("swim or wait? ")
    if user_input == "wait":
        user_input = input("Which door? Red, Yellow or Blue: ")
        if user_input == "Red":
            print("Burned by fire.\nGame Over.")
        elif user_input == "Blue":
            print("Eaten by beasts.\nGame Over.")
        elif user_input == "Yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")