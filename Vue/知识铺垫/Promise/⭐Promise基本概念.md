Promise使用

	promise它是一个对象，通过reslove和reject将promise由未决阶段推向已决阶段，通过then方法，catch方法，进行后续的处理。对于使用，从题中来看：

注意点和总结：

	- Promise的状态一经改变就不能再改变。
	- 在Promise中，如果你的返回值不是个promise，它会将你的返回值包成一个promise对象返回。
	- then方法和catch方法都会返回一个promise对象，并且可以被调用多次。
	- catch不管被链到哪里，都会捕获上层未捕获到的错误。
	- then方法和catch方法中return一个error对象并不会抛出错误，并不会被后续的catch所捕获。
	- then方法 或catch方法 返回的值不能是 promise 本身，否则会造成死循环。
	- then方法 或者catch方法的参数期望是函数，传入非函数则会发生值透传。
	- finally方法也是返回一个Promise，他在Promise结束的时候，无论结果为resolved还是rejected，都会执行里面的回调函数，它的回调函数不会接受任何参数，在其中如果抛出异常，后续用catch也可以接收到。



![[Pasted image 20230302141747.png]]
## Promise.then
![[Pasted image 20230302141849.png]]
![[Pasted image 20230302142356.png]]
![[Pasted image 20230302142549.png]]
![[Pasted image 20230302142823.png]]
![[Pasted image 20230302142847.png]]

## Promise.catch
![[Pasted image 20230302143253.png]]
![[Pasted image 20230302143556.png]]
![[Pasted image 20230302143654.png]]
![[Pasted image 20230302143621.png]]

## Promise.all
![[Pasted image 20230302143950.png]]

## Promise.race
![[Pasted image 20230302144148.png]]

## 基于Promise封装读文件的方法
![[Pasted image 20230302144354.png]]
![[Pasted image 20230302144500.png]]
![[Pasted image 20230302144557.png]]
![[Pasted image 20230302144938.png]]
![[Pasted image 20230302145032.png]]