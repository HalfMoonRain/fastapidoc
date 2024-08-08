from model import Creature
_creatures: list[Creature] = [
    Creature(name="yeti",
             country="CN",
             area="Himalayas",
             description="Hirsute Himalayan",
             aka="Abominable Snoeman"),
    Creature(name="sasquatch",
             country="US",
             area="*",
             description="Yeti's Coisom Eddie",
             aka="Bigfoot")
]

def get_creatures() -> list[Creature]:
    return _creatures


