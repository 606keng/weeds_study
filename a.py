import requests

data ={
  "carInfoDTO": {
    "carColor": "啊",
    "carInCity": "北京市",
    "carModel": "奥迪 奥迪A4L 2009款 2.0 TFSI 舒适型",
    "carVin": "LDCC23141C1336812",
    "listingTime": "2020-4-20",
    "mileage": "10",
    "numberPlate": ""
  },
  "carInfoGradeDTO": [
    {
      "carVin": "LDCC23141C1336812",
      "cityCode": "1",
      "grade": "S",
      "gradeContext": "车辆外观瑕疵及喷漆面积小于15%；内饰瑕疵不超过2处、无任何破损，属于头部最优质车源",
      "gradePrice": 4.5,
      "gradeStatus": "1"
    },
    {
      "carVin": "LDCC23141C1336812",
      "cityCode": "1",
      "grade": "A",
      "gradeContext": "车辆外观瑕疵及喷漆面积小于30%；内饰瑕疵不超过4处、破损处不超过2处，综合车况9成新，属于优质车源",
      "gradePrice": 4.26,
      "gradeStatus": "1"
    },
    {
      "carVin": "LDCC23141C1336812",
      "cityCode": "1",
      "grade": "B",
      "gradeContext": "车辆外观有多处瑕疵及喷漆；内饰有少量瑕疵及破损，综合车况8成新，属于精品车源",
      "gradePrice": 4.04,
      "gradeStatus": "1"
    }
  ],
  "reservationInfoDTO": {
    "areaCode": "110000",
    "centerUserId": "ff8080817180dab201718220f1210000",
    "centerUserName": "刘升",
    "centerUserPhone": "18100000000",
    "detailAddress": "望京",
    "serviceCenterId": "bef8a1fd458f40fcbabec9cff8d476ff",
    "sharingCenterId": "1b793649cae143f3b98bd3a3db9053e2"
  },
  "sharingCenterId": "ff8080817180dab201718220f1210000"
}
url = "http://test.carsir.xin:7002/api-olympic-admin/order/create"
hearders = {"token":"7f36ab1cc38746859168826ceb3b21ef",
            "agentId":"8ae854cf2f04417293a55a63420ef538",
            "Content-Type":"application/json; charset=utf-8",
            "version":"20191115",
            "grp":"carsir_app"
            }
r = requests.post(url=url,json=data,headers = hearders)
print(r.json())