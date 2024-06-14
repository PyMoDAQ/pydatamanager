from typing import List
import warnings


def deprecation_msg(message, stacklevel=2):
    warnings.warn(message, DeprecationWarning, stacklevel=stacklevel)


def find_object_if_matched_attr_name_val(obj, attr_name, attr_value):
    """check if an attribute  key/value pair match in a given object

    Parameters
    ----------
    obj: object
    attr_name: str
        attribute name to look for in the object
    attr_value: object
        value to match

    Returns
    -------
    bool: True if the key/value pair has been found in dict_tmp

    """
    if hasattr(obj, attr_name):
        if getattr(obj, attr_name) == attr_value:
            return True
    return False



def find_objects_in_list_from_attr_name_val(objects: List[object], attr_name: str,
                                            attr_value: object, return_first=True):
    """ lookup within a list of objects. Look for the objects within the list which has the correct attribute name,
    value pair

    Parameters
    ----------
    objects: list
        list of objects
    attr_name: str
        attribute name to look for in the object
    attr_value: object
        value to match
    return_first: bool
        if True return the first objects found in the list else all the objects matching

    Returns
    -------
    list of tuple(object, int): object and index or list of object and indexes
    """
    selection = []
    obj = None
    for ind, obj_tmp in enumerate(objects):
        if find_object_if_matched_attr_name_val(obj_tmp, attr_name, attr_value):
            obj = obj_tmp
            if return_first:
                break
            else:
                selection.append((obj_tmp, ind))

    if obj is None:
        if return_first:
            return None, -1
        else:
            return []
    else:
        if return_first:
            return obj, ind
        else:
            return selection