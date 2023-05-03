import random
import math
from configurations import configurations

#Simulated Annueling Algorithm that finds best configuration from a set of total outputs
def outputs_simulated_annealing(initial_config, allOutputsList, bestConfigurationsList, temperature):
    current_config = initial_config
    best_config = initial_config
    temperature_init = temperature
    countIter = 0

    while temperature > 0.1:
        cooling_rate = temperature / math.log(1 + countIter)

        neighbor_config = get_neighbor(current_config, allOutputsList)
        current_value = configurations.value(current_config)
        neighbor_value = configurations.value(neighbor_config)

        if neighbor_value > current_value:
            current_config = neighbor_config

            if neighbor_value > configurations.value(best_config):
               #potential solution to 2nd best issue: if neighbor config is the same as a config in the existing "best configs set",
               # then do not set best_config to neighbor config and continue 
               best_config = neighbor_config

        else:
            delta_value = (current_value - neighbor_value)
            acceptance_probability = math.exp(-delta_value / temperature)

            if random.uniform(0, 1) < acceptance_probability:
               current_config = neighbor_config

        temperature *= cooling_rate
        countIter += 1

    return best_config



def get_neighbor(config, allOutputsList):
    # Generate a random 'neighbor' of the current config
    # Configs are 'Neighbors if they only differ by one output

   length = len(allOutputsList)
   rand = random.randint(0,length)


