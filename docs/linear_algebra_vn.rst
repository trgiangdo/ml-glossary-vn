.. _linear_algebra:

=================
Đại số tuyến tính
=================

.. contents:: :local:

Đại số tuyến tính là một bộ công cụ toán học rất hữu dụng trong việc biến đổi và xử lý đồng thời các nhóm số liệu.
Trong đại số tuyến tính, các nhóm số liệu này được biểu diễn dưới dạng các vector và các ma trận (các bảng tính cũng là 1 dạng ma trận), đồng thời các phép cộng, trừ, nhân, chia cũng được định nghĩa lại.
Phần này sẽ mô tả khái quát các khái niệm cơ bản của đại số tuyến tính, nhất là các khái niệm được sử dụng nhiều trong học máy.

Vector - Hướng lượng
===================

Vector là các mảng 1 chiều chứa các số hoặc các biểu thức.
Trong hình học, vector biểu thị độ lớn, phương, và chiều của một sự thay đổi (ví dụ như tác động lực) lên 1 điểm trong không gian gọi là điểm gốc.
Ví dụ trong hệ toạ độ Descartes 2 chiều, vector :math:`[3, -2]` ám chỉ rằng từ điểm gốc ta di chuyển sang phải 3 đơn vị và đi xuống 2 đơn vị.
Một vector với nhiều hơn 1 chiều được gọi là một ma trận.

Ký hiệu
-------

Có rất nhiều cách để biểu diễn vector.
Dưới đây là một số cách thông dụng.

.. math::

  v = \begin{bmatrix}
  1 \\
  2 \\
  3 \\
  \end{bmatrix}
  =
  \begin{pmatrix}
  1 \\
  2 \\
  3 \\
  \end{pmatrix}
  =
  \begin{bmatrix}
  1 & 2 & 3\\
  \end{bmatrix}


Vector trong hình học
---------------------

Vector thường biểu diễn một sự thay đổi đối với 1 điểm trong không gian hình học.

.. figure:: images/vectors_geometry.png
    :align: center

    Vector :math:`[5, -2]` trong hệ toạ độ Descartes

Một vector có thể áp dụng vào bất cứ điểm nào trong không gian.
Chiều của vector bằng với độ dốc của đường chéo được vẽ bởi việc di chuyển theo mô tả của vector.
Ví dụ với vector :math:`[5, -2]` như hình minh hoạ trên, chiều của vector là đường chéo được tạo thành bằng cách di chuyển lên phía trên 5 và sang trái 2 đơn vị.
Độ lớn của vector bằng với độ dài của đường chéo đó.


Các phép toán với 1 số - *Scalar operations*
--------------------------------------------

Trong đại số tuyến tính, ta chỉnh sửa các vector bằng cách cộng, trừ, hay nhân 1 số với tất cả các giá trị thành phần của vector.
Các phép toán này trên vector được gọi là các phép toán với 1 số.

.. math::

  \begin{bmatrix}
  2 \\
  2 \\
  2 \\
  \end{bmatrix}
  +
  1
  =
  \begin{bmatrix}
  3 \\
  3 \\
  3 \\
  \end{bmatrix}


Các phép toán theo từng phần tử - *Elementwise operations*
----------------------------------------------------------

Đối với các phép toán giữa 2 vector trên từng phần tử như cộng, trừ, và chia, các giá trị tại cùng 1 vị trí được kết hợp với nhau để tạo ra 1 vector mới.
Phần từ đầu tiên của vector A được cặp với phần tử đầu tiên của vector B.
Phần từ thứ 2 của vector A được cặp với phần tử thứ 2 của vector B, và tương tự.
Điều này có nghĩa là các vector phải có cùng số phần tử, hay số chiều, để có thể tham gia thực hiện các phép toán này.

.. math::

  \begin{bmatrix}
  a_1 \\
  a_2 \\
  \end{bmatrix}
  +
  \begin{bmatrix}
  b_1 \\
  b_2 \\
  \end{bmatrix}
  =
  \begin{bmatrix}
  a_1+b_1 \\
  a_2+b_2 \\
  \end{bmatrix}

::

  y = np.array([1,2,3])
  x = np.array([2,3,4])
  y + x = [3, 5, 7]
  y - x = [-1, -1, -1]
  y / x = [.5, .67, .75]

Đoạn code trên minh hoạ các phép toán này sử dụng thư viện numpy.
Tuy các phép toán này yêu cầu các vector phải có số chiều bằng nhau, trong numpy có cung cấp :ref:`cơ chế broadcasting <numpy_broadcasting>` giúp các phép toán trên ma trận và vector được thực hiện dễ dàng hơn và sẽ được trình bày kỹ hơn sau.


.. _dot_product:

