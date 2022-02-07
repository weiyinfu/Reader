# 为什么用vuepress制作电子书？

* 为了练习vuepress的使用方法。

vuepress最大的缺点在于运行太慢，文件一旦达到几千个就几乎是不可用的状态（不可用体现在：1：构建太慢；2：文件多了之后会崩溃）。vitepress又不够成熟。    

构建时，如果发生内存不足问题，需要设置node选项`export NODE_OPTIONS=--max_old_space_size=8192`.
# 常用命令
* vuepress dev docs
* vuepress build docs
* vuepress serve docs

vitepress 用法与vuepress一致，但是性能更为强悍。
* vitepress dev docs
* vitepress build docs
* vitepress serve docs