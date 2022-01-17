.. _logistic_regression:

======================================
Hồi quy Logistic (Logistic Regression)
======================================

.. contents:: :local:

Giới thiệu
==========

Hồi quy logistic là một thuật toán được sử dụng để phân loại các quan sát theo các danh mục rời rạc.
Thay vì có đầu ra là các giá trị liên tục như thuật toán hồi quy tuyến tính, hồi quy logistic đưa đầu ra qua hàm logistic sigmoid để trả về một giá trị biểu thị xác suất mà quan sát đầu vào thể hiện tính chất của hai hay nhiều hơn các danh mục rời rạc.

.. note::
	- Tuy thường được sử dụng trong các bài toán "phân loại", bản thân hồi quy logistic không phải là một thuật toán phân loại mà là một thuật toán hồi quy. Thuật toán này ước lượng xác suất của các kết quả khả dĩ và kết hợp với một số quy tắc (giá trị ngưỡng) để đưa ra quyết định phân loại.

	- Tên gọi "Logistic" xuất phát từ hàm lôgit được sử dụng trong thuật toán này để tìm ra mối quan hệ giữa bộ dự đoán tuyến tính và trung bình của hàm xác suất.


So sánh với hồi quy tuyến tính
------------------------------

Giả sử ta có một tập dữ liệu bao gồm thời gian học tập và điểm kiểm tra của học sinh.
:doc:`linear_regression_vn` và hồi quy logistic sẽ dự đoán theo các cách thức khác nhau:

	- **Hồi quy tuyến tính** có thể giúp ta dự đoán điểm kiểm tra của học sinh theo thang điểm 100. Dự đoán của hồi quy tuyến tính là giá trị liên tục (trong một khoảng giá trị).

	- **Hồi quy logistic** có thẻ giúp ta dự đoán liệu học sinh đó sẽ đỗ hay trượt bài kiểm tra. Dự đoán của hồi quy logistic là giá trị rời rạc (các giá trị cụ thể hoặc các danh mục). Ta cũng có thể xem được xác suất làm cơ sở cho cách phân loại từng danh mục của mô hình.

Phân loại hồi quy logistic
----------------------------

  - Nhị phân (Đỗ/Trượt)
  - Đa lớp (Chó, Mèo, Thỏ, ...)
  - Thứ tự (Cao, Trung bình, Thấp)


Hồi quy logistic nhị phân
=========================

Giả sử ta được cung cấp `dữ liệu <http://scilab.io/wp-content/uploads/2016/07/data_classification.csv>`_ về kết quả kỳ thi của học sinh và mục tiêu của ta là dự đoán liệu một học sinh sẽ đỗ hay trượt bài kiểm tra dựa trên số giờ ngủ và số giờ học bài của học sinh đó.
Ta có hai đặc trưng (số giờ ngủ, số giờ học) và hai danh mục: đỗ (1) và trượt (0).


+----------------+---------------+--------+
| **Số giờ học** | **Số giờ ngủ** | **Đỗ** |
+----------------+---------------+--------+
| 4.85           | 9.63          | 1      |
+----------------+---------------+--------+
| 8.62           | 3.23          | 0      |
+----------------+---------------+--------+
| 5.43           | 8.23          | 1      |
+----------------+---------------+--------+
| 9.21           | 6.34          | 0      |
+----------------+---------------+--------+

Ta có thể biểu diễn dữ liệu này dưới dạng biểu đồ phân tán như sau.

.. figure:: images/logistic_regression_exam_scores_scatter.png
    :alt: scatter plot of exam scores
    :align: center

    Biểu đồ phân tán dữ liệu


Kích hoạt Sigmoid
------------------

Để có thể ánh xạ các giá trị dự đoán với xác suất, ta sử dụng hàm :ref:`sigmoid <activation_sigmoid>`.
Hàm này ánh xạ bất cứ dữ liệu thực nào thành một giá trị trong khoảng từ :math:`0` đến :math:`1`.
Trong học máy, ta sử dụng hàm sigmoid để ánh xạ các dự đoán với xác suất.

.. rubric:: Công thức toán học

.. math::

  S(z) = \frac{1} {1 + e^{-z}}

Trong đó:
  - :math:`s(z)` = đầu ra trong khoảng từ :math:`0` đến :math:`1` (giá trị xác suất ước lượng)
  - :math:`z` = đầu vào của hàm (giá trị dự đoán của thuật toán, ví dụ như :math:`mx + b`)
  - :math:`e` = hằng số Euler, và là cơ số của logarit tự nhiên