Tích vô hướng - *Dot product*
-----------------------------

Tích vô hướng của hai vector là một số vô hướng.
Tích vô hướng gữa các vector và ma trận (:ref:`phép nhân ma trận <matrix_multiplication>`) là một trong những phép toán quan trọng nhất trong học sâu.


.. math::

  \begin{bmatrix}
  a_1 \\
  a_2 \\
  \end{bmatrix}
  \cdot
  \begin{bmatrix}
  b_1 \\
  b_2 \\
  \end{bmatrix}
  = a_1 b_1+a_2 b_2

::

  y = np.array([1,2,3])
  x = np.array([2,3,4])
  np.dot(y,x) = 20


Tích Hadamard
-------------
Tích Hadamard giữa 2 vector là phép nhân theo từng phần tử (*elementwise multiplication*) và trả về một vector.

.. math::

  \begin{bmatrix}
  a_1 \\
  a_2 \\
  \end{bmatrix}
   \odot
  \begin{bmatrix}
  b_1 \\
  b_2 \\
  \end{bmatrix}
  =
  \begin{bmatrix}
  a_1 \cdot b_1 \\
  a_2 \cdot b_2 \\
  \end{bmatrix}

::

  y = np.array([1,2,3])
  x = np.array([2,3,4])
  y * x = [2, 6, 12]


Trường vector
-------------

Một trường vector là một kết cấu gán cho mỗi điểm trong không gian 1 vector tương ứng, giúp biểu diễn một điểm trong không gian :math:`(x,y)` sẽ di chuyển thế nào nếu ta áp dụng một phép toán vector lên điểm đó, ví dụ như cộng hay nhân [2]_.

.. figure:: images/vector_field.png
    :align: center

    Trường vector :math:`(sin(y), sin(x))`

Khác với 1 vector thông thường, trường vector tác động theo các hướng và độ lớn khác nhau phụ thuộc vào điểm gốc.
Lý do vì các vector trong trường vector có dạng các biểu thức :math:`2x` hay :math:`x^2` thay vì các số vô hướng như :math:`-2` hay :math:`5`.
Với mỗi điểm trong đồ thị, ta tính :math:`2x` hay :math:`x^2` theo trục hoành và vẽ một mũi tên từ điểm gốc đó tới vị trí mới.
Hình minh hoạ trên biểu diễn trường vector :math:`(sin(y), sin(x))`.
Trường vector rất hữu dụng trong việc biểu diễn một cách trực quan các kỹ thuật tối ưu trong học máy như :doc:`gradient_descent_vn`.


Ma trận - *Matrices*
====================

Một ma trận là một mảng hình chữ nhật chứa các số, các ký hiệu, hoặc các biểu thức (giống như một bảng tính Excel) với các quy tắc cộng, trừ, và nhân đặc biệt.

Chiều - *Dimensions*
--------------------

Ta mô tả các chiều của một ma trận dưới dạng hàng và cột.

.. math::

  \begin{bmatrix}
  2 & 4 \\
  5 & -7 \\
  12 & 5 \\
  \end{bmatrix}
  \begin{bmatrix}
  a² & 2a & 8\\
  18 & 7a-4 & 10\\
  \end{bmatrix}

Ma trận đầu tiên có chiều :math:`(3,2)`, hay 3 hàng 2 cột.
Ma trận thứ hai có chiều :math:`(2,3)`.

::

  a = np.array([
   [1,2,3],
   [4,5,6]
  ])
  a.shape == (2,3)
  b = np.array([
   [1,2,3]
  ])
  b.shape == (1,3)


Các phép toán với 1 số
-----------------

Các phép toán với 1 số của ma trận cũng giống như các vector, chỉ đơn giản là áp dụng phép toán với số đó cho từng phần tử của ma trận khi cộng, trừ, nhân, chia, ... một ma trận với 1 số.

.. math::

  \begin{bmatrix}
  2 & 3 \\
  2 & 3 \\
  2 & 3 \\
  \end{bmatrix}
  +
  1
  =
  \begin{bmatrix}
  3 & 4 \\
  3 & 4 \\
  3 & 4 \\
  \end{bmatrix}

::

  # Cộng ma trận với 1 số
  a = np.array(
  [[1,2],
   [3,4]])
  a + 1
  [[2,3],
   [4,5]]


Các phép toán theo từng phần tử - *Elementwise operations*
----------------------------------------------------------

Để có thể cộng, trừ, hay chia 2 ma trận thì 2 ma trận đó cần có cùng số chiều.
Ta kết hợp các giá trị tương ứng theo từng vị trí để tạo ra ma trận mới.

