.. _calculus:

========
Giải tích
========

.. contents:: :local:


.. _introduction:

Giới thiệu
==========

Phần này sẽ giới thiệu một số thuật ngữ giải tích cơ bản để tính toán sự biến thiên của hàm số theo thời gian (đạo hàm), và tính tổng giá trị của một hàm tích luỹ theo thời gian (tích phân).
Các thuật ngữ giải tích sẽ giúp ta phát biểu chính xác các tính chất của các hàm toán học và hiểu cách hoạt động của chúng một cách tốt hơn.

Thông thường, việc tham gia một khoá học giải tích sẽ yêu cầu học sinh phải làm rất nhiều bài tập tính toán dài dòng, nhưng nếu tận dụng được khả năng tính toán của máy tính thì sẽ giúp quá trình này thú vị hơn nhiều.
Phần này sẽ mô tả một số khái niệm căn bản trong giải tích mà bạn cần phải biết để có thể hiểu các khái niệm học máy.


.. _derivative:

Đạo hàm - *Derivatives*
=======================

Một đạo hàm có thể được định nghĩa theo 2 cách:

  #. Sự thay đổi tức thời (Vật lý)
  #. Độ nghiêng của một đường thẳng tại một điểm nhất định (Hình học)

Cả hai cách định nghĩa trên đều mô tả một nguyên lý chung, nhưng với các bài toán trong học máy, sẽ dễ hiểu hơn nếu ta sử dụng định nghĩa đạo hàm hình học.


Định nghĩa đạo hàm trong hình học
--------------------------------

Trong hình học, độ nghiêng (*slope*) biểu diễn mức độ dốc của một đường thẳng.
Giá trị này trả lời câu hỏi: giá trị :math:`y` hay :math:`f(x)` thay đổi bao nhiêu khi :math:`x` thay đổi một lượng nhất định?
Xét đồ thị dưới, với hàm :math:`f(x) = x^2 + 3`.

.. image:: images/calculus_slope_intro.png
    :align: center

Sử dụng công thức hệ số góc của một đường thằng, độ nghiêng của đoạn thẳng từ điểm :math:`(1,4)` đến :math:`(3,12)` là:

.. math::

    \text{Độ nghiêng} = \frac{y2-y1}{x2-x1} = \frac{12-4}{3-1} = 4

Nhưng nếu như thay vì đo độ dốc giữa 2 điểm, ta cần phải tính độ dốc tại 1 điểm duy nhất trên đường thẳng đó thì sao?
Giả sử, làm thế nào để ta tính độ dốc tại điểm :math:`(1,4)`?
Trường hợp này sẽ không có hai điểm nào cụ thể nào để tính toán hệ số góc.

Một cách để có thể thực hiện việc này là tìm ra hai điểm gần nhất, tính độ dốc tương đối theo :math:`x` và lấy trung bình độ dốc.
Nhưng trong giải tích có một công cụ cho phép thực hiện việc tính độ dốc tại 1 điểm dễ dàng và chính xác hơn: đạo hàm.
Tính đạo hàm của một hàm số về cơ bản thì giống với cách sử dụng hai điểm gần nhất, nhưng thay vì thực sự đi tìm hai điểm đó, ta tạo ra một điểm ảo cách :math:`x` một khoảng rất nhỏ và tính độ dốc giữa :math:`x` và điểm ảo mới.

Bằng cách này, đạo hàm giúp ta trả lời câu hỏi: :math:`f(x)` thay đổi như thế nào nếu ta tăng giá trị :math:`x` lên 1 lượng rất rất nhỏ?
Nói cách khác, đạo hàm giúp ta *ước lượng* độ dốc của 2 điểm cách nhau một khoảng rất nhỏ nhưng đủ để tính độ dốc.
Trong toán học, ta biểu diễn khoảng cách rất rất nhỏ đó bằng một giới hạn (*limit*, viết tắt trong các công thức toán học là :math:`\lim`).
Giới hạn được định nghĩa là giá trị của một hàm số khi đầu vào tiến đến một giá trị nào đó.
Trong trường hợp trên, giá trị :math:`x` tiến tới điểm mà ta cần đo độ dốc tại đó.

Tóm lại, đạo hàm là một biểu thức mô tả sự biến thiên của hàm số tại một điểm nào đó, tức là ta có thể sử dụng đạo hàm để tính *sự thay đổi tức thời*, hay độ dốc, của một điểm trên đồ thị.
Sau khi tìm ra được đạo hàm, ta có thể sử dụng hàm đó để tính độ dốc tức thời của bất cứ điểm nào trên đồ thị.

