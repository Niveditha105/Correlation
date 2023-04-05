#Correlation
#Positive correlation is were the x and y axis increases subsequently.

import pandas as pd
import numpy as np
eg = pd.read_csv("data.csv")
print(eg.corr())
round =round(eg.corr(),3)
print(round)

# correlation:
# Correlation simply implies a statistical association, or relationship, between two variables.
# Casuality:
# not only implies a relationship, it implies a causal relationship;
# it implies that a change in one variable is directly causing a change in the other.