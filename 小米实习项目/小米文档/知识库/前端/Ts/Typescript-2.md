

## 知识层面

先来看下面这张思维导图，回顾一下基础知识

![[Typescript-2.png]]

### 类型推断

#### 是什么？

在编译器typescript可以推断出变量的类型，它不是一个具体的语法，而是需要去理解这是typescript运作的一部分。如果在代码中没有指定type，而且typescript有不能从上下文中去推断出变量的类型，那么就会默认类型为any。

```
// 推算msg为string
let msg = "hello world!";
msg = 10;

const names = ["Alice", "Bob", "Eve"];
names.forEach((name) => {
    name.touppercase(); // 会报错，因为name的类型被推断为string
})

// getNumber的返回被推断为number
function getNumber() {
    return 10;
}

// 函数的返回类型被推断为number[] | string 
function getFirstThree(x: number[] | string) { 
    return x.slice(0, 3); 
}
```

这样做的好处主要是减少类型申明，不过不好的地方是写typescript的时候会把忽略掉这一能力，导致被错误弄得摸不着头脑

### 范型

#### 是什么？

范型可以代表多种类型，相当是一个类型变量

和联合类型的区别在于可以表明不同类型之间的关系，例如：

1. 函数的输出类型和输入存在关系

```
function add1(x: number, y: number): number {
    return x + y;
}
function add2(x: string, y: string): string {
    return x + y;
}
type numberOrString = number | string;
function add(x: numberOrString, y: numberOrString): numberOrString {
    return x + y;
}
add(0, '1') // 这样可能就和预期不符合，而typecript也没有办法发现问题
// 用范型
function addT<T>(x: T, y: T): T {
}
```

2. 场景范型变量（只是约定俗成而已，并无强制的规定）

- T（Type）：表示一个 TypeScript 类型
- K（Key）：表示对象中的键类型
- V（Value）：表示对象中的值类型
- E（Element）：表示元素类型

#### 使用场景

- 范型

```
interface Service<T> {
    type: T,
    data: T extends 'GET' ? string : number,
}
```

```
type MethodDecorator = <T>(target:Object, propertyKey: string | symbol,         descriptor: TypePropertyDescript<T>) => TypedPropertyDescriptor<T> | void;
```

- 函数

```
function identity<T>(arg: T) : T{ 
    return arg; 
} 
```

### 类型运算

类型运算的结果依然还是类型

- typeof：获取变量的类型
- keyof：获取类型的key值
- in：遍历类型
- infer：在条件类型语句中，可以用 `infer` 声明一个类型变量并且对它进行使用

```
type ReturnType<T> = T extends (
  ...args: any[]
) => infer R ? R : any;
```

- extends: 可以通过 extends 关键字添加泛型约束

## 实操层面

### 开源工程代码学习

1. https://github.com/k8w/tsrpc-base-client/blob/main/src/client/BaseClient.ts
2. https://github.com/k8w/tsrpc-base-client/blob/main/src/client/BaseHttpClient.ts

下面贴一下2的代码

