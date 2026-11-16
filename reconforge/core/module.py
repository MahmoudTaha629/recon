from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class Context:
    """كل اللي الـ module محتاجه. هتتملى بالحقيقي في Phase 1."""
    scan_id: int
    config: Any = None
    db: Any = None
    http: Any = None     # كل الـ requests لازم تعدّي من هنا (scope + rate limit)
    dns: Any = None
    ports: Any = None
    scope: Any = None
    events: Any = None


class BaseModule(ABC):
    name: str = ""
    depends_on: list[str] = []

    @abstractmethod
    async def run(self, ctx: Context) -> None:
        """يقرا مدخلاته من ctx.db ويكتب نتايجه فيها."""
