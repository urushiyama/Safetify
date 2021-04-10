# safetify

> Some shorthands for using python safer

- Isolate arguments between inside and outside of functions by `@args_isolated`

## Usage

### @args_isolated

- Safetify default arguments

```python
from safetify import args_isolated

class UnsafeContainer:
    
    def __init__(self, storage=[]):
        self.storage = storage
    
    def store(self, item):
        self.storage.append(item)
    
    def remove(self, item):
        self.storage.remove(item)

class SafeContainer:

    @args_isolated
    def __init__(self, storage=[]):
        self.storage = storage
    
    def store(self, item):
        self.storage.append(item)
    
    def remove(self, item):
        self.storage.remove(item)

#===Safetify default arguments===
uc1 = UnsafeContainer()
uc1.store('Shoes')
print(uc1.storage) # -> ['Shoes']
uc2 = UnsafeContainer()
print(uc2.storage) # -> ['Shoes']
sc1 = SafeContainer()
sc1.store('Hats')
print(sc1.storage) # -> ['Hats']
sc2 = SafeContainer()
print(sc2.storage) # -> []
#====================================
#===Safetify outside mutable lists===
overwritten_storage = ['Clothes', 'Shirts']
uc3 = UnsafeContainer(storage=overwritten_storage)
uc3.store('Coats')
print(uc3.storage) # -> ['Clothes', 'Shirts', 'Coats']
print(overwritten_storage) # -> ['Clothes', 'Shirts', 'Coats']
print(uc3.storage is overwritten_storage) # -> True
isolated_storage = ['Clothes', 'Shirts']
sc3 = SafeContainer(storage=isolated_storage)
sc3.store('Coats')
print(sc3.storage) # -> ['Clothes', 'Shirts', 'Coats']
print(isolated_storage) # -> ['Clothes', 'Shirts']
print(sc3.storage is isolated_storage) # -> False
```

## License

This library is released under [MIT License](LICENSE).
