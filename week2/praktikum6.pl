cat(garfield).
cat(sylvestor).
canary(tweety).
penguin(opus).
dog(dog).

mammal(X):- cat(X).
mammal(X):- dog(X).

pet(X):- dog(X).
pet(X):- canary(X).
pet(X):- cat(X).

bird(X):-canary(X).
bird(X):-penguin(X).

animal(X):- mammal(X).
animal(X):- bird(X).

has(X, tail):-mammal(X).
has(X, tail):-bird(X).
has(X, wing):-bird(X).
has(X, feather):-bird(X).

eat(X, cat_food):- cat(X).
eat(garfield, lasagna).
eat(X, seeds):- bird(X).

can(X, fly):- bird(X), \+ cannot(X, fly).
cannot(opus, fly).