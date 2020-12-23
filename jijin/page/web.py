from time import sleep

from jijin.page.base_web import BaseWeb


class Web(BaseWeb):
    def start(self):
        # 启动app
        self.base_url = "http://fund.eastmoney.com/trade/hh.html#zwf_,sc_3y,st_asc"
        self._driver.get(self.base_url)
        self._driver.implicitly_wait(5)
        return self


if __name__ == '__main__':
    a = Web().start()
    a.scroll(10000)
    sleep(5)
