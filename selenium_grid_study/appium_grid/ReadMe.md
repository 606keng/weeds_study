学习appium grid链接：http://appium.io/docs/en/advanced-concepts/grid/

下载selenium-server-standalone-3.141.59.jar地址：https://www.selenium.dev/downloads/

启动appium hub：java -jar selenium-server-standalone-3.141.59.jar -role hub

启动appium node：appium --nodeconfig appium_node.json

指定端口启动appium node：appium -p 5723 --nodeconfig appium_node.json

使用adb命令启动app：adb -s 192.168.206.102:5555 shell am start -n com.server.carsir/.garage.MainActivity

启动的服务和json文件中的端口号要一致