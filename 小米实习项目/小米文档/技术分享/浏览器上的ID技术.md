## ID技术

### Cookie

当用户通过浏览器访问网站的时候，服务器在response header中中会通过set-cookie的字段写入一段内容，当用户再次访问这个服务器的时候，request header中就会把写入的内容带回给服务器，服务器通过判断这个内容就可以进行用户身份的识别了。

Cookie又分为两种：第一方Cookie和第三方 Cookie

### 浏览器指纹

#### 浏览器的基础特征

通过window.navigator对象可以获取到一些浏览器以及设备的信息，这些特性可以从一定程度上标识设备的唯一性，通过一些组合以及编码后就可以作为设备的指纹了。经常用来组合的特性有：userAgent、screen、bluetooth、gpu等。

#### 通过Web API获取到的硬件指纹

##### 音频指纹：AudioContext

利用设备音频设置，把播放音频文件的方式模拟成一个正弦函数，再把正弦函数转化成哈希函数，作为附加熵，结合浏览器的基本特征信息，生成音频指纹。

使用 HTML5 AudioContext API 进行指纹识别，AudioContext 指纹是计算机音频堆栈本身的属性，并不会收集计算机播放和录制的声音。

```JavaScript
//  https://github.com/fingerprintjs/fingerprintjs/blob/master/src/sources/audio.ts
function getAudioFingerprint(): number | (() => Promise<number>) {
  const w = window
  const AudioContext = w.OfflineAudioContext || w.webkitOfflineAudioContext
  if (!AudioContext) {
    return SpecialFingerprint.NotSupported
  }

  // In some browsers, audio context always stays suspended unless the context is started in response to a user action
  // (e.g. a click or a tap). It prevents audio fingerprint from being taken at an arbitrary moment of time.
  // Such browsers are old and unpopular, so the audio fingerprinting is just skipped in them.
  // See a similar case explanation at https://stackoverflow.com/questions/46363048/onaudioprocess-not-called-on-ios11#46534088
  if (doesCurrentBrowserSuspendAudioContext()) {
    return SpecialFingerprint.KnownToSuspend
  }

  const hashFromIndex = 4500
  const hashToIndex = 5000
  const context = new AudioContext(1, hashToIndex, 44100)

  const oscillator = context.createOscillator()
  oscillator.type = 'triangle'
  oscillator.frequency.value = 10000

  const compressor = context.createDynamicsCompressor()
  compressor.threshold.value = -50
  compressor.knee.value = 40
  compressor.ratio.value = 12
  compressor.attack.value = 0
  compressor.release.value = 0.25

  oscillator.connect(compressor)
  compressor.connect(context.destination)
  oscillator.start(0)

  const [renderPromise, finishRendering] = startRenderingAudio(context)
  const fingerprintPromise = renderPromise.then(
    (buffer) => getHash(buffer.getChannelData(0).subarray(hashFromIndex)),
    (error) => {
      if (error.name === InnerErrorName.Timeout || error.name === InnerErrorName.Suspended) {
        return SpecialFingerprint.Timeout
      }
      throw error
    },
  )

  return () => {
    finishRendering()
    return fingerprintPromise
  }
}
// 关键方法： startRenderingAudio 和 getHash
```

##### **Canvas指纹**

使用 HTML5 提供的 Canvas API 绘制隐藏元素图片，相同的 Canvas 代码在不同的计算机上绘制出的结果也会出现差异，尽管在肉眼上很难看出区别。这是因为浏览器、操作系统、GPU 和图形驱动器任一设备的不同，都会导致绘制图画时渲染的方式不一样，而这恰恰是指纹的唯一识别。

技术实现的关键步骤：

1. 使用canvas的context绘制一个文本
    
2. 通过context的toDataURL方法获取该图片的base64编码字符串
    
3. 对base64的字符串进行MD5加密处理，处理后的结果作为指纹（或者对图片流数据做CRC，循环冗余算法）
    

