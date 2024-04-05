from pyecore.resources import global_registry
from .USchema-p import getEClassifier, eClassifiers
from .USchema-p import name, nsURI, nsPrefix, eClass
from .USchema-p import USchema-p, EntityType, Feature, Attribute, DataType, PList, Reference, Aggregate, PrimitiveType, Null, RelationshipType, SchemaType, PMap, PSet, PTuple, LogicalFeature, Key, StructuralFeature


from . import USchema-p

__all__ = ['USchema-p', 'EntityType', 'Feature', 'Attribute', 'DataType', 'PList', 'Reference', 'Aggregate', 'PrimitiveType',
           'Null', 'RelationshipType', 'SchemaType', 'PMap', 'PSet', 'PTuple', 'LogicalFeature', 'Key', 'StructuralFeature']

eSubpackages = []
eSuperPackage = None
USchema-p.eSubpackages = eSubpackages
USchema-p.eSuperPackage = eSuperPackage

USchema-p.entities.eType = EntityType
USchema-p.relationships.eType = RelationshipType
Attribute.type.eType = DataType
PList.elementType.eType = DataType
Reference.opposite.eType = Reference
Reference.refsTo.eType = EntityType
Reference.isFeaturedBy.eType = SchemaType
Aggregate.aggregates.eType = SchemaType
SchemaType.parents.eType = SchemaType
SchemaType.features.eType = Feature
PMap.keyType.eType = PrimitiveType
PMap.valueType.eType = DataType
PSet.elementType.eType = DataType
PTuple.elements.eType = DataType
Attribute.key.eType = Key
Attribute.references.eType = Reference
Reference.attributes.eType = Attribute
Reference.attributes.eOpposite = Attribute.references
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

register_packages = [USchema-p] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack
