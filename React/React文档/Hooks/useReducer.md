# useReducer

`useReducer` 是一个 React Hook，它允许你向组件里面添加一个 [reducer](https://zh-hans.react.dev/learn/extracting-state-logic-into-a-reducer)。

```jsx
const [state, dispatch] = useReducer(reducer, initialArg, init?)
```

- [参考](https://zh-hans.react.dev/reference/react/useReducer#reference)
    - [`useReducer(reducer, initialArg, init?)`](https://zh-hans.react.dev/reference/react/useReducer#usereducer)
    - [`dispatch` 函数](https://zh-hans.react.dev/reference/react/useReducer#dispatch)
- [用法](https://zh-hans.react.dev/reference/react/useReducer#usage)
    - [向组件添加 reducer](https://zh-hans.react.dev/reference/react/useReducer#adding-a-reducer-to-a-component)
    - [实现 reducer 函数](https://zh-hans.react.dev/reference/react/useReducer#writing-the-reducer-function)
    - [避免重新创建初始值](https://zh-hans.react.dev/reference/react/useReducer#avoiding-recreating-the-initial-state)
- [疑难解答](https://zh-hans.react.dev/reference/react/useReducer#troubleshooting)
    - [我已经 dispatch 了一个 action，但是打印出来仍然还是旧的 state](https://zh-hans.react.dev/reference/react/useReducer#ive-dispatched-an-action-but-logging-gives-me-the-old-state-value)
    - [我已经 dispatch 了一个 action，但是屏幕并没有更新](https://zh-hans.react.dev/reference/react/useReducer#ive-dispatched-an-action-but-the-screen-doesnt-update)
    - [在 dispatch 后 state 的某些属性变为了 `undefined`](https://zh-hans.react.dev/reference/react/useReducer#a-part-of-my-reducer-state-becomes-undefined-after-dispatching)
    - [在 dispatch 后整个 state 都变为了 `undefined`](https://zh-hans.react.dev/reference/react/useReducer#my-entire-reducer-state-becomes-undefined-after-dispatching)
    - [我收到了一个报错：“Too many re-renders”](https://zh-hans.react.dev/reference/react/useReducer#im-getting-an-error-too-many-re-renders)
    - [我的 reducer 和初始化函数运行了两次](https://zh-hans.react.dev/reference/react/useReducer#my-reducer-or-initializer-function-runs-twice)

---

## 参考 [](https://zh-hans.react.dev/reference/react/useReducer#reference "Link for 参考")

### `useReducer(reducer, initialArg, init?)` [](https://zh-hans.react.dev/reference/react/useReducer#usereducer "Link for this heading")

在组件的顶层作用域调用 `useReducer` 以创建一个用于管理状态的 [reducer](https://zh-hans.react.dev/learn/extracting-state-logic-into-a-reducer)。
```jsx
import { useReducer } from 'react';

function reducer(state, action) {
  // ...
}

function MyComponent() {
  const [state, dispatch] = useReducer(reducer, { age: 42 });
  // ...
```

[参见下方更多示例](https://zh-hans.react.dev/reference/react/useReducer#usage)。

#### 参数 [](https://zh-hans.react.dev/reference/react/useReducer#parameters "Link for 参数")

- `reducer`：用于更新 state 的纯函数。参数为 state 和 action，返回值是更新后的 state。state 与 action 可以是任意合法值。
- `initialArg`：用于初始化 state 的任意值。初始值的计算逻辑取决于接下来的 `init` 参数。
- **可选参数** `init`：用于计算初始值的函数。如果存在，使用 `init(initialArg)` 的执行结果作为初始值，否则使用 `initialArg`。

#### 返回值 [](https://zh-hans.react.dev/reference/react/useReducer#returns "Link for 返回值")

`useReducer` 返回一个由两个值组成的数组：

1. 当前的 state。初次渲染时，它是 `init(initialArg)` 或 `initialArg` （如果没有 `init` 函数）。
2. [`dispatch` 函数](https://zh-hans.react.dev/reference/react/useReducer#dispatch)。用于更新 state 并触发组件的重新渲染。

#### 注意事项 [](https://zh-hans.react.dev/reference/react/useReducer#caveats "Link for 注意事项")

- `useReducer` 是一个 Hook，所以只能在 **组件的顶层作用域** 或自定义 Hook 中调用，而不能在循环或条件语句中调用。如果你有这种需求，可以创建一个新的组件，并把 state 移入其中。
- 严格模式下 React 会 **调用两次 reducer 和初始化函数**，这可以 [帮助你发现意外的副作用](https://zh-hans.react.dev/reference/react/useReducer#my-reducer-or-initializer-function-runs-twice)。这只是开发模式下的行为，并不会影响生产环境。只要 reducer 和初始化函数是纯函数（理应如此）就不会改变你的逻辑。其中一个调用结果会被忽略。

---

### `dispatch` 函数 [](https://zh-hans.react.dev/reference/react/useReducer#dispatch "Link for this heading")

`useReducer` 返回的 `dispatch` 函数允许你更新 state 并触发组件的重新渲染。它需要传入一个 action 作为参数：

```jsx
const [state, dispatch] = useReducer(reducer, { age: 42 });

function handleClick() {
  dispatch({ type: 'incremented_age' });
  // ...
```

React 会调用 `reducer` 函数以更新 state，`reducer` 函数的参数为当前的 state 与传递的 action。

#### 参数 [](https://zh-hans.react.dev/reference/react/useReducer#dispatch-parameters "Link for 参数")

- `action`：用户执行的操作。可以是任意类型的值。通常来说 action 是一个对象，其中 `type` 属性标识类型，其它属性携带额外信息。

#### 返回值 [](https://zh-hans.react.dev/reference/react/useReducer#dispatch-returns "Link for 返回值")

`dispatch` 函数没有返回值。

#### 注意 [](https://zh-hans.react.dev/reference/react/useReducer#setstate-caveats "Link for 注意")

- `dispatch` 函数 **是为下一次渲染而更新 state**。因此在调用 `dispatch` 函数后读取 state [并不会拿到更新后的值](https://zh-hans.react.dev/reference/react/useReducer#ive-dispatched-an-action-but-logging-gives-me-the-old-state-value)，也就是说只能获取到调用前的值。
    
- 如果你提供的新值与当前的 `state` 相同（使用 [`Object.is`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/is) 比较），React 会 **跳过组件和子组件的重新渲染**，这是一种优化手段。虽然在跳过重新渲染前 React 可能会调用你的组件，但是这不应该影响你的代码。
    
- React [会批量更新 state](https://zh-hans.react.dev/learn/queueing-a-series-of-state-updates)。state 会在 **所有事件函数执行完毕** 并且已经调用过它的 `set` 函数后进行更新，这可以防止在一个事件中多次进行重新渲染。如果在访问 DOM 等极少数情况下需要强制 React 提前更新，可以使用 [`flushSync`](https://zh-hans.react.dev/reference/react-dom/flushSync)。
    

---

## 用法 [](https://zh-hans.react.dev/reference/react/useReducer#usage "Link for 用法")

### 向组件添加 reducer [](https://zh-hans.react.dev/reference/react/useReducer#adding-a-reducer-to-a-component "Link for 向组件添加 reducer")

在组件的顶层作用域调用 `useReducer` 来创建一个用于管理状态（state）的 [reducer](https://zh-hans.react.dev/learn/extracting-state-logic-into-a-reducer)。

```jsx
import { useReducer } from 'react';

function reducer(state, action) {
  // ...
}

function MyComponent() {
  const [state, dispatch] = useReducer(reducer, { age: 42 });
  // ...
```

`useReducer` 返回一个由两个值组成的数组：

1. 当前的 state，首次渲染时为你提供的 初始值。
2. `dispatch` 函数，让你可以根据交互修改 state。

为了更新屏幕上的内容，使用一个表示用户操作的 action 来调用 `dispatch` 函数：

```jsx
function handleClick() {
  dispatch({ type: 'incremented_age' });
}
```

React 会把当前的 state 和这个 action 一起作为参数传给 reducer 函数，然后 reducer 计算并返回新的 state，最后 React 保存新的 state，并使用它渲染组件和更新 UI。

```js
#! App.js
import { useReducer } from 'react';

function reducer(state, action) {
  if (action.type === 'incremented_age') {
    return {
      age: state.age + 1
    };
  }
  throw Error('Unknown action.');
}

export default function Counter() {
  const [state, dispatch] = useReducer(reducer, { age: 42 });

  return (
    <>
      <button onClick={() => {
        dispatch({ type: 'incremented_age' })
      }}>
        Increment age
      </button>
      <p>Hello! You are {state.age}.</p>
    </>
  );
}
```


`useReducer` 和 [`useState`](https://zh-hans.react.dev/reference/react/useState) 非常相似，但是它可以让你把状态更新逻辑从事件处理函数中移动到组件外部。详情可以参阅 [对比 `useState` 和 `useReducer`](https://zh-hans.react.dev/learn/extracting-state-logic-into-a-reducer#comparing-usestate-and-usereducer)。

---

### 实现 reducer 函数 [](https://zh-hans.react.dev/reference/react/useReducer#writing-the-reducer-function "Link for 实现 reducer 函数")

reducer 函数的定义如下：
```js
function reducer(state, action) {
  // ...
}
```

你需要往函数体里面添加计算并返回新的 state 的逻辑。一般会使用 [`switch` 语句](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/switch) 来完成。在 `switch` 语句中通过匹配 `case` 条件来计算并返回相应的 state。

```jsx
function reducer(state, action) {
  switch (action.type) {
    case 'incremented_age': {
      return {
        name: state.name,
        age: state.age + 1
      };
    }
    case 'changed_name': {
      return {
        name: action.nextName,
        age: state.age
      };
    }
  }
  throw Error('Unknown action: ' + action.type);
}
```

action 可以是任意类型，不过通常至少是一个存在 `type` 属性的对象。也就是说它需要携带计算新的 state 值所必须的数据。

```js
function Form() {
  const [state, dispatch] = useReducer(reducer, { name: 'Taylor', age: 42 });
  
  function handleButtonClick() {
    dispatch({ type: 'incremented_age' });
  }

  function handleInputChange(e) {
    dispatch({
      type: 'changed_name',
      nextName: e.target.value
    });
  }
  // ...
```

action 的 type 依赖于组件的实际情况。[即使它会导致数据的多次更新，每个 action 都只描述一次交互](https://zh-hans.react.dev/learn/extracting-state-logic-into-a-reducer#writing-reducers-well)。state 的类型也是任意的，不过一般会使用对象或数组。

阅读 [迁移状态逻辑至 Reducer 中](https://zh-hans.react.dev/learn/extracting-state-logic-into-a-reducer) 来了解更多内容。

### 陷阱

state 是只读的。即使是对象或数组也不要尝试修改它：
```jsx
function reducer(state, action) {
  switch (action.type) {
    case 'incremented_age': {
      // 🚩 不要像下面这样修改一个对象类型的 state：
      state.age = state.age + 1;
      return state;
    }
```

正确的做法是返回新的对象：
```js
function reducer(state, action) {
  switch (action.type) {
    case 'incremented_age': {
      // ✅ 正确的做法是返回新的对象
      return {
        ...state,
        age: state.age + 1
      };
    }
```

阅读 [更新对象类型的 state](https://zh-hans.react.dev/learn/updating-objects-in-state) 和 [更新数组类型的 state](https://zh-hans.react.dev/learn/updating-arrays-in-state) 来了解更多内容。

#### 第 1 个示例 共 3 个挑战: 表单（对象类型） [](https://zh-hans.react.dev/reference/react/useReducer#form-object "Link for this heading")

在这个示例中，state 是一个有 `name` 和 `age` 属性的对象。
```jsx
#! App.js
import { useReducer } from 'react';

function reducer(state, action) {
  switch (action.type) {
    case 'incremented_age': {
      return {
        name: state.name,
        age: state.age + 1
      };
    }
    case 'changed_name': {
      return {
        name: action.nextName,
        age: state.age
      };
    }
  }
  throw Error('Unknown action: ' + action.type);
}

const initialState = { name: 'Taylor', age: 42 };

export default function Form() {
  const [state, dispatch] = useReducer(reducer, initialState);

  function handleButtonClick() {
    dispatch({ type: 'incremented_age' });
  }

  function handleInputChange(e) {
    dispatch({
      type: 'changed_name',
      nextName: e.target.value
    }); 
  }

  return (
    <>
      <input
        value={state.name}
        onChange={handleInputChange}
      />
      <button onClick={handleButtonClick}>
        Increment age
      </button>
      <p>Hello, {state.name}. You are {state.age}.</p>
    </>
  );
}
```

#### 第 2 个示例 共 3 个挑战:  代办事项（数组类型） [](https://zh-hans.react.dev/reference/react/useReducer#todo-list-array "Link for this heading")

在这个示例中，reducer 管理一个名为 tasks 的数组。数组 [不能使用修改方法](https://zh-hans.react.dev/learn/updating-arrays-in-state) 来更新。
```jsx
#! App.js
import { useReducer } from 'react';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';

function tasksReducer(tasks, action) {
  switch (action.type) {
    case 'added': {
      return [...tasks, {
        id: action.id,
        text: action.text,
        done: false
      }];
    }
    case 'changed': {
      return tasks.map(t => {
        if (t.id === action.task.id) {
          return action.task;
        } else {
          return t;
        }
      });
    }
    case 'deleted': {
      return tasks.filter(t => t.id !== action.id);
    }
    default: {
      throw Error('Unknown action: ' + action.type);
    }
  }
}

export default function TaskApp() {
  const [tasks, dispatch] = useReducer(
    tasksReducer,
    initialTasks
  );

  function handleAddTask(text) {
    dispatch({
      type: 'added',
      id: nextId++,
      text: text,
    });
  }

  function handleChangeTask(task) {
    dispatch({
      type: 'changed',
      task: task
    });
  }

  function handleDeleteTask(taskId) {
    dispatch({
      type: 'deleted',
      id: taskId
    });
  }

  return (
    <>
      <h1>Prague itinerary</h1>
      <AddTask
        onAddTask={handleAddTask}
      />
      <TaskList
        tasks={tasks}
        onChangeTask={handleChangeTask}
        onDeleteTask={handleDeleteTask}
      />
    </>
  );
}

let nextId = 3;
const initialTasks = [
  { id: 0, text: 'Visit Kafka Museum', done: true },
  { id: 1, text: 'Watch a puppet show', done: false },
  { id: 2, text: 'Lennon Wall pic', done: false }
];

```

#### 第 3 个示例 共 3 个挑战: 使用 Immer 编写简洁的更新逻辑 [](https://zh-hans.react.dev/reference/react/useReducer#writing-concise-update-logic-with-immer "Link for this heading")

如果使用复制方法更新数组和对象让你不厌其烦，那么可以使用 [Immer](https://github.com/immerjs/use-immer#useimmerreducer) 这样的库来减少一些重复的样板代码。Immer 让你可以专注于逻辑，因为它在内部均使用复制方法来完成更新：
```jsx
#! App.js
import { useImmerReducer } from 'use-immer';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';

function tasksReducer(draft, action) {
  switch (action.type) {
    case 'added': {
      draft.push({
        id: action.id,
        text: action.text,
        done: false
      });
      break;
    }
    case 'changed': {
      const index = draft.findIndex(t =>
        t.id === action.task.id
      );
      draft[index] = action.task;
      break;
    }
    case 'deleted': {
      return draft.filter(t => t.id !== action.id);
    }
    default: {
      throw Error('Unknown action: ' + action.type);
    }
  }
}

export default function TaskApp() {
  const [tasks, dispatch] = useImmerReducer(
    tasksReducer,
    initialTasks
  );

  function handleAddTask(text) {
    dispatch({
      type: 'added',
      id: nextId++,
      text: text,
    });
  }

  function handleChangeTask(task) {
    dispatch({
      type: 'changed',
      task: task
    });
  }

  function handleDeleteTask(taskId) {
    dispatch({
      type: 'deleted',
      id: taskId
    });
  }

  return (
    <>
      <h1>Prague itinerary</h1>
      <AddTask
        onAddTask={handleAddTask}
      />
      <TaskList
        tasks={tasks}
        onChangeTask={handleChangeTask}
        onDeleteTask={handleDeleteTask}
      />
    </>
  );
}

let nextId = 3;
const initialTasks = [
  { id: 0, text: 'Visit Kafka Museum', done: true },
  { id: 1, text: 'Watch a puppet show', done: false },
  { id: 2, text: 'Lennon Wall pic', done: false },
];
```

```js
#! package.json
{
  "dependencies": {
    "immer": "1.7.3",
    "react": "latest",
    "react-dom": "latest",
    "react-scripts": "latest",
    "use-immer": "0.5.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --env=jsdom",
    "eject": "react-scripts eject"
  },
  "devDependencies": {}
}
```

### 避免重新创建初始值 [](https://zh-hans.react.dev/reference/react/useReducer#avoiding-recreating-the-initial-state "Link for 避免重新创建初始值")

React 会保存 state 的初始值并在下一次渲染时忽略它。

```jsx
function createInitialState(username) {
  // ...
}

function TodoList({ username }) {
  const [state, dispatch] = useReducer(reducer, createInitialState(username));
  // ...
```

虽然 createInitialState(username) 的返回值只用于初次渲染，但是在每一次渲染的时候都会被调用。如果它创建了比较大的数组或者执行了昂贵的计算就会浪费性能。

你可以通过给  useReducer 的第三个参数传入 初始化函数 来解决这个问题：
```jsx
function createInitialState(username) {
  // ...
}

function TodoList({ username }) {
  const [state, dispatch] = useReducer(reducer, username, createInitialState);
  // ...
```

需要注意的是你传入的参数是 `createInitialState` 这个 **函数自身**，而不是执行 `createInitialState()` 后的返回值。这样传参就可以保证初始化函数不会再次运行。

在上面这个例子中，`createInitialState` 有一个 `username` 参数。如果初始化函数不需要参数就可以计算出初始值，可以把 `useReducer` 的第二个参数改为 `null`。


#### 第 1 个示例 共 2 个挑战: 使用初始化函数 [](https://zh-hans.react.dev/reference/react/useReducer#passing-the-initializer-function "Link for this heading")

这个示例使用了一个初始化函数，所以 `createInitialState` 函数只会在初次渲染的时候进行调用。即使往输入框中输入内容导致组件重新渲染，初始化函数也不会被再次调用。

```jsx
#! todoList.js
import { useReducer } from 'react';

function createInitialState(username) {
  const initialTodos = [];
  for (let i = 0; i < 50; i++) {
    initialTodos.push({
      id: i,
      text: username + "'s task #" + (i + 1)
    });
  }
  return {
    draft: '',
    todos: initialTodos,
  };
}

function reducer(state, action) {
  switch (action.type) {
    case 'changed_draft': {
      return {
        draft: action.nextDraft,
        todos: state.todos,
      };
    };
    case 'added_todo': {
      return {
        draft: '',
        todos: [{
          id: state.todos.length,
          text: state.draft
        }, ...state.todos]
      }
    }
  }
  throw Error('Unknown action: ' + action.type);
}

export default function TodoList({ username }) {
  const [state, dispatch] = useReducer(
    reducer,
    username,
    createInitialState
  );
  return (
    <>
      <input
        value={state.draft}
        onChange={e => {
          dispatch({
            type: 'changed_draft',
            nextDraft: e.target.value
          })
        }}
      />
      <button onClick={() => {
        dispatch({ type: 'added_todo' });
      }}>Add</button>
      <ul>
        {state.todos.map(item => (
          <li key={item.id}>
            {item.text}
          </li>
        ))}
      </ul>
    </>
  );
}
```


#### 第 2 个示例 共 2 个挑战: 直接传入初始值 [](https://zh-hans.react.dev/reference/react/useReducer#passing-the-initial-state-directly "Link for this heading")

这个示例 **没有使用** 初始化函数，所以当你往输入框输入内容导致组件重新渲染的时候，`createInitialState` 函数就会执行。虽然在渲染结果上看没有什么区别，但是多余的逻辑会导致性能变差。
```jsx
#! todoList.js
import { useReducer } from 'react';

function createInitialState(username) {
  const initialTodos = [];
  for (let i = 0; i < 50; i++) {
    initialTodos.push({
      id: i,
      text: username + "'s task #" + (i + 1)
    });
  }
  return {
    draft: '',
    todos: initialTodos,
  };
}

function reducer(state, action) {
  switch (action.type) {
    case 'changed_draft': {
      return {
        draft: action.nextDraft,
        todos: state.todos,
      };
    };
    case 'added_todo': {
      return {
        draft: '',
        todos: [{
          id: state.todos.length,
          text: state.draft
        }, ...state.todos]
      }
    }
  }
  throw Error('Unknown action: ' + action.type);
}

export default function TodoList({ username }) {
  const [state, dispatch] = useReducer(
    reducer,
    createInitialState(username)
  );
  return (
    <>
      <input
        value={state.draft}
        onChange={e => {
          dispatch({
            type: 'changed_draft',
            nextDraft: e.target.value
          })
        }}
      />
      <button onClick={() => {
        dispatch({ type: 'added_todo' });
      }}>Add</button>
      <ul>
        {state.todos.map(item => (
          <li key={item.id}>
            {item.text}
          </li>
        ))}
      </ul>
    </>
  );
}

```