.. math::

  \begin{bmatrix}
  a & b \\
  c & d \\
  \end{bmatrix}
  +
  \begin{bmatrix}
  1 & 2\\
  3 & 4 \\
  \end{bmatrix}
  =
  \begin{bmatrix}
  a+1 & b+2\\
  c+3 & d+4 \\
  \end{bmatrix}

::

  a = np.array([
   [1,2],
   [3,4]])
  b = np.array([
   [1,2],
   [3,4]])

  a + b
  [[2, 4],
   [6, 8]]

  a — b
  [[0, 0],
   [0, 0]]


Tích Hadamard
-------------

Tích Hadamard giữa các ma trận là phép nhân theo từng phần tử (*elementwise multiplication*).
Các giá trị tương ứng theo từng vị trí được nhân với nhau và trả về một ma trận mới.

.. math::

  \begin{bmatrix}
  a_1 & a_2 \\
  a_3 & a_4 \\
  \end{bmatrix}
  \odot
  \begin{bmatrix}
  b_1 & b_2 \\
  b_3 & b_4 \\
  \end{bmatrix}
  =
  \begin{bmatrix}
  a_1 \cdot b_1 & a_2 \cdot b_2 \\
  a_3 \cdot b_3 & a_4 \cdot b_4 \\
  \end{bmatrix}

::

  a = np.array(
  [[2,3],
   [2,3]])
  b = np.array(
  [[3,4],
   [5,6]])

  # Sử dụng toán tử nhân của Python
  a * b
  [[ 6, 12],
   [10, 18]]

Trong thư viện numpy, ta có thể tính tích Hadamard của một ma trận với một vector nếu như số chiều của chúng thoả mãn điều kiện của :ref:`cơ chế broadcasting <numpy_broadcasting>`.

.. math::

  \begin{bmatrix}
  {a_1} \\
  {a_2} \\
  \end{bmatrix}
  \odot
  \begin{bmatrix}
  b_1 & b_2 \\
  b_3 & b_4 \\
  \end{bmatrix}
  =
  \begin{bmatrix}
  a_1 \cdot b_1 & a_1 \cdot b_2 \\
  a_2 \cdot b_3 & a_2 \cdot b_4 \\
  \end{bmatrix}


Ma trận chuyển vị - *Matrix transpose*
-------------------------------------

Mạng nơ-ron thường xuyên phải tính toán các trọng số và đầu vào với các kích thước khác nhau và không thoả mãn điều kiện của :ref:`phép nhân ma trận <matrix_multiplication>`.
Phép chuyển vị ma trận (*Matrix transposition*), thường được ký hiệu bằng chỉ số trên 'T' ví dụ như :math:`M^T`, cho phép ta "xoay" một ma trận sao cho ma trận mới tuân theo điều kiện của phép nhân ma trận và giúp việc tính toán dễ dàng hơn.
Phép chuyển vị ma trận gồm 2 bước:

  1. Xoay phải ma trận 90°

  2. Đảo thứ tự của mỗi phần tử tại mỗi hàng (ví dụ, :math:`[a\ b\ c]` thành :math:`[c\ b\ a]`)

Ví dụ sau đảo ma trận :math:`M` thành ma trận :math:`T`:

.. math::

  \begin{bmatrix}
  a & b \\
  c & d \\
  e & f \\
  \end{bmatrix}
  \quad \Rightarrow \quad
  \begin{bmatrix}
  a & c & e \\
  b & d & f \\
  \end{bmatrix}

::

  a = np.array([
     [1, 2],
     [3, 4]])

  a.T
  [[1, 3],
   [2, 4]]


.. _matrix_multiplication:

Nhân ma trận
------------

Không phải tất cả các ma trận đều có thể nhân được với nhau.
Để thực hiện phép nhân các ma trận với nhau và tạo thành ma trận mới, cần thoả mãn các điều kiện sau:

**Điều kiện**


  1. Số cột của ma trận thứ nhất phải bằng với số hàng của ma trận thứ 2.

  2. Tích của một ma trận kích thước M x N và một ma trận kích thước N x K là một ma trận kích thước M x K, tức là số chiều của ma trận mới là số hàng của ma trận đầu tiên và số cột của ma trận thứ 2.

**Các bước nhân ma trận**

Phép nhân ma trận phụ thuộc vào :ref:`tích vô hướng <dot_product>` giữa các hàng và cột của 2 ma trận ban đầu.
Trong hình minh hoạ ở dưới, được trích từ khoá học về đại số tuyến tính trên Khan Academy [3]_, mỗi phần tử của ma trận :math:`C` là một tích vô hướng của một hàng của ma trận :math:`A` và một cột của ma trận :math:`B`.

.. image:: images/khan_academy_matrix_product.png
    :align: center

