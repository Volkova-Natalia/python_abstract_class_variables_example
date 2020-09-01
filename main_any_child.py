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
    def check_required_class_variables(cls, parent, child):
        # print('\n----------\n', parent)
        parent__required_class_variables = '_' + parent.__name__ + '__required_class_variables'
        child__required_class_variables = '_' + child.__name__ + '__required_class_variables'
        if hasattr(parent, parent__required_class_variables):
            for var in getattr(parent, parent__required_class_variables):
                # print('var ', var,
                #       '\nchild.__dict__ ', child.__dict__,
                #       '\nhasattr(child, var): ', hasattr(child, var))
                if not hasattr(child, var):
                    if ((not hasattr(child, child__required_class_variables)) or
                            (var not in getattr(child, child__required_class_variables))):
                        raise NotImplementedError(
                            f'Class {child} lacks required `{var}` class attribute'
                        )

    @classmethod
    def __init_subclass__(cls):
        parent = cls.__base__
        child = cls
        parent().check_required_class_variables(parent=parent, child=child)


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
