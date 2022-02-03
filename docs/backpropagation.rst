.. _backpropagation:

====================================
Lan truyền ngược - *Backpropagation*
====================================

.. contents:: :local:

Mục đích của quá trình lan truyền ngược khá hiển nhiên: điều chỉnh hay cập nhật trọng số của mạng tuỳ vào ảnh hưởng của nó tới tổng lỗi dự đoán của mạng.
Nếu ta có thể liên tục làm giảm lỗi dự đoán của từng trọng số, cuồi cùng ta sẽ thu được một tập trọng số mà có thể đưa ra dự đoán đủ tốt.


Nhắc lại về Quy tắc chuỗi - *Chain rule*
========================================

Như đã đề cập trong :doc:`forwardpropagation_vn`, quá trình lan truyền xuôi có thể được coi là một chuỗi các hàm số lồng nhau.
Theo cách hiểu này, lan truyền ngược (*backpropagation*) gần như là một phương pháp ứng dụng :ref:`chain_rule` để tìm :ref:`derivative` của hàm chi phí theo bất cứ biến số (hay các trọng số) nào trong các hàm số lồng nhau đó.
Cho hàm lan truyền xuôi có dạng:

.. math::

  f(x) = A(B(C(x)))

A, B, và C là các hàm kích hoạt tại các tầng khác nhau trong mạng. Sử dụng quy tắc chuỗi, ta có thể dễ dàng tính được đạo hàm của :math:`f(x)` theo :math:`x`:

.. math::

  f'(x) = f'(A) \cdot A'(B) \cdot B'(C) \cdot C'(x)

Vậy còn đạo hàm theo hàm :math:`B` thì sao?
Để tính đạo hàm này, ta có thể coi :math:`B(C(x))` là hằng số, thay bằng biến tạm thời :math:`B`, và tính đạo hàm của :math:`f(x)` theo biến :math:`B`.

.. math::

  f'(B) = f'(A) \cdot A'(B)

Phương pháp đơn giản này giúp mở rộng quy tắc chuỗi để ta có thể tính được đạo hàm theo bất cứ biến nào trong hàm hợp, cho phép ta xác định chính xác ảnh hưởng của từng biến lên đầu ra dự đoán của mạng.


Áp dụng quy tắc chuỗi
=====================

Hãy cùng sử dụng quy tắc chuỗi để tính đạo hàm của hàm chi phí theo bất kỳ trọng số nào trong mạng.
Quy tắc chuỗi giúp ta xác định ảnh hưởng của từng trọng số lên lỗi dự đoán và hướng cập nhật cho từng trọng số để giảm lỗi.
Các phương trình sau là các phương trình được sử dụng trong quá trình dự đoán và xác định lỗi dự đoán của mạng.

.. image:: images/backprop_ff_equations.png
    :align: center

Cho một mạng chỉ có 1 nơ-ron duy nhất, tổng chi phí của mạng có thể được tính bằng:

.. math::

  \text{Chi phí} = C(R(Z(X W)))

Sử dụng quy tắc chuỗi, ta có thể dễ dàng tính đạo hàm của chi phí theo trọng số :math:`W` bằng:

.. math::

  C'(W) &= C'(R) \cdot R'(Z) \cdot Z'(W) \\
        &= (\hat{y} -y) \cdot R'(Z) \cdot X

Giờ quay lại với trường hợp mạng nơ-ron đơn giản 1 tầng ẩn.

.. image:: images/simple_nn_diagram_zo_zh_defined.png
    :align: center

Đạo hàm của hàm chi phí theo :math:`W_o` bằng

.. math::

  C'(W_O) &= C'(\hat{y}) \cdot \hat{y}'(Z_O) \cdot Z_O'(W_O) \\
          &= (\hat{y} - y) \cdot R'(Z_O) \cdot H

Còn đạo hàm theo :math:`W_h` thì sao?
Để tính đạo hàm này, ta tiếp tục áp dụng quy tắc chuỗi cho tới khi ta thu được đạo hàm theo biến :math:`Wh`.

.. math::

  C'(W_h) &= C'(\hat{y}) \cdot O'(Z_o) \cdot Z_o'(H) \cdot H'(Z_h) \cdot Z_h'(W_h) \\
          &= (\hat{y} - y) \cdot R'(Z_o) \cdot W_o \cdot R'(Z_h) \cdot X

Hãy thử 1 ví dụ khá thú vị với mạng nơ-ron 10 tầng ẩn. Đạo hàm của hàm chi phí với trọng số đầu tiên :math:`w_1` sẽ có dạng thế nào?

