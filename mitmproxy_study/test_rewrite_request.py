#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_rewrite_request.py
@time: 2020/09/24 
"""
import json
import base64

"""Take incoming HTTP requests and replay them with modified parameters."""
from mitmproxy import ctx


def request(flow):
    # Avoid an infinite loop by not replaying already replayed requests
    if flow.request.is_replay:
        return
    flow = flow.copy()
    if "https://test.carsir.xin/olympic/api-olympic-admin/sharingcentercity/centerShopByCityId" in flow.request.pretty_url:
        # Only interactive tools have a view. If we have one, add a duplicate entry
        # for our flow.
        if "view" in ctx.master.addons:
            ctx.master.commands.call("view.flows.add", [flow])
        data = flow.request.content
        print(data)
        a = eval(data)
        # data = str(flow.request.content, encoding="utf-8")
        # data = json.loads(data)
        a["serviceAreaId"] = "130100"
        flow.request.content = bytes('{}'.format(a), 'utf-8')
        print(flow.request.content)
        ctx.master.commands.call("replay.client", [flow])