```
import { BaseServiceType, ServiceProto, TsrpcError } from "tsrpc-proto";
import { TransportOptions } from "../models/TransportOptions";
import { BaseClient, BaseClientOptions, defaultBaseClientOptions, PendingApiItem } from "./BaseClient";

/**
 * Base HTTP Client
 */
export class BaseHttpClient<ServiceType extends BaseServiceType> extends BaseClient<ServiceType> {

    readonly type = 'SHORT';

    private _http: IHttpProxy;
    private _jsonServer: string;

    readonly options!: Readonly<BaseHttpClientOptions>;
    constructor(proto: ServiceProto<ServiceType>, http: IHttpProxy, options?: Partial<BaseHttpClientOptions>) {
        super(proto, {
            ...defaultBaseHttpClientOptions,
            ...options
        });
        this._http = http;
        this._jsonServer = this.options.server + (this.options.server.endsWith('/') ? '' : '/');
        this.logger?.log('TSRPC HTTP Client :', this.options.server);
    }

    protected async _sendData(data: Uint8Array | string, options: TransportOptions, serviceId: number, pendingApiItem?: PendingApiItem): Promise<{ err?: TsrpcError | undefined; }> {
        let sn = pendingApiItem?.sn;
        let promise = (async (): Promise<{ err: TsrpcError | undefined; res?: undefined } | { res: string | Uint8Array, err?: undefined }> => {
            // Do Send
            let { promise: fetchPromise, abort } = this._http.fetch({
                url: typeof data === 'string' ? (this._jsonServer + this.serviceMap.id2Service[serviceId].name) : this.options.server,
                data: data,
                method: 'POST',
                timeout: options.timeout || this.options.timeout,
                headers: { 'Content-Type': typeof data === 'string' ? 'application/json' : 'application/octet-stream' },
                transportOptions: options,
                responseType: typeof data === 'string' ? 'text' : 'arraybuffer',
            });

            if (pendingApiItem) {
                pendingApiItem.onAbort = () => {
                    abort();
                }
            }

            // Aborted
            if (pendingApiItem?.isAborted) {
                return new Promise(rs => { });
            }

            let fetchRes = await fetchPromise;
            if (!fetchRes.isSucc) {
                return { err: fetchRes.err };
            }
            return { res: fetchRes.res };
        })();
        
        promise.then(v => {
            if (v.res) {
                this._onRecvData(v.res, pendingApiItem);
            }
        })

        // Finally
        promise.catch(e => { }).then(() => {
            if (pendingApiItem) {
                pendingApiItem.onAbort = undefined;
            }
        })

        return promise;
    }
}

export const defaultBaseHttpClientOptions: BaseHttpClientOptions = {
    ...defaultBaseClientOptions,
    server: 'http://localhost:3000',
    // logger: new TerminalColorLogger(),
    jsonPrune: true
}

export interface BaseHttpClientOptions extends BaseClientOptions {
    /** Server URL, starts with `http://` or `https://`. */
    server: string;

    /**
     * Whether to automatically delete excess properties that not defined in the protocol.
     * @defaultValue `true`
     */
    jsonPrune: boolean;
}


export interface IHttpProxy {
    fetch(options: {
        url: string,
        data: string | Uint8Array,
        method: string,
        /** ms */
        timeout?: number,
        headers?: { [key: string]: string },
        transportOptions: TransportOptions,
        responseType: 'text' | 'arraybuffer'
    }): {
        abort: () => void,
        promise: Promise<{ isSucc: true, res: string | Uint8Array } | { isSucc: false, err: TsrpcError }>
    };
}
```

> 越是底层逻辑代码，所需要的类型越丰富，需要用到的类型运算也越复杂

### mobile工程写法优化

1. 写代码的时候需要代码提示的地方就有必要添加类型描述

```
  // base 设置
  base({
    recordParams: {
      ref: PAGE_REF,
      oneTrackRef: PAGE_REF,
    },
  });
  
  // 现在的base是这么写的
  export default function base(options: Record<string, any>): void {
      
  }
  
  // 可以改成
  interface BaseOption {
      recordParams: {
          ref: string, 
          oneTrackRef: string,
      },
      scrollEl?: HTMLElement,
      backEventCb: () => boolean
  }
  export default function base(options: BaseOption): void {
  
  }
```

2. 服务端接口请求返回结果的类型定义

```
abstract class Service<T> {}

export default class getPageInfoService<T> extends Service<T> {}

new getPageInfoService<{ code: number }>({
    // 接口参数设置
  })
.get({
  path: url,
  load: load,
  nativeLoad: nativeLoad,
})
.then((msg) => {
  if (msg.code === 0) {
    // 接口处理
    // window.vm.pageData = reformData(msg);
  }
})


```

## 参考文档

https://www.typescriptlang.org/assets/typescript-handbook.pdf

https://xiaomi.f.mioffice.cn/drive/folder/fldk4tj4Of6PVEVhfMLMpf22Whg