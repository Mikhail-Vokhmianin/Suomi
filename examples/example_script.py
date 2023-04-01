from suomi import text_analysis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# link to datasets: https://www.kaggle.com/datasets/kamendamov/russiaukraine-conflict-youtube-comments
kotkin = pd.read_csv("kotkin_comments.csv", index_col=0)
stone = pd.read_csv("stone_comments.csv", index_col=0)
kotkin.rename({'0': 'Comments'}, axis=1, inplace=True)
stone.rename({'0': 'Comments'}, axis=1, inplace=True)

df = pd.concat([kotkin['Comments'], stone['Comments']], keys=['kotkin', 'stone'])
df = pd.DataFrame(df)
df['origin'] = df.index.get_level_values(0)

total_comments = len(df)
result = text_analysis(df['Comments'][0])
result['origin'] = df['origin'][0]
s = 4
i = 0
for c in df['Comments']:
    i += 1
    if type(c) == str and len(c) > 0:
        r = text_analysis(c)
        r['origin'] = df['origin'][i]
        result = pd.concat([result, r], ignore_index=True)
        print('comment #' + str(i) + ' out of ' + str(total_comments))

# histogram:
sns.displot(result, x="quantiles", col="labels", hue="origin", kind="kde", fill=True)
plt.show()
