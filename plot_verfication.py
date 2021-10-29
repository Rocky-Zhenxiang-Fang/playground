import numpy as np
from matplotlib import pyplot as plt
import random as rand



def main():
    mean_reflect = 3
    var = 0.5
    ground_truth = np.random.normal(mean_reflect, var, 10000)
    left_channel = np.random.normal(mean_reflect * 0.75, var * 0.95, 10000)
    right_channel = np.random.normal(mean_reflect * 1.3, var * 1.1, 10000)
    # plt.hist(ground_truth, 30, histtype=u'step')
    # plt.hist(left_channel, 30, histtype=u'step')
    # plt.hist(right_channel, 30, histtype=u'step')
    # plt.show()

    ground_truth = np.random.normal(mean_reflect, var, 10000)
    left_channel = np.random.normal(mean_reflect * 0.95, var * 0.95, 10000)
    right_channel = np.random.normal(mean_reflect * 1.05, var * 1.1, 10000)
    plt.hist(ground_truth, 30, histtype=u'step')
    plt.hist(left_channel, 30, histtype=u'step')
    plt.hist(right_channel, 30, histtype=u'step')
    plt.show()






if __name__ == "__main__":
    main()