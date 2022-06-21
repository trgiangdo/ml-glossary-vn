.. _optimizers:

=======================
Bộ Tối ưu - *Optimizer*
=======================

.. rubric:: Bộ tối ưu là gì?

Trong giai đoạn huấn luyện, tác vụ quan trọng nhất là cập nhật các tham số của mô hình sao cho dự đoán của mô hình càng chính xác và càng tối ưu càng tốt.
Nhưng chính xác thì việc cập nhật tham số được thực hiện thế nào?
Những tham số nào của mô hình cần cập nhật, khi nào thì cập nhật và cập nhật 1 lượng bằng bao nhiêu?

Câu trả lời tốt nhất cho các câu hỏi trên là *các bộ tối ưu*.
Bộ tối ưu liên kết hàm mất mát với các tham số mô hình bằng cách cập nhật mô hình dựa theo giá trị trả về của hàm mất mát.
Nói đơn giản hơn, bộ tối ưu giúp định hình mô hình thành dạng chính xác nhất có thể thông qua việc điều chỉnh trọng số.
Hàm mất mát có thể được coi là bộ phận dẫn đường cho bộ tối ưu cho biết nên di chuyển theo hướng nào.

Phần này sẽ liệt kê một số bộ tối ưu trong học máy.

.. contents:: :local:

.. figure:: images/optimizers.gif
    :align: center

    Nguồn: `CS231n <https://cs231n.github.io/neural-networks-3/>`_


.. _optimizer_adagrad:

Adagrad
-------

Adagrad (viết tắt của gradient thích ứng - *Adaptive Gradient*) tự động thay đổi :ref:`tốc độ học <glossary_learning_rate>` của 1 tham số để thích nghi với giá trị gradient của tham số đó.

- Các tham số có gradient cao hoặc được cập nhật thường xuyên nên có tốc độ học chậm hơn để tránh trường hợp mô hình không cập nhật lệch khỏi giá trị tối ưu nhất.
- Các tham số có graident thấp hoặc ít được cập nhật nên có tốc độ học nhanh hơn để quá trình huấn luyện diễn ra nhanh hơn.

Adagrad thích nghi tốc độ học bằng cách chia tốc độ học cho tổng bình phương của tất cả các gradient trước đó theo từng tham số.
Khi tổng bình phương đó có giá trị cao, tốc độ học sẽ được chia cho số lớn hơn 1 để giảm tốc độ học đi.
Tương tự, khi tổng bình phương đó có giá trị thấp, tốc độ học sẽ được chia cho số nhỏ hơn 1 để tăng tốc độ học lên.

Về mặt toán học, tốc độ học tỉ lệ nghịch với tổng bình phương của tất cả gradient tại các bước trước theo tham số đó.

.. math::

    g_{t}^{i} = \frac{\partial \mathcal{J}(w_{t}^{i})}{\partial W} \\
    W = W - \alpha \frac{\partial \mathcal{J}(w_{t}^{i})}{\sqrt{\sum_{r=1}^{t}\left ( g_{r}^{i} \right )^{2} + \varepsilon }}

trong đó:

    - :math:`g_{t}^{i}` - gradient theo một tham số, :math:`\Theta` tại vòng lặp :math:`t`.
    - :math:`\alpha` - tốc độ học.
    - :math:`\epsilon` - một giá trị rất nhỏ để tránh lỗi chia cho :math:`0`.

.. literalinclude:: ../code/optimizers.py
    :language: python
    :pyobject: Adagrad

Adadelta
--------

AdaDelta là một phiên bản mở rộng của :ref:`Adagrad <optimizer_adagrad>`, thuộc họ các thuật toán :ref:`hạ gradient ngẫu nhiên <optimizer_sgd>` (*stochastic gradient descent*), cung cấp giải pháp tinh chỉnh tập siêu tham số.
AdaDelta viết tắt cho delta thích ứng (*adaptive delta*), trong đó delta ý chỉ sự chênh lệch giữa trọng số hiện tại và trọng số mới được cập nhật.

Nhược điểm chính của Adagrad là nó cần tính tổng bình phương tất cả gradient.
Trong quá trình huấn luyện, tổng này tăng liên tục, và từ công thức của Adagrad ta có thể thấy rằng việc tăng tổng bình phương gradient sẽ dần khiến cho tốc độ học giảm đến quá nhỏ, và đến một lúc nào đó quá trình huấn luyện sẽ bị ngưng lại và không thể học thêm được kiến thức gì từ dữ liệu nữa.

