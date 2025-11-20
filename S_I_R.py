# Ref : https://stackoverflow.com/questions/47366712/correct-implementation-of-si-sis-sir-models-python
from time import sleep

import matplotlib.pyplot as plt

def si():
    N = 1000000
    S = N - 1
    I = 1
    beta = 0.6

    sus = []  # infected compartment
    inf = []  # susceptible compartment
    prob = []  # probability of infection at time t

    def infection(S, I, N):
        t = 0
        while (t < 100):
            S = S - beta * ((S * I / N))
            I = I + beta * ((S * I) / N)
            p = beta * (I / N)

            sus.append(S)
            inf.append(I)
            prob.append(p)
            t = t + 1

    infection(S, I, N)
    figure = plt.figure()
    # figure.canvas.set_window_title('SI model')

    figure.add_subplot(211)
    inf_line, = plt.plot(inf, label='I(t)')

    sus_line, = plt.plot(sus, label='S(t)')
    plt.legend(handles=[inf_line, sus_line])

    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))  # use scientific notation

    ax = figure.add_subplot(212)
    prob_line = plt.plot(prob, label='p(t)')
    plt.legend(handles=prob_line)

    type(ax)  # matplotlib.axes._subplots.AxesSubplot

    # manipulate
    vals = ax.get_yticks()
    ax.set_yticklabels(['{:3.2f}%'.format(x * 100) for x in vals])

    plt.xlabel('T')
    plt.ylabel('p')

    plt.show()

def sis():
    N = 1000000
    S = N - 1
    I = 1
    beta = 0.3
    gamma = 0.1

    sus = []
    inf = []

    def infection(S, I, N):
        for t in range(0, 1000):
            S = S - (beta * S * I / N) + gamma * I
            I = I + (beta * S * I / N) - gamma * I

            sus.append(S)
            inf.append(I)

    infection(S, I, N)

    figure = plt.figure()
    # figure.canvas.set_window_title('SIS model')

    inf_line, = plt.plot(inf, label='I(t)')

    sus_line, = plt.plot(sus, label='S(t)')
    plt.legend(handles=[inf_line, sus_line])

    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    plt.xlabel('T')
    plt.ylabel('N')

    plt.show()

def sir():
    N = 1000000
    S = N - 1
    I = 1
    R = 0
    beta = 0.5
    mu = 0.1

    sus = []
    inf = []
    rec = []

    def infection(S, I, R, N):
        for t in range(1, 100):
            S = S - (beta * S * I) / N
            I = I + ((beta * S * I) / N) - R
            R = mu * I

            sus.append(S)
            inf.append(I)
            rec.append(R)

    infection(S, I, R, N)

    figure = plt.figure()
    # figure.canvas.set_window_title('SIR model')

    inf_line, = plt.plot(inf, label='I(t)')

    sus_line, = plt.plot(sus, label='S(t)')

    rec_line, = plt.plot(rec, label='R(t)')
    plt.legend(handles=[inf_line, sus_line, rec_line])

    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    plt.xlabel('T')
    plt.ylabel('N')

    plt.show()

if __name__ == '__main__':
    si()
    sleep(1)
    sis()
    sleep(1)
    sir()