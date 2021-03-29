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
##UI
>#create(func) 引入函数
>###func(self)
>- self - UI底层对象,请使用 ui .get ( self , 路径 ) 来获取ui实例
>
>#load(ui实例) 创建mcjquery对象 
>#tick(func) 引入帧函数
>###func(self)
>- self - UI底层对象，帧函数是每次刷新时调用的，官方所给信息是一秒30次
>
>#init(func) 初始化
>###func(self) 
>- self UI 底层对象

##MCJQUERY
>#选择器
>- 单元选择
>
>### #uiname 依照名称筛选UI
>### .type 依照类型筛选UI
>### :src: 依照绝对路径筛选UI
>### *[first] 第一个
>### *[last] 最后一个
>### *[int:] 区间int到99999个
>### *[:int] 区间0到int个
>### *[int1:int2] 区间int1到int2个
>- 单元拼接
>
>###unit1+unit2 unit1与unit2的并集
>###unit1!unit2 不包括!unit2的内容
>- 单元集成
>
>###unit1,unit2 unit1与unit2单元的并集
>#示例
>```python
> jq ( ':/main: ! .button ' ) #选取 /main 路径下所有子节点, 不包括 button 类型
> jq ( ':/main:[0:5] + .button ' ) #选取 /main 路径下子节点1到5 和 所有 button 类型
> jq ( '#test + #main , .button[3:16] ! #test1' ) #选取 名字叫test和main的节点 与 类型为button的3到16个但名字不为 test1 的节点的集合
>```
