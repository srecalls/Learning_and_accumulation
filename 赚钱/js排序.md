### 1. 冒泡排序

```js
const fn = (arr) => {
    for(let i = 0; i < arr.length - 1; i++) {
      for(let j = 0; j < arr.length - 1 - i; j++) {
        if (arr[j] > arr[j+1]) {
          const temp = arr[j]
          arr[j] = arr[j+1]
          arr[j+1] = temp
        }
      }
    }
    return arr
  }
```

###  2. 选择排序



``` js
//快速排序
/*
	1. 选择一个基准数，通常是数组的第1个数。
	2. 重新排序数组，所有数比基准数小的挪放在基准数前面，所有数比基准数大的挪在基准数的后面。
	3. 在这个排序之后，该基准数就处于数组有序后的正确位置。
	4. 把基准数前后两个子数组，按照上述步骤继续排序，直到整个数组有序。
*/
function quickSort(arr) {
  if(arr.length < 2) {
    return arr;
  } else {
    const pivot = arr[0]; // 基准值
    const pivotArr = []; // 一样大的放中间
    const lowArr= []; // 小的放左边
    const hightArr = []; // 大的放右边
    arr.forEach(current => {
      if(current === pivot) pivotArr.push(current);
      else if(current > pivot) hightArr.push(current);
      else lowArr.push(current);
    })
    return quickSort(lowArr).concat(pivotArr).concat(quickSort(hightArr));
  }
}
```

``` js
//堆排序
function buildMaxHeap(arr) {
    for (let i = Math.floor(arr.length / 2 - 1); i >= 0; i--) {
        heapify(arr, i, arr.length);
    }
}
function heapify(arr, i, len) {
    let left = i * 2 + 1,
        right = i * 2 + 2,
        largest = i;
    if (left < len && arr[left] > arr[largest]) {
        largest = left;
    }
    if (right < len && arr[right] > arr[largest]) {
        largest = right;
    }
    if (largest != i) {
        swap(arr, i, largest);
        heapify(arr, largest, len);
    }
}
function swap(arr, i, j) {
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
function heapSort(arr) {
    buildMaxHeap(arr);
    for (let i = arr.length - 1; i > 0; i--) {
        swap(arr, 0, i);
        heapify(arr, 0, i);
    }
    return arr;
}
```

``` js
//归并排序
function mergeSort(arr) {
    if (arr.length < 2) {
        return arr;
    }
    let middle = Math.floor(arr.length / 2);
    return merge(mergeSort(arr.slice(0, middle)), mergeSort(arr.slice(middle)));
}
function merge(leftArr,rightArr){
    let result = [];
    while(leftArr.length && rightArr.length){
        if(leftArr[0] <= rightArr[0]){
            result.push(leftArr.shift());
        }else{
            result.push(rightArr.shift());
        }
    }
    return result.concat(leftArr).concat(rightArr);
}
```

