# DiceTests
code for testing random number generation in python


I started out building a DnD character generator for exercism.io, but started wondering about the distributions.
(https://exercism.io/my/solutions/7efc10b6213542a49a51019c4e10a487)

The initial code was for doing a 4d6 roll with a discard of the lowest value, but it can be used for any number of dice/sides/discards.


This repo has experiments on how to make life-like dice rolling, plus investigation into how the random number generator works.

File naming convention:

dice_rolls [number of dice] [dice sides] [how many low numbers to discard]_ [number of cycles of generation].csv
