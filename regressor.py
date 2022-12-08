import numpy as np

class PolyRegressor:
    def __init__(self, d):
        self.d = d
        self.p = np.arange(d + 1)[np.newaxis, :]
    
    def fit(self, x_sample, y_sample):
        ## Xを作る
        x_s = x_sample[:, np.newaxis]
        X_s = x_s ** self.p
        ##係数aを求める
        y_s = y_sample[:, np.newaxis]
        X_inv = np.linalg.inv(X_s.T @ X_s)  # linalgは線形, invが逆行列を示す
        self.a = X_inv @ X_s.T @ y_s  # .T で転置を表せる
    
    def predict(self, x):
        # yの予測値を計算
        y_pred = np.squeeze((x[:, np.newaxis] ** self.p) @ self.a)  
        # np.squeeze は配列を一次元にする
        return y_pred

def build_regressor(regressor_name, regressor_kwargs):
    REGRESSORS = dict(
        poly = PolyRegressor
    )
    regressor_cls = REGRESSORS[regressor_name]
    init_kwargs = regressor_kwargs[regressor_name]
    return regressor_cls(**init_kwargs)