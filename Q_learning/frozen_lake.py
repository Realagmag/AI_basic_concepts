import gymnasium as gym
import numpy as np
import random as rand
import matplotlib.pyplot as plt

DEFAULT = 1
AVOID_HOLES = 2
AVOID_HOLES_AND_WALLS = 3
DONT_GO_BACK = 4


def main():
    averaged_reward = q_learning(False, DEFAULT)
    averaged_reward_base = averaged_reward
    averaged_reward = q_learning(False, DONT_GO_BACK)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(averaged_reward_base, 'r')
    plt.plot(averaged_reward, 'b')
    plt.savefig("test.png")
    plt.show()


def q_learning(slippery, strategy):
    env = gym.make('FrozenLake-v1', desc=None, map_name='8x8', is_slippery=slippery)
    state_size = env.observation_space.n
    action_size = env.action_space.n
    epsilon = 0.1
    beta = 0.9
    gamma = 0.8
    num_of_ind_runs = 25
    num_episodes = 1000 if not slippery else 10000
    averaged_reward = np.zeros(num_episodes)
    for run in range(num_of_ind_runs):
        qtable = np.zeros((state_size, action_size))
        state, _ = env.reset()
        previous_state = state
        for episode in range(num_episodes):
            done = False
            while not done:
                action = choose_action(state, qtable, epsilon, env.action_space)
                new_state, reward, terminated, truncated, _ = env.step(action=action)
                done = terminated or truncated

                # change reward depending on strategy
                if reward == 0 and terminated and (strategy == AVOID_HOLES or strategy==AVOID_HOLES_AND_WALLS or strategy ==DONT_GO_BACK):
                    reward = -1
                elif state == new_state and (strategy == AVOID_HOLES_AND_WALLS or strategy == DONT_GO_BACK):
                    reward = -1
                elif previous_state == new_state and strategy == DONT_GO_BACK:
                    reward = -0.1

                qtable[state, action] += beta*(reward + gamma*max(qtable[new_state, :]) - qtable[state, action])

                previous_state = state
                state = new_state

            if reward == 1:
                averaged_reward[episode] = averaged_reward[episode] + reward
            state, _ = env.reset()
    averaged_reward = averaged_reward/(num_of_ind_runs)
    return averaged_reward


def choose_action(state, qtable, epsilon, action_space):
    random_number = rand.uniform(0, 1)
    if random_number < epsilon:
        return action_space.sample()
    else:
        max_indeces = np.where(qtable[state, :] == qtable[state, :].max())[0]
        return rand.choice(max_indeces)


if __name__ == "__main__":
    main()
