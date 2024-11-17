#/ Match is similar to the match
#/Write a program to ask the user which browser he wants to run automation
browser_name=input("Enter the browser name:\n")
match browser_name:
     case "firefox":
         print("Starting firefox browser !!!")
     case "edge":
         print("Starting edge browser !!!")
     case "chrome":
         print("Starting chrome browser !!!")
     case "safari":
         print("Starting safari browser !!!")
     case _:
         print("Browser Not found !!!")
