import pandas as pd

df = pd.read_csv('../data/labels.csv')


# Parse the stringified lists
df["labels"] = df["labels"].str.split(',')

# Flatten into a list of (composer, label) with duplicates preserved
all_label_counts = []

for _, row in df.iterrows():
    composer = row["composer"]
    for label in row["labels"]:
        all_label_counts.append((composer, label))

# Create a DataFrame from the flattened list
flat_df = pd.DataFrame(all_label_counts, columns=["composer", "label"])

# Cross-tabulate
cross_tab = pd.crosstab(flat_df["label"],flat_df["composer"])

cross_tab = cross_tab.reindex(columns=['Mozart', 'Beethoven', 'Czerny', 'Clementi', 'Haydn'])
cross_tab = cross_tab.reindex(["Sonata", "Rondo-Sonata", "Binary", "Minuet", "Ternary", "Rondo", "Scherzo","Variation"])

cross_tab['total'] = cross_tab.sum(axis=1, numeric_only=True)
cross_tab.loc['total'] = cross_tab.sum(axis=0, numeric_only=True)


print("Number of movements: ",len(df),"\n")
print("Movement counts per composer","\n",df['composer'].value_counts(),"\n")
print("Movement label cross-tabulation","\n",cross_tab)


df = pd.read_csv('../data/labels.csv')

# Step 1: turn labels into lists
df['labels'] = df['labels'].str.split(',')

# Step 2: compute number of unique labels per movement
df['n_unique_labels'] = df['labels'].apply(lambda labels: len(set(labels)))

# Step 3: count movements with >1 unique label
n_total = len(df)
n_multiple_labels = (df['n_unique_labels'] > 1).sum()

percentage_multiple = 100 * n_multiple_labels / n_total

print(f"Percentage of movements with >1 label: {percentage_multiple:.2f}%")




