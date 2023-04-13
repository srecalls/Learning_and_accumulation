# 表格标签 Total
<font size=5>① [[表格的基本标签 table tr td| 表格基本标签]]：table > tr > td </font>

<font size=5>② [[表格标题和表头单元格标签 caption th|表格标题和表头单元格标签]]：table >  caption  +    tr  > th</font>

<font size=5>③ [[表格的结构标签 thead tbody tfoot|表格结构标签]]：table > thead > tr > td</font>

<font size=5>④ [[表格的相关属性 border width height|表格相关属性]]表格相关属性</font>

<font size=5>⑤ 合并单元格步骤 </font>

<font size=5>[[合并单元格 --思路|思路]]</font>
<font size=5>[[合并单元格 --代码实现|代码实现]]</font>
1. 明确合并哪几个单元格 
2. 通过左上原则，确定保留谁删除谁 
• 上下合并→只保留最上的，删除其他 
• 左右合并→只保留最左的，删除其他 
3. 给保留的单元格设置：跨行合并（rowspan）或者跨列合并（colspan）


①

 ![[Pasted image 20220905194832.png]]

 
 ②
![[Pasted image 20220905194739.png]]


③![[Pasted image 20220905195411.png]]


④![[Pasted image 20220905195432.png]]

⑤![[Pasted image 20220905195445.png]]