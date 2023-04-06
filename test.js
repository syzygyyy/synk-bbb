// 安全问题：使用了 eval() 函数执行用户输入的代码
const userInput = prompt('请输入你的名字：');
eval('alert("你好，" + userInput + "!");');

// 代码质量问题：未使用的变量
const x = 10;
const y = 20;
console.log(x); // x 变量未使用

// 可靠性问题：未处理异常
try {
  const result = 1 / 0;
  console.log(result);
} catch (err) {
  // 没有处理异常
}

// 安全问题：使用了未经转义的用户输入
const userMessage = '<script>alert("Hello!");</script>';
document.getElementById('message').innerHTML = userMessage;

// 代码质量问题：重复的代码
function foo() {
  console.log('foo');
}

function bar() {
  console.log('bar');
}

foo(); // 调用了两次相同的函数
foo();