Khác với Adagrad, AdaDelta mạnh mẽ hơn ở chỗ nó thích nghi tốc độ học dựa theo một cửa sổ chứa một số cập nhật gradient nhất định, thay vì toàn bộ các gradient tại các bước cập nhật trước.
Bằng cách này, AdaDelta có thể liên tục học và cập nhật ngay cả khi đã qua rất nhiều bước cập nhật trọng số.

Với AdaDelta, ta không cần phải xác định giá trị tốc độ học mặc định do tốc độ học không còn cần thiết trong công thức cập nhật nữa.

Công thức toán học có dạng như sau:

.. math::

  v_t = \rho v_{t-1} + (1-\rho) \nabla_\theta^2 J( \theta) \\
  \Delta\theta &= \dfrac{\sqrt{w_t + \epsilon}}{\sqrt{v_t + \epsilon}} \nabla_\theta J( \theta) \\
  \theta &= \theta - \eta \Delta\theta \\
  w_t = \rho w_{t-1} + (1-\rho) \Delta\theta^2

.. literalinclude:: ../code/optimizers.py
    :language: python
    :pyobject: Adadelta


.. _optimizer_adadelta:

Adam
----

Adam, viết tắt cho Ước lượng Mô-men Thích ứng (*Adaptive Moment Estimation*), là ý tưởng kết hợp giữa :ref:`RMSProp <optimizer_rmsprop>` và :ref:`Tối ưu theo động lượng <optimizer_momentum>`.
Bộ tối ưu này thích ứng tốc độ học cho từng tham số theo các bước sau:

- Tính trung bình trọng số mũ của các gradient trước đó (:math:`v_{dW}`).
- Tính trung bình trọng số mũ của bình phương các gradient trước đó (:math:`s_{dW}`).
- Các giá trị trung bình trên có xu hướng tiến tới :math:`0` và do đó một bước điều chỉnh độ lệch được áp dụng (:math:`v_{dW}^{corrected}`, :math:`s_{dW}^{corrected}`).
- Cập nhật tham số mô hình sử dụng các trung bình tính được ở trên.

.. math::

    v_{dW} = \beta_1 v_{dW} + (1 - \beta_1) \frac{\partial \mathcal{J} }{ \partial W } \\
    s_{dW} = \beta_2 s_{dW} + (1 - \beta_2) (\frac{\partial \mathcal{J} }{\partial W })^2 \\
    v^{corrected}_{dW} = \frac{v_{dW}}{1 - (\beta_1)^t} \\
    s^{corrected}_{dW} = \frac{s_{dW}}{1 - (\beta_1)^t} \\
    W = W - \alpha \frac{v^{corrected}_{dW}}{\sqrt{s^{corrected}_{dW}} + \varepsilon}

trong đó:

  - :math:`v_{dW}` - trung bình trọng số mũ của các gradient trước đó.
  - :math:`s_{dW}` - trung bình trọng số mũ của bình phương các gradient trước đó.
  - :math:`\beta_1` - siêu tham số cần tinh chỉnh.
  - :math:`\beta_2` - siêu tham số cần tinh chỉnh.
  - :math:`\frac{\partial \mathcal{J} }{ \partial W }` - gradient chi phí theo tầng hiện tại.
  - :math:`W` - ma trận trọng số (các tham số cần cập nhật).
  - :math:`\alpha` - tốc độ học.
  - :math:`\epsilon` - một giá trị rất nhỏ để tránh lỗi chia cho :math:`0`.


Gradient Liên hợp - *Conjugate Gradients*
-----------------------------------------

Be the first to `contribute! <https://github.com/trgiangdo/ml-glossary-vn>`__


.. _optimizers_lbfgs:

BFGS
----

Be the first to `contribute! <https://github.com/trgiangdo/ml-glossary-vn>`__


.. _optimizer_momentum:

Tối ưu theo Động lượng - *Momentum*
-----------------------------------

Bộ tối ưu Mô-men sử dụng gradient tại các bước cập nhật trước để làm mượt quá trình cập nhật tham số trong :ref:`Hạ gradient ngẫu nhiên <optimizer_sgd>` hoặc Hạ gradient theo batch nhỏ.
Động lượng được thể hiện qua biến :math:`v` ký hiệu trung bình trọng số mũ của gradient tại các bước cập nhật trước.
Việc này giúp giảm sự dao động của hàm lỗi và tăng tốc độ hội tụ của quá trình huấn luyện.

