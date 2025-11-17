## husky

### commit-msg

```Bash
#!/bin/sh.
"$(dirname "$0")/_/husky.sh"
npx --no-install commitlint --edit $1
```

- `npx`: 这是一个 npm 包执行器，用于在不安装全局包的情况下运行本地安装的包。它在每次运行时都会检查本地包的最新版本并执行它。这里使用 `npx` 来执行 `commitlint`。
    
- `--no-install`: 用于告诉 `npx` 不要尝试安装缺少的包。它适用于已经安装了 `commitlint` 的情况。
    
- `commitlint`: 要执行的Commitlint 工具包名，用于验证提交消息的格式是否符合规范。
    
- `--edit $1`: 这个部分将 `$1` 作为参数传递给 `commitlint`。`$1` 是一个占位符，表示脚本执行时传递给脚本的第一个参数，通常是提交消息的文件路径。使用 `--edit` 选项告诉 `commitlint` 打开一个编辑器，以便你可以在编辑器中输入提交消息。
    

  

### pre-commit

```Bash

#!/bin/sh.
"$(dirname "$0")/_/husky.sh"
exec < /dev/tty && git cz --hook || true
```

这段脚本的作用是在执行 Git Commitizen（`git cz`）命令之前，将标准输入重定向到终端（tty）设备，并在执行完毕后返回一个退出状态码。它通常用于在 Git 提交时使用 Commitizen 提供的交互式界面来规范提交信息的格式。

- `exec < /dev/tty`: 这部分将标准输入（stdin）重定向到终端设备（tty），即使脚本在一个非交互式环境中运行，也能够接收终端的输入。这是为了让 Commitizen 命令能够与用户进行交互，以获取提交信息。
    
- `git cz --hook`: 这是实际执行的命令部分。`git cz` 是 Commitizen 提供的命令，用于生成符合规范的提交信息。`--hook` 标志用于在提交前应用 Git 钩子脚本。
    
- `|| true`: 这部分是一个逻辑操作符，用于忽略 `git cz` 命令的退出状态码，并始终返回一个成功的状态码。这是为了确保即使 `git cz` 命令出现错误或中断，整个脚本也会继续执行而不会导致失败。
    

  

## bin

软件的安装后文件夹中大部分软件或服务器软件都有个bin文件夹，因为 bin (binary)其中文意思既是:二进制。里面存放的一般是可执行的二进制文件所以我们通常使用较大型的软件时都会发现有这个名称的文件夹。

### Cil（待说明）

```JavaScript
const inquirer = require('inquirer');
const meow = require('meow');
const path = require('path');
const chalk = require('chalk');
const isGitClean = require('is-git-clean');
const boxen = require('boxen')

const packageJson = require('../package.json')

const converterDirectory = path.join(__dirname, '../', 'converters');


//检查是否git存在
function checkGitStatus(force) {
  let clean = false;
  try {
    clean = isGitClean.sync(process.cwd());
  } catch (err) {
    if (err && err.stderr && err.stderr.indexOf('Not a git repository') >= 0) {
      clean = true;
    }
  }

  if (!clean) {
    if (force) {
      console.log(chalk.yellowBright(`WARNING: Forcily continuing.`));
    } else {
      console.log(chalk.yellow('\nBefore we continue, please stash or commit your git changes.'));
      console.log('\nYou may use the --force flag to override this safety check.\n');
      process.exit(1);
    }
  }
}

const CONVERTERS_INQUIRER_CHOICES = [
  //添加git commit标准
  {
    name: 'commit-spec:  Add git commit specification for gitlab or github commit log.',
    value: 'commit-spec'
  },
  // 添加editorconfig 文件
  {
    name: 'editorconfig: Add .editorconfig file for Editor configuration. ',
    value: 'editorconfig'
  },
  //添加gitlabCI/CD集成
  {
    name: 'gitlab-ci:    Add gitlab ci for cloud MICE template.',
    value: 'gitlab-ci'
  }
];

function runConverter({ converter, input, flags }) {
  const converterPath = path.join(converterDirectory, `${converter}/run.js`);
  const handler = require(converterPath);
  if(handler) {
    handler({ input: input, flags: flags });
  }
}

function run() {
  console.log(
    boxen(chalk.blueBright('=== MI APPSTORE UTILS ==='), { padding: 1, margin: 1, borderStyle: 'round', borderColor: 'blue' }),
  )
  const cli = meow(
    {
      description: 'MI commition for git commit specification.',
      help: `
  Usage
          $ npx ${packageJson.name} <converter> <...options>

          converter     One of the choices from under.

                  ${CONVERTERS_INQUIRER_CHOICES.map(x => '- ' + x.name).join('\n    ')}

  Options

          --force       Bypass Git safety checks and forcity run commition cli.
    --help        help.
        `
    }, {
    boolean: ['force', 'help'],
    string: ['_'],
    alias: {
      h: 'help'
    }
  });

  checkGitStatus(cli.flags.force);

  if (cli.input[0] &&
    !CONVERTERS_INQUIRER_CHOICES.find(x => x.value === cli.input[0])
  ) {
    console.error('Invalid converter choice, Pick one of:');
    console.error(CONVERTERS_INQUIRER_CHOICES.map(x => '- ' + x.value).join('\n'));
    process.exit(1);
  }

  inquirer.prompt([
    {
      type: 'list',
      name: 'converter',
      message: 'Which converter would you like to apply?',
      when: !cli.input[0],
      pageSize: CONVERTERS_INQUIRER_CHOICES.length,
      choices: CONVERTERS_INQUIRER_CHOICES
    }
  ]).then(answers => {
    const { converter } = answers;
    const selectedConverter = cli.input[0] || converter;

    return runConverter({
      converter: selectedConverter,
      input: cli.input,
      flags: cli.flags
    })
  })
}


module.exports = {
  run: run
}
```