```JavaScript
// https://stackblitz.com/edit/vitejs-vite-ik1gkg?file=main.js&terminal=dev
const ret = makeCanvasContext();
const canvas = ret[0];
const ctx = ret[1];
renderText(canvas, ctx);

const text1 = canvasToImage(canvas);
const text2 = canvasToImage(canvas);

console.log(text1);
console.log(text2);
console.log(text1 === text2);  // true

function makeCanvasContext() {
  const canvas = document.createElement('canvas');
  canvas.width = 1;
  canvas.height = 1;
  const ctx = canvas.getContext('2d');
  return [canvas, ctx];
}

function renderText(canvas, ctx) {
  // 这里的文本类型可以复杂一些
  const txt = 'canvas <fingerprint>👍';
  ctx.textBaseline = 'top';
  ctx.font = "14px 'Arial'";
  ctx.textBaseline = 'alphabetic';
  ctx.fillStyle = '#f60';
  ctx.fillRect(125, 1, 62, 20);
  // 增加一些选项，也可以提高撞库率
  ctx.fillStyle = '#069';
  ctx.fillText(txt, 2, 15);
  ctx.fillStyle = 'rgba(102, 204, 0, 0.7)';
  ctx.fillText(txt, 4, 17);
}

function canvasToImage(canvas) {
  // 执行toDataURL，返回一个base64-encoded字符串
  return canvas.toDataURL();
}
```

> 实际能获取到的指纹如下：

![](https://xiaomi.f.mioffice.cn/space/api/box/stream/download/asynccode/?code=ZDUwZjk5NDVlYzM4ODUwNDQ2ZjQyNmExNzEzYThjNTRfWWs5VTFNQ21CejhYYzZveWlZbzZyMEdOb3F4dnlEbFVfVG9rZW46Ym94azQwOHI3Ymk2S2tjV1c1WkNlZjR5ZnllXzE3MDEzMTU0MTY6MTcwMTMxOTAxNl9WNA)

来自https://browserleaks.com/canvas

##### WebRTC指纹

浏览器提供 WebRTC 功能，通过 UDP 协议建立连接，从而获取到公共 IP 地址、本地 IP 地址和媒体设备（如摄像头、麦克风）的数量及其哈希值。由于是通过 UDP 协议，所以即便是使用了代理，网站也能够获取到真实的公共和本地 IP 地址。

##### WebGL指纹

WebGL 是一个 JavaScript API,可在任何兼容的 Web 浏览器中渲染高性能的交互式 3D 和 2D 图形。不同组合的硬件设备会将该图形转换成唯一的hash值 综合指纹。和Canvas指纹类似。

> 实际能获取到的指纹如下：

![](https://xiaomi.f.mioffice.cn/space/api/box/stream/download/asynccode/?code=NzU1YWY3NDFlOWViZDdmMmM1MzE1OTdiODlhNjFkNjlfYUJRM01XZ1RXYkdqOHFFQjY3SVJIUDUxc2g3ZksyM1BfVG9rZW46Ym94azRoZnNSbVdGWTlwSll2V3VXNWZ0aU9TXzE3MDEzMTU0MTY6MTcwMTMxOTAxNl9WNA)

https://browserleaks.com/webgl#howto-enable-disable-webgl

  

> 总结：分析计算指纹的方法还有许多，以上四种巧妙的方法仍然会出现**指纹碰撞**的几率。但通过各种综合计算出哈希值的指纹，能够提高它的唯一性。目前已有开源的浏览器指纹库(https://github.com/fingerprintjs/fingerprintjs) ，可查询浏览器属性并从中计算出哈希值，生成浏览器指纹。

## 防ID技术

### 浏览器无痕模式

当用户在浏览器中开启无痕模式的时候，用户退出所有的无痕模式的浏览器窗口后，浏览器会将以下信息删掉：

- 浏览记录
    
- Cookie 和网站数据
    
- 在表单中输入的信息
    
- 为网站授予的权限
    

这些**存储在本地的信息**在无痕模式下会被删掉，不过有一些信息是删不掉的，网站依然可以获取一些信息，比如：

- IP 地址（通过IP可以确定大致的区域）
    
- 登陆网站后的ID身份
    
- 在无痕模式下的操作行为
    

### 禁用Javascript和Cookie

浏览器在设置中提供了选项，用户可以根据需要选择禁用掉Javascript和Cookie，禁用掉这两项后基本上网站就没有办法来生成唯一的ID了，不过禁用Javascript后浏览器的可用性会大大降低。

### 禁用WebRTC和Geolocation

可以防止网站开发着通过这两个信息生成用户唯一ID。

### 防追踪浏览器

候鸟浏览器 https://www.ehouniao.com/ 通过欺骗站点所能获得的参数，修改数字指纹，达到防追踪的目的，类似miui上的照明弹功能

TODO：什么原理？

  

  

参考文档：

[初探Web客户端追踪技术](https://mp.weixin.qq.com/s/HyHsoIr0kcu8o9fuCl29AQ)

[硬件指纹](https://docs.multilogin.com/l/zh/article/aJHHdYrdmY-audio-context)

[浏览器指纹解读](https://blog.51cto.com/lixi/5377134)