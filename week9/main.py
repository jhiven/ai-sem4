import pandas as pd
import numpy as np


def find_s(train, target):
    hyphotesis = train[0]

    for i, val_train in enumerate(train):
        if target[i] == "Yes":
            for j in range(len(hyphotesis)):
                if val_train[j] != hyphotesis[j]:
                    hyphotesis[j] = "?"

    return hyphotesis


def main():
    dataset = pd.read_csv("./sport.csv")

    data_training = np.array(dataset)[:, 1:-1]
    target = np.array(dataset)[:, -1]

    print(find_s(data_training, target))

    # print(dataset)
    # print(data_training)
    # print(target)


if __name__ == "__main__":
    main()
