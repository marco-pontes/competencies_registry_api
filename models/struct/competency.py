class Competency:
    def __init__(self, id, uuid, description, category, children):
        self.id = id
        self.uuid = uuid
        self.description = description
        self.category = category
        self.children = children

    def __eq__(self, other):
        if not isinstance(other, Competency):
            return NotImplemented
        self_children_hashes = [child.__hash__() for child in self.children]
        other_children_hashes = [child.__hash__() for child in other.children]
        self_children_hash = tuple(self_children_hashes)
        other_children_hash = tuple(other_children_hashes)
        return self.id == other.id and self.uuid == other.uuid and self.description == other.description and self.category == other.category and self_children_hash == other_children_hash

    def __key(self):
        return (self.id, self.uuid, self.description, self.category)

    def __hash__(self):
        return hash(self.__key())
