#YMPACK
#### 这是一个简易的封装包，用于一些简单的mc py交互代码，适用且仅适用于我的世界中国版
- 导入
```python
from ym import 名称
```
##结构
|属性名称|用途|
|:-|:-|
|ui|ui封装和mcjQuery类似选择器|

#API
> ##UI
>>create(func) 引入函数
>>>func(self)
>>> self - UI底层对象,请使用 ui .get ( self , 路径 ) 来获取ui实例

>>load(ui实例) 创建mcjquery对象 
>>