from utils import naik, turun


class Centroid:

    titik1 = 0
    titik2 = 60
    titik3 = 70
    titik4 = 80
    titik5 = 90
    titik6 = 100

    def __init__(self, cdi):
        self.cdi = cdi

    def poor(self):
        if self.cdi >= self.titik1 and self.cdi <= self.titik2:
            return 1
        elif self.cdi > self.titik2 and self.cdi < self.titik3:
            return turun(self.titik2, self.titik3, self.cdi)
        else:
            return 0

    def fair(self):
        if self.cdi > self.titik2 and self.cdi < self.titik3:
            return naik(self.titik2, self.titik3, self.cdi)
        elif self.cdi is self.titik3:
            return 1
        elif self.cdi > self.titik3 and self.cdi < self.titik4:
            return turun(self.titik3, self.titik4, self.cdi)
        else:
            return 0

    def good(self):
        if self.cdi > self.titik3 and self.cdi < self.titik4:
            return naik(self.titik3, self.titik4, self.cdi)
        elif self.cdi is self.titik4:
            return 1
        elif self.cdi > self.titik4 and self.cdi < self.titik5:
            return turun(self.titik4, self.titik5, self.cdi)
        else:
            return 0

    def verygood(self):
        if self.cdi > self.titik4 and self.cdi < self.titik5:
            return naik(self.titik4, self.titik5, self.cdi)
        elif self.cdi is self.titik5:
            return 1
        elif self.cdi > self.titik5 and self.cdi < self.titik6:
            return turun(self.titik5, self.titik6, self.cdi)
        else:
            return 0

    def excellent(self):
        if self.cdi > self.titik5 and self.cdi < self.titik6:
            return naik(self.titik5, self.titik6, self.cdi)
        else:
            return 0
