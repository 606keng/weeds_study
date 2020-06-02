"""
相当于charles的map local
"""
from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.
    #如果请求参数中包含"quote.json"和"x="，则将文件response.json中的内容作为响应，返回给移动端
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        with open("response.json",encoding="utf-8") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )