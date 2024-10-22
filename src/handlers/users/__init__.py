# ADMIN

# MANAGER


# USER
from .echo import echo_router
from .start import start_router
from .help import help_router
from .message import message_router

user_routers_list = [
    start_router,
    help_router,
    message_router,
    echo_router,  # echo_router must be last
]

__all__ = [
    "user_routers_list",
]
