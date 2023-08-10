```js
// 用react实现一个倒计时组件CountDown
// 组件接收一个名为count的参数，类型为数字（大于0）
// 组件渲染出count的值，并且每秒减一，直到0

import { useState, useEffect } from 'react'
function CountDown({count}) {
	// ...
  const [timer, setTimer] = useState(count)
  useEffect(() => {
   
    if (timer >= 1) {
      const timeId = setInterval(() => {
        setTimer(timer - 1)
      }, 1000)
      return () => clearInterval(timeId)
    }
  },[timer])
  
  return (
    <div>
    	{timer}
  	</div>
  )
}


function Parent() {
	const [count, setCount] = useState(10)

  useEffect(
    () => {
		// setTimeout(() => {
			setCount(20)
    // }, 1000)
		},
 		[]
  )
  
  return <CountDown count={count}/>
}
```