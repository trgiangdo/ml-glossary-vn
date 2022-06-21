.. _cost_function:

==============================
Hàm Mất mát - *Loss Functions*
==============================

.. contents:: :local:


.. _loss_cross_entropy:

Entropy chéo - *Cross-Entropy*
==============================

Mất mát entropy chéo, hay mất mát log, đo hiệu năng của mô hình phân loại đưa ra kết quả dự đoán là giá trị xác xuất từ :math:`0` đến :math:`1`.
Mất mát entropy chéo tăng khi giá trị xác xuất dự đoán bị lệch xa khỏi nhãn thực tế.
Tức là nếu mô hình dự đoán xác suất :math:`0.012` trong khi nhãn của quan sát đó trong thực tế là :math:`1` (tức là dự đoán sai hoàn toàn) thì giá trị mất mát sẽ rất cao.

Một mô hình phân loại hoàn hảo sẽ có mất mát log bằng :math:`0`.

.. image:: images/cross_entropy.png
    :align: center

Đồ thị trên mô tả khoảng giá trị của hàm mất mát entropy chéo theo một quan sát dương tính (:code:`isDog = 1`).
Với giá trị xác suất dự đoán tiến tới :math:`1`, mất mát log giảm rất chậm và tiến tới :math:`0`.
Tuy nhiên, khi xác suất dự đoán giảm dần, mất mát log tăng theo cấp số nhân và tiến tới vô cùng.
Điều này có nghĩa là dù mất mát log phạt tất cả giá trị dự đoán khác giá trị nhãn thực, những dự đoán sai với độ tin cậy cao sẽ bị phạt rất nặng.

.. note::

Mất mát entropy chéo và mất mát log có 1 chút khác biệt tuỳ thuộc vào cách dùng, nhưng trong học máy khi giá trị đầu ra trong khoảng từ :math:`0` đến :math:`1`, chúng có ý nghĩa tương đương nhau.

.. rubric:: Code

.. literalinclude:: ../code/loss_functions.py
    :pyobject: CrossEntropy

.. rubric:: Công thức toán học

Trong bài toán phân loại nhị phân, khi số danh mục :math:`M = 2`, entropy chéo có thể được tính bằng:

.. math::

    -{(y\log(p) + (1 - y)\log(1 - p))}

Nếu :math:`M > 2` (tức là bài toán phân loại đa lớp), ta tính mất mát cho từng danh mục theo mỗi quan sát và sau đó tính tổng mất mát.

.. math::

    -\sum_{c=1}^My_{o,c}\log(p_{o,c})

trong đó:

    - :math:`M` là số danh mục.
    - :math:`\log` là hàm logarit tự nhiên.
    - :math:`y` là chỉ mục (mang giá trị :math:`1` hoặc :math:`0`) thể hiện việc phân loại quan sát :math:`o` vào danh mục :math:`c` là đúng hay sai.
    - :math:`p` là xác suất dự đoán quan sát :math:`o` thuộc danh mục :math:`c`.


.. _hinge_loss:

Mất mát Hinge
=============

Là mất mát được sử dụng trong bài toán phân loại.

.. rubric:: Code

.. literalinclude:: ../code/loss_functions.py
    :pyobject: Hinge


.. _huber_loss:

Mất mát Huber
=============

Mất mát Huber thường được sử dụng trong bài toán hồi quy.
Loại mất mát này ít bị ảnh hưởng bởi các điểm dữ liệu ngoại lai hơn so với MSE do nó chỉ tính bình phương lỗi trong một khoảng nhất định (:math:`[-\delta, \delta]`), ngoài khoảng đó lỗi được tính theo hàm tuyến tính.

.. rubric:: Công thức toán học

.. math::

  L_{\delta}=\left\{\begin{matrix}
  \frac{1}{2}(y - \hat{y})^{2} & if \left | (y - \hat{y})  \right | < \delta\\
  \delta ((y - \hat{y}) - \frac1 2 \delta) & otherwise
  \end{matrix}\right.

.. rubric:: Code

.. literalinclude:: ../code/loss_functions.py
      :pyobject: Huber

Bạn đọc có thể tham khảo `Trang Wikipedia về Mất mát Huber`_.

.. _`Huber Loss in Wikipedia`: https://en.wikipedia.org/wiki/Huber_loss

.. _kl_divergence:

Mất mát Kullback-Leibler
========================

.. rubric:: Code

.. literalinclude:: ../code/loss_functions.py
    :pyobject: KLDivergence


.. _mae:

MAE (L1)
========

Trung bình Sai số Tuyệt đối (*Mean Absolute Error - MAE*), hay mất mát L1.
Bạn đọc có thể tham khảo thêm chi tiết trong bài viết [9]_ và [10]_.

.. rubric:: Code

.. literalinclude:: ../code/loss_functions.py
      :pyobject: L1


.. _mse:

MSE (L2)
========

Trung bình Bình phương Sai số (*Mean Squared Error - MSE*), hay mất mát L2.
Bạn đọc có thể tham khảo thêm chi tiết trong bài viết [9]_ và [10]_.

.. literalinclude:: ../code/loss_functions.py
    :language: python
    :pyobject: MSE

.. literalinclude:: ../code/loss_functions.py
    :language: python
    :pyobject: MSE_prime


.. rubric:: Tài liệu tham khảo

.. [1] https://en.m.wikipedia.org/wiki/Cross_entropy
.. [2] https://www.kaggle.com/wiki/LogarithmicLoss
.. [3] https://en.wikipedia.org/wiki/Loss_functions_for_classification
.. [4] http://www.exegetic.biz/blog/2015/12/making-sense-logarithmic-loss/
.. [5] http://neuralnetworksanddeeplearning.com/chap3.html
.. [6] https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient
.. [7] https://en.wikipedia.org/wiki/Huber_loss
.. [8] https://en.wikipedia.org/wiki/Hinge_loss
.. [9] http://rishy.github.io/ml/2015/07/28/l1-vs-l2-loss/
.. [10] http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization/
