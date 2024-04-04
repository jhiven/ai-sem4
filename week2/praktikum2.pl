laki(rudi).
laki(roy).
laki(ali).
laki(budi).
laki(sukri).
laki(jaya).

perempuan(asiah).
perempuan(uun).
perempuan(nuni).
perempuan(imas).
perempuan(siti).

suami(asiah, rudi).
suami(uun, roy).
suami(nuni, ali).
suami(imas, budi).

istri(rudi, asiah).
istri(roy, uun).
istri(ali, nuni).
istri(budi, imas).

anak(rudi, roy).
anak(roy, ali).
anak(roy, imas).
anak(ali, siti).
anak(ali, sukri).
anak(budi, jaya).

menikah(A, B):-istri(A, B) | suami(A, B).

orangtua(Anak, OrangTua):-anak(OrangTua, Anak) | menikah(OrangTua, B), anak(B, Anak).

kakek(A, K):-orangtua(A, B), orangtua(B, K), laki(K).
nenek(A, N):-orangtua(A, B), orangtua(B, N), perempuan(N).

saudara(A, S):-laki(OR), orangtua(A, OR), orangtua(S, OR), A \== S.

ipar(A, Ipar):-saudara(A, Saudara), menikah(Saudara, Ipar).

nenekmoyang(A, B):-orangtua(A, B).
nenekmoyang(Anak, Moyang):-orangtua(Anak, BC), nenekmoyang(BC, Moyang).