## converters/commit-spec

```JavaScript
const fs = require('fs');
// fs 模块是 Node.js 的内置模块，用于提供文件系统相关的功能
const path = require('path');
// path 是 Node.js 内置的模块，用于处理文件路径和目录路径的操作。
const execa = require('execa');
// execa 是一个第三方库，用于在 Node.js 中执行外部命令。
const utils = require('../../src/utils.js')
// 引入util.js
const _ = require('lodash');
// 引入 Lodash 库。
const chalk = require('chalk');
// chalk 是一个第三方库，用于为终端输出添加颜色和样式。

// 命令行界面配置对象
const cliConfig = {
  stdio: 'inherit',
  stripEof: false
};

module.exports = function ({ input, flags }) {
  const projectRootDir = utils.getNearestProjectRootDirectory();
  // 获取项目根目录路径
  const projectNodeModuleDir = utils.getNearestNodeModulesDirectory();
  // 获取项目node_module文件路径
  const isYarn = fs.existsSync(path.join(projectRootDir, 'yarn.lock'));
  // "existSync" 方法用于同步地检查指定路径的文件或目录是否存在。
  // 这里用于判断项目根目录中是否有yarn.lock文件
  
  const args = {};
 
  if (isYarn) {
    args.yarn = '--yarn';
    args.install = 'yarn add';
    args.dev = '--dev';
    args.exact = '--exact';
  } else {
    args.yarn = '';
    args.install = 'npm install';
    args.dev = '--save-dev';
    args.exact = '--save-exact';
  };
  // 判断包安装工具是yarn或npm，并对安装参数进行配置
  
  const { indent, packageJsonPath, packageJsonContent } = utils.getPackageJson();
  // 调用utils中getPackageJson函数，获取package的缩进情况，文件路径以及文件对象。
  const isHusky4 = packageJsonContent.husky; //是否配置了husky4，如果没有就安装最新版本的husky
  const packages = ['commitizen', 'cz-conventional-changelog', 'conventional-changelog', 'lint-staged'];
  const isInstalledHuskyPackage = (packageJsonContent.devDependencies && packageJsonContent.devDependencies.husky || packageJsonContent.dependencies && packageJsonContent.dependencies.husky)
  // 判断在devDependencies或dependencies中是否有安装husky工具
    
  if (!isHusky4 && !isInstalledHuskyPackage) {
    packages.push('husky')
  }
  // 如果既没有安装husky@4，也没有安装其他版本的husky，则在packages中添加
  
  const hasInstalledCommitlint = fs.existsSync(path.join(projectNodeModuleDir, '@commitlint'));
  // 判断node_module文件中时候有已经安装的commitlint工具
  if (!hasInstalledCommitlint) {
    packages.push('@commitlint/cli');
    packages.push('@commitlint/config-conventional');
  }
  // 如果没有安装，则在packages中添加

  // note: 安装commitizen
  {
    utils.executeCommand(
      `${args.install} ${args.dev} ${packages.join(' ')}`,
      // 利用模版字符串，三个字段分别为：使用的包安装工具的安装， 安装至生产环境， 安装的包
      cliConfig
      // 安装的参数
    );

    console.log(utils.logSymbols.success, chalk.magentaBright('installed dependencies package.'));
  }
  {
    // note: 初始化
    utils.executeCommand(
      `commitizen init cz-conventional-changelog ${args.yarn} ${args.dev} ${args.exact} ${flags.force ? '--force' : ''}`,
      { ...cliConfig, shell: true, cwd: process.cwd() }
    );
    console.log(utils.logSymbols.success, chalk.magentaBright('installed git commit log flow configuration.'));
  }
  // note: 配置changelog相关命令（待说明）
  {
    const { packageJsonContent } = utils.getPackageJson();
    const changelogAdaterConfig = { scripts: { 'changelog': 'conventional-changelog -p angular -i CHANGELOG.md -s' } }

    if (!packageJsonContent.scripts) {
      packageJsonContent.scripts = {};
    }
    if (packageJsonContent.scripts.changelog && !flags.force) {
      console.log(chalk.yellowBright('WARNING: The changelog script has already exists, it will be covered.'))
    }
    const newPackageJsonContent = _.merge(packageJsonContent, changelogAdaterConfig);

    fs.writeFileSync(packageJsonPath, JSON.stringify(newPackageJsonContent, null, indent) + '\n');

    console.log(utils.logSymbols.success, chalk.magentaBright('installed [changelog] script.'));
  }

  // note: commitlint
  {
    const commitLintConfig = { extends: ["@commitlint/config-conventional"] };
    // 采用@commitlint/config-conventional规则为commitlint规则
    const commitlintConfigPath = path.join(projectRootDir, 'commitlint.config.js');
    // 获取commitlint配置规则的路径
    const hasConfigCommitLint = fs.existsSync(commitlintConfigPath);
    // 判断当前项目中是否存在已有的配置规则
    if (!hasConfigCommitLint) {
      fs.writeFileSync(commitlintConfigPath, `module.exports = ${JSON.stringify(commitLintConfig, null, indent)};\n`);
    } else {
      const config = require(commitlintConfigPath);
      fs.writeFileSync(commitlintConfigPath, `module.exports = ${JSON.stringify(_.merge(config, commitLintConfig), null, indent)};\n`);
    }
    // 采用fs.writeFileSync写入配置规则
    console.log(utils.logSymbols.success, chalk.magentaBright('installed commitlint.config.js file.'));
  }

  // note: 判断与安装husky
  {
    const { packageJsonContent } = utils.getPackageJson();
    const huskyAdaterConfig = {
      husky: {
        hooks: {
          "prepare-commit-msg": "exec < /dev/tty && git cz --hook || true",
          "commit-msg": "commitlint -E HUSKY_GIT_PARAMS",
          "pre-commit": "npx lint-staged",
        }
      }
      // 详细说明在本文档husky模块中
    };
    if (isHusky4) {
      fs.writeFileSync(packageJsonPath, JSON.stringify(_.merge(packageJsonContent, huskyAdaterConfig), null, indent) + '\n');
      // 如果采用的husky版本为4.x，则直接在package.json文件中写入
    } else {

      const huskyConfigPath = path.join(projectRootDir, '.husky');
      // 否则获取项目中.husky文件目录
      if (!fs.existsSync(huskyConfigPath)) {
        utils.executeCommand(`npx husky-init`, { ...cliConfig, shell: true });
        fs.unlinkSync(path.join(huskyConfigPath, 'pre-commit'));
      }
      if (!fs.existsSync(path.join(huskyConfigPath, 'commit-msg'))) {
        utils.executeCommand(`npx husky add .husky/commit-msg 'npx --no-install commitlint --edit $1'`, { ...cliConfig, shell: true });
        // 判断是否已存在commit-msg配置，并对不存在的钩子进行配置。
        // 这里用于处理提交时进行的提交描述校验
      } else {
        console.log(chalk.yellowBright(`.husky/commit-msg file has already exists. If you want to change it, add '${huskyAdaterConfig.husky.hooks['commit-msg']}'`))
      }

      if (!fs.existsSync(path.join(huskyConfigPath, 'prepare-commit-msg'))) {
        utils.executeCommand(`npx husky add .husky/prepare-commit-msg '${huskyAdaterConfig.husky.hooks['prepare-commit-msg']}'`, { ...cliConfig, shell: true });
       // 判断是否已存在prepare-commit-msg配置，并对不存在的钩子进行配置。
       // 这里用于在提交描述时采用commizen进行描述提示
      } else {
        console.log(chalk.yellowBright(`.husky/prepare-commit-msg file has already exists. If you want to change it, add '${huskyAdaterConfig.husky.hooks['prepare-commit-msg']}'`))
      }

      if (!fs.existsSync(path.join(huskyConfigPath, 'pre-commit'))) {
        utils.executeCommand(`npx husky add .husky/pre-commit '${huskyAdaterConfig.husky.hooks['pre-commit']}'`, { ...cliConfig, shell: true });
        // 判断是否已存在pre-commit配置，并对不存在的钩子进行配置。
       // 这里用于在对提交代码进行规则性校验。
      } else {
        console.log(chalk.yellowBright(`.husky/pre-commit file has already exists. If you want to change it, add '${huskyAdaterConfig.husky.hooks['pre-commit']}'`))
      }
    }

    console.log(utils.logSymbols.success, chalk.magentaBright('installed husky hooks.'));
  }

  // note: lint-staged配置
  {
    const { packageJsonContent } = utils.getPackageJson();
    // 通过getPackageJson获取经过JSON.parse转换的package.json对象
    const lintStagedConfig = {
      "lint-staged": {
        "*.{js,jsx,ts,tsx,vue}": "eslint --cache"
        // 在暂存区内对后缀为.js, .jsx, .ts, .tsx, .vue的文件进行lint校验
      }
    };
    // 对lint-staged工具进行配置
    if(!packageJsonContent["lint-staged"]) packageJsonContent["lint-staged"] = {}
    // 对原有package.json内对lint-staged配置进行情况
    const newPackageJsonContent = _.merge(packageJsonContent, lintStagedConfig);
    // 利用lodash库函数中的merge函数对packjson内对lint-staged工具进行重新配置。
    fs.writeFileSync(packageJsonPath, JSON.stringify(newPackageJsonContent, null, indent) + '\n');
    // 通过fs.writeFileSync将配置完的lint-staged写入package.json文件
    console.log(utils.logSymbols.success, chalk.magentaBright('installed [lint-staged] script.'));
  }
}
```

  

