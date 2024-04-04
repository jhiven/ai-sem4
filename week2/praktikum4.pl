lulusan_sd(anas).
wni(anas).
lahir(anas, 1962).
tahun_sekarang(2023).
daftar_pns(anas, 1990).

usia(X, AGE):-lahir(X, BIRTH), tahun_sekarang(Y), AGE is (Y-BIRTH).

tidak_dapat_menjadi_pns_lagi(X):-wni(X), lulusan_sd(X),usia(X, AGE), AGE > 35.

apakah_pensiun(X):-usia(X, AGE), AGE >= 60.