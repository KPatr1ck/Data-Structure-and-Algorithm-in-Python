#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import Dict, List
from numpy import ndarray
import numpy as np
import random
from sklearn.datasets import load_iris


def sigmoid(X: ndarray) -> ndarray:
    return 1.0/(1 + np.exp(-X))


def d_sigmoid(X: ndarray) -> ndarray:
    s = sigmoid(X)
    return s * (1 - s)


def init_parameters(layer_dims: List[int]) -> Dict:
    """
    layer_dims描述了神经网络的结构
    W需要用标准正太分布随机化，然后再进行缩小得到随机的较小的权重值
    b可以直接全0

    :param layer_dims: 神经网络的结构信息
    :return: 初始化后的参数
    """
    layer_count = len(layer_dims)

    parameters = {}
    for i in range(1, layer_count):
        parameters['W' + str(i)] = np.random.randn(layer_dims[i], layer_dims[i-1]) * 0.01
        parameters['b' + str(i)] = np.zeros((layer_dims[i], 1))

    return parameters


def one_hot(label: ndarray) -> ndarray:
    """
    将label转化成one hot

    :param label: 训练/测试集的标签
    :return: one hot的标签
    """
    m = label.shape[0]
    classes = max(label) + 1
    one_hot_label = np.zeros((m, classes))
    one_hot_label[np.arange(0, m), label] = 1
    return one_hot_label


def forward_one_layer(W: ndarray, b: ndarray, A_prev: ndarray) -> ndarray:
    """
    单层网络的前向传播

    :param W: 当前层的权重
    :param b: 当前层的偏置
    :param A_prev: 上一层的输出
    :return: 当前层的输出
    """
    return np.dot(W, A_prev) + b


def forward_propagation(parameters: Dict, X: ndarray) -> Dict:
    """
    前向传播
    :param parameters: 神经网络每一层的W和b, {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2 ...}
    :param X: 训练集X
    :return: 缓存每一层的输入和输出
    """
    # 层数，不计输入层
    L = len(parameters)//2

    cache = {}
    cache['A0'] = X

    A = X
    for l in range(1, L+1):
        A_prev = A
        W, b = parameters['W' + str(l)], parameters['b' + str(l)]
        Z = forward_one_layer(W, b, A_prev)
        A = sigmoid(Z)
        cache['Z' + str(l)] = Z
        cache['A' + str(l)] = A

    return cache


def back_propagation(Y_hat: ndarray, Y: ndarray, parameters: Dict, cache: Dict) -> Dict:
    """
    反向传播算法
    :param Y_hat:
    :param Y:
    :param paramaters:
    :return:
    """
    # ret = {}
    gradient = {}

    # 样本数
    _, m = Y_hat.shape

    # 层数，不计输入层
    L = len(parameters)//2

    for l in range(L, 0, -1):
        Z = cache['Z' + str(l)]
        A_prev = cache['A' + str(l-1)]

        if l == L:
            dZ = Y_hat - Y
        else:
            W_next = parameters['W' + str(l+1)]
            dZ = np.dot(W_next.T, dZ) * d_sigmoid(Z)

        dW = np.dot(dZ, A_prev.T)/m
        db = np.sum(dZ, axis=1, keepdims=True)/m

        gradient['dW' + str(l)] = dW
        gradient['db' + str(l)] = db

    return gradient


def cost(Y: ndarray, A: ndarray) -> float:
    """
    神经网络的cost function
    cross entropy loss

    :param Y: 实际标签
    :param A: 神经网络的输出
    :return: cost数值
    """
    _, m = Y.shape
    return -np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A), keepdims=False)/m


def train(layer_dims: List[int], X: ndarray, Y: ndarray, learning_rate: float, iters: int, print_cost=False) -> Dict:
    # 参数初始化
    parameters = init_parameters(layer_dims)

    # 层数，不计输入层
    L = len(parameters)//2

    for i in range(iters):
        # 正向传播
        cache = forward_propagation(parameters, X)
        Y_hat = cache['A' + str(L)]

        # 反向传播
        gradient = back_propagation(Y_hat, Y, parameters, cache)

        # 更新参数
        for j in range(L, 0, -1):
            parameters['W' + str(j)] = parameters['W' + str(j)] - learning_rate * gradient['dW' + str(j)]
            parameters['b' + str(j)] = parameters['b' + str(j)] - learning_rate * gradient['db' + str(j)]

        if print_cost and (i % 1000 == 0):
            predict_labels = predict(parameters, X)
            origin_labels = Y.argmax(0)
            train_acc = 100.0 * np.sum(predict_labels == origin_labels)/predict_labels.shape[0]
            print('[iters: {:>5}]: {:.5f} {:3f}%'.format(i, cost(Y, Y_hat), train_acc))

    return parameters


def predict(parameters: Dict, X: ndarray) -> ndarray:
    L = len(parameters)//2
    pred = forward_propagation(parameters, X)['A' + str(L)]
    pred = pred.argmax(0)
    return pred


if __name__ == '__main__':
    # np.random.seed(1)
    # random.seed(1)

    # 训练集
    # X_train = np.array([[6, 2], [1, 2], [5, 1], [0, 2], [4, 10], [2, 2]]).T
    # Y_train = np.array([[0, 1, 0, 1, 1, 0]])

    # m = 600
    # X_train = []
    # Y_train = []
    # for i in range(m):
    #     x = random.randrange(-50, 50)
    #     y = random.randrange(-50, 50)
    #     X_train.append([x, y])
    #     Y_train.append(1 if y >= x else 0)
    #
    # X_train = np.array(X_train).T
    # Y_train = np.array([Y_train])
    #
    # layer_dims = [2, 3, 1]
    # learning_rate = 0.03
    # iters = 50001
    #
    # parameters = train(layer_dims, X_train, Y_train, learning_rate, iters, print_cost=True)

    # 测试集
    # X_test = np.array([[3, 8], [1, 10], [8, 2], [0, 4], [4, 25]]).T
    # Y_predict = predict(parameters, X_test)
    # print(Y_predict)

    iris = load_iris()
    X_iris = iris.data
    Y_iris = iris.target
    m = 100

    picks = list(range(Y_iris.shape[0]))
    random.shuffle(picks)

    # split training set and test set
    X_orig_train, Y_orig_train = X_iris[picks[: m]], Y_iris[picks[: m]]
    X_orig_test, Y_orig_test = X_iris[picks[m:]], Y_iris[picks[m:]]

    Y_one_hot_train = one_hot(Y_orig_train)
    Y_one_hot_test = one_hot(Y_orig_test)

    X_train, Y_train = X_orig_train.T, Y_one_hot_train.T
    X_test, Y_test = X_orig_test.T, Y_one_hot_test.T

    # hyper parameters
    layer_dims = [4, 5, 3]
    learning_rate = 0.03
    iters = 50001

    # train
    parameters = train(layer_dims, X_train, Y_train, learning_rate, iters, print_cost=True)
    output_after_train = forward_propagation(parameters, X_train)['A' + str(len(parameters)//2)]

    # test
    pred = predict(parameters, X_test)
    test_acc = 100 * np.sum(pred == Y_orig_test)/Y_orig_test.shape[0]
    print("test_acc: {}%".format(test_acc))