## src/utils

```JavaScript
const fs = require('fs');
// fs 模块是 Node.js 的内置模块，用于提供文件系统相关的功能
const path = require('path');
// path 是 Node.js 内置的模块，用于处理文件路径和目录路径的操作。
const execa = require('execa');
// execa 是一个第三方库，用于在 Node.js 中执行外部命令。
const chalk = require('chalk')
// chalk 是一个第三方库，用于为终端输出添加颜色和样式。
const detectIndent = require('detect-indent');
// detect-indent 是一个第三方库，用于检测代码文件中的缩进风格和缩进大小。
const findNodeModules = require('find-node-modules');
// findNodeModules是一个第三方库，这个库的作用是用于在 Node.js 项目中查找 node_modules 目录的路径

// 获取最近的NodeModules目录
function getNearestNodeModulesDirectory() {
        const nodeModulesDirectories = findNodeModules({ relative: false });
        // 原本findNodeMoudles会返回目录的相对路径，但是加了参数relative后就会返回目录的绝对路径
        if (nodeModulesDirectories && nodeModulesDirectories.length > 0) {
                return nodeModulesDirectories[0];
        // 利用findNodeMoudles函数找到的是所有模块目录的路径
        // 为什么找到的node_module是一个数组呢？
        // 因为一个项目中会有很多依赖，每个依赖目录中都会有一个node_modules
        // 因此这里获取数组下标为0的元素，即项目中的node_module
        } else {
                console.error(`Error: Could not locate node_modules in your project's root directory. Did you forget to npm init or npm install?`)
        }
        // 否则报错，无法定位到node_modules在你的项目目录中
}


