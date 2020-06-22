import numpy as np
import matplotlib.pyplot as plt


def return_throughput(rewards):
	N = int(1000)
	temp_sum = 0
	throughput = []
	for i in range(len(rewards)):
		if i < N:
			temp_sum += rewards[i]
			throughput.append(temp_sum / (i+1))
		else:
			temp_sum += rewards[i] - rewards[i-N]
			throughput.append(temp_sum / N)
	return throughput




M = 4 # state length
E = 1000 # memory size
F = 20 # target network update frequency
B = 64 # mini-batch size
gamma = 0.9 # discount factor

alpha = 0 # fairness index
max_iter = int(1e4)
idx = 1


window = 1000

for idx in range(1, 2):
	reward1 = np.loadtxt(f'rewards/reward1_len{max_iter}_M{M}_E{E}_F{F}_B{B}_gamma{gamma}_alpha{alpha}_idx{idx}.txt')
	reward2 = np.loadtxt(f'rewards/reward2_len{max_iter}_M{M}_E{E}_F{F}_B{B}_gamma{gamma}_alpha{alpha}_idx{idx}.txt')
	throughput1 = return_throughput(reward1)
	throughput2 = return_throughput(reward2)
	sum_throughput = [throughput1[i]+throughput2[i] for i in range(max_iter)]

	plt.plot(sum_throughput)
	plt.plot(throughput1, c='r', label='DLMA')
	plt.plot(throughput2, c='b', label='TDMA')
	plt.legend()
	plt.show()