.. rubric:: Đồ thị

.. figure:: images/sigmoid.png
	:alt: graph of sigmoid function
	:align: center
	:scale: 80

	Đồ thị hàm số Sigmoid

.. rubric:: Code

.. literalinclude:: ../code/activation_functions.py
    :language: python
    :pyobject: sigmoid


Ranh giới quyết định (Decision boundary)
---------------------------------------

Hàm dự đoán của ta lúc này sẽ trả về giá trị xác suất trong khoảng từ :math:`0` đến :math:`1`.
Để có thể ánh xạ xác suất này tới các danh mục rời rạc (đúng/sai, chó/mèo), ta cần chọn một giá trị ngưỡng mà nếu xác suất lớn hơn giá trị này thì ta sẽ phân loại thành danh mục đó, còn nếu thấp hơn thì ta phân loại thành danh mục còn lại.

.. math::

  p \geq 0.5, class=1 \\
  p < 0.5, class=0

Ví dụ, nếu giá trị ngưỡng là :math:`0.5` và hàm dự đoán trả về :math:`0.7`, ta có thể phân loại điểm dữ liệu đó là dương tính.
Nếu dự đoán là :math:`0.2` thì ta có thể phân loại điểm đữ liệu đó là âm tính.
Đối với hồi quy tuyến tính đa lớp, ta có thể chọn danh mục mà có xác suất dự đoán cao nhất.

.. figure:: images/logistic_regression_sigmoid_w_threshold.png
	:align: center
	:alt: decision boundary

	Ranh giới quyết định (màu xanh lam). Các giá trị ở phía trên ranh giới là dương tính, còn lại là âm tính.


Đưa ra dự đoán
--------------

Với các kiến thức về hàm sigmoid và ranh giới quyết định, lúc này ta có thể viết hàm dự đoán cho mô hình.
Một hàm dự đoán trong hồi quy logistic trả về xác suất mà quan sát đầu vào là dương tính, nghĩa là việc quan sát đầu vào thuộc danh mục đó là Đúng (True).
Ta gọi danh mục này là :math:`1` và được ký hiệu là :math:`P(class=1)`.
Khi xác suất này tiến gần tới :math:`1`, mô hình sẽ càng chắc chắn hơn là quan sát đó thuộc danh mục :math:`1`.


Ở phần này, ta sử dụng :ref:`phương trình dự đoán hồi quy tuyến tính đa biến <multiple_linear_regression_predict>` từ bài hướng dẫn trước về hồi quy tuyến tính.

.. math::

  z = W_0 + W_1 \times \text{\{Số giờ học\}} + W_2 \times \text{\{Số giờ ngủ\}}

Khác với bài hồi quy tuyến tính, ở đây ta sẽ biến đổi đầu ra qua hàm sigmoid để trả về giá trị xác suất từ :math:`0` đến :math:`1`.

.. math::

  P(class=1) = \frac{1} {1 + e^{-z}}

Nếu mô hình trả về :math:`0.4` thì có nghĩa là mô hình tin rằng học sinh đó chỉ có 40% cơ hội đỗ.
Nếu ranh giới quyết định bằng :math:`0.5`, ta có thể phân loại quan sát này là "Trượt".

.. rubric:: Code

Ta sẽ lồng hàm sigmoid ra ngoài hàm dự đoán của :ref:`hồi quy tuyến tính đa biến <multiple_linear_regression_predict>`.

.. literalinclude:: ../code/logistic_regression.py
    :language: python
    :pyobject: predict


Hàm chi phí
-----------

Đáng tiếc rằng ta không thể (hay đúng hơn là không nên) sử dụng cùng hàm chi phí :ref:`trung bình bình phương sai số <mse>` như trong hồi quy tuyến tính.
Chương 3 trong cuốn sách về học sâu (deep learning) của Michael Neilson [5]_ giải thích rất chi tiết về vấn đề này về mặt toán học, tuy nhiên ở đây ta chỉ cần hiểu đơn giản rằng lý do là vì hàm dự đoán trong hồi quy logistic là phi tuyến (do biến đổi sigmoid).
Bình phương dự đoán như trong MSE sẽ tạo ra một hàm không lồi (non-convex) với rất nhiều cực tiểu cục bộ.
Nếu hàm chi phí có nhiều cực tiểu cục bộ, thuật toán hạ gradient sẽ khó mà có thể tìm được điểm tối ưu tại cực tiểu toàn cục.

