import numpy as np
from numpy._typing import NDArray

from centroid import Centroid
from gpa import GPA
from gre import GRE


# RULE
def hitung_u(gre_test: GRE, gpa_test: GPA):
    u_Status = np.empty(9, dtype=float)
    u_Status[0] = min(gre_test.high(), gpa_test.high())  # Sangat Sehat
    u_Status[1] = min(gre_test.medium(), gpa_test.high())  # Sehat
    u_Status[2] = min(gre_test.low(), gpa_test.high())  # Agak Sehat
    u_Status[3] = min(gre_test.high(), gpa_test.medium())  # Tidak Sehat
    u_Status[4] = min(gre_test.medium(), gpa_test.medium())  # Tidak Sehat
    u_Status[5] = min(gre_test.low(), gpa_test.medium())  # Sehat
    u_Status[6] = min(gre_test.high(), gpa_test.low())  # Sangat Sehat
    u_Status[7] = min(gre_test.medium(), gpa_test.low())  # Sehat
    u_Status[8] = min(gre_test.low(), gpa_test.low())  # Agak Sehat

    return u_Status


# Max Method
def max_method(u_Status: NDArray, z_Status: list[str]):
    status = ""
    max = 0
    for i in range(len(u_Status)):
        if max < u_Status[i]:
            max = u_Status[i]
            status = z_Status[i]

    return max, status


def centroid_method(u_Status: NDArray, z_Status: list[str]):
    centroid = {
        "Poor": 65,
        "Fair": 70,
        "Good": 80,
        "Very Good": 90,
        "Excellent": 95,
    }

    cdi = 0
    hasil = np.empty(len(centroid), dtype=float)

    for i, value in enumerate(u_Status):
        cdi += value * centroid[z_Status[i]]

    cdi /= sum(u_Status)

    centroid_test = Centroid(cdi)

    hasil[0] = centroid_test.poor()
    hasil[1] = centroid_test.fair()
    hasil[2] = centroid_test.good()
    hasil[3] = centroid_test.verygood()
    hasil[4] = centroid_test.excellent()

    centroid_status = list(centroid.keys())[np.argmax(hasil)]

    return max(hasil), centroid_status


def run():
    z_Status = [
        "Excellent",
        "Very Good",
        "Fair",
        "Good",
        "Good",
        "Poor",
        "Fair",
        "Poor",
        "Poor",
    ]

    gre = int(input("Masukkan nilai GRE: "))
    gpa = float(input("Masukkan nilai GPA: "))
    gpa_test = GPA(gpa)
    gre_test = GRE(gre)

    u_Status = hitung_u(gre_test, gpa_test)

    max_bobot, max_status = max_method(u_Status, z_Status)
    centroid_bobot, centroid_status = centroid_method(u_Status, z_Status)

    for index, value in enumerate(u_Status):
        print(f"u_ke-{index}, Value: {value}")

    print("\nMax Method")
    print("Bobot: ", max_bobot, "dengan status nilai: ", max_status)

    print("\nCentroid Method")
    print("Bobot: ", centroid_bobot, "dengan status nilai: ", centroid_status)


if __name__ == "__main__":
    run()