Các bước tính đạo hàm
---------------------

Tính đạo hàm cũng giống như tính độ dốc thông thường, chỉ khác là độ dốc giữa điểm cần tính đạo hàm và 1 điểm khác rất gần với nó.
Ta sử dụng biến :math:`h` để biểu diễn khoảng cách rất nhỏ.
Các bước tính đạo hàm bao gồm:

1. Cho hàm sau:

.. math::

  f(x) = x^2

2. Tăng :math:`x` lên một khoảng rất rất nhỏ :math:`h (h = Δx)`

.. math::

  f(x + h) = (x + h)^2

3. Áp dụng công thức hệ số góc

.. math::

  \frac{f(x + h) - f(x)}{h}

4. Rút gọn phương trình

.. math::

  \frac{x^2 + 2xh + h^2 - x^2}{h} \\

  \frac{2xh+h^2}{h} = 2x+h

5. Đặt :math:`h` bằng :math:`0` (tức là tính giới hạn của độ dốc khi :math:`h` tiến tới :math:`0`).

.. math::

  {2x + 0} = {2x}

Công thức ta thu được ở bước trên có nghĩa là với hàm :math:`f(x) = x^2`, độ dốc tại bất kỳ điểm nào bằng :math:`2x`.

Chú ý rằng công thức tính giới hạn ở trên chỉ là 1 trường hợp tính giới hạn đơn giản.
Các hàm số khác có thể có công thức phức tạp hơn, nhưng tóm lại, công thức của đạo hàm được định nghĩa như sau:

.. math::

  \lim_{h\to0}\frac{f(x+h) - f(x)}{h}


.. rubric:: Code

Ta sẽ thử viết 1 đoạn code để tính đạo hàm của bất kỳ hàm số :math:`f(x)` nào.
Ta sẽ kiểm tra thử xem liệu với hàm số đầu vào là :math:`f(x)=x^2`, hàm này có hoạt động tốt và trả về giá trị gần với đạo hàm thực :math:`2x` hay không.

::

    def get_derivative(func, x):
        """Tính đạo hàm của hàm số `func` tại điểm `x`
        bằng cách sử dụng khoảng cách `h` rất nhỏ."""
        h = 0.0001                          # khoảng cách
        return (func(x+h) - func(x)) / h    # độ dốc

    def f(x): return x**2                   # định nghĩa hàm f(x)=x^2

    x = 3                                   # điểm tính độ dốc
    computed = get_derivative(f, x)
    actual = 2*x                            # đạo hàm thực tế

    computed, actual   # = 6.0001, 6        # kết quả ước lượng khá sát với kết quả thực


Thông thường, việc sử dụng toán để tính ra công thức đạo hàm chính xác sẽ tối ưu hơn là xấp xỉ đạo hàm như trên.
Nhưng nhớ rằng, bạn luôn có thể tính xấp xỉ đạo hàm bằng cách tính độ dốc khi di chuyển 1 khoảng cách rất nhỏ :math:`h`.


Ứng dụng trong học máy
----------------------

Trong học máy, đạo hàm được sử dụng rất phổ biến trong các phương pháp tối ưu.
Các thuật toán tối ưu như :docs:`gradient_descent_vn` sử dụng đạo hàm để quyết định liệu nên tăng hay giảm các trọng số để tối đa hoặc tối thiểu hoá hàm mục tiêu nào đó (ví dụ như độ chính xác của mô hình hay hàm chi phí).
Đạo hàm cũng được sử dụng để xấp xỉ các hàm phi tuyến thành hàm tuyến tính (đường tiếp tuyến), với độ dốc là hằng số.
Từ đó ta có thể di chuyển lên hoặc xuống dốc (tăng hoặc giảm trọng số) để tiến gần tới mục tiêu tối ưu.


.. _chain_rule:

Quy tắc chuỗi - *Chain rule*
============================

Quy tắc chuỗi là một công thức giúp tính đạo hàm của các hàm hợp.
Hàm hợp là các hàm mà được tạo thành bởi nhiều hàm được sử dụng làm biến số trong một (nhiều) hàm khác.

Quy tắc
-------

