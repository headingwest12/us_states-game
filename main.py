import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
guessed_states_list = []
score = 0
attempt = 0
FONT = ("Courier", 10, "normal")
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
print(data["x"])
# data = {"":[0123], "state":[ohio , arizona,....]}

all_states = data["state"].to_list()
while score < 50:
    guess = screen.textinput(title=f"{score}/50 correct states.", prompt="What's another state name.").title()

    if guess in all_states:
        score += 1
        correct_guess = turtle.Turtle()
        correct_guess.penup()
        correct_guess.hideturtle()
        state_data = data[data["state"] == f"{guess}"]
        correct_guess.goto(x=int(state_data["x"]), y=int(state_data["y"]))
        correct_guess.write(f"{guess}", align="center", font= FONT)

        guessed_states_list.append(guess)
    else:
        attempt +=1
    if attempt > 10 or guess == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states_list]

        score = 51
# screen.mainloop()
data_dict = {
    "State": missed_states
}
print(missed_states)
df = pandas.DataFrame(data_dict)
df.to_csv("learn.csv")

# screen.exitonclick()