Thao tác :math:`a_1 \cdot b_1` nghĩa là ta tính tích vô hướng giữa hàng đầu tiên của ma trận :math:`A` :math:`[1,7]` với cột đầu tiên của ma trận :math:`B` :math:`[3,5]`.

.. math::

  a_1 \cdot b_1 =
  \begin{bmatrix}
  1 \\
  7 \\
  \end{bmatrix}
  \cdot
  \begin{bmatrix}
  3 \\
  5 \\
  \end{bmatrix}
  = (1 \cdot 3) + (7 \cdot 5) = 38

.. math::

  \begin{bmatrix}
  a & b \\
  c & d \\
  e & f \\
  \end{bmatrix}
  \cdot
  \begin{bmatrix}
  1 & 2 \\
  3 & 4 \\
  \end{bmatrix}
  =
  \begin{bmatrix}
  1a + 3b & 2a + 4b \\
  1c + 3d & 2c + 4d \\
  1e + 3f & 2e + 4f \\
  \end{bmatrix}


Thư viện Numpy
=============

Tích vô hướng
-------------

Thư viện numpy sử dụng hàm :code:`np.dot(A,B)` cho cả phép nhân ma trận và vector.
Hàm này có một số chức năng khá hay à bạn đọc có thể tham khảo thêm `tại đây <https://numpy.org/doc/stable/reference/generated/numpy.dot.html>`_ để sử dụng hiệu quả hơn.

::

  a = np.array([
   [1, 2]
   ])
  a.shape == (1,2)
  b = np.array([
   [3, 4],
   [5, 6]
   ])
  b.shape == (2,2)

  # Nhân ma trận
  mm = np.dot(a,b)
  mm == [13, 16]
  mm.shape == (1,2)


.. _numpy_broadcasting:

Cơ chế Broadcasting
-------------------

Trong numpy, các yêu cầu về chiều trong phép nhân từng phân tử khá thoải mái nhờ một cơ chế có tên gọi **broadcasting**.
Hai ma trận được coi là phù hợp nếu các chiều tương ứng của mỗi ma trận (hàng với hàng, hoặc cột với cột) thoả mãn một trong 2 điều kiện sau:

    1. Tất cả các số chiều là bằng nhau, hoặc

    2. Có 1 chiều có kích thước bằng 1

::

  a = np.array([
   [1],
   [2]
  ])
  b = np.array([
   [3,4],
   [5,6]
  ])
  c = np.array([
   [1,2]
  ])

  # Có cùng số hàng
  # Nhưng khác số cột
  # Tuy nhiên vẫn nhân từng phần tử được do số cột của a bằng 1
  a * b
  [[ 3, 4],
   [10, 12]]

  # Có cùng số cột
  # Nhưng khác số hàng
  # Tuy nhiên vẫn nhân từng phần tử được do số hàng của c bằng 1
  b * c
  [[ 3, 8],
   [5, 12]]

  # Khác số hàng
  # Khác số hàng
  # Nhưng cả a và c đều thoả mãn điều kiện
  # có kích thước 1 chiều bằng 1
  a + c
  [[2, 3],
   [3, 4]]


.. rubric:: Một số tài liệu hướng dẫn về đại số tuyến tính

- `Khan Academy Linear Algebra <https://medium.com/r/?url=https%3A%2F%2Fwww.khanacademy.org%2Fmath%2Flinear-algebra>`_

- `Deep Learning Book Math <https://medium.com/r/?url=http%3A%2F%2Fwww.deeplearningbook.org%2Fcontents%2Fpart_basics.html>`_

- `Andrew Ng Course Notes <https://medium.com/r/?url=https%3A%2F%2Fwww.coursera.org%2Flearn%2Fmachine-learning%2Fresources%2FJXWWS>`_

- `Linear Algebra Better Explained <https://medium.com/r/?url=https%3A%2F%2Fbetterexplained.com%2Farticles%2Flinear-algebra-guide%2F>`_

- `Understanding Matrices Intuitively <https://medium.com/r/?url=http%3A%2F%2Fblog.stata.com%2F2011%2F03%2F03%2Funderstanding-matrices-intuitively-part-1%2F>`_

- `Intro To Linear Algebra <https://medium.com/r/?url=http%3A%2F%2Fwww.holehouse.org%2Fmlclass%2F03_Linear_algebra_review.html>`_

- `Immersive Math <https://medium.com/r/?url=http%3A%2F%2Fimmersivemath.com%2Fila%2Findex.html>`_


.. rubric:: Tài liệu tham khảo

.. [1] http://mathinsight.org/vector_introduction
.. [2] https://en.wikipedia.org/wiki/Vector_field
.. [3] https://www.khanacademy.org/math/precalculus/precalc-matrices/properties-of-matrix-multiplication/a/properties-of-matrix-multiplication