// 获取项目根目录路径
function getNearestProjectRootDirectory () {
  return path.join(getNearestNodeModulesDirectory(), '/../');
}
// path.join() 是 Node.js 内置的路径处理函数，用于将多个路径片段连接成一个规范化的路径。
// 它接受一个或多个路径参数，并返回连接后的路径。
// 这里将getNearestNodeModulesDirectory()返回的项目目录中的node_modules路径后，与'/../'字符串进行连接
// 从而获得项目根目录的路径
// 注意：但是即使这里使用的是正斜杠/，通过path.join都能正确的在不同平台上进行正确的转换。
// 为什么这里不直接利用字符串来进行连接？
// path.join() 可以以平台无关的方式连接路径片段，确保生成的路径在不同操作系统上都是有效的
// 比如我在window平台上，路径的连接方式是反斜杠\，而在linux平台上，路径的连接方式是正斜杠/
// 如果直接利用字符串连接，就会造成在window平台上无法正常获取到项目的跟路径

function executeCommand(command, cliConfig) {
  // command：要执行的命令行指令，作为一个字符串。
  // cliConfig：命令行配置选项，作为一个对象传入。
  const result = execa.commandSync(command, cliConfig);
  // execa.commandSync() 方法来同步执行命令行指令
  // 这里使用同步执行的原因是诶为了等待执行结果返回，确保在继续执行后续代码之前获取到命令的执行结果。
  if (result.error) {
    throw result.error;
  }
}