.. rubric:: Công thức toán học

Thay vì sử dụng MAE, ta sẽ sử dụng một hàm chi phí có tên gọi là :ref:`loss_cross_entropy`, hay cũng có thể gọi là hàm mất mát Log.
Hàm chi phí entropy chéo được chia làm hai hàm chi phí riêng biệt: một hàm cho :math:`y=1` và một cho :math:`y=0`.

.. math::
	J(\theta) = \frac{1}{m} \sum_{i=1}^{m} Cost(h_{\theta}(x^{(i)}), y^{(i)}) \\

trong đó:

.. math::
	& Cost(h_{\theta}(x^{(i)}), y^{(i)}) = -\log(h_{\theta}(x))	&& \text{ nếu } y=1	\\
	& Cost(h_{\theta}(x^{(i)}), y^{(i)}) = -\log(1 - h_{\theta}(x)) && \text{ nếu } y=0

Lợi ích của việc sử dụng logarit có thể thấy rõ qua đồ thị của hàm chi với lần lượt với :math:`y=1` và :math:`y=0`.
Các hàm số trơn đơn điệu (luôn tăng hoặc luôn giảm) giúp việc tính toán gradient và tối thiểu chi phí dễ dàng hơn.

.. figure:: images/y1andy2_logistic_function.png
	:align: center

	Hình vẽ minh hoạ được trích từ slide về hồi quy logistic của Andrew Ng [1]_.

Ý tưởng chủ đạo của hàm chi phí cần chú ý là nó "phạt" các dự đoán sai với độ chắc chắn cao nhiều hơn so với "thưởng" các dự đoán đúng với độ chắc chắn cao.
Cụ thể, ví dụ với :math:`y=1`, khi mô hình dự đoán đúng và trả về :math:`h_{\theta}(x)` tiến tới :math:`1` thì hàm entropy chéo trả về chi phí xấp xỉ :math:`0`, tuy nhiên khi mô hình dự đoán sai với :math:`h_{\theta}(x)` tiến tới :math:`0` thì giá trị hàm entropy chéo trả về tiến tới vô cực theo cấp số mũ.
Hệ quả là với độ chính xác càng cao thì chi phí hàm trả về càng thấp do bản chất logistic của hàm chi phí.

.. rubric:: Công thức ngắn gọn

.. math::
	J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} [y^{(i)} \log(h_{\theta}(x^{(i)})) + (1-y^{(i)}) \log(1 - h_{\theta}(x^{(i)}))]

Phương trình trên nhân từng hàm chi phí với :math:`y` và :math:`(1-y)` để ta có thể sử dụng cùng một hàm cho cả hai trường hợp :math:`y=1` và :math:`y=0`.
Nếu :math:`y=0`, số hạng đầu tiên trong phép cộng bị khử.
Nếu :math:`y=1`, số hạng thứ hai bị khử.
Đối với cả hai trường hợp, ta chỉ tính toán đúng vế mà ta cần tính.

.. rubric:: Vectorized cost function

.. math::
	J(\theta) = \frac{1}{m} \cdot (-y^T log(h) - (1-y)^T log(1-h))

trong đó:

.. math::
	h = g(X \cdot \theta)

.. rubric:: Code

.. literalinclude:: ../code/logistic_regression.py
    :language: python
    :pyobject: cost_function


Hạ gradient
-----------

Để tối thiểu hoá mất mát, ta sử dụng :doc:`gradient_descent_vn` giống như mô tả trong :doc:`linear_regression_vn`.
Có nhiều thuật toán tối ưu khác phức tạp hơn ví dụ như :ref:`gradient liên hợp <optimizers_lbfgs>`, tuy nhiên bạn không cần phải quá tập trung vào các thuật toán này.
Các thư viện học máy như Scikit-learn hỗ trợ toàn bộ phần lập trình chúng để bạn có thể tập trung vào các vấn đề khác thú vị hơn.

.. rubric:: Công thức toán học

Một trong những tính chất hay nhất của hàm sigmoid là công thức đạo hàm của nó rất đẹp.
Nếu bạn quan tâm, có một bài khá hay mô tả chi tiết đạo hàm này trên stackoverflow [6]_.
Tác giả Michael Neilson cũng có trình bày vấn đề này trong chương 3 trong quyển sách về học sâu của ông ấy.

