## PySh

> Yet another shell can run anywhere Python exists.

### Why another shell

> Because it's fun.

### Supported shell feature

Common shell features can be found [here](http://www.tldp.org/LDP/intro-linux/html/x12120.html). Pysh already have:

- `|`, Pipe output
- `$var`, Use value for variable
- `" "`, Double quote (allows variable and command expansion)
- `*`, Match any character(s) in filename
- `?`, Match single character in filename
- `[ ]`, Match any characters enclosed


### Usage

```
git clone https://github.com/jiacai2050/pysh.git
cd pysh
python -m pysh.shell

## Demo
> ls README*
README.md

> ls README.??
README.md

> echo $HOME
/Users/liujiacai

> echo ${JAVA_HOME}
/Library/Java/JavaVirtualMachines/jdk1.8.0_40.jdk/Contents/Home

> pwd
/Users/liujiacai/codes/python/pysh

> cd ..
/Users/liujiacai/codes/python

> pwd
/Users/liujiacai/codes/python

> cat /etc/hosts | grep 127.0.0.1
127.0.0.1       localhost

> grep 127.0.0.1 /etc/hosts
127.0.0.1       localhost
```

Supported commands can be found [here](./pysh/builtins).

More commands are on the way. PR welcomed !

Have fun 😄

### How PySh work

A shell in unix box is a bridge bewteen user and the kernel through [system call](https://en.wikipedia.org/wiki/System_call).

![how unix shell work](./assets/unix_shell.gif)

As we can see from above picture (taken from [here](http://docstore.mik.ua/orelly/unix/upt/ch01_02.htm#UPT-ART-1002-FIG-0)), some commands (eg `ls`, `cat`) are passed to other programs, while built-in commands (eg `cd`, `exit`) are executed inside shell. This way can keep shell small in size and strong in function.

In order to let PySh run anywhere (hi, Windows, I mean you), PySh implmented all commands in its core, so there is no [differences](http://unix.stackexchange.com/questions/11454/what-is-the-difference-between-a-builtin-command-and-one-that-is-not) bewteen builtins and one that is not, also you can say all commands are builtins.

One thing I should mention here is:

> Pipelines between commands are supported by generator in Python.

So, every command should `yield` something, this is like s-expression in Lisp world, where every s-expression should return a value.

### How to contribute

PySh use [pre-commit](http://pre-commit.com/) to ensure code quality, so you should install it before contribute.

Fork and PR 🍺

### TODO

- [redirection](https://en.wikipedia.org/wiki/Redirection_%28computing%29)
- [wildcarding](https://en.wikipedia.org/wiki/Wildcard_character)
- [here documents](https://en.wikipedia.org/wiki/Here_document)
- [command substitution](https://en.wikipedia.org/wiki/Command_substitution)
- [variables](https://en.wikipedia.org/wiki/Variable_%28programming%29)
- [control structures for condition-testing and iteration](https://en.wikipedia.org/wiki/Control_flow)
- more useful commands
    - curl
    - wget
    - sed

### License

[MIT License](http://liujiacai.net/license/MIT.html?year=2016) © Jiacai Liu

PySh is inspired from [yosh](https://github.com/supasate/yosh).
