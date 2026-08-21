'''
House price prediction model using Multiple Linear Regression.
'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sys
import math
import pickle
import warnings

warnings.filterwarnings("ignore")


class HouseValue:

    def __init__(self):

        try:
            f = pd.read_csv("data.csv")
            f = f.drop(["country"], axis=1)
            b = list(f['city'].unique())
            d = {}
            for i in range(len(b)):
                d[b[i]] = i
            f['city'] = f['city'].map(d)
            f['date'] = pd.to_datetime(f['date'])
            f["day"] = f['date'].dt.day
            f['month'] = f['date'].dt.month
            f['year'] = f['date'].dt.year
            f = f.drop("date", axis=1)
            self.X = f.iloc[:, 1:]
            self.y = f.iloc[:, 0]
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no {er_line.tb_lineno} due to {er_msg} reason {er_ty} ")

    def spliting_data(self):

        try:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2,
                                                                                    random_state=42)
            return self.X_train, self.X_test, self.y_train, self.y_test

        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no {er_line.tb_lineno} due to {er_msg} reason {er_ty} ")

    def model_training(self):

        try:
            self.mod = LinearRegression()
            self.mod.fit(self.X_train, self.y_train)

        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no {er_line.tb_lineno} due to {er_msg} reason {er_ty} ")

    def predictions(self):

        try:
            train_prediction = self.mod.predict(self.X_train)
            test_prediction = self.mod.predict(self.X_test)
            return train_prediction, test_prediction

        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no {er_line.tb_lineno} due to {er_msg} reason {er_ty} ")

    def accu_and_loss(self, a1, a2):
        try:
            # accuracy
            num = ((a1 - a2) ** 2).sum()
            den = ((a1 - (a1.mean())) ** 2).sum()
            accu = 1 - (num / den)
            print(accu * 100)
            # loss
            loss = math.sqrt(((a1 - a2) ** 2).mean())
            print(loss)
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no {er_line.tb_lineno} due to {er_msg} reason {er_ty} ")

    def model_file(self):
        try:
            with open("mul_lin_reg.pkl", "wb") as m:
                pickle.dump(obj.mod, m)
            with open("mul_lin_reg.pkl", "rb") as p:
                k = pickle.load(p)
            print("pred_amount:", k.predict([[2, 1.5, 1300, 7000, 1, 0, 3, 1340, 0, 1955, 2005, 300, 0, 1, 12, 2015]]))
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no {er_line.tb_lineno} due to {er_msg} reason {er_ty} ")


if __name__ == "__main__":
    obj = HouseValue()
    X_train, X_test, y_train, y_test = obj.spliting_data()
    obj.model_training()
    pred1, pred2 = obj.predictions()
    obj.accu_and_loss(y_train, pred1)
    obj.accu_and_loss(y_test, pred2)
    obj.model_file()


