.. _linear_regression:

======================================
Hồi Quy Tuyến Tính (Linear Regression)
======================================

.. contents::
    :local:
    :depth: 2


Giới thiệu
==========

Hồi quy tuyến tính trong học máy là một thuật toán học có giám sát, với đầu ra là giá trị liên tục và có hệ số góc là hằng số.
Thuật toán này được sử dụng để dự đoán các giá trị trong một khoảng liên tục (ví dụ như giá cả, doanh thu bán hàng) thay vì học cách phân loại chúng thành các danh mục riêng biệt (ví dụ như cho hay mèo).

.. note::
  Cần phân biệt với phương pháp hồi quy tuyến tính trong thống kê.

Ta có thể phân loại hồi quy tuyến tính thành hai loại chính:

.. rubric:: Hồi quy tuyến tính đơn biến (Simple regression)

Hồi quy tuyến tính đơn biến sử dụng dạng đường chéo cơ bản, với :math:`m` và :math:`b` là những biến số trong thuật toán mà sẽ cố gắng "học" để dự đoán đầu ra một cách chính xác nhất có thể, :math:`x` ký hiệu dữ liệu đầu vào và :math:`y` ký hiệu cho dự đoán ở đầu ra.

.. math::

  y = mx + b

.. rubric:: Hồi quy tuyến tính đa biến (Multivariable regression)

Hồi quy tuyến tính đa biến phức tạp hơn và có dạng như sau, trong đó :math:`w` ký hiệu các hệ số, hay trọng số (weight), mà mô hình cần học.

.. math::

  f(x,y,z) = w_1 x + w_2 y + w_3 z

Các biến số :math:`x, y, z` ký hiệu các thuộc tính, hay những số liệu riêng biệt, mà ta có tại mỗi quan sát (observation).
Ví dụ, để dự đoán doanh thu, các thuộc tính này có thể là số tiền mà công ty đầu tư vào quảng cáo lần lượt trên đài radio, TV, và báo (news).

.. math::

  \text{Doanh thu} = w_1 Radio + w_2 TV + w_3 News


Hồi quy tuyến tính đơn biến
===========================

Giả sử ta được cung cấp một `tập dữ liệu <http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv>`_ với các cột (đặc trưng) sau: **số tiền** mà một công ty đã dành để quảng cáo trên đài radio mỗi năm và **doanh thu** hàng năm tính bằng số sản phẩm bán ra.
Ta đang cố gắng phát triển một phương trình mà sẽ cho phép chúng ta có thể dự đoán số sản phẩm bán ra dựa trên số tiền mà một công ty đã dành cho quảng cáo qua đài radio.
Các hàng (các quan sát) tương ứng với các công ty.

+--------------+-------------------+---------------+
| **Công ty**  | **Đài radio ($)** | **Doanh thu** |
+--------------+-------------------+---------------+
| Amazon       | 37.8              | 22.1          |
+--------------+-------------------+---------------+
| Google       | 39.3              | 10.4          |
+--------------+-------------------+---------------+
| Facebook     | 45.9              | 18.3          |
+--------------+-------------------+---------------+
| Apple        | 41.3              | 18.5          |
+--------------+-------------------+---------------+


Đưa ra dự đoán
--------------

Hàm dự đoán của chúng ta có đầu ra là doanh thu ước lượng dựa trên số tiền mà công ty đó dành cho quảng cáo qua đài radio cùng với giá trị hiện tại của *Trọng số* và *Hệ số điều chỉnh (Bias)*.

.. math::

  \text{Doanh thu} = \text{Trọng số} \times \text{Số tiền quảng cáo qua radio} + \text{Hệ số điều chỉnh}

Trọng số
  hệ số của biến độc lập chỉ Số tiền quảng cáo qua radio. Trong học máy, ta gọi các hệ số này là *trọng số*.

Radio
  biến độc lập. Trong học máy, ta gọi các biến này là các *đặc trưng (features)*.

Hệ số điều chỉnh
  giá trị mà đường tuyến tính giao với trục y. Trong học máy, ta có thể gọi giá trị này là *hệ số điều chỉnh (bias)*. Hệ số điều chỉnh được cộng vào tất cả các dự đoán mà ta đưa ra và sẽ được phân tích kỹ hơn sau.

Thuật toán này của chúng ta sẽ cố để *học* giá trị tốt nhất của Trọng số và Hệ số điều chỉnh.
Khi hoàn thành quá trình huấn luyện, phương trình của chúng ta sẽ có dạng xấp xỉ *đường thẳng phù hợp nhất* với dữ liệu.

