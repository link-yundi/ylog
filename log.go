package ylog

import (
	"github.com/pkg/errors"
	"io"
	log_ "log"
	"os"
)

/**
------------------------------------------------
Created on 2022-10-27 10:50
@Author: ZhangYundi
@Email: yundi.xxii@outlook.com
------------------------------------------------
**/

type logLevel int

const (
	LevelTrace logLevel = iota
	LevelDebug
	LevelInfo
	LevelWarn
	LevelError
	logFormat = log_.Ldate | log_.Ltime | log_.Lshortfile // log格式
)

var (
	l = &logger{
		Logger: log_.New(os.Stdout, "", logFormat),
	}
	MapLevel = map[string]logLevel{
		"trace": LevelTrace,
		"debug": LevelDebug,
		"info":  LevelInfo,
		"warn":  LevelWarn,
		"error": LevelError,
	}
)

type logger struct {
	level logLevel
	*log_.Logger
}

func SetLogLevel(logLevel logLevel) {
	l.level = logLevel
}

// 设置log文件路径
func SetLogFile(logPath string) {
	file, err := os.OpenFile(logPath, os.O_RDWR|os.O_APPEND|os.O_CREATE, os.ModePerm)
	if err != nil {
		Error(err)
	}
	writers := []io.Writer{
		file, os.Stdout,
	}
	fileAndStdoutWriter := io.MultiWriter(writers...)
	l.Logger = log_.New(fileAndStdoutWriter, "", logFormat)

}

func canInfo(level logLevel) bool {
	return l.level <= level
}

func Trace(v ...any) {
	if !canInfo(LevelTrace) {
		return
	}
	l.Logger.Println("[TRACE]", v)
}

func Debug(v ...any) {
	if !canInfo(LevelDebug) {
		return
	}
	l.Logger.Println("[DEBUG]", v)
}

func Warn(v ...any) {
	if !canInfo(LevelWarn) {
		return
	}
	l.Logger.Println("[WARN]", v)
}

func Error(err error) {
	if !canInfo(LevelError) {
		return
	}
	l.Printf("[ERROR] original err:%T\n", errors.Cause(err))
	l.Printf("[ERROR] msg: %v\n", errors.Cause(err))
	l.Printf("[ERROR] stack trace: \n %+v\n", err)
}

func Info(v ...any) {
	if !canInfo(LevelInfo) {
		return
	}
	l.Logger.Println("[INFO]", v)
}

func Fatal(v ...any) {
	l.Logger.Fatal("[FATAL]", v)
}
