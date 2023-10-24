import pandas as pd
predict=pd.read_csv('data/dm/test_results.tsv', sep='\t', names=['1', '2', '3', '4', '5', '6'])
labels = ['neural', 'happy', 'angry', 'sad', 'fear', 'surprise']
result = []
for index, row in predict.iterrows():
    row = row * 1e10
    prob = row.tolist()
    prob = list(map(int, prob))
    t = max(prob)
    r = labels[prob.index(t)]
    result.append(r)
df = pd.DataFrame(data=result)
df.to_csv("data/dm/test_results.csv")
