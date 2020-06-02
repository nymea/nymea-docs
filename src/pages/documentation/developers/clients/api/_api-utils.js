export function getRefs(refs, value) {
  if (typeof value === 'string') {
    if (value.includes('$ref:')) {
      refs = [ ...refs, value.replace('$ref:', '') ];
    }
  } else if (Array.isArray(value)) {
    value.forEach((valueItem) => {
      refs = getRefs(refs, valueItem);
    });
  } else if (Object.prototype.toString.call(value) === '[object Object]') {
    Object.values(value).forEach((valueItem) => {
      refs = getRefs(refs, valueItem);
    });
  }
  return refs;
}
