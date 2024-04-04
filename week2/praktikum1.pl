bawahanlangsung(adi, burhan).
bawahanlangsung(burhan, bahrun).
bawahanlangsung(burhan, bisrin).
bawahanlangsung(bahrun, fahri).
bawahanlangsung(bisrin, ferdi).
bawahanlangsung(bahrun, farah).

atasanlangsung(B, A):-bawahanlangsung(A, B).

anakbuah(A, B):-atasanlangsung(B, A).
anakbuah(A, B):-atasanlangsung(B, AL),anakbuah(A, AL).
