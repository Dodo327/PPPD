import numpy as np
from sklearn import datasets, svm
import math

def F(a, b):
    """
    Nie interesuje nas, co funkcja robi:
    traktujemy ja jako "czarna skrzynke".
    Wazne jest jedynie to, ze F(a, b) zwraca wartość z przedzialu [0,1]
    dla a, b > 0
    Przykład inspirowany http://scikit-learn.org/stable/auto_examples/
    exercises/plot_iris_exercise.html
    """
    iris = datasets.load_iris() # zbior iris
    X, y = iris.data, iris.target
    X, y = X[y != 0, :2], y[y != 0] # tylko klasy 1 i 2
    n_sample = len(X)
    np.random.seed(1234)
    order = np.random.permutation(n_sample)
    X = X[order]
    y = y[order].astype(np.float)
    X_train = X[:int(0.8 * n_sample)] # proba uczaca = losowe 80%
    y_train = y[:int(0.8 * n_sample)]
    X_test = X[int(0.8 * n_sample):] # proba testowa = pozostale 20%
    y_test = y[int(0.8 * n_sample):]
    clf = svm.SVC(gamma=a, C=b) # support vector classifier
    1
    clf.fit(X_train, y_train)
    
    return np.mean(clf.predict(X_test) == y_test) # accuracy, wartość z [0,1]

def main():
    with open("input.txt") as input_file:
        a_1 = float(input_file.readline())
        a_n = float(input_file.readline())
        n = int(input_file.readline())
        b_1 = float(input_file.readline())
        b_m = float(input_file.readline())
        m = int(input_file.readline())

    if a_n < a_1 or b_m < b_1 or n < 1 or m < 1:
        raise ValueError("Błędne dane")

    with open("output.txt", 'w') as output_file:
        f_max = 0
        f_min = math.inf

        for i in range(n):
            a_i = a_1 * (i + 1)
            for j in range(m):
                b_j = b_1 * (j + 1)
                f = F(a_i, b_j)
                output_file.write(str(f))
                output_file.write(' ')
                if f > f_max:
                    f_max = f
                    a_max = a_i
                    b_max = b_j
                if f < f_min:
                    f_min = f
                    a_min = a_i
                    b_min = b_j

            output_file.write('\n')
    print(f"Wartosc najwieksza rowna {f_max} dla a, b = ({a_max, b_max})")
    print(f"Wartosc najmniejsza rowna {f_min} dla a, b = ({a_min, b_min})")


if __name__ == '__main__':
    main()
