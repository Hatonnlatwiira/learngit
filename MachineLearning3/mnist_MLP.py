import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier

print(__doc__)

X, Y = fetch_openml("mnist_784", version=1, return_X_y=True)
X = X / 255

x_train, x_test = X[:60000], X[60000:]
y_train, y_test = Y[:60000], Y[60000:]

mlp = MLPClassifier(hidden_layer_sizes=(250, 200, 150, 100, 50), max_iter=400, alpha=1e-4, activation='relu', solver='sgd',
                    verbose=10, tol=1e-4, random_state=1, learning_rate_init=.1)
mlp.fit(x_train, y_train)
print("Training set score: %f" % mlp.score(x_train, y_train))
print("Test set score: %f" % mlp.score(x_test, y_test))

fig, axes = plt.subplots(10, 10)
vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
show = zip(mlp.coefs_[0].T, axes.ravel())
for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=.5 * vmin, vmax=.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