.. math::

    v_{dW} = \beta v_{dW} + (1 - \beta) \frac{\partial \mathcal{J} }{ \partial W } \\
    W = W - \alpha v_{dW}

trong đó:

  - :math:`v` - trung bình trọng số mũ của gradient tại các bước cập nhật trước.
  - :math:`\frac{\partial \mathcal{J} }{ \partial W }` - gradient chi phí theo trọng số tại tầng hiện tại.
  - :math:`W` - ma trận trọng số.
  - :math:`\beta` - siêu tham số cần tinh chỉnh.
  - :math:`\alpha` - tốc độ học.


.. _optimizer_nesterov_momentum:

Nesterov Momentum
-----------------

Be the first to `contribute! <https://github.com/trgiangdo/ml-glossary-vn>`__


Newton's Method
---------------

Be the first to `contribute! <https://github.com/trgiangdo/ml-glossary-vn>`__


.. _optimizer_rmsprop:

RMSProp
-------

RMSProp, viêt tắt cho Lan truyền theo Căn bậc hai Trung bình Bình phương (*Root Mean Square Propagation*), là một thuật toán tối ưu thích ứng tốc độ học khác hoạt động bằng cách tính giá trị trung bình trọng số mũ của gradient tại các bước cập nhật trước.
RMSProp sau đó chi tốc độ học cho giá trị trung bình này để tăng tốc độ hội tụ.

.. math::


    s_{dW} = \beta s_{dW} + (1 - \beta) (\frac{\partial \mathcal{J} }{\partial W })^2 \\
    W = W - \alpha \frac{\frac{\partial \mathcal{J} }{\partial W }}{\sqrt{s^{corrected}_{dW}} + \varepsilon}

trong đó:

  - :math:`s` - trung bình trọng số mũ của bình phương các gradient trước đó.
  - :math:`\frac{\partial \mathcal{J} }{\partial W }` - gradient chi phí theo trọng số tại tầng hiện tại.
  - :math:`W` - ma trận trọng số.
  - :math:`\beta` - siêu tham số cần tinh chỉnh.
  - :math:`\alpha` - tốc độ học.
  - :math:`\epsilon` - một giá trị rất nhỏ để tránh lỗi chia cho :math:`0`.


.. _optimizer_sgd:

Hạ Gradient Ngẫu nhiên - *Stochastic Gradient Descent*
------------------------------------------------------

Trong SGD, viết tắt cho Hạ Gradient Ngẫu nhiên (*Stochastic Gradient Descent*), tại mỗi bước cập nhật, chỉ 1 vài mẫu dữ liệu được lựa chọn ngẫu nhiên được sử dụng để huấn luyện thay vì toàn bộ tập dữ liệu.
Tuy việc sử dụng cả tập dữ liệu để tính gradient rất hữu dụng trong việc tìm điểm giá trị mất mát nhỏ nhất một cách ít nhiễu và ít ngẫu nhiên, nhưng sẽ là một vấn đề khó nếu tập dữ liệu của ta rất lớn.

Vấn đề này được giải quyết bằng hạ gradient ngẫu nhiên.
SGD chỉ sử dụng 1 mẫu dữ liệu được chọn ngẫu nhiên để tính gradient.

Do chỉ sử dụng 1 điểm dữ liệu trong tập dữ liệu được chọn ngẫu nhiên tại mỗi bước tính toán, quá trình mà thuật toán tìm giá trị nhỏ nhất thường nhiễu hơn nhiều so với thuật toán hạ gradient thông thường.
Nhưng con đường đi tới giá trị nhỏ nhất đó không quan trọng, miễn là ta tìm được điểm nhỏ nhất đó với khoảng thời gian huấn luyện nhanh hơn.

Trong :ref:`Hạ Gradient <gradient_descent>`, có một phương pháp khác có tên gọi Hạ Gradient theo Batch.
Thuật ngữ gọi là "batch" ở đây ý chỉ số mẫu dữ liệu trong tập dữ liệu được sử dụng để tính gradient tại mỗi bước cập nhật thay vì chỉ 1 mẫu dữ liệu hay cả tập dữ liệu.

.. literalinclude:: ../code/optimizers.py
    :language: python
    :pyobject: SGD


.. rubric:: Tài liệu tham khảo

.. [1] http://sebastianruder.com/optimizing-gradient-descent/
.. [2] http://www.deeplearningbook.org/contents/optimization.html
.. [3] https://arxiv.org/pdf/1502.03167.pdf