Xét hàm hợp :math:`f(x) = A(B(x))`, đạo hàm của :math:`f(x)` bằng tích đạo hàm của :math:`A` theo :math:`B(x)` và đạo hàm của :math:`B` theo :math:`x`.

.. math::

  \mbox{Đạo hàm hàm hợp} = \mbox{Đạo hàm hàm ngoài} * \mbox{Đạo hàm hàm trong}

Ví dụ, với hàm hợp :math:`f(x)`, trong đó:

.. math::

  f(x) = h(g(x))

Theo quy tắc chuỗi, đạo hàm của :math:`f(x)` bằng

.. math::

    \frac{df}{dx} = \frac{dh}{dg} \cdot \frac{dg}{dx}


Các bước tính toán
------------------

Gọi :math:`f(x)` là hàm hợp của hai hàm :math:`h(x) = x^3` and :math:`g(x) = x^2`. Tức là:

.. math::

    f(x) &= h(g(x)) \\
         &= (x^2)^3

Đạo hàm của :math:`f(x)` bằng:

.. math::

    \frac{df}{dx} & = \frac{dh}{dg} \frac{dg}{dx} \\
                  & = \frac{dh}{d(x^2)} \frac{dg}{dx}


.. rubric:: Các bước

1. Tính đạo hàm của hàm trong :math:`g(x) = x^2`

.. math::

    \frac{dg}{dx} = 2x

2. Tính đạo hàm của hàm ngoài :math:`h(x) = x^3`, sử dụng biến :math:`b` để biểu diễn hàm trong :math:`x^2`

.. math::

    \frac{dh}{db} = 3b^2

3. Thay biến tạm thời :math:`b` bằng hàm trong :math:`g(x)`

.. math::

    3b^2 = 3(x^2)^2 = 3x^4

4. Trả về tích của 2 đạo hàm

.. math::

  \frac{df}{dx} = 3x^4 \cdot 2x = 6x^5


Quy tắc chuỗi cho nhiều hàm
---------------------------

Trong ví dụ trên, ta giả sử hàm hợp chỉ gồm có 1 hàm trong.
Với hàm hợp nhiều cấp độ hơn, quy tắc chuỗi cũng có thể được áp dụng một cách tương tự như sau:

.. math::

  f(x) = A(B(C(x)))

Đạo hàm của hàm trên theo quy tắc chuỗi bằng:

.. math::

    \frac{df}{dx} = \frac{dA}{dB} \frac{dB}{dC} \frac{dC}{dx}

Ta cũng có thể viết đạo hàm của hàm bằng ký hiệu :math:`f'` như sau:

