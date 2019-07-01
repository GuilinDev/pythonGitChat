# 函数定义
    * 传递参数
    * 实参和形参
        * 位置实参 - 按照位置顺序关联每个实参到函数定义中的每个形参
        * 关键字实参 - 每个实参用变量名和值组成，根据变量名来找，顺序不重要；也可以使用list和dict
        * 默认值 - 没有参数传入就是用默认值，默认值的形参须放在后面，没有默认值的形参放在前面
        * 调用方法不同的参数顺序是等效的
        
# 返回值
    * 简单值
    * 返回字典

# 传递列表作为参数
    * 修改列表 - python是pass by object reference，注意一个变量不是object，value of variable才是object
    * 禁止修改 - 利用切片

# 传递任意数量的实参
    * 使用 '*' 封装成元组
    * 使用 '**' 封装成字典

# 函数存储在模块中
    * from module_name import function_name - 这里vscode提示module名字有错是没关系的
    * 使用as可以给函数和模块指定别名
    * 使用'*'导入模块下的所有函数
