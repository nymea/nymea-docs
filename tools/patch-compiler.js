/*
  node_modules/svelte/patch-compiler.js

  replace push with reassign

  cd node_modules/svelte
  mv compiler.js compiler.js.orig
  ln -s compiler.js.new compiler.js
  node patch-compiler.js
*/

const acorn_parse = require("acorn").parse;
const estree_walk = require("estree-walker").walk;
const magicString = require("magic-string");
const fs = require("fs");

let input_file = "compiler.js.orig";
let output_file = "compiler.js.new";

// input
let content = fs.readFileSync(input_file, 'utf8');

// output
let code = new magicString(content);

let ast = acorn_parse(
  content, {
  // ecmaVersion: 10, // default in year 2019
  sourceType: 'module',
});

let funcName = "push";

let arrayNameList = [];

function setCharAt(str, index, chr) {
  if (index > str.length-1) return str;
  return str.substr(0,index) + chr + str.substr(index+1);
}

estree_walk( ast, {
  enter: function ( node, parent, prop, index ) {

    // filter for array.push()
    if (
      node.type !== 'CallExpression' ||
      node.callee === undefined ||
      node.callee.property === undefined ||
      node.callee.property.name !== funcName
    ) {
      return;
    }

    // filter for spread operator
    if (node.arguments.find(a => {
      return (a.type == 'SpreadElement');
    }) === undefined) {
      return;
    }

    let nodeSrc = content.substring(
      node.start, node.end);

    let arrayName = content.substring(
      node.callee.object.start,
      node.callee.object.end);
    
    arrayNameList.push(arrayName);

    // patch .push(
    let nodePatch = nodeSrc.replace(
      ".push(", " /* PATCHED */ = [..."+arrayName+", ");

    // patch closing bracket
    nodePatch = setCharAt(nodePatch, nodePatch.lastIndexOf(")"), "]");

    code.overwrite(node.start, node.end, nodePatch);

}});

code = code.toString();

function filterUnique(value, index, array) { 
  return array.indexOf(value) === index;
}

// replace const with let
arrayNameList.filter(filterUnique).forEach(arrayName => {
  console.log(`arrayName = ${arrayName}`)

  code = code.replace(
    // new RegExp("const "+arrayName+" = \\[", 'g'), // global = replace all
    // "let "+arrayName+" = ["
    new RegExp("const "+arrayName+" = ", 'g'), // global = replace all
    "let "+arrayName+" = "
  );
})

fs.writeFileSync(output_file, code);
