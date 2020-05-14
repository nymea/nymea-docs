import { isNumber, isObject, isString } from './property';
import { availableBreakpoints } from './breakpoints';

export function createStyle(style, propertyValueMap) {
  let currentValue;

  style = '';
  
  Object.keys(propertyValueMap).forEach((property) => {
    currentValue = propertyValueMap[property];
    if (isNumber(currentValue) || isString(currentValue)) {
      style = createStyleFromString(style, property, currentValue);
    } else if (isObject(currentValue)) {
      style = createStyleFromObject(style, property, currentValue);
    }
  });

  return style;
}

function createStyleFromString(style, property, value) {
  style = style + (value ? `${property}: ${value};` : '');
  return style;
}

function createStyleFromObject(style, property, value) {
  Object.keys(value).forEach((breakpoint) => {
    if (availableBreakpoints.includes(breakpoint)) {
      style = style + (value ? `${property}-${breakpoint}: ${value[breakpoint]};` : '');
    }
  });
  return style;
}