.. image:: images/linear_regression_line_intro.png
    :align: center
    :scale: 80

.. rubric:: Code

::

  def predict_sales(radio, weight, bias):
      return weight*radio + bias


Hàm chi phí (Cost function)
---------------------------

Hàm dự đoán thì hay đấy, nhưng với mục đích để *học* thì ta không thực sự cần hàm này. Cái ta cần là một :doc:`hàm chi phí (hay hàm mất mát) <loss_functions>` để ta có thể bắt đầu tối ưu các trọng số.

Ở ví dụ này, chúng ta sẽ sử dụng :ref:`mse` làm hàm chi phí.
MSE đo trung bình độ lệch bình phương giữa giá trị thực tế quan sát được và giá trị dự đoán.
Đầu ra của MSE là một số, hay điểm số, thể hiện chi phí tương ứng với tập các trọng số hiện có.
Mục tiêu của chúng ta là phải tối thiểu hoá MSE để cải thiện độ chính xác của mô hình.

.. rubric:: Công thức toán học

Với hàm tuyến tính đơn giản :math:`y = mx + b`, ta có thể tính MSE theo công thức:

.. math::

  MSE =  \frac{1}{N} \sum_{i=1}^{n} (y_i - (m x_i + b))^2

Trong đó:
  - :math:`N` là số các quan sát (điểm dữ liệu).
  - :math:`\frac{1}{N} \sum_{i=1}^{n}` là giá trị trung bình.
  - :math:`y_i` là giá trị thực quan sát được và :math:`m x_i + b` là giá trị dự đoán.

.. rubric:: Code

::

  def cost_function(radio, sales, weight, bias):
      companies = len(radio)
      total_error = 0.0
      for i in range(companies):
          total_error += (sales[i] - (weight*radio[i] + bias))**2
      return total_error / companies


Hạ Gradient (Gradient descent)
------------------------------

Để tối thiểu hoá MSE, ta sử dụng :doc:`thuật toán hạ gradient <gradient_descent>` để tính toán gradient của hàm chi phí.
Thuật toán hạ gradient bao gồm bước tính sai số của dự đoán sinh bởi tập trọng số hiện có, sử dụng đạo hàm của hàm chi phí để tìm gradient (độ dốc của hàm chi phí với tập trọng số hiện có), và sau đó thay đổi trọng số theo hướng ngược lại với hướng của gradient.
Việc thay đổi ngược lại với hướng của gradient là do gradient hướng theo chiều tăng lên của độ dốc thay vì chiều giảm, do đó ta cần đi theo hướng ngược lại để có thể giảm sai số.

.. rubric:: Công thức toán học

Có hai :ref:`tham số <glossary_parameters>` (hệ số) trong hàm chi phí mà ta có thể kiểm soát: trọng số :math:`m` và hệ số điều chỉnh :math:`b`.
Do ta cần phải cân nhắc đến ảnh hưởng của từng tham số đối với kết quả dự đoán, ta cần sử dụng đạo hàm riêng.
Để tìm đạo hàm riêng, ta sử dụng :ref:`quy tắc chuỗi (chain rule) <chain_rule>`.
Ta cần quy tắc chuỗi do :math:`(y - (mx + b))^2` thực chất là 2 hàm lồng nhau: hàm :math:`y - (mx + b)` bên trong và hàm :math:`x^2` lồng bên ngoài.

Quay trở lại với hàm chi phí ở trên:

.. math::

    f(m,b) =  \frac{1}{N} \sum_{i=1}^{n} (y_i - (mx_i + b))^2

Bằng cách sử dụng dạng biểu diễn sau:

.. math::

    (y_i - (mx_i + b))^2 = A(B(m,b))

Ta có thể tách đạo hàm thành

.. math::

    A(x) = x^2

    \frac{df}{dx} = A'(x) = 2x

và

.. math::

    B(m,b) = y_i - (mx_i + b) = y_i - mx_i - b

    \frac{dx}{dm} = B'(m) = 0 - x_i - 0 = -x_i

    \frac{dx}{db} = B'(b) = 0 - 0 - 1 = -1

Và sau đó sử dụng :ref:`quy tắc chuỗi (chain rule) <chain_rule>` theo công thức:

.. math::

    \frac{df}{dm} = \frac{df}{dx} \frac{dx}{dm}

    \frac{df}{db} = \frac{df}{dx} \frac{dx}{db}

