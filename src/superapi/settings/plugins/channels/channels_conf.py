#!/usr/bin/env python
# -*- coding: utf-8 -*-


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "superapi.routing.channel_routing",
    },
}
