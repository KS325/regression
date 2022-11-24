import numpy as np
from matplotlib.figure import Figure
import japanize_matplotlib as _


def main():
    # x, f(x)の準備
    x = np.linspace(-1, 1, 101) # -1~1の間を101等分（両端を含む）
    y = np.sin(np.pi * x)

    # サンプルの準備
    x_sample = np.random.uniform(-1, 1, (20, )) # 右端，左端，量
    range_y = np.max(y) - np.min(y)
    noise_sample = np.random.normal(0, range_y * 0.05, (20, ))
    y_sample = np.sin(np.pi * x_sample) + noise_sample

    # 多項式フィッティング
    ## Xを作る
    d = 3
    p = np.arange(d + 1)[np.newaxis, :]
    x_s = x_sample[:, np.newaxis]
    X_s = x_s ** p
    ##係数aを求める
    y_s = y_sample[:, np.newaxis]
    X_inv = np.linalg.inv(X_s.T @ X_s) # linalgは線形, invが逆行列を示す
    a = X_inv @ X_s.T @ y_s # .T で転置を表せる
    ## yの予測値を計算
    y_pred = np.squeeze((x[:, np.newaxis] ** p) @ a) # np.squeezeは配列を一次元に

    # 評価指標の算出
    norm_diff = np.sum(np.abs(y - y_pred)) # np.abs で絶対値, np.sum は和
    norm_y = np.sum(np.abs(y))
    eps_score = 1e-8
    score = norm_diff / (norm_y + eps_score)
    print(f'{score = :.3f}')

    # グラフの作成
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1) # 縦に1つ，横に1つ で分けた，右上(第一象限)
    ax.plot(x, y, label = '真の関数 $f$')
    ax.plot(x, y_pred, label = '回帰関数 $\\hat{f}$')
    ax.scatter(x_sample, y_sample, color = 'red', label = '学習サンプル')
    ax.legend()
    ax.set_title('$y = \\sin (\\pi x)$')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.axhline(color = '#777777') # 水平線
    ax.axvline(color = '#777777') # 垂直線
    fig.savefig('out.png')

if __name__ == '__main__':
    main()