Ta áp dụng vào từng phần để thu được các đạo hàm riêng sau:

.. math::

    \frac{df}{dm} = A'(B(m,f)) B'(m) = 2(y_i - (mx_i + b)) \cdot -x_i

    \frac{df}{db} = A'(B(m,f)) B'(b) = 2(y_i - (mx_i + b)) \cdot -1

Ta có thể tính gradient của hàm chi phí này theo công thức:

.. math::
  \begin{align}
  f'(m,b) =
    \begin{bmatrix}
      \frac{df}{dm}\\
      \frac{df}{db}\\
    \end{bmatrix}
  &=
    \begin{bmatrix}
      \frac{1}{N} \sum -x_i \cdot 2(y_i - (mx_i + b)) \\
      \frac{1}{N} \sum -1 \cdot 2(y_i - (mx_i + b)) \\
    \end{bmatrix}\\
  &=
    \begin{bmatrix}
       \frac{1}{N} \sum -2x_i(y_i - (mx_i + b)) \\
       \frac{1}{N} \sum -2(y_i - (mx_i + b)) \\
    \end{bmatrix}
  \end{align}

.. rubric:: Code

Để tính gradient, ta lặp qua tất cả các điểm dữ liệu với giá trị trọng số và hệ số điều chỉnh mới, sau đó lấy trung bình các đạo hàm riêng.
Kết quả gradient thu được cho ta biết độ dốc của hàm chi phí tại thời điểm hiện tại (tức là với trọng số và hệ số điều chỉnh hiện có) và ta cần phải cập nhật các giá trị để giảm hàm chi phí đi (bằng cách đi ngược lại gradient).
Độ lớn của bước cập nhật được quy định bởi :ref:`tốc độ học (learning rate) <glossary_learning_rate>`.

::

  def update_weights(radio, sales, weight, bias, learning_rate):
      weight_deriv = 0
      bias_deriv = 0
      companies = len(radio)

      for i in range(companies):
          # Tính các đạo hàm riêng
          # -2x(y - (mx + b))
          weight_deriv += -2*radio[i] * (sales[i] - (weight*radio[i] + bias))

          # -2(y - (mx + b))
          bias_deriv += -2*(sales[i] - (weight*radio[i] + bias))

      # Ta sử dụng phép trừ do đạo hàm riêng có hướng là hướng dốc nhất
      # theo chiều đi lên (tăng dần) của hàm chi phí
      weight -= (weight_deriv / companies) * learning_rate
      bias -= (bias_deriv / companies) * learning_rate

      return weight, bias


.. _simple_linear_regression_training:

Huấn luyện
----------

Huấn luyện một mô hình là quá trình liên tục cải thiện hàm dự đoán bằng cách lặp nhiều lần qua tập dữ liệu, mỗi lần lặp lại cập nhật giá trị trọng số và hệ số điều chỉnh theo hướng quy định bởi độ dốc của hàm chi phí (gradient).
Huấn luyện hoàn thành khi ta đạt đến một ngưỡng sai số chấp nhận được, hoặc khi các vòng lặp tiếp theo không thể giúp giảm chi phí đi được nữa.

Trước khi huấn luyện, ta cần phải khởi tạo các trọng số (theo giá trị mặc định), quy định các :ref:`siêu tham số (hyperparameters) <glossary_hyperparameters>` (tốc độ học và số vòng lặp huấn luyện), và chuẩn bị ghi lại nhật ký quá trình học qua mỗi lần lặp.

.. rubric:: Code

::

  def train(radio, sales, weight, bias, learning_rate, iters):
      cost_history = []

      for i in range(iters):
          weight,bias = update_weights(radio, sales, weight, bias, learning_rate)

          # Tính chi phí
          cost = cost_function(radio, sales, weight, bias)
          cost_history.append(cost)

          # Ghi lại nhật ký quá trình học của mô hình
          if i % 10 == 0:
              print "iter={:d}    weight={:.2f}    bias={:.4f}    cost={:.2}".format(i, weight, bias, cost)

      return weight, bias, cost_history


Đánh giá mô hình
----------------

Nếu mô hình của chúng ta thực sự hoạt động, ta sẽ thấy chi phí giảm dần sau mỗi vòng lặp.

.. rubric:: Nhật ký huấn luyện

