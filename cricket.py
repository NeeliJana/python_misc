import sys
each_ball = []
def cricket(run):
    c_run = 0
    try:
        c_run = (input("Runs scored in this delivery-"))
        
        each_ball.append(int(c_run))
        print(each_ball)
        run =  run + int(c_run)
        print("Total Runs Till Now = ", run, ",", "Total Overs and balls = ", len(each_ball)//6, "Overs", len(each_ball)%6, "Balls")
        cricket(run)
    except ValueError:
        if str(c_run) == "exit":
            print("Exited!")
            sys.exit()

        print("Please enter numbers else enter exit to exit the code.")
        cricket(run)

def speak_balls():
    print("Remaining Balls are: ", 6-len(each_ball))
    
cricket(0)
print(each_ball)

