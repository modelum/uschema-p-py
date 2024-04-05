
from .USchemap import getEClassifier, eClassifiers
from .USchemap import name, nsURI, nsPrefix, eClass
from .USchemap import USchemap, EntityType, Feature, Attribute, DataType, PList, Reference, Aggregate, PrimitiveType, Null, RelationshipType, SchemaType, PMap, PSet, PTuple, LogicalFeature, Key, StructuralFeature


from . import USchemap

__all__ = ['USchemap', 'EntityType', 'Feature', 'Attribute', 'DataType', 'PList', 'Reference', 'Aggregate', 'PrimitiveType',
           'Null', 'RelationshipType', 'SchemaType', 'PMap', 'PSet', 'PTuple', 'LogicalFeature', 'Key', 'StructuralFeature']

eSubpackages = []
eSuperPackage = None
USchemap.eSubpackages = eSubpackages
USchemap.eSuperPackage = eSuperPackage

USchemap.entities.eType = EntityType
USchemap.relationships.eType = RelationshipType
Attribute.type.eType = DataType
PList.elementType.eType = DataType
Reference.opposite.eType = Reference
Reference.refsTo.eType = EntityType
Reference.isFeaturedBy.eType = SchemaType
Aggregate.aggregates.eType = SchemaType
SchemaType.parents.eType = SchemaType
PMap.keyType.eType = PrimitiveType
PMap.valueType.eType = DataType
PSet.elementType.eType = DataType
PTuple.elements.eType = DataType
Feature.owner.eType = SchemaType
Attribute.key.eType = Key
Attribute.references.eType = Reference
Reference.attributes.eType = Attribute
Reference.attributes.eOpposite = Attribute.references
SchemaType.features.eType = Feature
SchemaType.features.eOpposite = Feature.owner
Key.attributes.eType = Attribute
Key.attributes.eOpposite = Attribute.key

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
