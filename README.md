# PLE_agent
Training an agent to play on the "Pygame Learning Environment" - Playing 'Flappy Bird'

Exploring a genetic algorithm to update the neural network parametres as opposed to Backpropagation.
We maintain a set of Agents, with a set of parametres which on a feedforward of the network will output a move.

Each agent has a 'fitness' which is a function of the score obtained in the game. After some iterations of the game, we take the initially random agents who performed the best and kill the other agents.

We replicate the top agents and add a small amount of gaussian noise to their parametres to replace them. The idea being that eventually the agents who performed well will be outperformed by their slightly modified friends, who then become the top agents
