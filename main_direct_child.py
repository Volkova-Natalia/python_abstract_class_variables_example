"""
A direct child HAS TO define required class variables (pseudo "abstract").
"""


class ClassWithAbstractVariables(object):

    @classmethod
    def __init_subclass__(cls):
        required_class_variables = [
            'abstract_class_variables_0',
            'abstract_class_variables_1',
            'abstract_class_variables_2',
        ]
        for var in required_class_variables:
            if not hasattr(cls, var):
                raise NotImplementedError(
                    f'Class {cls} lacks required `{var}` class attribute'
                )


class MainClassSuccess(ClassWithAbstractVariables):
    abstract_class_variables_0 = None
    abstract_class_variables_1 = None
    abstract_class_variables_2 = None
    pass


class MainClassFail(ClassWithAbstractVariables):
    """
    Class <class '__main__.MainClassFail0'> lacks required `abstract_class_variables_0` class attribute
    Class <class '__main__.MainClassFail0'> lacks required `abstract_class_variables_1` class attribute
    Class <class '__main__.MainClassFail0'> lacks required `abstract_class_variables_2` class attribute
    """
    pass


if __name__ == '__main__':
    pass