.. math::

  f' = A'(B(C(x)) \cdot B'(C(x)) \cdot C'(x)


.. rubric:: Các bước


Cho hàm :math:`f(x) = A(B(C(x)))`, giả sử:

.. math::

    A(x) & = sin(x) \\
    B(x) & = x^2 \\
    C(x) & = 4x

Đạo hàm của các hàm trên lần lượt bằng:

.. math::

    A'(x) &= cos(x) \\
    B'(x) &= 2x \\
    C'(x) &= 4

Ta tính đạo hàm :math:`f(x)` sử dụng quy tắc chuỗi:

.. math::

  f'(x) = A'( (4x)^2) \cdot B'(4x) \cdot C'(x)

Lần lượt thay các biểu thức đạo hàm vào công thức trên, ta thu được biểu thức rút gọn sau:

.. math::

    f'(x) &= cos((4x)^2) \cdot 2(4x) \cdot 4 \\
            &= cos(16x^2) \cdot 8x \cdot 4 \\
            &= cos(16x^2)32x


.. _gradient:

Gradients
=========

Gradient là một vector cột chứa các đạo hàm riêng của một hàm đa biến, với mục đích giúp ta tính được độ dốc tại một điểm nhất định trên đồ thị của một hàm với nhiều biến độc lập.
Để có thể tính được các độ dốc phức tạp này, ta cần tách biệt từng biến để xét mức ảnh hưởng của nó lên đầu ra.
Ta cần lặp qua từng biến một và tính đạo hàm của hàm số khi coi tất cả các biến còn lại là hằng số.
Mỗi vòng lặp sẽ trả về một đạo hàm riêng và được lưu trong gradient.


Đạo hàm riêng
-------------

Trong các hàm có 2 biến hoặc nhiều hơn, đạo hàm riêng là đạo hàm của hàm số theo 1 biến.
Nếu :math:`x` biến thiên trong khi tất cả các biến còn lại là hằng số, hàm số :math:`f(x,z)` sẽ thay đổi thế nào?
Tương tự, nếu :math:`z` biến khi khi :math:`x` là hằng số, :math:`f(x,z)` sẽ thay đổi thế nào?
Ta lưu các đạo hàm riêng của hàm số vào vector gradient.


Các bước
--------

Các bước sau đây mô tả quá trình tính gradient của một hàm đa biến:

1. Cho hàm đa biến

.. math::

  f(x,z) = 2z^3x^2

2. Tính đạo hàm của hàm số theo biến :math:`x`

.. math::

  \frac{df}{dx}(x,z)

3. Thay :math:`2z^3` bằng một hẳng số giả định :math:`b` (tức là coi :math:`z` là hằng số)

.. math::

  f(x,z) = bx^2

4. Tính đạo hàm theo :math:`x` với hằng số :math:`b`

.. math::

    \frac{df}{dx} & = \lim_{h\to0}\frac{f(x+h) - f(x)}{h} \\
                  & = \lim_{h\to0}\frac{b(x+h)^2 - b(x^2)}{h} \\
                  & = \lim_{h\to0}\frac{b((x+h)(x+h)) - bx^2}{h} \\
                  & = \lim_{h\to0}\frac{b((x^2 + xh + hx + h^2)) - bx^2}{h} \\
                  & = \lim_{h\to0}\frac{bx^2 + 2bxh + bh^2 - bx^2}{h} \\
                  & = \lim_{h\to0}\frac{2bxh + bh^2}{h} \\
                  & = \lim_{h\to0} 2bx + bh

Khi :math:`h —> 0` thì

.. math::

    \frac{df}{dx} = 2bx + 0 = 2bx

5. Thay :math:`2z^3` vào phương trình trên, ta thu được dạng đúng của đạo hàm hàm số theo biến :math:`x`

.. math::

    \frac{df}{dx}(x,z) &= 2(2z^3)x \\
                       &= 4z^3x

6. Lặp lại từ bước 2 để tính đạo hàm hàm số theo biến :math:`z`

.. math::

  \frac{df}{dz}(x,z) = 6x^2z^2

7. Lưu các đạo hàm riêng vào vector gradient

.. math::

    \nabla f(x,z)=\begin{bmatrix}
        \frac{df}{dx} \\
        \frac{df}{dz} \\
    \end{bmatrix}
    = \begin{bmatrix}
        4z^3x \\
        6x^2z^2 \\
    \end{bmatrix}


Đạo hàm có hướng
-----------------------

Một khái niệm quan trọng khác là đạo hàm có hướng.
Khi tính toán các đạo hàm riêng của hàm đa biến ở ví dụ trên, ta sử dụng phương pháp truyền thống là phân tích hàm số khi công một giá trị rất rất nhỏ vào từng biến độc lập để xác định sự ảnh hưởng tới đầu ra theo sự biến thiên của biến đó.
Theo cách tăng từng biến lên 1 khoảng rất rất nhỏ này, ta thay đổi hàm số theo một hướng nhất định.

Nhưng nếu ta muốn tìm đạo hàm theo 1 hướng khác thì sao?
Ví dụ, ta đang đi trên một vùng địa hình đồi núi.
Thông qua việc tính gradient, ta xác định được độ dốc của vị trí hiện tại ta đang đứng theo từng hướng Đông, Tây, Nam, Bắc.
Tuy nhiên nếu ta muốn di chuyển theo hướng Tây Nam và cần phải xác định độ dốc của địa hình theo hướng Tây Nam thì sao?
Đạo hàm có hướng sẽ giúp ta xác định độ dốc nếu ta di chuyển theo một hướng khác với các hướng được chỉ định bởi gradient.

.. rubric:: Công thức toán học

Đạo hàm có hướng được tính bằng cách nhân vô hướng vector gradient :math:`f` và vector đơn vị :math:`\vec{v}` mô tả hướng cần tính đạo hàm.
Đầu ra của phép tính này là một số nguyên biểu diễn :math:`f` sẽ thay đổi bao nhiêu nếu ta thay đổi đầu vào hiện tại đi theo hướng chỉ định bởi :math:`\vec{v}` 1 khoảng rất rất nhỏ.

Giả sử ta có hàm :math:`f(x,y,z)` và ta muốn tính đạo hàm có hướng được mô tả bằng vector sau:

.. math::

 \vec{v}=\begin{bmatrix}
   2 \\
   3 \\
   -1  \\
  \end{bmatrix}


Như đề cập ở trên, ta sẽ tính tích vô hướng của vector gradient và vector hướng:

.. math::

   \begin{bmatrix}
     \frac{df}{dx} \\
     \frac{df}{dy} \\
     \frac{df}{dz} \\
    \end{bmatrix}
    \cdot
    \begin{bmatrix}
       2 \\
       3 \\
       -1  \\
    \end{bmatrix}


Ta có thể viết lại phép nhân vô hướng như sau:

.. math::

  \nabla_\vec{v} f = 2 \frac{df}{dx} + 3 \frac{df}{dy} - 1 \frac{df}{dz}

Công thức trên khá dễ hiểu do việc di chuyển 1 khoảng rất nhỏ theo :math:`\vec{v}` có thể được chia nhỏ thành các bước di chuyển độc lập, gồm 1 bước rất nhỏ theo hướng :math:`x`, 3 bước rất nhỏ theo hướng :math:`y`, và 1 bước rất nhỏ theo hướng ngược lại với :math:`z`, tức -1.


Tính chất
---------

Có 2 tính chất khác của gradient vô cũng hữu dụng trong học sâu.
Gradient của một hàm số:

    #. Luôn trỏ theo hướng có chiều tăng nhanh nhất của hàm số (được giải thích kỹ hơn `ở đây <https://betterexplained.com/articles/understanding-pythagorean-distance-and-the-gradient>`_)
    #. Bằng không tại các cực đại hoặc cực tiểu cục bộ


.. _integrals:

Tích phân
=========

Tích phân của :math:`f(x)` tương đương với việc tính phần diện tích phía dưới độ thị của :math:`f(x)`.
Phân diện tích phía dưới đồ thị :math:`f(x)` giữa hai điểm :math:`x=a` và :math:`x=b` được ký hiệu như sau:

.. math::

   A(a,b) = \int_a^b f(x) \: dx.

.. image:: images/integral_definition.png
   :align: center
   :scale: 70

Phần diện tích :math:`A(a,b)` bị giới hạn bởi đồ thị hàm số :math:`f(x)` ở phía trên, trục :math:`x` ở phía dưới, cùng với hai đường thẳng :math:`x=a` và :math:`x=b`.
Điểm :math:`x=a` và :math:`x=b` lần lượt được gọi là cận dưới và cận trên của tích phân.
Ký hiệu :math:`\int` lấy từ tiếng Latin *summa*, thể hiện việc tính tích phân tức là tính tổng ("sum") các giá trị của hàm :math:`f(x)` giữa hai cận.

The *integral function* :math:`F(c)` corresponds to the area calculation as a function of the upper limit of integration:
*Nguyên hàm* :math:`F(c)` là một hàm theo cận trên của tích phân, mô tả phần diện tích phía dưới độ thị hàm số gốc:

.. math::

  F(c) \equiv \int_0^c \! f(x)\:dx\,.

Có hai biến số và một hằng số trong công thức này.
Biến :math:`c` mô tả cận trên của tích phân.
Biến tích phân :math:`x` thực hiện việc quét từ :math:`x=0` đến :math:`x=c` để tính tích phân.
Hằng số :math:`0` mô tả cận dưới của tích phân.
Chú ý rằng việc chọn :math:`0` làm cận dưới chỉ đơn giản là 1 quy ước.
Việc chọn các hằng số khác làm cận dưới khác không ảnh hưởng đến kết quả nguyên hàm.

Nói cách khác, nguyên hàm :math:`F(c)` biểu diễn dạng tổng quát của phần diện tích phía dưới đồ thị :math:`f(x)`.
Với đạo hàm :math:`f'(x)`, ta có thể biết được độ dốc của đồ thị hàm số :math:`f(x)` tại tất cả các giá trị :math:`x` mà có tồn tại đạo hàm.
Tương tự, nguyên hàm :math:`F(c)` cho ta biết phần diện tích phía dưới đồ thị của hàm số :math:`f(x)` với bất cứ các cận tích phân nào khả thi.

Ta có thể tính phần diện tích phía dưới đồ thị hàm số :math:`f(x)` giữa :math:`x=a` và :math:`x=b` được tính bằng hiệu hai nguyên hàm như sau:

.. math::

   A(a,b) = \int_a^b \! f(x)\:dx
   	=  F(b)-F(a).

.. image:: images/integral_as_change_in_antriderivative.png
   :align: center


Tính tích phân
-------------------

Ta có thể tính xấp xỉ tổng diện tích phía dưới đồ thị hàm :math:`f(x)` giữa :math:`x=a` và :math:`x=b` bằng cách chia phần diện tích này thành nhiều hình chữ nhật với chiều rộng :math:`h` rất nhỏ, sau đó lấy tổng diện tích tất cả các hình chữ nhật.
Hình dưới mô tả cách tính phần diện tích dưới đồ thị :math:`f(x)=x^2` giữa :math:`x=1` và :math:`x=3` bằng cách xấp xỉ phần diện tích này bằng 4 hình chữ nhật với chiều rộng :math:`h=0.5`.
Thông thường, ta muốn chọn :math:`h` rất nhỏ để phép tính xấp xỉ chính xác hơn.

.. image:: images/integral_as_rectangular_strips.png
   :align: center

Đoạn code dưới đây mô tả cách tính xấp xỉ tích phân sử dụng phương pháp trên.

::

    def get_integral(func, a, b):
        """Tính diện tích phía dưới đồ thị hàm số `func` giữa x=a và x=b."""
        h = 0.0001               # chiều rộng của một hình chữ nhật nhỏ
        x = a                    # cận dưới x=a
        total = 0
        while x <= b:            # lặp đến khi tới cận trên x=b
            total += h*func(x)   # diện tích hình chữ nhật bằng chiều dài * chiều rộng
            x += h
        return total

    def f(x): return x**2                   # hàm f(x)=x^2
    computed = get_integral(f, 1, 3)

    def actualF(x): return 1.0/3.0*x**3     # nguyên hàm của f(x)=x^2

    actual = actualF(3) - actualF(1)
    computed, actual    # = 8.6662, 8.6666  # phép xấp xỉ khá chính xác

Ta có thể tìm nguyên hàm bằng cách sử dụng các công thức đạo hàm với một vài kỹ thuật đảo ngược.
Giả sử ta cần tìm nguyên hàm :math:`F(x)` của hàm :math:`f(x)`.

.. math::

   F(x) = \int \! f(x)\: dx.

Để thực hiện bài toán này, ta cần tìm hàm :math:`F(x)` sao cho :math:`F'(x)=f(x)`.

.. math::

  F'(x) = f(x).

Ví dụ, giả sử ta cần tìm nguyên hàm bất định :math:`\int \!x^2\:dx`.
Ta có thể viết lại bài toán này rằng ta cần tìm hàm số :math:`F(x)` sao cho

.. math::

  F'(x) = x^2.

Nhớ lại một số công thức đạo hàm ở phần trước, ta có thể đoán rằng :math:`F(x)` sẽ có :math:`x^3` do đạo hàm của luỹ thừa bậc 3 là một hàm bình phương.
Do đó, hàm số ta cần tìm có dạng :math:`F(x)=cx^3`, với hằng số :math:`c` nào đó.
Chọn hằng số :math:`c` để thoả mãn biểu thức sau:

.. math::

  F'(x) = 3cx^2 = x^2.

Giải :math:`3c=1`, ta thu được :math:`c=\frac{1}{3}` và nguyên hàm cần tìm là

.. math::

  F(x) = \int x^2 \:dx = \frac{1}{3}x^3 + C.

Bạn có thể khẳng định lại bằng cách tính :math:`\frac{d}{dx}\left[\frac{1}{3}x^3 + C\right] = x^2`.
Ta cũng có thể tìm nguyên hàm của hàm số sử dụng một số `công thức toán <https://www.teachoo.com/5643/728/Integration-Formulas---Trig--Definite-Integrals-Properties-and-more/category/Miscellaneous/>`_.


Ứng dụng của tích phân
----------------------

Tích phân được ứng dụng rất rộng rãi trong khoa học nói chung.
Ở đây, ta sẽ chỉ xem xét 1 vài ví dụ về ứng dụng của tích phân trong xác suất thống kê.


Tính xác suất
~~~~~~~~~~~~~

Một biến ngẫu nhiên liên tục :math:`X` được mô tả bởi một hàm mật độ xác suất :math:`p(x)`.
Một hàm mật độ xác suất là một hàm số dương có tổng diện tích phía dưới đồ thị bằng :math:`1`.

.. math::

	  p(x) \geq 0, \forall x 
    \qquad
	   \textrm{and}
	   \qquad
	   \int_{-\infty}^\infty p(x)\; dx = 1.

Xác suất ta quan sát được :math:`X` mang giá trị trong khoảng từ :math:`a` đến :math:`b` được tính bằng tích phân sau:

.. math::

	 \textrm{Pr}(a \leq X \leq b)
   =
	 \int_a^b p(x)\; dx.

Do đó, tích phân là một khái niệm trọng tâm trong lý thuyết xác suất với biến ngẫu nhiên liên tục.

Ta cũng sử dụng tích phân để tính các tính chất khác của một biễn ngẫu nhiên.
Giá trị *kỳ vọng* hay *phương sai* là hai tính chất quan trọng thể hiện hành vi của bất cứ biến ngẫu nhiên :math:`X` nào.


Kỳ vọng - *Expected value*
~~~~~~~

Giá trị *kỳ vọng* của biến ngẫu nhiên :math:`X` được tính bằng công thức

.. math::

  \mu
	% \equiv \mathbb{E}_X[X]
	= \int_{-\infty}^\infty x\, p(x).

Giá trị kỳ vọng là một số cho ta biết giá trị trung bình, hay giá trị mà ta "kỳ vọng" thu được khi quan sát biến ngẫu nhiên :math:`X`.
Kỳ vọng cũng có thể được gọi là giá trị *trung bình* của biến ngẫu nhiên :math:`X`.



Phương sai - *Variance*
~~~~~~~~~~

*Phương sai* của một biến ngẫu nhiên :math:`X` được định nghĩa bằng:

.. math::

   \sigma^2
	 % \equiv  \mathbb{E}_X\!\big[(X-\mu)^2\big]
	 = \int_{-\infty}^\infty (x-\mu)^2 \, p(x).

Công thức phương sai tính giá trị kỳ vọng của bình phương độ lệch của biến ngẫu nhiên :math:`X` so với giá trị kỳ vọng (giá trị trung bình).
Phương sai :math:`\sigma^2`, hay cũng có thể ký hiệu bằng :math:`\textrm{var}(X)`, cho ta biết độ phân tán của :math:`X`.
Giá trị phương sai nhỏ ám chỉ rằng các quan sát trên biến ngẫu nhiên :math:`X` chỉ xoay quanh giá trị kỳ vọng :math:`\mu`, ngược lại, giá trị phương sai lớn ám chỉ các giá trị của biến ngẫu nhiên :math:`X` phân tán rộng hơn.
Căn bậc hai của phương sai được gọi là *độ lệch chuẩn (standard deviation*) và thường được ký hiệu bằng :math:`\sigma`.

Giá trị kỳ vọng :math:`\mu` và phương sai :math:`\sigma^2` là hai khái niệm căn bản trong lý thuyết xác suất thống kê bởi chúng giúp ta mô tả bất kỳ biến ngẫu nhiên nào.
Giá trị kỳ vọng là đại lượng đo *xu hướng trung bình* của biễn ngẫu nhiên, còn phương sai là đại lượng đo *độ phân tán* của nó.
Các độc giả quen thuộc với các khái niệm vật lý có thể tưởng tượng giá trị kỳ vọng là *khối tâm (centre of mass)* của phân phối xác suất, và phương sai là *mô-men quán tính* của phân phối đó.


.. rubric:: Tài liệu tham khảo

.. [1] https://en.wikipedia.org/wiki/Derivative
.. [2] https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/directional-derivative-introduction
.. [3] https://en.wikipedia.org/wiki/Partial_derivative
.. [4] https://en.wikipedia.org/wiki/Gradient
.. [5] https://betterexplained.com/articles/vector-calculus-understanding-the-gradient
.. [6] https://www.mathsisfun.com/calculus/derivatives-introduction.html
.. [7] http://tutorial.math.lamar.edu/Classes/CalcI/DefnOfDerivative.aspx
.. [8] https://www.khanacademy.org/math/calculus-home/taking-derivatives-calc/chain-rule-calc/v/chain-rule-introduction
.. [9] http://tutorial.math.lamar.edu/Classes/CalcI/ChainRule.aspx
.. [10] https://youtu.be/pHMzNW8Agq4?t=1m5s
