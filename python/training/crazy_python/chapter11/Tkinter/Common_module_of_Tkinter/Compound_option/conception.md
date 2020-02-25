#使用compound选项
> 程序可以为按钮或label等组件同时指定text和image两个选项，其中text用于指定该组件上
  的文本;image用于显示该组件上的图片，当同时指定两个选项时，通常image会覆盖text。
  但在某些时候，程序希望组件能同时显示文本和图片，此时就需要通过Compund选项进行控制。

> compound选项支持如下属性。
<pre>
    /> None:图片覆盖文字
    /> LEFT常量(值为'left'字符串):图片在左，文本在右
    /> RIGHT常量(值为'right'字符串):图片在右，文本在左
    /> TOP常量(值为'top'字符串):图片在上，文本在下
    /> BOTTOM常量(值为'bottom'字符串):图片在底，文本在上
    /> CENTER常量(值为'center'字符串):文本在图片上方
</pre>
