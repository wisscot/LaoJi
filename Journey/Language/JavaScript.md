# JavaScript


Array operations:
arr.filter(func)   return new array
arr.map(func)  return new array
arr.forEach(func)  return null

arr.map(func).flat()    =>      arr.flatmap(func)



Object:
Object.keys(obj)  =>  Array of the keys of the object
Object.values(obj) => Array of the values of the object
Object.entries(obj) => key value pairs

obj = {k1:v1, k2:v2}
Object.keys(obj)  => [k1, k2]
Object.values(obj)  => [v1, v2]
Object.entries(obj)  => [[k1, v1], [k2, v2]]



function(d){} can be replaced with d => {}  if `this`, `arguments` not used nor called with `new`