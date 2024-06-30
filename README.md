# ylog
logger 颜色+代码定位

### 安装
```shell
pip install ylog
```

### 示例

```python
import ylog

# 默认日志级别为 info, debug 将不会打印
ylog.Debug('debug msg')
ylog.Info('info msg')
ylog.Warn('warn msg')
ylog.Error('error msg')

# 设置日志级别
ylog.set_level(ylog.LEVEL_WARNING)
```