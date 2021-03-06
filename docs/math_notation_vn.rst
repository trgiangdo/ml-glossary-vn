.. _math_notation:

================
Ký hiệu Toán học
================

Các ký hiệu toán học thường được sử dụng trong các văn bản và tài liệu về học máy.

.. contents:: :local:



Đại số tuyến tính
-----------------

+-----------------+---------------+------------------------------------------------------+-----------------------------------+
| Ký hiệu         | Tên gọi       | Mô tả                                                | Ví dụ                             |
+=================+===============+======================================================+===================================+
| :math:`[\ ]`    | ngoặc vuông   | ma trận hoặc vector                                  | :math:`v = [1\ 3\ 5]`             |
+-----------------+---------------+------------------------------------------------------+-----------------------------------+
| :math:`\cdot`   | nhân vô hướng | tính tích vô hướng giữa 2 vector hoặc nhân 2 ma trận | :math:`Z = X \cdot W`             |
+-----------------+---------------+------------------------------------------------------+-----------------------------------+
| :math:`\odot`   | tích Hadamard | tính tích Hadamard hay nhân theo từng phần tử        | :math:`A = B \odot C`             |
+-----------------+---------------+------------------------------------------------------+-----------------------------------+
| :math:`X^T`     | chuyển vị     | ma trận chuyển vị                                    | :math:`W^T \cdot X`               |
+-----------------+---------------+------------------------------------------------------+-----------------------------------+
| :math:`\vec{x}` | vector        |                                                      |                                   |
+-----------------+---------------+------------------------------------------------------+-----------------------------------+
| :math:`X`       | ma trận       | các ký tự viết hoa là ma trận                        | :math:`X, W, B`                   |
+-----------------+---------------+------------------------------------------------------+-----------------------------------+
| :math:`\hat{u}` | vector đơn vị | vector có độ lớn bằng :math:`1`                      | :math:`\hat{u} = [0.2\ 0.5\ 0.3]` |
+-----------------+---------------+------------------------------------------------------+-----------------------------------+


Giải tích
---------

+---------------------+------------------------+------------------------------------------------------------------+---------------------------------------------+
| Ký hiệu             | Tên gọi                | Mô tả                                                            | Ví dụ                                       |
+=====================+========================+==================================================================+=============================================+
| :math:`x'`          | đạo hàm                | đạo hàm bậc 1 của hàm số                                         | :math:`(x^2)' = 2x`                         |
+---------------------+------------------------+------------------------------------------------------------------+---------------------------------------------+
| :math:`x''`         | đạo hàm bậc 2          | đạo hàm bậc 2 của hàm số, tức là đạo hàm của đạo hàm bậc 1       | :math:`(x^2)'' = 2`                         |
+---------------------+------------------------+------------------------------------------------------------------+---------------------------------------------+
| :math:`\lim`        | giới hạn               | giá trị giới hạn của hàm số khi 1 biến tiến tới 1 giá trị nào đó | :math:`\lim_{x \to \infty} f(x)`            |
+---------------------+------------------------+------------------------------------------------------------------+---------------------------------------------+
| :math:`\nabla`      | nabla                  | ký hiệu gradient của 1 hàm số                                    | :math:`\nabla f(a,b,c)`                     |
+---------------------+------------------------+------------------------------------------------------------------+---------------------------------------------+
| :math:`(f \circ g)` | hàm hợp                | là hàm lồng trong hàm                                            | :math:`(f \circ g)(x) = f(g(x))`            |
+---------------------+------------------------+------------------------------------------------------------------+---------------------------------------------+
| :math:`\Delta`      | delta                  | mô tả giá trị biến thiên                                         | :math:`\Delta x = x_1 - x_0`                |
+---------------------+------------------------+------------------------------------------------------------------+---------------------------------------------+
| :math:`e`           | hằng số Euler          | :math:`e = 2.718281828`                                          | :math:`s = \frac{1}{1+e^{-z}}`              |
+---------------------+------------------------+------------------------------------------------------------------+---------------------------------------------+
| :math:`\sum`        | phép lấy tổng (sigma)  | tổng tất cả các giá trị                                          | :math:`\sum x_i = x_1 + x_2 + x_3`          |
+---------------------+------------------------+------------------------------------------------------------------+---------------------------------------------+
| :math:`\prod`       | phép lấy tích (Pi hoa) | tích tất cả các giá trị                                          | :math:`\prod x_i = x_1 \cdot x_2 \cdot x_3` |
+---------------------+------------------------+------------------------------------------------------------------+---------------------------------------------+
| :math:`\epsilon`    | epsilon                | một số rất bé gần :math:`0`                                      | :math:`\epsilon = 1e-4`                     |
+---------------------+------------------------+------------------------------------------------------------------+---------------------------------------------+


Xác suất thống kê
-----------------

+-------------------------------------------+-------------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| Ký hiệu                                   | Tên gọi           | Mô tả                                                                            | Ví dụ                                         |
+===========================================+===================+==================================================================================+===============================================+
| :math:`\mu`                               | trung bình        | trung bình, hay kỳ vọng, của phân phối xác suất (theo biến ngẫu nhiên :math:`X`) |                                               |
+-------------------------------------------+-------------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| :math:`\bar{x}`                           | trung bình mẫu    | trung bình của tập mẫu ngẫu nhiên lấy từ phân phối gốc, hay trung bình số học    | :math:`\bar{x} = \frac{2 + 5 + 9}{3} = 5.333` |
+-------------------------------------------+-------------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| :math:`\tilde{x}`                         | trung vị          | trung vị của phân phối xác suất / mẫu                                            |                                               |
+-------------------------------------------+-------------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| :math:`\sigma^2` hoặc :math:`var(X)`      | phương sai        | phương sai của phân phối xác suất (theo biến ngẫu nhiên :math:`X`)               |                                               |
+-------------------------------------------+-------------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| :math:`s^2`                               | phương sai mẫu    | phương sai của tập mẫu ngẫu nhiên                                                |                                               |
+-------------------------------------------+-------------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| :math:`\sigma` hoặc :math:`std(X)`        | độ lệch chuẩn     | độ lệch chuẩn của phân phối xác suất (theo biến ngẫu nhiên :math:`X`)            |                                               |
+-------------------------------------------+-------------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| :math:`s`                                 | độ lệch chuẩn mẫu | độ lệch chuẩn của tập mẫu ngẫu nhiên                                             |                                               |
+-------------------------------------------+-------------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| :math:`\rho (X,Y)` hoặc :math:`corr(X,Y)` | tương quan        | độ tương quan giữa hai biến ngẫu nhiên :math:`X` và :math:`Y`                    |                                               |
+-------------------------------------------+-------------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| :math:`P(A)`                              | xác suất          | xác suất xảy ra của sự kiện A                                                    | :math:`P(x=1) = 0.5`                          |
+-------------------------------------------+-------------------+----------------------------------------------------------------------------------+-----------------------------------------------+


Tập hợp
-------

+---------------+---------+--------------------------------------------------------------------+----------------------------+
| Ký hiệu       | Tên gọi | Mô tả                                                              | Ví dụ                      |
+===============+=========+====================================================================+============================+
| :math:`\{\ \}`| tập hợp | mô tả 1 tập các phần tử khác nhau, thường có cùng tính chất nào đó | :math:`S = \{1, 5, 7, 9\}` |
+---------------+---------+--------------------------------------------------------------------+----------------------------+


.. rubric:: Tài liệu tham khảo

.. [1] http://www.rapidtables.com/math/symbols/Basic_Math_Symbols.htm