const main = {
        info: chalk.blue('ℹ'),    // 这里利用chalk库函数，将ℹ符号转变成蓝色。
        success: chalk.green('✔'),    // 这里利用chalk库函数，将✔符号转变成绿色。
        warning: chalk.yellow('⚠'),    // 这里利用chalk库函数，将⚠符号转变成黄色。
        error: chalk.red('✖')    // 这里利用chalk库函数，将✖符号转变成红色。
};

const fallback = {
        info: chalk.blue('i'),
        success: chalk.green('√'), 
        warning: chalk.yellow('‼'),
        error: chalk.red('×')
}; // 颜色变化同上

// 这里inUnicodeSupported函数用于判断对应的终端是否支持相应的Unicode字符
// 结合下面代码，如果是不为windows操作系统，或者 。。。。则使用main函数中的信息标志。
// 否则使用fallback函数中的信息标志。
const logSymbols = isUnicodeSupported() ? main : fallback;

function isUnicodeSupported() {
        // process 是一个全局变量。
        //它是 Node.js 运行时环境提供的一个全局对象。它包含了有关当前 Node.js 进程的信息和控制方法。
        if (process.platform !== 'win32') {
                return true;
        }
        // 这里判断使用的操作系统是否为windows
        // 同时这里需要注意，win32并不是代表window32位操作系统
        // 无论是 32 位还是 64 位的 Windows 操作系统，process.platform 返回的都是 'win32'。
        // 这是由于历史原因，在 Node.js 中，Windows 平台的标识统一使用 'win32'。

        return Boolean(process.env.CI) ||
                Boolean(process.env.WT_SESSION) || // Windows Terminal
                process.env.TERM_PROGRAM === 'vscode' ||
                process.env.TERM === 'xterm-256color' ||
                process.env.TERM === 'alacritty';
        // process.env 是 Node.js 中的一个特殊对象，它包含了当前进程的环境变量。
        // process.env.CI 是一个环境变量，通常用于指示当前进程是否在持续集成环境中运行。
        // process.env.WT_SESSION 是一个环境变量，用于表示当前 Windows 终端的会话标识符。
        // process.env.TERM_PROGRAM 是一个环境变量，用于指示当前终端程序的名称或标识符。
        // process.env.TERM 是一个环境变量，用于指示当前终端的类型或名称。       
}


function getPackageJson(){
  const projectRootDir = getNearestProjectRootDirectory(); // 获取项目的根目录路径
  const packageJsonPath = path.join(projectRootDir, 'package.json'); // 获取项目根目录中国的package.json文件路径
  const packageJsonString = fs.readFileSync(packageJsonPath, 'utf-8');
  // fs.readFileSync() 是 fs 模块提供的一个同步方法，用于读取指定路径下的文件内容。
  // 这里读取了package.json文件的内容，并读取到的内容作为字符串返回。
  const indent = detectIndent(packageJsonString).indent || '  ';
  // 检验返回字符串中的packageJsonString中的缩进格式，如果缩进方式不统一，indent会出现undefined的情况
  // 这时候就将indent的值设为'  ',即两个空格
  // 这里需要注意，detectIndent返回对象包含的indent属性的检测，
  // 会分析代码文件的前几行，并找到最常见的缩进字符作为代表性的缩进方式,将其设为indent的值。
  const packageJsonContent = JSON.parse(packageJsonString);
  // 通过JSON.parse对字符串进行解析
  return {
    indent,
    packageJsonContent,
    packageJsonPath
  }
}

module.exports = {
  getNearestNodeModulesDirectory: getNearestNodeModulesDirectory,
  // 返回获取项目Node_module路径的函数
  getNearestProjectRootDirectory: getNearestProjectRootDirectory,
  // 返回获取项目根目录路径的函数
  executeCommand: executeCommand,
  logSymbols: logSymbols,
  // 返回终端日志符号对象
  getPackageJson: getPackageJson
  // 返回获取Package.json中相关数据的函数
}
```