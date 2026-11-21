import pandas as pd
import scipy.stats as stats

data = pd.read_csv("rare_elements.csv")
sample = data.sample(30)

mean = sample.mean()[0]
ci = stats.t.interval(0.95, len(sample)-1, loc=mean, scale=stats.sem(sample[0]))

print("Sample Mean:", mean)
print("95% CI:", ci)
