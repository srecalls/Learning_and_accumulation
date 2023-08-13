## Hooks（钩子）
### useHistory
```jsx
// useHistory
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Link, Route, Switch, useHistory, withRouter } from 'react-router-dom';

const Home = () => {
  return <div>Home</div>;
};

const About = () => {
  const history = useHistory();

  const handleClick = () => {
    console.log(useHistory);
    history.push('/');
  };
  return (
    <>
      <div>About</div>
      <button type="button" onClick={handleClick}>
        Go home
      </button>
    </>
  );
};

const TestHomeButton = () => {
  const history = useHistory();

  const errClick = () => {
    console.log(useHistory);
    history.push('/');
  };
  return (
    <>
      <BrowserRouter>
        <button type="button" onClick={errClick}>
          Go home(错误方式)
        </button>
        <h1>App</h1>
        <ul>
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link to="/">home</Link>
          </li>
        </ul>
        <Switch>
          <Route exact={true} path="/" component={Home} />
          <Route exact={true} path="/about" component={About} />
        </Switch>
      </BrowserRouter>
    </>
  );
};

ReactDOM.render(<TestHomeButton />, document.body);
```

注意useHistory使用的条件，使用不当会报错 ' Cannot read property 'push' of undefined',原因： 您正试图在`Router`之外使用`history`钩子。在`对应`组件中编写函数。
![[react-router-dom API 详解，入门（一）.png]]