::

  iter=1     weight=.03    bias=.0014    cost=197.25
  iter=10    weight=.28    bias=.0116    cost=74.65
  iter=20    weight=.39    bias=.0177    cost=49.48
  iter=30    weight=.44    bias=.0219    cost=44.31
  iter=30    weight=.46    bias=.0249    cost=43.28

.. rubric:: Đồ thị hàm dự đoán qua mỗi vòng lặp

.. image:: images/linear_regression_line_1.png
    :scale: 80
    :align: center

.. image:: images/linear_regression_line_2.png
    :scale: 80
    :align: center

.. image:: images/linear_regression_line_3.png
    :scale: 80
    :align: center

.. image:: images/linear_regression_line_4.png
    :scale: 80
    :align: center


.. rubric:: Chi phí qua mỗi vòng lặp

.. image:: images/linear_regression_training_cost.png
    :scale: 80
    :align: center


Tổng kết
--------

Sau khi học được giá trị trọng số :math:`(.46)` và hệ số điều chỉnh :math:`(.25)`, ta lúc này thu được một phương trình đơn giản giúp dự đoán doanh thu dựa trên mức đầu tư vào quảng cáo qua đài radio.

.. math::

  \text{Doanh thu} = .46 Radio + .025

Liệu mô hình này có thể hoạt động tốt trong thực tế? Các bạn hãy thử suy nghĩ xem nhé :)



Hồi quy đa biến
===============

Giả sử ta được cung cấp `tập dữ liệu <http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv>`_ gồm số tiền quảng cáo qua TV, radio, và báo của một loạt các công ty, và mục đích của chúng ta là dự đoán doanh thu tính bằng số sản phẩm bán ra.

+----------+-------+-------+------+-----------+
| Công ty  | TV    | Radio | Báo  | Doanh thu |
+----------+-------+-------+------+-----------+
| Amazon   | 230.1 | 37.8  | 69.1 | 22.1      |
+----------+-------+-------+------+-----------+
| Google   | 44.5  | 39.3  | 23.1 | 10.4      |
+----------+-------+-------+------+-----------+
| Facebook | 17.2  | 45.9  | 34.7 | 18.3      |
+----------+-------+-------+------+-----------+
| Apple    | 151.5 | 41.3  | 13.2 | 18.5      |
+----------+-------+-------+------+-----------+

Khi số đặc trưng tăng lên, độ phức tạp của mô hình cũng tăng theo, và càng lúc càng khó để vẽ đồ thị biểu diễn trực quan hay quan trọng hơn là để hiểu được dữ liệu.

.. image:: images/linear_regression_3d_plane_mlr.png
    :align: center

Một trong những giải pháp là tách dữ liệu ra thành nhiều phần và chỉ so sánh 1-2 đặc trưng một lúc.
Trong hình minh hoạ trên, ta sẽ khảo sát sự ảnh hưởng của việc đầu tư vào quảng cáo qua TV và Radio lên Doanh thu.


Chuẩn hoá
---------

Khi số đặc trưng tăng lên, việc tính toán gradient cũng tốn nhiều thời gian hơn.
Ta có thể đẩy nhanh việc này bằng cách "chuẩn hoá" dữ liệu đầu vào để đảm bảo rằng tất cả các giá trị nằm trong cùng một khoảng.
Quá trình này vô cùng quan trọng đối với những tập dữ liệu có độ lệch chuẩn lớn hoặc có sự khác nhau đáng kể trong khoảng giá trị của các đặc trưng.
Mục tiêu của chúng ta lúc này là chuẩn hoá các đặc trưng sao cho tất cả chúng đều trong khoảng từ :math:`-1` đến :math:`1`.

.. rubric:: Code

.. code-block:: md

  Với mỗi cột đặc trưng {
      #1 Trừ đi giá trị trung bình của cột (chuẩn hoá trung bình - mean normalization)
      #2 Chia cho khoảng giá trị của cột (biến đổi tỉ lệ theo đặc trưng - feature scaling)
  }

Đầu vào của chúng ta là ma trận :math:`200 \times 3` bao gồm dữ liệu TV, Radio, và báo.
Đầu ra sẽ là một ma trận được chuẩn hoá có cùng kích thước với tất cả các giá trị đều trong khoảng từ :math:`-1` đến :math:`1`.

::

  def normalize(features):
      **
      features     -   (200, 3)
      features.T   -   (3, 200)

      Ta chuyển vị ma trận đầu vào (.T), hoán đổi hàng với cột
      để giúp các hàm toán học thực hiện dễ dàng hơn.
      **

      for feature in features.T:
          fmean = np.mean(feature)
          frange = np.amax(feature) - np.amin(feature)

          # Phép trừ vector
          feature -= fmean

          # Phép chia vector
          feature /= frange

      return features

