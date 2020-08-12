# Java Buildins 

## Primitive vs. Wrapper Classes

- boolean, byte, short, char, int, long, float, double
- Boolean, Byte, Short, Character, Integer, Long, Float, Double

### Primitive <-> Wrapper

```java
Integer object = new Integer(1);
int i = Integer.parseInt(object);

Integer object = 2; // auto boxing
int i = object; // auto unboxing
```

### Primitive <-> Primitive

auto convert smaller range to larger range, e.g. int -> long, float -> double
```java
int i = 123;
long longval = i;
```

force convert from larger range to smaller range
```java
int i = (int) longval;
char ch = (char) 130;
```

### To/From String

To String:
```java
String s = obj.toString();
String s = String.valueOf(primitiveData)
```

From String:
```java
byte b = Byte.parseByte(s);
int i = Integer.parseInt(s);
...
char ch = s.charAt(0);
```