from abc import ABC, abstractmethod
class Artifact(ABC):
    @abstractmethod
    def activate(self):
        pass

class HealingArtifact(Artifact):
    def activate(self):
        return "Восстановлено 50 здоровья"


class DamageArtifact(Artifact):
    def activate(self):
        return "Нанесено 30 урона врагу"



healingArtifact = HealingArtifact()

damageArtifact = DamageArtifact()

print(healingArtifact.activate())
print(damageArtifact.activate())