import math
import numpy as np

# Mạng Nơ-ron với các phép toán trên ma trận

INPUT_LAYER_SIZE = 1
HIDDEN_LAYER_SIZE = 2
OUTPUT_LAYER_SIZE = 2

def init_weights():
    Wh = np.random.randn(INPUT_LAYER_SIZE, HIDDEN_LAYER_SIZE) * \
                np.sqrt(2.0/INPUT_LAYER_SIZE)
    Wo = np.random.randn(HIDDEN_LAYER_SIZE, OUTPUT_LAYER_SIZE) * \
                np.sqrt(2.0/HIDDEN_LAYER_SIZE)


def init_bias():
    Bh = np.full((1, HIDDEN_LAYER_SIZE), 0.1)
    Bo = np.full((1, OUTPUT_LAYER_SIZE), 0.1)
    return Bh, Bo

def relu(Z):
    return np.maximum(0, Z)

def relu_prime(Z):
    '''
    Z - ma trận đầu vào đã được đánh trọng số

    Trả về gradient của Z với
    các giá trị âm được gán bằng 0 và
    các giá trị dương được gán bằng 1
    '''
    Z[Z < 0] = 0
    Z[Z > 0] = 1
    return Z

def cost(yHat, y):
    cost = np.sum((yHat - y)**2) / 2.0
    return cost

def cost_prime(yHat, y):
    return yHat - y

def feed_forward(X):
    '''
    X    - Ma trận đầu vào
    Zh   - Đầu vào được đánh trọng số qua tầng ẩn
    Zo   - Kết quả đánh trọng số qua tầng đầu ra
    H    - Đầu ra kích hoạt tầng ẩn
    yHat - Kết quả dự đoán ở tầng đầu ra
    '''

    # Tầng ẩn - Hidden layer
    Zh = np.dot(X, Wh) + Bh
    H = relu(Zh)

    # Tầng đầu ra - Output layer
    Zo = np.dot(H, Wo) + Bo
    yHat = relu(Zo)
    return yHat

def backprop(X, y, lr):

    yHat = feed_forward(X)

    # Layer Error
    Eo = (yHat - y) * relu_prime(Zo)
    Eh = np.dot(Eo, Wo.T) * relu_prime(Zh)

    # Cost derivative for weights
    dWo = np.dot(H.T, Eo)
    dWh = np.dot(X.T, Eh)

    # Cost derivative for bias
    dBo = np.sum(Eo, axis=0, keepdims=True)
    dBh = np.sum(Eh, axis=0, keepdims=True)

    # Update weights
    Wo -= lr * dWo
    Wh -= lr * dWh

    # Update biases
    Bo -= lr * dBo
    Bh -= lr * dBh
