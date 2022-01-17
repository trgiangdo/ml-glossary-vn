import numpy as np
from matplotlib import pyplot as plt
from .activation_functions import sigmoid, sigmoid_prime


def predict(features, weights):
    '''
    Trả về một mảng 1D là các xác suất
    mà nhãn danh mục đó == 1
    '''
    z = np.dot(features, weights)
    return sigmoid(z)


def cost_function(features, labels, weights):
    '''
    Sử dụng MAE (Mean Absolute Error)

    Features:(100,3)
    Labels: (100,1)
    Weights:(3,1)

    Trả về mảng 1D các dự đoán
    cost = (labels*log(predictions) + (1-labels)*log(1-predictions) ) / len(labels)
    '''

    # Số quan sát trong tập dữ liệu
    observations = len(labels)

    predictions = predict(features, weights)

    # Tính sai số nếu nhãn = 1
    class1_cost = -labels*np.log(predictions)

    # Tính sai số nếu nhãn = 1
    class2_cost = (1-labels)*np.log(1-predictions)

    # Tính tổng của cả 2 loại sai số
    cost = class1_cost - class2_cost

    # Tính trung bình lỗi làm chi phí
    cost = cost.sum() / observations

    return cost


def update_weights(features, labels, weights, lr):
    '''
    Thuật toán Hạ Gradient được vector hoá

    Features:(200, 3)
    Labels: (200, 1)
    Weights:(3, 1)
    '''
    N = len(features)

    #1 - Dự đoán kết quả
    predictions = predict(features, weights)

    #2 -  Chuyển vị ma trận đặc trưng từ kích thước (200, 3) về (3, 200)
    # để ta có thể nhân với ma trận sai số (200,1).
    # Trả về một ma trận (3,1) gồm có 3 đạo hàm riêng -
    # mỗi đạo hàm cho một đặc trưng -- đại diện cho tổng
    # độ nghiêng của hàm chi phí qua tất cả các quan sát.
    gradient = np.dot(features.T,  predictions - labels)

    #3 - Tính trung bình đạo hàm của hàm chi phí với mỗi đặc trưng
    gradient /= N

    #4 - Nhân gradient với tốc độ học
    gradient *= lr

    #5 - Cập nhật trọng số bằng cách trừ đi gradient để tối thiểu hoá chi phí
    weights -= gradient

    return weights


def decision_boundary(prob):
  return 1 if prob >= .5 else 0


def classify(predictions):
  '''
  input  - N element array of predictions between 0 and 1
  output - N element array of 0s (False) and 1s (True)
  '''
  decision_boundary = np.vectorize(decision_boundary)
  return decision_boundary(predictions).flatten()


def train(features, labels, weights, lr, iters):
    cost_history = []

    for i in range(iters):
        weights = update_weights(features, labels, weights, lr)

        #Calculate error for auditing purposes
        cost = cost_function(features, labels, weights)
        cost_history.append(cost)

        # Log Progress
        if i % 1000 == 0:
            print("iter: "+str(i) + " cost: "+str(cost))

    return weights, cost_history


def accuracy(predicted_labels, actual_labels):
    diff = predicted_labels - actual_labels
    return 1.0 - (float(np.count_nonzero(diff)) / len(diff))


def plot_decision_boundary(trues, falses):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    no_of_preds = len(trues) + len(falses)

    ax.scatter([i for i in range(len(trues))], trues, s=25, c='b', marker="o", label='Trues')
    ax.scatter([i for i in range(len(falses))], falses, s=25, c='r', marker="s", label='Falses')

    plt.legend(loc='upper right');
    ax.set_title("Decision Boundary")
    ax.set_xlabel('N/2')
    ax.set_ylabel('Predicted Probability')
    plt.axhline(.5, color='black')
    plt.show()
