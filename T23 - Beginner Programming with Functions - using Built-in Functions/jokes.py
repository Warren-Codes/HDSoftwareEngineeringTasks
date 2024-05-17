# This file uses the random module to print a joke at random each time the program runs.

# The random module is imported to use random.choices later
import random

# These jokes were found on https://parade.com/1040121/marynliles/one-liners/
# List of jokes to be called on
jokes = ["I heard there were a bunch of break-ins over at the car park. That is wrong on so many levels.",
         "I want to die peacefully in my sleep, like my grandfather… Not screaming and yelling like the passengers "
         "in his car.",
         "When life gives you melons, you might be dyslexic.",
         "Don’t you hate it when someone answers their own questions? I do.",
         "It takes a lot of balls to golf the way I do.",
         "I told him to be himself; that was pretty mean, I guess.",
         "I know they say that money talks, but all mine says is ‘Goodbye.’",
         "My father has schizophrenia, but he’s good people.",
         "The problem with kleptomaniacs is that they always take things literally.",
         "I can’t believe I got fired from the calendar factory. All I did was take a day off.",
         "Most people are shocked when they find out how bad I am as an electrician.",
         "Never trust atoms; they make up everything."]



# random.choic(jokes) will choice an item in the list at random and print it.
print(random.choice(jokes))