.. note::

  **Phép toán trên ma trận**. Trước khi tiếp tục, bạn cần hiểu các khái niệm cơ bản của :doc:`đại số tuyến tính <linear_algebra>` cũng như một số hàm numpy như `numpy.dot() <https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html>`_.


.. _multiple_linear_regression_predict:

Đưa ra dự đoán
--------------

Hàm dự đoán có đầu ra là doanh thu ước lượng dựa theo các trọng số (hệ số) hiện có và khoản đầu tư của công ty vào quảng cáo qua TV, Radio, và báo.
Mô hình của chúng ta sẽ cố gắng tìm ra các giá trị trọng số sao cho hàm chi phí là tối thiểu.

.. math::

  \text{Doanh thu} = W_1 \text{TV} + W_2 \text{Radio} + W_3 \text{Báo}

::

  def predict(features, weights):
    **
    features - (200, 3)
    weights - (3, 1)
    predictions - (200,1)
    **
    predictions = np.dot(features, weights)
    return predictions


Khởi tạo trọng số
----------------

::

  W1 = 0.0
  W2 = 0.0
  W3 = 0.0
  weights = np.array([
      [W1],
      [W2],
      [W3]
  ])


Hàm chi phí
-----------

Ta cần một hàm chi phí để đánh giá xem mô hình đang chạy thế nào.
Công thức toán thì vẫn vậy, ngoại trừ việc biểu thức :math:`mx + b` được đổi thành :math:`W_1 x_1 + W_2 x_2 + W_3 x_3`.
Ta cũng chia biểu thức này thành 2 phần nhằm đơn giản hoá bước tính đạo hàm riêng.

.. math::

  MSE =  \frac{1}{2N} \sum_{i=1}^{n} (y_i - (W_1 x_1 + W_2 x_2 + W_3 x_3))^2

::

  def cost_function(features, targets, weights):
      **
      features:(200,3)
      targets: (200,1)
      weights:(3,1)
      **
      N = len(targets)

      predictions = predict(features, weights)

      # Các phép toán trên ma trận cho phép ta viết lệnh như sau
      # mà không cần vòng lặp
      sq_error = (predictions - targets)**2

      # Trả về trung bình bình phương sai số của tất cả các dự đoán
      return 1.0/(2*N) * sq_error.sum()


Hạ Gradient
-----------

Một lần nữa bằng cách sử dụng :ref:`quy tắc chuỗi <chain_rule>`, ta có thể tính gradient--một vector của các đạo hàm riêng mô tả độ dốc của hàm chi phí với từng trọng số.

.. math::

  \begin{align}
  f'(W_1) = -x_1(y - (W_1 x_1 + W_2 x_2 + W_3 x_3)) \\
  f'(W_2) = -x_2(y - (W_1 x_1 + W_2 x_2 + W_3 x_3)) \\
  f'(W_3) = -x_3(y - (W_1 x_1 + W_2 x_2 + W_3 x_3))
  \end{align}

::

  def update_weights(features, targets, weights, lr):
      '''
      Features:(200, 3)
      Targets: (200, 1)
      Weights:(3, 1)
      '''
      predictions = predict(features, weights)

      # Tách riêng từng đặc trưng
      x1 = features[:,0]
      x2 = features[:,1]
      x3 = features[:,2]

      # Sử dụng phép nhân ma trận có hướng để tính đồng thời
      # các đạo hàm riêng cho các trọng số
      d_w1 = -x1*(targets - predictions)
      d_w2 = -x2*(targets - predictions)
      d_w3 = -x3*(targets - predictions)

      # Cập nhật các trọng số bằng cách trừ đi tích giá trị trung bình đạo hàm với tốc độ học
      # (nhớ rằng gradient có hướng là hướng dốc nhất theo chiều ĐI LÊN)
      weights[0][0] -= (lr * np.mean(d_w1))
      weights[1][0] -= (lr * np.mean(d_w2))
      weights[2][0] -= (lr * np.mean(d_w3))

      return weights

Và đó là toàn bộ về Hồi quy tuyến tính đa biến.



Đơn giản hoá với ma trận
-----------------------

