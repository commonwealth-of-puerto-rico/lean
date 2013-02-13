class Setting(object):
    def __init__(self, module, name, global_name, description, exists, default):
        self.module = module
        self.name = name
        self.global_name = global_name
        self.description = description
        self.exists = exists
        self.default = default
