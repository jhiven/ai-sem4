man(oscar).
woman(antje).

person(X):- man(X) | woman(X).
    
married(oscar, antje).
married(antje, oscar).

father(bernd, oscar).
mother(bernd, antje).

aunt(susi, antje).
uncle(susi, oscar).

cousin(bernd, susi).
cousin(susi, bernd).
