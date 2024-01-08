var express = require('express');
var router = express.Router();
var path = require('path');
const { spawn } = require('child_process');
const fs = require('fs');

/* GET home page. */
router.get('/', function (req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/call-python', (req, res) => {
  // 设置Python脚本的路径和传递的参数
  const options = {
    scriptPath: path.join(__dirname, '../python/'),  // 指定Python脚本所在的目录
    args: [req.query.prompt]   // 传递给Python脚本的参数
  };

  // 使用spawn函数启动一个Python子进程
  const pythonProcess = spawn('python', [path.join(__dirname, `../python/${req.query.script}.py`), req.query.prompt]);

  // 监听子进程的输出事件
  pythonProcess.stdout.on('data', (message) => {
    message = String(message).trim();
    if (message !== 'Over')
      console.error(message);
    res.send(message);
  });

  // 监听子进程的错误事件
  pythonProcess.stderr.on('data', (error) => console.error(error));
});

router.post('/load-story', (req, res) => {
  fs.readFile(path.join(__dirname, '../result/story'),
    (err, data) => {
      data = String(data);

      if (err) {
        console.error(err.message);
        res.send({
          title: '',
          content: '',
          error: err.message
        });

        return;
      }

      const textArray = data.split('\n');
      const titleIndex = textArray[0].includes('《') ? 0 : 1;
      res.send({
        title: textArray[titleIndex].split("：").pop().replace(/《|》/g, ''),
        content: textArray.slice(titleIndex + 1, textArray.length - 1).join('\n'),
        error: null
      });
    });
});

module.exports = router;
