import pandas as pd
import random

# Source of Colors from https://data.world/dilumr/color-names
df = pd.read_csv('https://query.data.world/s/2kdcmtzai2p9wh9itzlsodvh5')
lengthofColorList = len(df.index)
randomNumber = random.choice(range(lengthofColorList))
randomNumber2 = random.choice(range(lengthofColorList))
print df.iloc[randomNumber][0], "and", df.iloc[randomNumber2][0]
