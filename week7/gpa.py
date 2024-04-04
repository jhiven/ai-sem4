class GPA:

    titik1 = 0
    titik2 = 2.2
    titik3 = 3.0
    titik4 = 3.8

    def __init__(self, nilai):
        self.nilai = nilai

    def low(self):
        if self.nilai >= self.titik1 and self.nilai <= self.titik2:
            return 1
        elif self.nilai > self.titik2 and self.nilai < self.titik3:
            return (float)(self.titik3 - self.nilai) / (self.titik3 - self.titik2)
        else:
            return 0

    def medium(self):
        if self.nilai > self.titik2 and self.nilai < self.titik3:
            return (float)(self.nilai - self.titik2) / (self.titik3 - self.titik2)
        elif self.nilai >= self.titik3 and self.nilai <= self.titik4:
            return 1
        elif self.nilai > self.titik3 and self.nilai < self.titik4:
            return (float)(self.titik4 - self.nilai) / (self.titik4 - self.titik3)
        else:
            return 0

    def high(self):
        if self.nilai > self.titik3 and self.nilai < self.titik4:
            return (float)(self.nilai - self.titik3) / (self.titik4 - self.titik3)
        elif self.nilai > self.titik4:
            return 1
        else:
            return 0
