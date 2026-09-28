from .schemas import ECHO_TEXT_SCHEMA
from .tools import echo_text


def register(ctx):
    ctx.register_tool(
        name="echo_text",
        toolset="ctn-test",
        schema=ECHO_TEXT_SCHEMA,
        handler=echo_text
    )
