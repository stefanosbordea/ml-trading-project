from load import data_split
import torch.nn as nn
import torch
import os
from torch.utils.data import DataLoader, TensorDataset
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler


class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(18,64),

            nn.ReLU(),

            nn.Linear(64,32),

            nn.ReLU(),

            nn.Linear(32,1)
        )

    def forward(self,x):
        return self.layers(x)
        

x_train,x_cv,x_test,y_train,y_cv,y_test = data_split()

x_train_np = x_train.to_numpy()
x_cv_np = x_cv.to_numpy()
x_test_np = x_test.to_numpy()
y_train_np = y_train.to_numpy()
y_cv_np = y_cv.to_numpy()
y_test_np= y_test.to_numpy()

scaler = StandardScaler()
x_train_np_scaled = scaler.fit_transform(x_train_np)
x_cv_np_scaled = scaler.transform(x_cv_np)
x_test_np_scaled = scaler.transform(x_test_np)

x_train_tensor = torch.from_numpy(x_train_np_scaled).float()
x_cv_tensor = torch.from_numpy(x_cv_np_scaled).float()
x_test_tensor = torch.from_numpy(x_test_np_scaled).float()
y_train_tensor = torch.from_numpy(y_train_np).float().unsqueeze(1)
y_cv_tensor = torch.from_numpy(y_cv_np).float().unsqueeze(1)
y_test_tensor = torch.from_numpy(y_test_np).float().unsqueeze(1)



train_dataset = TensorDataset(x_train_tensor,y_train_tensor)
trainloader = torch.utils.data.DataLoader(train_dataset, batch_size=100, shuffle=True)

test_dataset = TensorDataset(x_test_tensor,y_test_tensor)
testloader = torch.utils.data.DataLoader(test_dataset,batch_size=100, shuffle = False)

mlp = MLP()

loss_function = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(mlp.parameters(), lr=1e-4)


epochs = 5

for epoch in range(0,epochs):
    print("Epoch:",epoch+1,"/", end=" ")

    current_loss = 0.0

    for i,data in enumerate(tqdm(trainloader)):
        inputs,targets = data

        optimizer.zero_grad()

        outputs = mlp(inputs)

        loss = loss_function(outputs,targets)

        loss.backward()

        optimizer.step()

        current_loss +=loss.item()

    print("Training Loss:", current_loss/len(trainloader))

print("Training process has finished.")    








