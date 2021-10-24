import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf

#using this to learn neural networks

dataset = pd.read_csv("cancer.csv")

x = dataset.drop(columns=["diagnosis(1=m, 0=b)"]) # drop is used to remove a column
y= dataset["diagnosis(1=m, 0=b)"] # take this column

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) # split dataset into a test and a learning set by 20%

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(
    256, input_shape=x_train.shape, activation='sigmoid'))
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1000)

model.evaluate(x_test, y_test)
