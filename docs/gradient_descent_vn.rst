.. _gradient_descent:

==============================
Hạ Gradient (Gradient Descent)
==============================

Hạ Gradient là một thuật toán tối ưu được sử dụng để tối thiểu hoá một hàm nào đó bằng cách liên tục di chuyển hàm chi phí theo hướng dốc nhất hướng xuống được định nghĩa bởi chiều âm của gradient.
Trong học máy, ta sử dụng hạ gradient để cập nhật :ref:`các tham số <glossary_parameters>` trong mô hình.
Các tham số ở đây chính là các hệ số trong :doc:`hồi quy tuyến tính<linear_regression>` và :ref:`các trọng số <nn_weights>` trong mạng nơ-ron.


Giới thiệu
==========

Xét đồ thị 3 chiều dưới đây mô tả một hàm chi phí, với toạ độ chính là các tham số của mô hình.
Mục tiêu của chúng ta là phải đi từ đỉnh núi ở góc trên bên phải (chi phí cao) xuống vùng nước biển sâu phía dưới bên trái (chi phí thấp).
Các mũi tên mô tả hướng dốc nhất theo chiều xuống (chiều âm của gradient) từ bất kì điểm nào--hướng mà sẽ giảm hàm chi phí nhanh nhất.

.. figure:: images/gradient_descent.png
   :alt: Gradient Descent illustration.
   :align: center

   `Nguồn ảnh. <http://www.adalta.it/Pages/-GoldenSoftware-Surfer-010.asp>`_

Bắt đầu từ đỉnh núi, ta đi 1 bước theo dốc xuống có hướng được xác định bởi chiều âm của gradient.
Sau đó ta tính lại chiều âm của gradient (bằng cách đưa vào toạ độ của vị trí mới) và tiếp tục đi thêm 1 bước nữa theo hướng được chỉ định.
Ta tiếp tục quá trình này cho đến khi ta đến được đáy của đồ thị, hoặc tới một vị trí mà không còn dốc xuống để đi nữa--một cực tiểu cục bộ.


Tốc độ học
==========

Kích thước của từng bước di chuyển ở trên được gọi là *tốc độ học (learning rate)*.
Với tốc độ học cao, ta có thể bước xa hơn với mỗi bước di chuyển, tuy nhiên có nguy cơ sẽ bước lệch khỏi điểm thấp nhất do độ dốc của địa hình thay đổi liên tục.
Với một tốc độ học quá thấp, ta có thể tự tin di chuyển theo chiều âm của gradient do ta liên tục tính lại giá trị này.
Tốc độ học thấp sẽ cho độ chính xác tốt hơn, tuy nhiên việc tính gradient nhiều lần rất tốn thời gian, do đó ta sẽ cần nhiều thời gian hơn để bước được tới đáy.


Hàm chi phí
===========

Một :ref:`hàm chi phí <cost_function>` cho ta biết "khả năng" của mô hình trong việc đưa ra dự đoán với một tập tham số nhất định.
Độ dốc của đồ thị này cho ta biết nên cập nhật các tham số như thế nào để giúp dự đoán đầu ra chính xác hơn.


Ứng dụng
========

Thuật toán hạ gradient được ứng dụng rất phổ biến trong học máy.
Bạn đọc có thể đọc thêm chi tiết cách thức lập trình hạ gradient trong :doc:`linear_regression_vn` hay :doc:`logistic_regression_vn` và nhiều mô hình khác.

Các biến thể (TODO)
===================


.. rubric:: References

.. [1] http://sebastianruder.com/optimizing-gradient-descent/
