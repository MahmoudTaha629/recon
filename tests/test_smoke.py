import pytest
from reconforge.core.module import BaseModule, Context


class Dummy(BaseModule):
    name = "dummy"

    async def run(self, ctx):
        ctx.events = "ran"


async def test_module_runs():
    ctx = Context(scan_id=1)
    await Dummy().run(ctx)
    assert ctx.events == "ran"


def test_base_module_is_abstract():
    with pytest.raises(TypeError):
        BaseModule()
