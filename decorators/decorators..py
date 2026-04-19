def is_alive(func):
    def wrapper(self, *args, **kwargs):
        health = self.health
        if health <= 0:
            print(f'{self.name} мертв и не может действовать!')
            return None
        else:
            return func(self, *args, **kwargs)
    return wrapper

def log_action(func):
    def wrapper(self, *args, **kwargs):
        print(f'[LOG] Начало действия:  {func.__name__}')
        result = func(self, *args, **kwargs)
        print(f'[LOG] Действие завершено')
        return result
    return wrapper

#event
def health_boost(func):
    def wrapper(self, *args, **kwargs):
        self.health = self.health * 2
        result = func(self, *args, **kwargs)
        self.health = self.health / 2
        return result
    return wrapper

#event
def mana_boost(func):
    def wrapper(self, *args, **kwargs):
        self.mana = self.mana * 1.5
        result = func(self, *args, **kwargs)
        self.mana = self.mana / 1.5
        return result
    return wrapper

#event
def holy_staff(func):
    def wrapper(self, *args, **kwargs):
        bonus = 0
        if self.hero_class == "wizzard":
            bonus = 5
            self.mana += bonus
        result = func(self, *args, **kwargs)
        self.mana -= bonus
        return result
    return wrapper

#my decorator
def stamina_cost(func):
    def wrapper(self, *args, **kwargs):
        cost = 5
        if self.stamina < cost:
            print(f'{self.name} устал и не может действовать!')
            return None
        self.stamina -= cost
        result = func(self, *args, **kwargs)
        return result
    return wrapper

class Hero:
    def __init__(self, name: str, health: int, mana: int, hero_class, spells_names: dict, items: dict):
        self.name = name
        self.health = health
        self.mana = mana
        self.hero_class = hero_class
        self.spells_names = spells_names
        self.items = items
        self.stamina = 100

    @stamina_cost #my decorator
    @health_boost #event
    @is_alive
    def attack(self, damage):
        print(f'Герой нанес урон {damage}')

    @stamina_cost #my decorator
    @health_boost #event
    @log_action
    def heal(self, amount):
        self.health += amount

    @stamina_cost #my decorator
    @mana_boost #event
    @holy_staff #event
    @is_alive
    def cast_spell(self, spell_name):
        mana_cost = self.spells_names[spell_name]['mana_cost']
        self.mana -= mana_cost
        print(spell_name)

    def add_spell(self, spell_name):
        self.spells_names= self.spells_names[spell_name]
        return self.spells_names

    def add_item(self, item):
        self.items = self.items[item]