.. math::

  	s'(z) = s(z)(1 - s(z))

Which leads to an equally beautiful and convenient cost function derivative:
từ đây ta có thể suy ra công thức đạo hàm rất đẹp và dễ tính toán của hàm chi phí:


.. math::

  C' = x(s(z) - y)

trong đó:

  - :math:`C'` là đạo hàm chi phí theo các trọng số.
  - :math:`y` là nhãn thực mô tả danh mục quan sát được (:math:`0` hoặc :math:`1`).
  - :math:`s(z)` là dự đoán của mô hình.
  - :math:`x` là đặc trưng, hay vector các đặc trưng.

Chú ý rằng gradient này giống với gradient của :ref:`MSE <mse>`, khác biệt duy nhất nằm ở hàm giả định *(hypothesis function)*.

.. rubric:: Mã giả

::

  Repeat {

    1. Tính trung bình gradient
    2. Nhân với tốc độ học
    3. Trừ tích trên khỏi các trọng số

  }

.. rubric:: Code

.. literalinclude:: ../code/logistic_regression.py
    :language: python
    :pyobject: update_weights


.. Mapping probabilities to classes
Ghép xác suất với các lớp
-------------------------

The final step is assign class labels (0 or 1) to our predicted probabilities.
Bước cuối cùng là gán nhãn các danh mục (:math:`0` hoặc :math:`1`) cho các giá trị xác suất mô hình dự đoán.

.. rubric:: Ranh giới quyết định

.. literalinclude:: ../code/logistic_regression.py
    :language: python
    :pyobject: decision_boundary

.. rubric:: Ánh xạ xác suất sang các danh mục

.. literalinclude:: ../code/logistic_regression.py
    :language: python
    :pyobject: classify

.. rubric:: Example output

::

	Probabilities = [ 0.967, 0.448, 0.015, 0.780, 0.978, 0.004]
  	Classifications = [1, 0, 0, 1, 1, 0]


Huấn luyện
--------

Our training code is the same as we used for :ref:`linear regression <simple_linear_regression_training>`.
Code huấn luyện mô hình trong ví dụ này giống với đoạn code sử dụng trong :ref:`hồi quy tuyến tính <simple_linear_regression_training>`.

.. literalinclude:: ../code/logistic_regression.py
    :language: python
    :pyobject: train


Đánh giá mô hình
----------------

Nếu mô hình của chúng ta thực sự hoạt động, ta sẽ thấy chi phí giảm dần sau mỗi vòng lặp.

::

  iter: 0 cost: 0.635
  iter: 1000 cost: 0.302
  iter: 2000 cost: 0.264

**Chi phí sau huấn luyện:**  0.2487.  **Trọng số sau huấn luyện:** [-8.197, .921, .738]

.. rubric:: Nhật ký huấn luyện

.. figure:: images/logistic_regression_loss_history.png
    :align: center

    Đồ thị chi phí của hồi quy logistic trong quá trình huấn luyện.

.. rubric:: Độ chính xác

:ref:`Độ chính xác <glossary_accuracy>` đo khả năng dự đoán của mô hình.
Trong trường hợp này, ta chỉ đơn giản so sánh nhãn được dự đoán với nhãn thực tế và chia cho tổng số các quan sát kiểm tra.

.. literalinclude:: ../code/logistic_regression.py
    :language: python
    :pyobject: accuracy


.. rubric:: Ranh giới quyết định

Một kỹ thuật hữu ích khác để có thể biểu diễn độ chính xác của mô hình một cách trực quan là vẽ ranh giới quyết định trên cùng đồ thị với các dự đoán của mô hình để so sánh nhãn dự đoán với nhãn thực.
Để thực hiện việc này, ta cần vẽ đồ thị các xác suất mà mô hình dự đoán và tô màu các quan sát dựa theo giá trị nhãn thực.
Trong đồ thị dưới, các xác suất phía trên ranh giới quyết định sẽ được phân loại là "True", tuy nhiên mô hình phân loại sai một số quan sát thành "False" (màu đỏ), và ngược lại đối với vùng phía dưới ranh giới.

.. figure:: images/logistic_regression_final_decision_boundary.png
    :align: center

    Ranh giới quyết định sau huấn luyện.

.. rubric:: Code để vẽ đồ thị với ranh giới quyết định

