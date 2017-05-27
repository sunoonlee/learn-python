图片处理任务，首先想到 PIL 模块。读 PIL 的 Tutorial，未发现如何在图片上写入文字。

google 搜 python image，找到 the hitchhiker's guide to python，其中提到 python 图片处理常用的两个库，除了 PIL 之外，还有功能更为强大的 OpenCV. 本题这样简单的一个任务，有必要动用这个重型的武器吗？

果然不需要。搜 python text to image，可知 PIL 的 ImageDraw 模块可实现在图片上批注的功能。直接照搬文档里的[这个例子](http://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html#example-draw-partial-opacity-text) 即可。


