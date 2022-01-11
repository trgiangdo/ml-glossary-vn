# Thuật ngữ chuyên ngành Máy Học

Hiện nay, các sách, báo, bài hướng dẫn chuyên ngành Máy Học tiếng Việt, cũng như các luận văn Thạc sĩ, Tiến sĩ hầu hết đều sử dụng các thuật ngữ tiếng Anh, và nếu có dịch ra tiếng Việt thì cũng chưa có được sự thống nhất.
Tôi thực hiện dự án này trước hết là để cung cấp tài liệu học cho cá nhân tôi, và cũng như mong rằng có thể hỗ trợ trong việc Việt hoá tài liệu chuyên ngành Máy Học và Trí tuệ nhân tạo ở Việt Nam

Bản thuật ngữ này trước tiên tập trung vào dịch lại bản thuật ngữ tiếng Anh.
Tiếp đó, cần thu thập thêm thuật ngữ từ nhiều nguồn khác để làm mới và mở rộng kho thuật ngữ này.

Rất mong nhận được sự hỗ trợ và đóng góp từ mọi người.

- [Bản thuật ngữ tiếng Anh](http://ml-cheatsheet.readthedocs.io/en/latest/)

## Hướng dẫn đóng góp

1. Clone kho chứa nội dung

```
git clone https://github.com/trgiangdo/ml-glossary-vn.git
```

2. Cài đặt các gói cần thiết

Mục này giả sử bạn đã cài đặt các thư viện thường dùng trong lập trình máy học: `numpy`, `scipy`, v.v.
Chạy các câu lệnh sau trên cửa sổ lệnh (terminal).
```
pip install sphinx sphinx-autobuild
pip install sphinx_rtd_theme
pip install recommonmark
```
Với python-3.x trên môi trường Linux, sử dụng:
```
pip3 install sphinx sphinx-autobuild
pip3 install sphinx_rtd_theme
pip3 install recommonmark
```

3. Xem trước các thay đổi của bạn

Với Windows, chạy các lệnh:
```
cd ml-glossary
cd docs
build.bat html
```

Nếu bạn sử dụng `make` trên môi trường Linux:
```
cd ml-glossary
cd docs
make html
```

4. Xác nhận các thay đổi của bạn bằng cách mở tệp `index.html` trong thư mục `_build/` sử dụng trình duyệt bất kỳ và tìm đến mục bạn thay đổi

5. [Đề xuất một Pull Request mới](https://help.github.com/articles/creating-a-pull-request/)

### Báo cáo lỗi hoặc đề xuất thay đổi

Bạn có thể báo cáo lỗi hoặc đề xuất thêm bớt nội dung bằng cách tạo một [issue](https://github.com/trgiangdo/ml-glossary-vn/issues) mà không cần phải tạo pull request.


## Hướng dẫn định dạng văn bản

Mỗi đầu mục trong bản thuật ngữ PHẢI đảm bảo các tiêu chí tối thiểu sau:

1. **Giải thích ngắn gọn** - càng ngắn gọn và súc tích càng tốt, nhưng đừng ngắn quá.
2. **Trích dẫn** - đến các bài báo khoa học, hướng dẫn, v.v.

Để tăng tính tường minh, các đầu mục cũng có thể bao gồm:

1. **Hình minh hoạ** - sơ đồ, biểu đồ, hoạt hoạ, hình ảnh.
2. **Code** - các mẩu code python/numpy, class hoặc các hàm minh hoạ.
3. **Phương trình** - theo cú pháp Latex.

Bạn cũng có thể đề xuất một pull request "thô" mà không cần hình minh hoạ hay code để trình bày ý tưởng của mình, và có thể nhờ đến sự giúp đỡ của cộng đồng đề cải thiện bản đề xuất của bạn.


## Mẹo

* [Thêm và chỉnh sửa phương trình](http://www.sphinx-doc.org/en/stable/ext/math.html)
* [Làm việc với Jupyter Notebook](http://louistiao.me/posts/demos/ipython-notebook-demo/)
<!-- * Quickstart with Jupyter notebook template
* Graphs and charts
* Importing images
* Linking to code -->


## Tham khảo

* [Công cụ vẽ đồ thị Desmos](https://www.desmos.com/calculator)
* [Công cụ vẽ đồ thị 3D](https://www.geogebra.org/3d)
* [Làm thế nào để đề xuất Pull Request](https://help.github.com/articles/creating-a-pull-request/)
* [RST Cheatsheet](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Cộng cụ tạo trích dẫn](http://www.citationmachine.net)
* [MathJax Cheatsheet](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)
* [Nhúng phương trình toán học](http://www.sphinx-doc.org/en/stable/ext/math.html)
* [Hướng dẫn làm việc với Sphinx](https://pythonhosted.org/an_example_pypi_project/sphinx.html)
* [Tài liệu Sphinx](http://www.sphinx-doc.org/en/stable/markup/code.html)
* [Sphinx Cheatsheet](http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html)