.. literalinclude:: ../code/logistic_regression.py
    :language: python
    :pyobject: plot_decision_boundary


Hồi quy logistic đa lớp (Multiclass logistic regression)
========================================================

Thay vì :math:`y = {0,1}`, ta sẽ mở rộng định nghĩa này thành :math:`y = {0,1...n}`.
Ý tưởng cơ bản để giải quyết bài toàn này là ta sẽ chạy thuật toán phân loại nhị phân nhiều lần, mỗi lần tương ứng với phân loại một danh mục.

Thuật toán
----------

* Chia nhỏ bài toán thành :math:`n` bài toán phân loại nhị phân.
* Với mỗi danh mục:
    * Dự đoán xác suất mà các quan sát thuộc danh mục đó.
* :math:`\text{dự đoán} = max(\text{xác suất quan sát thuộc các danh mục})`

For each sub-problem, we select one class (YES) and lump all the others into a second class (NO). Then we take the class with the highest predicted value.
Với mỗi bài toán con, ta chọn một danh mục (:math:`1`) và coi tất cả các danh mục còn lại là một danh mục duy nhất (:math:`0`).
Sau khi hoàn thành dự đoán xác suất của tất cả các bài toán con, ta phân loại quan sát vào danh mục với giá trị dự đoán cao nhất.


Kích hoạt Softmax
-----------------

Hàm kích hoạt softmax (có tên gọi khác là softargmax hay hàm trung bình mũ) là một hàm nhận đầu vào là vector gồm K số thực, và chuẩn hoá nó thành một phân phối xác suất gồm có K xác suất được chia tỉ lệ theo hàm mũ tự nhiên của các số đầu vào.
Nghĩa là trước khi áp dụng hàm softmax, một số phần tử của vector có thể mang dấu âm, hoặc lớn hơn :math:`1`, hay tổng các phần tử vector đầu vào có thể không bằng :math:`1`; tuy nhiên sau khi áp dụng hàm softmax, mỗi phân tử xác suất đầu ra sẽ có giá trị trong khoảng :math:`[0,1]`, và tổng các xác suất sẽ bằng :math:`1` để đảm bảo điều kiện tổng các xác suất của một quan sát bằng :math:`1`.

Hàm softmax chuẩn được định nghĩa bằng công thức sau.

.. math::

   \sigma(z_i) & = \frac{e^{z_{(i)}}}{\sum_{j=1}^K e^{z_{(j)}}} \\
   \text{for } & i=1,.,.,.,K \\
   \text{and } & z=z_1,.,.,.,z_K

In words: we apply the standard exponential function to each element :math:`z_i` of the input vector :math:`z` and normalize these values by dividing by the sum of all these exponentials; this normalization ensures that the sum of the components of the output vector :math:`σ(z)` is 1. [9]_
Nói cách khác: ta áp dụng hàm mũ tự nhiên lên từng phần tử :math:`z_i` của vector đầu vào :math:`z` và chuẩn hoá các giá trị này bằng cách chia cho tổng tất cả các hàm mũ; việc chuẩn hoá giúp đảm bảo rằng tổng của các phần tử của vector xác suất đầu ra :math:`\sigma(z)` bằng :math:`1`.


Ví dụ với Scikit-Learn
----------------------

Hãy cùng so sánh hiệu năng mô hình trên với mô hình ``LogisticRegression`` cung cấp bởi scikit-learn [8]_.

.. literalinclude:: ../code/logistic_regression_scipy.py


**Độ chính xác của Scikit:**  0.88. **Độ chính xác mô hình trên:** 0.89


.. rubric:: Tài liệu tham khảo

.. [1] http://www.holehouse.org/mlclass/06_Logistic_Regression.html
.. [2] http://machinelearningmastery.com/logistic-regression-tutorial-for-machine-learning
.. [3] https://scilab.io/machine-learning-logistic-regression-tutorial/
.. [4] https://github.com/perborgen/LogisticRegression/blob/master/logistic.py
.. [5] http://neuralnetworksanddeeplearning.com/chap3.html
.. [6] http://math.stackexchange.com/questions/78575/derivative-of-sigmoid-function-sigma-x-frac11e-x
.. [7] https://en.wikipedia.org/wiki/Monotoniconotonic_function
.. [8] http://scikit-learn.org/stable/modules/linear_model.html#logistic-regression>
.. [9] https://en.wikipedia.org/wiki/Softmax_function
