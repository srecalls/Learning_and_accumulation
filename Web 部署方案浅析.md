## 引言

入门前端的最初，你已经知道，想要打开一个网页，只需双击HTML文件，浏览器就会自动打开文件给你

![](https://xiaomi.f.mioffice.cn/space/api/box/stream/download/asynccode/?code=NjllOTM3MWRlYzQxMGU4NWRiZGQwODE3OGUxNzdiMjRfSk5BRHBPelVoRXVzWUpCSjh4UG5HVXY1TFdkQ2ZsMnFfVG9rZW46Ym94azQyVGd3OVNEYTRHMWd3THlFdTI0RkZmXzE3MDExNjY0MzM6MTcwMTE3MDAzM19WNA)

  

借助 npm上的 serve 等工具，你也可以迅速的开启一个HTTP服务，将你的文件暴露在内网之上供他人访问

> pnpm dlx serve ./ -p 80

![](https://xiaomi.f.mioffice.cn/space/api/box/stream/download/asynccode/?code=NDEzYzFlNjNiZDJjOTZhNzIyYzU5ODRhMWJmOWJlNjlfWkNadGI4UDZOdmhYcVZoUWxZQk9DdVF2bENaVVZwdmZfVG9rZW46Ym94azRrNmhVdGF1WHdFRGtTSDluRlc3dm5lXzE3MDExNjY0MzM6MTcwMTE3MDAzM19WNA)

  

此时如果你还有能力修改电脑的域名解析，就可以直接通过域名来访问你的文件

> 10.189.45.12 imac.leezx.cn

![](https://xiaomi.f.mioffice.cn/space/api/box/stream/download/asynccode/?code=OTcwNzY2NWQ3NmIyNzNkNzhhZDEwMWM4MjRkOGZkOTRfblZlN2FjcUxVdWZ1bmZ3c3Zzc3A0QWNCVjhTTjVlSFlfVG9rZW46Ym94azRkTnhnaFRzaFJENHNFOGRiOXB1VXU0XzE3MDExNjY0MzM6MTcwMTE3MDAzM19WNA)

  

上面的例子可以简单的抽象为下图：

暂时无法在飞书文档外展示此内容

下面的介绍基本都不脱离这个简单的结构，让我们开始吧！

  

## 平台能力

#### Gitlab-CI

Gitlab 是内网的远端代码仓库，基于社区版的 Gitlab 构建，提供代码托管服务，同时也提供了持续集成能力

#### IAM

IAM 通过树的方式管理不同的节点资源，用于部署资源的授权管理

![](https://xiaomi.f.mioffice.cn/space/api/box/stream/download/asynccode/?code=YWJiMzkzZmY0NDIxNTJjM2NkNTlhMDJkZmE3NmE2MThfeW15bVl3TDExSHNYVGlwTnpVazQ3R3lZZ0JraFBmQnhfVG9rZW46Ym94azQ3QjQxaUlUS1dTb1BSd2t4Mkc5MFpiXzE3MDExNjY0MzM6MTcwMTE3MDAzM19WNA)

IAM 上获得授权是其余资源使用的前提，因此操作相关树节点资源前，必须确保已经获得授权

#### MiFlow

MiFlow 用于持续集成流水线的创建与编排，在这个层面上功能与 Gitlab-CI 是比较一致的

不同的是，Gitlab-CI 通过 yml 格式的文件进行编码式的配置，MiFlow 则完全是可视化的

~~目前，通常在构建内部类库时使用 Gitlab-CI（不涉及~~ ~~IAM~~ ~~节点授权），构建业务应用时使用~~ ~~MiFlow~~

#### MiCR

内网的 Docker 镜像源，用以存储构建最终服务使用的镜像

> 针对前端而言，可以理解为 Docker 容器的 npm 平台

镜像通常生产自流水线中的构建步骤，当然在项目部署环境搭建阶段，也可以直接在本地创建镜像后推送至 MiCR，用来验证镜像仓库是否创建成功、Matrix 容器能否正常启动等

#### Matrix

内网的容器管理平台，用以管理容器服务，在以容器为核心的部署方案中，最终的服务承载点

#### MIFE

内网网关，用以承接外部流量并将请求转发给实际的容器实例

  

## 部署方案

### ToC 商城

暂时无法在飞书文档外展示此内容

- 发布时文件上传至 FDS，通过静态文件发布服务，通知 SPPS 服务拉取资源文件
    
- 用户访问时 ，域名通过区域解析至 CDN 节点，存在文件则直接返回，不存在则回源至 SPPS
    

  

### ToB 服务

暂时无法在飞书文档外展示此内容

- 主入口文件存放在后端，其余资源放在 FDS，通过版本标识保留历史版本的记录
    
- 后端通过指定的标识生成主入口文件，指向 FDS 上对应版本的资源文件
    
- 回滚时，通过后端服务提供的接口修改版本标识
    

  

### ToB 其他

> 包括北京/武汉研产供、销售、企业效率、基础平台

暂时无法在飞书文档外展示此内容

- 前端静态资源在流水线构建完成后直接打入 Nginx 镜像，使用 Matrix 启动容器，MiFE 代理指向容器
    

  

### 单独 FDS 部署方案

> 例如：[海外商城分享SDK使用指南](https://i02.appmifile.com/i18n/share-sdk/event-external/docs/index.html)

暂时无法在飞书文档外展示此内容

- 静态文件放在 FDS 上，绑定 CDN 域名，直接访问
    
- 缺点：无法使用 history 路由，且了解路径的情况下，可以访问 Bucket 中的全部文件
    

  

### 分流服务访问 FDS 方案

暂时无法在飞书文档外展示此内容

- 使用 Matrix 创建分流服务(Nginx / Nodejs)，流量首先打到分流服务上，随后根据内置逻辑向FDS取回文件
    
- 可在分流服务中实现权限控制、灰度发布等功能
    
- 缺点：需自行实现版本发布、回滚等功能
    

  

### Gitlab Pages 部署

> 内网 Gitlab 提供的静态网站部署服务，可以用来部署基础库的示例文档等，例如：[@mi/spreadjs 文档](http://mit.pages.n.xiaomi.com/fe/mi-spreadjs/#/pages/start/Introduction)

Gitlab Pages 使用文档：https://git.n.xiaomi.com/help/user/project/pages/index

配置实例：https://git.n.xiaomi.com/mit/fe/mi-spreadjs/-/blob/master/.gitlab-ci.yml#L10-L22

  

## 其他特殊场景

### 多测试环境

> [SCM引入独立测试环境的主要变更点](https://xiaomi.f.mioffice.cn/docs/dock4oV0H1W5pt3gJhQAyUAPr7c)

暂时无法在飞书文档外展示此内容

- MiFE 通过不同路径指向**相同** IAM 节点、**相同应用**的**不同部署空间**实例
    

  

### 多业务共享单域名

> [相同域名多系统使用Spreadjs](https://xiaomi.f.mioffice.cn/docx/doxk4JtTbmizvV4e1qzeC3Oay5b)

暂时无法在飞书文档外展示此内容

- MiFE 通过不同路径指向**不同** IAM 节点、**不同应用**的**不同部署空间**实例
    
- 可以视为一种非常规的、特殊的微前端实现
    

  

## 参考

实操案例：[北京研产供前端代码部署方案释义](https://xiaomi.f.mioffice.cn/docx/doxk47aYpwvQr3cguAmD1boFz7c)