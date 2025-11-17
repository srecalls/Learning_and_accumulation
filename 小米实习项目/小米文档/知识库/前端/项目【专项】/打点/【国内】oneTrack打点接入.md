
# 一、背景：

通过接入oneTrack打点，提供更多类型的打点上报数据，从而更好的分析用户行为、优化用户体验。

# 二、方案：

## 1、前端方案：

场景分析：本次打点需上报曝光、点击、评论、详情页浏览等事件类型的数据，并且需要保留singleRecord的打点逻辑，所以这里在singleRecord打点方案的基础上封装了oneTrack打点方法。

## 2、API的封装使用：

### a. marketAPI:

- oneTrackMonitor（单独打点上报，例：click，comment）：
![[【国内】oneTrack打点接入.png]]
- oneTrackMonitorMultiple（Array形式的打点上报，例：exposure、view）：
![[【国内】oneTrack打点接入-2.png]]


event的mark里
![[【国内】oneTrack打点接入-3.png]]
- 参数说明：

|   |   |   |   |
|---|---|---|---|
|params|type|mean|mark|
|event|string|oneTrack打点事件类型||
|item/itemList|Object/Array|oneTrack打点参数，有格式要求<br><br>itemList：{<br><br>[],<br><br>[]<br><br>...<br><br>}、<br><br>item：{<br><br>oneTrackParams:{<br><br>params...<br><br>}<br><br>}||
|ext|Object|自定义打点数据（可为空）||

- 上报类型：

|   |   |
|---|---|
|eventType|mean|
|[‘CLICK’]/['COUNT_ONLY_CLICK']|对应点击事件|
|click|点击|
|comment（新增）|发表评论打点|
|download|下载|
|exposure|曝光|
|install|安装|
|other|other|
|subscribe|预约应用打点|
|view（新增）|用户退出页面打点|

- 使用举例：

![[【国内】oneTrack打点接入-4.png]]

item :

包含appInfo 和 oneTrackParams
![[【国内】oneTrack打点接入-5.png]]### b. font-end function:

在接收到页面请求到的appInfo之后，需要对appInfo进行处理，然后再使用oneTrack打点接口进行打点上报。在appstore-h5/assets/js/format/formatOneTrackParams.js中封装了对返回回来的数据进行处理的方法。

- handMsg：对请求回来的数据进行处理
![[【国内】oneTrack打点接入-6.png]]
- handleOneTrackParams：构造oneTrack. API所需要的参数对象，然后添加到对应appInfo对象中
![[【国内】oneTrack打点接入-7.png]]
- 在需要打点的时机，调用oneTrack打点API即可
![[【国内】oneTrack打点接入-8.png]]
![[【国内】oneTrack打点接入-12.png]]

# 三、打点逻辑：
![[【国内】oneTrack打点接入-10.png]]
# 四、其他细节

## 1、组件曝光：

曝光逻辑与之前保持一致，oneTrace数据处理流程与singleRecord不同
![[【国内】oneTrack打点接入-9.png]]
区别：oneTrack曝光，拼接oneTrackMonitorMultiple所需参数格式，然后进行曝光打点。

## 2、用户停留时长

打开app、打开搜索结果页的秒开应用、跳转第三方的deepLink、打开新的页面、跳转到app详情页都会触发view打点。

![](https://xiaomi.f.mioffice.cn/space/api/box/stream/download/asynccode/?code=NTEzMzJmZTZmMGFmYmRiOTRjNDhmNDE0OWFlNDVlMzFfUFpIV1JNeUhyendCcVoxamNvWDFzaDB0VjE5N2g0aVRfVG9rZW46Ym94azRibTFoTko2NFRodUFzQXA0Uk5LbWZoXzE3MDE0MDIxNDk6MTcwMTQwNTc0OV9WNA)

页面可见时，初始化pageStartTime，触发退出应用的时候，初始化pageEndTime退出时间

![](https://xiaomi.f.mioffice.cn/space/api/box/stream/download/asynccode/?code=YzBmMjk1MmI5NjMzNmI4ODZiZDQ5ZDNkYmJhOGMxM2JfRkZ6cjZtZGpHMW9aME9JZGZyaVNGQlNISWFiTHVtSkJfVG9rZW46Ym94azQwT0VRTXJ1dHNpd0RmM1FLU0VuRXdnXzE3MDE0MDIxNDk6MTcwMTQwNTc0OV9WNA)

# 五、相关文档

1、[应用商店onetrack打点方案](https://xiaomi.f.mioffice.cn/docs/dock4cA1GddAHgARbAMOZXvXsuf)

2、[埋点文档](https://wiki.n.miui.com/pages/viewpage.action?pageId=541369936)