key属性是DOM元素的唯一标识。有一个数组，数组发生增加和删除的时候，默认要把发生改动的项全部进行一个重绘，如果我往数组中添加一个元素，那所有的项都要进行一个重绘，就会浪费资源。添加了唯一表示后，重绘前会vue检查哪些新元素是需要增加和删除的，没有就用之前的，如果不增加和删除 key是没有作用的

减少DOM的操作，提高性能
![[Pasted image 20230412012437.png]]
key属性是DOM元素的唯一标识
作用:
1.提高虚拟DOM的更新
2.若不设置key，可能哙触发一些bug
3.为了触发过度效果


https://www.bilibili.com/video/BV14s4y1x7kA/?spm_id_from=333.337.search-card.all.click&vd_source=8d6fb7b59b6cb13b7bf0f3383fc26f3f