from logic import *

# Propositions
#J = Joker
#R = Riddler
#P = Penguin
#A = Acid
#C = Cards
#B = Buzzers
#U = Umbrella
#T = Tell-tale clue
#S = Street criminal
#Q = Riddle clues (word games, etc.)
# H = A hole was found

J, P, R, A, C, B, U, T, S, Q, H = vars('J', 'P', 'R', 'A', 'C', 'B', 'U', 'T', 'S', 'Q', 'H')

# Formulas

f01 = T # A tell-tale clue was found
f02 = T >> ~S # If a tell-tale clue is found, it is not a street criminal
f03 = T >> (J | R | P) # If a tell-tale clue is found, it's a supervillain
f04 = R << Q # Riddler is guilty if and only if there are riddle clues
f05 = P << U # Penguin is guilty if and only if there is an umbrella mark
f06 = J << (A | B | C) # Joker is guilty if and only if there is acid, buzzer, or cards
f07 = H     # Batman found the hole!
f08 = H >> (A | U) # The hole is from acid or umbrella


# ArgumentForms
# jokers argument form
joker_arg = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, conclusion=J)
# penguins argument form
penguin_arg = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, conclusion=P)
# riddlers argument form
riddler_arg = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, conclusion=R)
# street criminals argument form
street_arg = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, conclusion=S)


#Evaluate the argument forms
print("Who definitely committed this crime:")
#checking the low-level criminal Joker, Penguin, and Riddler argument forms
print(f"A low-level criminal: {street_arg.is_valid()}")
print(f"The Joker: {joker_arg.is_valid()}")
print(f"The Penguin: {penguin_arg.is_valid()}")
print(f"The Riddler: {riddler_arg.is_valid()}")


