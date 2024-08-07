from src.model.explorer import Explorer
# 가짜 데이터. 10장에서 실제 데이터베이스와 SQL로 바꾼다. 
_explores = [
    Explorer(name="Claude Hande"
             , country="FR"
             , description="보름달이 뜨면 만나기 힘듦"
             ),
    Explorer(name="Noah Weiser"
             , country="DE"
             , description="눈이 나쁘고 벌모도를 가지고 다님"
             )
]


def get_all() -> list[Explorer]:
    """탐험가 목록을 반환한다."""
    return _explores

def get_one(name: str) -> Explorer:
    """검색한 탐험가를 반환한다."""
    for _explorer in _explores:
        if _explorer.name == name:
            return _explorer
    return None