.. math::

  C'(w_1) = \frac{dC}{d\hat{y}} \cdot \frac{d\hat{y}}{dZ_{11}} \cdot \frac{dZ_{11}}{dH_{10}} \cdot \\ \frac{dH_{10}}{dZ_{10}} \cdot \frac{dZ_{10}}{dH_9} \cdot \frac{dH_9}{dZ_9} \cdot \frac{dZ_9}{dH_8} \cdot \frac{dH_8}{dZ_8} \cdot \frac{dZ_8}{dH_7} \cdot \frac{dH_7}{dZ_7} \cdot \\ \frac{dZ_7}{dH_6} \cdot \frac{dH_6}{dZ_6} \cdot \frac{dZ_6}{dH_5} \cdot \frac{dH_5}{dZ_5} \cdot \frac{dZ_5}{dH_4} \cdot \frac{dH_4}{dZ_4} \cdot \frac{dZ_4}{dH_3} \cdot \\ \frac{dH_3}{dZ_3} \cdot \frac{dZ_3}{dH_2} \cdot \frac{dH_2}{dZ_2} \cdot \frac{dZ_2}{dH_1} \cdot \frac{dH_1}{dZ_1} \cdot \frac{dZ_1}{dW_1}

Số lượng phép tính cần thực hiện để tính đạo hàm tăng lên theo chiều sâu của mạng.
Tuy nhiên chú ý rằng phép tính này bị dư thừa rất nhiều.
Đạo hàm hàm chi phí tại mỗi tầng thì sẽ có thêm 2 số hạng so với biểu thức tính đạo hàm mà đã được tính bởi tầng trước nó.
Vậy thì liệu có cách nào có thể lưu lại giá trị tính bởi tầng trước để tránh bị lặp lại khi thực hiện đạo hàm cho tầng đằng sau không?


Lưu lại kết quả đạo hàm tầng trước
=================================

Memoization is a computer science term which simply means: don’t recompute the same thing over and over. In memoization we store previously computed results to avoid recalculating the same function. It's handy for speeding up recursive functions of which backpropagation is one. Notice the pattern in the derivative equations below.

.. image:: images/memoization.png
    :align: center

Each of these layers is recomputing the same derivatives! Instead of writing out long derivative equations for every weight, we can use memoization to save our work as we backprop error through the network. To do this, we define 3 equations (below), which together encapsulate all the calculations needed for backpropagation. The math is the same, but the equations provide a nice shorthand we can use to track which calculations we've already performed and save our work as we move backwards through the network.

.. image:: images/backprop_3_equations.png
    :align: center

We first calculate the output layer error and pass the result to the hidden layer before it. After calculating the hidden layer error, we pass its error value back to the previous hidden layer before it. And so on and so forth. As we move back through the network we apply the 3rd formula at every layer to calculate the derivative of cost with respect that layer's weights. This resulting derivative tells us in which direction to adjust our weights to reduce overall cost.

.. note::

  The term *layer error* refers to the derivative of cost with respect to a layer's *input*. It answers the question: how does the cost function output change when the input to that layer changes?

.. rubric:: Output layer error

To calculate output layer error we need to find the derivative of cost with respect to the output layer input, :math:`Z_o`. It answers the question — how are the final layer's weights impacting overall error in the network? The derivative is then:

.. math::

  C'(Z_o) = (\hat{y} - y) \cdot R'(Z_o)

To simplify notation, ml practitioners typically replace the :math:`(\hat{y}-y) * R'(Zo)` sequence with the term :math:`E_o`. So our formula for output layer error equals:

.. math::

  E_o = (\hat{y} - y) \cdot R'(Z_o)

.. rubric:: Hidden layer error

To calculate hidden layer error we need to find the derivative of cost with respect to the hidden layer input, Zh. 

.. math::

  C'(Z_h) = (\hat{y} - y) \cdot R'(Z_o) \cdot W_o \cdot R'(Z_h)

Next we can swap in the :math:`E_o` term above to avoid duplication and create a new simplified equation for Hidden layer error:

.. math::

  E_h = E_o \cdot W_o \cdot R'(Z_h)

This formula is at the core of backpropagation. We calculate the current layer's error, and pass the weighted error back to the previous layer, continuing the process until we arrive at our first hidden layer. Along the way we update the weights using the derivative of cost with respect to each weight.

.. rubric:: Derivative of cost with respect to any weight

Let’s return to our formula for the derivative of cost with respect to the output layer weight :math:`W_o`. 

.. math::

  C'(W_O) = (\hat{y} - y) \cdot R'(Z_O) \cdot H

We know we can replace the first part with our equation for output layer error :math:`E_o`. H represents the hidden layer activation.

.. math::

  C'(W_o) = E_o \cdot H

So to find the derivative of cost with respect to any weight in our network, we simply multiply the corresponding layer's error times its input (the previous layer's output).

.. math::

  C'(w) = CurrentLayerError \cdot CurrentLayerInput

.. note::

  *Input* refers to the activation from the previous layer, not the weighted input, Z.

.. rubric:: Summary

Here are the final 3 equations that together form the foundation of backpropagation.

.. image:: images/backprop_final_3_deriv_equations.png
    :align: center

Here is the process visualized using our toy neural network example above.

.. image:: images/backprop_visually.png
    :align: center

Code example
============

.. literalinclude:: ../code/nn_simple.py
    :language: python
    :lines: 17-41


.. rubric:: Tài liệu tham khảo

.. [1] ...
