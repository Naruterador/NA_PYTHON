#Entry和Text组件
> Text实际上是一个功能强大的"富文本"编辑组件，这意味着使用Text不仅可以插入文本内容，也可以插入
图片，通过image_create(self,index,cnf={},**kw)方法来插入。

> Text也可以设置被插入文本内容的格式，此时就需要为insert(self,index,chars,*args)方法的最后一个参数
传入多个tag进行控制，这样就可以使用Text组件实现图文并茂的效果。

> 此外，当Text内容较多时就需要对该组件使用滚动条，以便该Text能实现滚动显示。为了让滚动条控制Text组件
内容的滚动,实际上就是将它们进行双向关联。这里需要两步操作实现:
<pre>
   1. 将Scrollbar的command设为目标组件的xview或yview,其中xview用于水平滚动条控制目标组件水平滚动;
      yview用于垂直滚动条控制目标组件垂直滚动。
   2. 将目标组件的xscrollcommand或者yscrollcommand属性设为Scrollbar的set方法。
</pre>
