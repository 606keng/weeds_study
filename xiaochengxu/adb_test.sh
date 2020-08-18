#获取已安装的输入法列表
adb shell ime list -s
#切换到指定的输入法
adb shell settings put secure default_input_method com.android.adbkeyboard/.AdbIME
#使用adb命令在输入框中输入汉字
adb shell am broadcast -a ADB_INPUT_TEXT --es msg '测试可用'