package ylog

import "testing"

/**
------------------------------------------------
Created on 2022-10-27 11:05
@Author: ZhangYundi
@Email: yundi.xxii@outlook.com
------------------------------------------------
**/

func TestDebug(t *testing.T) {
	SetLogLevel(LevelDebug)
	msg := "debug"
	Trace(msg)
	Debug(msg)
	Info(msg)
	Warn(msg)
}

func TestSetLogFile(t *testing.T) {
	SetLogFile("logtest")
	msg := "this is debug msg"
	Debug(msg)
}
