import numpy as np

X = np.random.uniform(-1, 1, (10, 2))

p1 = np.random.uniform(-1, 1, 2)
p2 = np.random.uniform(-1, 1, 2)

def get_label(x):
    side = ((p2[0] - p1[0]) * (x[1] - p1[1])
            - (p2[1] - p1[1]) * (x[0] - p1[0]))
    return 1 if side >= 0 else -1

y = np.array([get_label(x) for x in X])

# training
def train_perceptron(X, y, alpha=1):
    X_aug = np.column_stack((np.ones(len(X)), X))
    w = np.zeros(3)
    steps = 0

    while True:
        predictions = np.where(X_aug @ w >= 0, 1, -1)
        wrong = np.where(predictions != y)[0]

        if len(wrong) == 0:
            break

        i = np.random.choice(wrong)
        w += alpha * (y[i] - predictions[i]) * X_aug[i]

        steps += 1
    return steps

results = []

for _ in range(1000):
    steps = train_perceptron(X, y, alpha=1)
    results.append(steps)

average = np.mean(results)

print("Durchschnittliche Schritte:", average)

# experimente
for m in [100, 1000]:

    X_exp = np.random.uniform(-1, 1, (m, 2))
    y_exp = np.array([get_label(x) for x in X_exp])

    for alpha in [1, 0.1]:
        results = []
        for _ in range(1000):
            steps = train_perceptron(X_exp, y_exp, alpha)
            results.append(steps)

        average = np.mean(results)

        print(f"m={m}, alpha={alpha}: {average:.2f} Schritte")