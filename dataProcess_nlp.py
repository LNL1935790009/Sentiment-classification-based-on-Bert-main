import pandas as pd

df = pd.read_csv("data/nlp/data_raw.csv")
train = df[:20000]
print(train)
train.to_csv("data/nlp/train.csv")

dev = df[20000:21800]
print(dev)
dev.to_csv("data/nlp/dev.csv")

test = df[21800:]
print(test)
test.to_csv("data/nlp/test.csv")