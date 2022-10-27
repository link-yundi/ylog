# ylog

### 安装

```sh
go get -u github.com/link-yundi/ylog
```

### 特性

- 级别
- 控制台+文件输出
- `error stack trace`

### 示例

```go
import log "github.com/link-yundi/ylog"

// 设置log level
log.SetLogLevel(log.LevelDebug)

// 通过string设置
if logLevel, ok := log.MapLevel["debug"]; ok {
    log.SetLogLevel(logLevel)
} 

// 设置log file
logFilePath := "log/to/path"
log.SetLogFile(logFilePath)
```

