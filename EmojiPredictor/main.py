import pandas as pd 
import matplotlib.pyplot as plt

#reading train data
df = pd.read_csv('data/train.csv')
df = df.drop(['Unnamed: 0'],axis=1)
print(df)

#reading emoticon data
mapping_df = pd.read_csv('data/mapping.csv')
mapping_df = mapping_df.drop(['Unnamed: 0'],axis=1)
print(mapping_df)

#merging data to get the final train data
train_data = pd.merge(df, mapping_df, left_on='Label', right_on='number', how='left')
print(train_data)

emoji_counts = train_data['emoticons'].value_counts()
emoji_counts.plot(kind='bar', figsize=(10, 5), title='Emoji Frequency')
plt.show()