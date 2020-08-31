"""
A direct child CAN define required class variables (pseudo "abstract"),
but it is not necessary if the variables are defined by its child.
But in this case you have to define all the required class variables in an intermediate class.
"""


class ClassWithAbstractVariables(object):

    __required_class_variables = [
        'abstract_class_variables_0',
        'abstract_class_variables_1',
        'abstract_class_variables_2',
    ]

    @classmethod
    def __init_subclass__(cls):
        for var in cls.__base__().__required_class_variables:
            if not hasattr(cls, var):
                if ((not hasattr(cls, '_' + cls.__name__ + '__required_class_variables')) or
                    (var not in cls.__required_class_variables)):
                    raise NotImplementedError(
                        f'Class {cls} lacks required `{var}` class attribute'
                    )


class IntermediateClassFail(ClassWithAbstractVariables):
    """
    You can not inherit other classes from the class.
    """
    pass


class IntermediateClass(ClassWithAbstractVariables):
    """
    The class may be correct. It depends on its child.
    """
    __required_class_variables = [
        'abstract_class_variables_0',
        'abstract_class_variables_1',
        'abstract_class_variables_2',
    ]
    pass


class MainClassSuccess(IntermediateClass):
    abstract_class_variables_0 = None
    abstract_class_variables_1 = None
    abstract_class_variables_2 = None
    pass


class MainClassFail(IntermediateClass):
    """
    Class <class '__main__.MainClassFail0'> lacks required `abstract_class_variables_0` class attribute
    Class <class '__main__.MainClassFail0'> lacks required `abstract_class_variables_1` class attribute
    Class <class '__main__.MainClassFail0'> lacks required `abstract_class_variables_2` class attribute
    """
    pass


if __name__ == '__main__':
    pass
