import numpy as np


class HMM:
    def __init__(self, observed, transition_matrix, emission_matrix, initial_distribution):
        self.I = initial_distribution
        self.V = np.array(observed)
        self.A = np.array(transition_matrix)
        self.B = np.array(emission_matrix)

        self.K = self.A.shape[0]
        self.N = self.V.shape[0]

    def forward(self):
        alpha = np.zeros((self.N, self.K))
        # TODO: calculate forward values
        # prawd., że po T krokach bedziesz w jakims stanie
        alpha[0, :] = self.I *self.B[:, self.V[0]]

        for t in range(1, self.V.shape[0]):
            for j in range(self.A.shape[0]):
                alpha[t, j] = alpha[t - 1].dot(self.A[:, j]) * self.B[j, self.V[t]]

        return np.argmax(alpha, axis=1), alpha

    def backward(self):
        beta = np.zeros((self.N, self.K))
        # TODO: calculate backward values

        return np.argmax(beta, axis=1), beta

    def forward_backward(self):
        fbv = np.zeros((self.N, self.K))
        # TODO: calculate forward-backward values

        return np.argmax(fbv, axis=1)

    def viterbi(self):
        T1 = self.V.shape[0]
        T2 = self.A.shape[0]
        omega = np.zeros((T1, T2))
        omega[0, :] = np.log(self.I * self.B[:, self.V[0]])
        prev = np.zeros((T1 - 1, T2))

        for t in range(1, T1):
            for j in range(T2):
                # Same as Forward Probability
                np.seterr(divide='ignore') # hide warning
                probability = omega[t - 1] + np.log(self.A[:, j]) + np.log(self.B[j, self.V[t]])
                np.seterr(divide='warn') # unhidd warning
                # This is our most probable state given previous state at time t (1)
                prev[t - 1, j] = np.argmax(probability)
                # This is the probability of the most probable state (2)
                omega[t, j] = np.max(probability)
        # Path Array
        S = np.zeros(T1)

        # Find the most probable last hidden state
        last_state = np.argmax(omega[T1 - 1, :])

        S[0] = last_state

        backtrack_index = 1
        for i in range(T1 - 2, -1, -1):
            S[backtrack_index] = prev[i, int(last_state)]
            last_state = prev[i, int(last_state)]
            backtrack_index += 1

        # Flip the path array since we were backtracking
        vitrebi = np.flip(S, axis=0)

        return vitrebi
