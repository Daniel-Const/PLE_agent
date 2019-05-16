from ple.games.flappybird import FlappyBird
from ple import PLE
import operator
import time

SHAPE_A = 12
SHAPE_B = 12

numAgents = 50
inputShape = 8
actionShape = 2



game = FlappyBird()
p = PLE(game, fps=30, display_screen=True)
#agent = Agent()

p.init()
reward = 0.0


for i in range(1000):
   if p.game_over():
           p.reset_game()

   observation = p.getScreenRGB()
   action = 0
   reward = p.act(action)




class Agent:
    def __init__(self):
            self.weightSetA = tf.Variable(tf.random_uniform([inputShape, SHAPE_A]))
            self.biasA = tf.Variable(tf.random_uniform([SHAPE_A]))

            self.weightSetB = tf.Variable(tf.random_uniform([SHAPE_A, SHAPE_B]))
            self.biasB = tf.Variable(tf.random_uniform([SHAPE_B]))

            self.output = tf.Variable(tf.random_uniform([SHAPE_B, actionShape])
            self.biasOut = tf.Variable(tf.random_uniform([actionShape]))

            self.fitness = 0  #reward from an iteration of playing

    def copy(self, agent):

        self.weightSetA = agent.weightSetA
        self.biasA =  agent.biasA

        self.weightSetB =  agent.weightSetB
        self.biasB =  agent.biasB

        self.output =  agent.output
        self.biasOut =  agent.biasOut

        self.fitness =  agent.fitness


    def pickAction(self, reward, observation):
        logits = tf.matmul(observation,self.weightSetA)
        logits = tf.add(logits, self.biasA)

        activation = tf.nn.relu(logits)

        logits = tf.matmul(activation, self.WeightSetB)
        logits = tf.add(logits, self.biasB)

        activation = tf.nn.relu(logits)

        logits = tf.matmul(activation, self.output)
        logits = tf.add(logits, self.biasOut)

        activation = tf.nn.softmax(logits)

        return tf.argmax(input=activation, axis=1)  #get action with best probability

    def addNoise(self):

        self.weightSetA = tf.add(self.weightSetA, tf.random_uniform([inputShape, SHAPE_A]))
        self.biasA = tf.add(self.biasA, tf.random_uniform([SHAPE_A]))

        self.weightSetB = tf.add(self.weightSetB, tf.random_uniform([SHAPE_A, SHAPE_B]))
        self.biasB = tf.add(self.biasB, tf.random_uniform([SHAPE_B]))

        self.output = tf.add(self.output, tf.random_uniform([SHAPE_B, p.getActionSet.shape[0]]))
        self.biasOut = tf.add(self.biasOut, tf.random_uniform([p.getActionSet.shape[0]]))

class AgentSet:

    def __init__(self, inputs):
        self.agents = []

    def initAgents(self):
        for i in range(numAgents):
            a = Agent()
            agents.append(a)

    #delete bottom 90 %, and copy the top 10% to replace them
    def cullLosers(self):
        sortedAgents = sorted(self.agents, key=operator.attrgetter('fitness'), reverse=True)
        perc = 5
        for i in range(perc + 1, numAgents):
            a = Agent()
            a.copy(sortedAgents[i % perc])
            a.addNoise()

            sortedAgents[i] = a

        self.agents = sortedAgents
