"""Definition of meta model 'USchemap'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'USchemap'
nsURI = 'http://www.modelum.es/USchemap'
nsPrefix = 'USchemap'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class USchemap(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    entities = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    relationships = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, entities=None, relationships=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if entities:
            self.entities.extend(entities)

        if relationships:
            self.relationships.extend(relationships)


@abstract
class Feature(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    owner = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, name=None, owner=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if owner is not None:
            self.owner = owner


@abstract
class DataType(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class SchemaType(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    parents = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    features = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, parents=None, features=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if parents:
            self.parents.extend(parents)

        if features:
            self.features.extend(features)


class EntityType(SchemaType):

    root = EAttribute(eType=EBoolean, unique=True, derived=False,
                      changeable=True, default_value=False)

    def __init__(self, *, root=None, **kwargs):

        super().__init__(**kwargs)

        if root is not None:
            self.root = root


class PList(DataType):

    elementType = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, elementType=None, **kwargs):

        super().__init__(**kwargs)

        if elementType is not None:
            self.elementType = elementType


class PrimitiveType(DataType):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):

        super().__init__(**kwargs)

        if name is not None:
            self.name = name


class Null(DataType):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class RelationshipType(SchemaType):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PMap(DataType):

    keyType = EReference(ordered=True, unique=True, containment=True, derived=False)
    valueType = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, keyType=None, valueType=None, **kwargs):

        super().__init__(**kwargs)

        if keyType is not None:
            self.keyType = keyType

        if valueType is not None:
            self.valueType = valueType


class PSet(DataType):

    elementType = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, elementType=None, **kwargs):

        super().__init__(**kwargs)

        if elementType is not None:
            self.elementType = elementType


class PTuple(DataType):

    elements = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, elements=None, **kwargs):

        super().__init__(**kwargs)

        if elements:
            self.elements.extend(elements)


@abstract
class LogicalFeature(Feature):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class StructuralFeature(Feature):

    optional = EAttribute(eType=EBoolean, unique=True, derived=False,
                          changeable=True, default_value=False)

    def __init__(self, *, optional=None, **kwargs):

        super().__init__(**kwargs)

        if optional is not None:
            self.optional = optional


class Attribute(StructuralFeature):

    type = EReference(ordered=True, unique=True, containment=True, derived=False)
    key = EReference(ordered=True, unique=True, containment=False, derived=False)
    references = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, type=None, key=None, references=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if key is not None:
            self.key = key

        if references:
            self.references.extend(references)


class Reference(LogicalFeature):

    upperBound = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    lowerBound = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    opposite = EReference(ordered=True, unique=True, containment=False, derived=False)
    refsTo = EReference(ordered=True, unique=True, containment=False, derived=False)
    isFeaturedBy = EReference(ordered=True, unique=True, containment=False, derived=False)
    attributes = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, opposite=None, refsTo=None, isFeaturedBy=None, attributes=None, upperBound=None, lowerBound=None, **kwargs):

        super().__init__(**kwargs)

        if upperBound is not None:
            self.upperBound = upperBound

        if lowerBound is not None:
            self.lowerBound = lowerBound

        if opposite is not None:
            self.opposite = opposite

        if refsTo is not None:
            self.refsTo = refsTo

        if isFeaturedBy is not None:
            self.isFeaturedBy = isFeaturedBy

        if attributes:
            self.attributes.extend(attributes)


class Aggregate(StructuralFeature):

    upperBound = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    lowerBound = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    aggregates = EReference(ordered=True, unique=False, containment=False, derived=False)

    def __init__(self, *, aggregates=None, upperBound=None, lowerBound=None, **kwargs):

        super().__init__(**kwargs)

        if upperBound is not None:
            self.upperBound = upperBound

        if lowerBound is not None:
            self.lowerBound = lowerBound

        if aggregates is not None:
            self.aggregates = aggregates


class Key(LogicalFeature):

    isID = EAttribute(eType=EBoolean, unique=True, derived=False,
                      changeable=True, default_value=True)
    attributes = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, attributes=None, isID=None, **kwargs):

        super().__init__(**kwargs)

        if isID is not None:
            self.isID = isID

        if attributes:
            self.attributes.extend(attributes)
