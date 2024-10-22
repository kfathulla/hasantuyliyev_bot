from .reply_message import reply_message_router


group_routers_list = [
    reply_message_router
]

__all__ = [
    "group_routers_list",
]
