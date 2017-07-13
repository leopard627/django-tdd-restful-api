from channels.routing import route
channel_routing = [
    route("http.request", "talk.consumers.http_consumer"),
]

