# 分析泛型工具类型Partial的实现

**注意 keyof可以获取对象的所有键，然后组合成联合类型**
```ts
Partial<Type>的实现

type Partial<t> =  {
	[P in Typeof T]? T[P] // T[P]表示获取T中每个键的类型
}


用法：
type Props = { a: number; b: string; c: boolean }
type PartialProps = Partial<Props>
```
![[Pasted image 20230328034026.png]]