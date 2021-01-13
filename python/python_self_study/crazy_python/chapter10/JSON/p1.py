#coding = utf - 8

'''
JSON是一种轻量级、跨平台、跨语言的数据交换格式，JSON格式被广泛应用于各种语言的数据交换中，Python也提供了对
JSON的支持。

JSON的全称是JavaScript Object Notation，即JavaScript对象符号，它是一种轻量级的数据交换格式。
JSON的数据格式既适合人来读写，也适合计算机本身解析和生成。最早的时候，JSON是JavaScript语言的数据交换
格式，后来慢慢发展成为一种语言无关的数据交换格式，这一点非常类似于XML。

JSON主要在类似于C的编成语言中广泛使用，这些语言包括C、C++、C#、JAVA、JavaScript、Perl、Python等
JSON提供了多种语言之间完成数据交换的能力，因此JSON也是一种非常理想的数据交换格式。
JSON主要提供如下两种数据结构:
1.由key-value对，组成的数据结构。这种数据结构在不同的语言中有不同的实现。例如在JavaScript中是一个对象;
  在Python中是一种dict对象;在C语言中是一个struct;在其它语言中，则可能是record、dictionary、hash table等。

2.有序集合。这种数据结构在Python中对应于列表;在其他语言中，可能对应与list、vector、数组和序列等。

上面两种数据结构在不同的语言中都有对应的实现，因此这种简便的数据表示方式完全可以实现跨语言。所以，JSON可以作为程序
设计语言中通用的数据交换格式。在JavaScript中主要有两种JSON语言，其中一种用于创建对象；另一种用于创建数组。


使用JSON语法创建对象是一种简单的方式。使用JSON语法可避免书写函数，也可避免使用new关键字，而是可以直接获取一个
JavaScript对象。对于早期的JavaScript版本，如果要使用JavaScript创建一个对象。一般会这么写:

//定义一个函数，可以作为该类的构造器
function Person(name,gender)
{
	this.name = name;
	this.gender = gender;
}
//创建一个Person实例
var p = new Person('yeeku','male')
//输出Person实例的name属性
alert(p.name)


从JavaScript1.2开始，创建对象又有了一种更快捷的语法:
var p = ("name":"yeekuy","gender":"male");
alert(p);
上面这种语法就是一种JSON语法。显然，使用JSON语法创建对象更加简捷、方便。

JSON创建对象语法示意图:
object = {
	
propertyName1 : propertyValue1,
propertyName2 : propertyValue2,
....

}
在创建对象object时，总是以"{"开始，以"}"结束，对象的每个属性名和属性值直接用:隔开，多个属性定义之间用逗号","隔开。

-------------------------------------------------------------------------------------------------------
在使用JSON语法创建JavaScript对象时，属性值不仅可以使普通字符串，也可以是任何基本数据类型，还可以是函数、数组、甚至
是另外一个使用JSON语法创建的对象。

Person = 
{
	name : 'yeeku',
	gender : 'male',
	//使用JSON语法为其指定一个属性
	son : {
		name : 'tiger',
		grade: 1

	},
	//使用JSON语法为Person直接分配一个方法
	info:function()
	{
		console.log("姓名:" + this.name + "性别:" + this.sex);
	}
}

-------------------------------------------------------------------------------------------------------
使用JSON语法创建数组
使用JSON语法创建数组也是非常常见的情形，在早期的JavaScript语法中，我们通过如下方式来创建数组。
//创建数组对象
var a = new Array();
//为数组元素赋值
a[0] = 'yeeku';
//为数组元素赋值
a[1] = 'nono';

或者，通过如下方式创建数组。
//在创建数组对象时直接赋值
var a = new Array('yeeku','nono')
但如果使用JSON语法，则可以通过如下方式创建数组
//使用JSON语法创建数组
var a = ['yeeku','nono']

使用JSON创建数组的语法格式:
arr = [value1,value2 ...]

使用JSON语法可以简单写成如下形式
person = 
{
	name: 'yeeku'
	gender: 'male'
	age : 29
}

'''