Đoạn code hạ gradient ở trên có khá nhiều đoạn trùng lặp.
Liệu bằng cách nào đó ta có thể cải thiện vấn đề này?
Một trong những cách để tổ chức lại đoạn code này là lặp qua từng đặc trưng và trọng số -- cho phép hàm có thể tính toán với bao nhiêu đặc trưng cũng được.
Tuy nhiên, có một kỹ thuật khác tốt hơn nhiều: *vector hoá thuật toán hạ gradient*.

.. rubric:: Công thức toán học

Ta sử dụng y nguyên công thức ở trên, nhưng thay vì thực hiện trên từng đặc trưng một, ta sử dụng toán tử nhân ma trận để tính toán với tất cả các đặc trưng và trọng số cùng một lúc.
Ta thay các ký hiệu :math:`x_i` bằng một ma trận đặc trưng duy nhất :math:`X`.

.. math::

  gradient = -X(targets - predictions)

.. rubric:: Code

::

  X = [
      [x1, x2, x3]
      [x1, x2, x3]
      .
      .
      .
      [x1, x2, x3]
  ]

  targets = [
      [1],
      [2],
      [3]
  ]

  def update_weights_vectorized(X, targets, weights, lr):
      **
      gradient = X.T * (predictions - targets) / N
      X: (200, 3)
      Targets: (200, 1)
      Weights: (3, 1)
      **
      companies = len(X)

      #1 - Dự đoán kết quả
      predictions = predict(X, weights)

      #2 - Tính sai số/lỗi
      error = targets - predictions

      #3 - Chuyển vị ma trận đặc trưng từ kích thước (200, 3) về (3, 200)
      # để ta có thể nhân với ma trận sai số (200,1).
      # Trả về một ma trận (3,1) gồm có 3 đạo hàm riêng -
      # mỗi đạo hàm cho một đặc trưng -- đại diện cho tổng độ nghiêng
      # của hàm chi phí qua tất cả các quan sát.
      gradient = np.dot(-X.T,  error)

      #4 - Tính trung bình đạo hàm của sai số với mỗi đặc trưng
      gradient /= companies

      #5 - Nhân gradient với tốc độ học
      gradient *= lr

      #6 - Cập nhật trọng số bằng cách trừ đi gradient để tối thiểu hoá chi phí
      weights -= gradient

      return weights


Hệ số điều chỉnh
---------------

Hàm huấn luyện ở trên giống với trường hợp hồi quy tuyến tính đơn giản, tuy nhiên ta sẽ thay đổi một chút trước khi kết thúc: thêm một :ref:`hệ số điều chỉnh <glossary_bias_term>` vào ma trận đặc trưng.

Trong ví dụ ở trên, khó mà có thể xảy ra trường hợp doanh thu bằng 0 nếu như các công ty ngừng quảng cáo.
Lý do cho việc này có thể bao gồm các quảng cáo trong quá khứ, mối quan hệ với các khách hàng hiện có, vị trí cửa hàng, và đội ngũ kinh doanh.
Một hệ số điều chỉnh sẽ giúp ta nắm bắt được trường hợp không quảng cáo này.

.. rubric:: Code

Ở đoạn code dưới đây, ta thêm hằng số :math:`1` vào ma trận đặc trưng.
Bằng cách đặt giá trị này bằng :math:`1`, ta coi như hệ số điều chỉnh là một hằng số, và các trọng số tương ứng với từng hệ số điều chỉnh sẽ được học như các trọng số bình thường.

::

  bias = np.ones(shape=(len(features),1))
  features = np.append(bias, features, axis=1)


Đánh giá mô hình
----------------

Sau khi huấn luyện mô hình qua 1000 bước lặp với tốc độ học :math:`0.0005`, ta thu được một tập trọng số mầ ta có thể sử dụng để đưa ra dự đoán

.. math::

  \text{Doanh thu} = 4.7 \text{TV} + 3.5 \text{Radio} + .81 \text {Báo} + 13.9

MSE giảm từ :math:`110.86` xuống :math:`6.25`.

.. image:: images/multiple_regression_error_history.png
    :align: center
    :scale: 0.8


.. rubric:: Tài liệu tham khảo

.. [1] https://en.wikipedia.org/wiki/Linear_regression
.. [2] http://www.holehouse.org/mlclass/04_Linear_Regression_with_multiple_variables.html
.. [3] http://machinelearningmastery.com/simple-linear-regression-tutorial-for-machine-learning
.. [4] http://people.duke.edu/~rnau/regintro.htm
.. [5] https://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression
.. [6] https://www.analyticsvidhya.com/blog/2015/08/common-machine-learning-algorithms
