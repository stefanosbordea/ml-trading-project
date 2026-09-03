from load import data_split
import torch.nn as nn
import torch

class LogisticRegression(nn.Module):
    def __init__(self,daily_return,log_return,vol_20,vol_60,lag_1,lag_5,lag_10,rsi,macd,bollinger_bands,volume_ratio,is_monday,is_tuesday,is_wednesday,is_thursday,is_friday,is_saturday,volatility_regime):
        super(LogisticRegression,self).__init__()
        self.linear = nn.Linear(daily_return,log_return,vol_20,vol_60,lag_1,lag_5,lag_10,rsi,macd,bollinger_bands,volume_ratio,is_monday,is_tuesday,is_wednesday,is_thursday,is_friday,is_saturday,volatility_regime, 1)

    def forward(self,x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred


x_train,x_cv,x_test,y_train,y_cv,y_test = data_split()

x_train_tensor = torch.tensor(x_train)
x_cv_tensor = torch.tensor(x_cv)
x_test_tensor = torch.tensor(x_train)
y_train_tensor = torch.tensor(y_train)
y_cv_tensor = torch.tensor(y_cv)
y_test_tensor= torch.tensor(y_test)

model = LogisticRegression(daily_return,log_return,vol_20,vol_60,lag_1,lag_5,lag_10,rsi,macd,bollinger_bands,volume_ratio,is_monday,is_tuesday,is_wednesday,is_thursday,is_friday,is_saturday,volatility_regime)





