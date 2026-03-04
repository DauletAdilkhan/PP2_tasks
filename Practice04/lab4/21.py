import importlib

q = int(input().strip())

for _ in range(q):
    module_path, attr = input().strip().split()
    
    try:
        module = importlib.import_module(module_path)
        
        if hasattr(module, attr):
            attr_value = getattr(module, attr)
            if callable(attr_value):
                print("CALLABLE")
            else:
                print("VALUE")
        else:
            print("ATTRIBUTE_NOT_FOUND")
            
    except (ImportError, ModuleNotFoundError):
        print("MODULE_NOT_FOUND")