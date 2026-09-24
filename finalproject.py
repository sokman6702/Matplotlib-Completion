import matplotlib.pyplot as plt
import pandas as pd

data={
    "Epoch": [1, 2, 3, 4, 5, 6],
    "Training_Accuracy": [55, 64, 72, 80, 87, 91],
    "Validation_Accuracy": [53, 61, 69, 75, 78, 77],
    "Training_Loss": [0.90, 0.72, 0.55, 0.40, 0.30, 0.22],
    "Validation_Loss": [0.95, 0.80, 0.65, 0.52, 0.48, 0.55]
}
df=pd.DataFrame(data)
print(df)
print(df.describe())
print(df.head())
print(df.shape)

#training plot
plt.subplot(2,2,1)
plt.plot(df["Epoch"],df["Training_Accuracy"])
plt.title("Training Upward ACCURACY")
plt.xlabel("Epoch")
plt.ylabel("Training Accuracy")

#validation plot
plt.subplot(2,2,2)
plt.plot(df["Epoch"],df["Validation_Accuracy"])
plt.title("Validation Time ACCURACY")
plt.xlabel("Epoch")
plt.ylabel("Validation accuracy")

#training loos plot 
plt.subplot(2,2,3)
plt.plot(df["Epoch"],df["Training_Loss"])
plt.title("Training downward Loss")
plt.xlabel("Epoch")
plt.ylabel("training  loss")

#validation loss plot
plt.subplot(2,2,4)
plt.plot(df["Epoch"],df["Validation_Loss"])
plt.title("Validation downward Loss")
plt.xlabel("Epoch")
plt.ylabel("Validation   loss") 

plt.savefig('finalproject.png')
plt.tight_layout()
plt.show()

