import pystache
class Test_pystache:
    def test_pystache(self):
        print(pystache.render(
            "hi {{person}}",
            {"person": "doulihang"}
        ))
