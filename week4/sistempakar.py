import ipywidgets as widgets
from ipywidgets import Button, Checkbox, FloatText

# Hierarki atau tree dari penyakit gastro usus
bagansakit: list[list[int]] = [
    [0, 1, 2, 3, 9],  # 20,21,22,23,29
    [0, 1, 2, 4, 10],  # 20,21,22,24,30
    [0, 1, 2, 5, 6, 9],  # 20,21,22,25,26,29
    [1, 7, 11],  # 21,27,31
    [8, 2, 5, 12],  # 28,22,25,32
]


bagangejala: list[list[int]] = [
    [1, 2, 4, 5],  # 0
    [4, 5, 6],  # 1
    [4, 7],  # 2
    [4, 8, 9],  # 3
    [8, 10],  # 4
    [4, 5, 9, 11],  # 5
    [4, 8, 11, 12],  # 6
    [4, 13],  # 7
    [1, 2, 3, 4],  # 8
    [14, 15],  # 9
    [14, 16],  # 10
    [14, 17],  # 11
    [18, 19],  # 12
]

penyakit: list[str] = [
    "Staphylococcus aureus",
    "Jamur beracun",
    "Salmonellae",
    "Clostridium botulinum",
    "Campylobacter",
]


# tampilan form gejala
txtgejala: list[str] = [
    "1. Sering mengalami buang air besar (> 2 kali)?",
    "2. Mengalami berak encer?",
    "3. Mengalami berak berdarah?",
    "4. Merasa lesu dan tidak bergairah?",
    "5. Tidak selera makan?",
    "6. Merasa mual dan sering muntah (lebih dari 1 kali) ?",
    "7. Merasa sakit di bagian perut ?",
    "8. Tekanan darah anda rendah ?",
    "9. Anda merasa pusing ?",
    "10. Anda mengalami pingsan ?",
    "11. Suhu badan anda tinggi ?",
    "12. Mengalami luka di bagian tertentu ?",
    "13. Tidak dapat menggerakkan anggota badan tertentu ?",
    "14. Pernah memakan sesuatu ?",
    "15. Memakan daging ?",
    "16. Memakan jamur ?",
    "17. Memakan makanan kaleng ?",
    "18. Membeli susu ?",
    "19. Meminum susu ?",
]
var: dict[int, Checkbox] = {}
for i, txt in enumerate(txtgejala):
    var[i] = widgets.Checkbox(
        value=False, description=txtgejala[i], disabled=False, indent=False
    )
    # display(var[i])

threshold: FloatText = widgets.FloatText(
    value=20, description="Th(%): ", disabled=False
)

threshold.layout = widgets.Layout(width="150px")
# display(threshold)


persentase_bagansakit: list[float] = [100 / len(sakit) for sakit in bagansakit]
persentase_bagangejala: list[list[float]] = [
    [
        persentase_bagansakit[i] / len(bagangejala[bagansakit[i][j]])
        for j in range(len(bagansakit[i]))
    ]
    for i in range(len(persentase_bagansakit))
]


def proses(self):
    results: list[float] = [float(0) for _ in bagansakit]
    answer_keys: list[int] = []
    answers: dict[int, bool] = {}
    i: int = 0

    while i < len(var):
        answers[i] = bool(var[i].value)
        i += 1

    for key, value in answers.items():
        if value:
            answer_keys.append(key + 1)

    for answer_key in answer_keys:
        for i, sakit in enumerate(bagansakit):
            for j, gejala in enumerate(sakit):
                if answer_key in bagangejala[gejala]:
                    results[i] += persentase_bagangejala[i][j]

    for i, result in enumerate(results):
        print(f"{penyakit[i] }: {result}%")

    print(f"Anda terkena penyakit: {penyakit[results.index(max(results))]}")


button: Button = widgets.Button(
    description="Proses",
    disabled=False,
    button_style="success",
    tooltip="Proses Gejala Gastro-Usus",
)
# display(button)
button.on_click(proses)
