安装allure：brew install allure
安装allure-pytest:pip install allure-pytest
执行测试用例，生成测试报告数据：pytest 用例文件 --alluredir=报告数据存放的路径
启动allure server查看报告：allure serve 报告数据存放的路径
