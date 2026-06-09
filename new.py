class D:
    @classmethod
    @property
    def __doc__(cls):
        return f'I love python ---from class{cls.__name__}'
d=D()
print(d.__doc__)
#这是直接访问的d的属性
#--->I love python ---from classD
"""  """
print(D.__doc__)
#--->I love python ---from classD

print(D.__dict__.get('__doc__'))
print(D.__doc__ is D.__dict__.get('__doc__'))