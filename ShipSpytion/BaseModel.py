from copy import deepcopy


def is_obj_list(ls: list) -> bool:
    if not isinstance(ls, list):
        return False
    for item in ls:
        if not isinstance(item, BaseModel):
            return False
    return True


class BaseModel:
    def update(self, ref: dict):  # NOTE: Could be optimized
        if not isinstance(ref, dict):
            return
        for attr, value in ref.items():
            if isinstance(value, dict):
                obj = getattr(self, attr)
                obj.update(value)
            elif isinstance(value, list):
                to_set = []
                obj_attr = getattr(self, attr)[0]
                if isinstance(obj_attr, int):
                    for num in value:
                        to_set.append(num)
                else:
                    for item in value:
                        obj = deepcopy(obj_attr)
                        obj.__init__()
                        if not isinstance(item, dict):
                            print("Wrong format")
                            return
                        obj.update(item)
                        to_set.append(obj)
                setattr(self, attr, to_set)
            else:
                setattr(self, attr, value)

    def as_dict(self):
        variables = vars(self)
        to_return = variables.copy()
        for k, v in variables.items():
            if isinstance(v, BaseModel):
                to_return[k] = v.as_dict()
            if is_obj_list(v):
                ls = []
                for item in v:
                    ls.append(item.as_dict())
                to_return[k] = ls
        return to_return
