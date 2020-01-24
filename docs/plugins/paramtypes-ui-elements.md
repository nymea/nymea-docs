---
id:  paramtypes-ui-elements
title:  States, Actions and UI elements
---

On this page you can find different examples how a ParamType can be displayed in a client application. The images used for this examples were created with the Ubuntu SDK and are ment as an example, not as a directive.

Depending on where a ParamType will be read there are different methods how to present them to the user. If you have an Action, you can check out the Actions list to get a feeling how an ActionType can be interpreted.

If a user has to fill out a list of Param for a Device setup or configuration, some examples can be found in the Params list.

## Actions

### Button

A Device Action without Params can be represented by a single button. The button contains the name of the ActionType.

```
"actionTypes": [
    {
        "id": "uuid",
        "name": "buttonPress",
        "displayName": "Button"
    }
]
```

### Toggle Button

A Device Action with a bool Param which has no corresponding state value can be represented with two buttons. One button for true, one button for false. The button name can be created with the paramType name + On/Off. The description of the button could be the name of the ActionType.

```
"stateTypes": [
    {
        "id": "uuid",
        "name": "button",
        "displayName": "Button",
        "displayNameEvent": "Button changed",
        "displayNameAction": "Set button",
        "type": "bool",
        "defaultValue": false,
        "writable": true
    }
]
```

### Numeric Fields

An Action with one numeric Param (int, uint or double) can be represented by a text line and an button. The Action will be executed with the value in the text line. The client developer has to make sure the user can only enter the corresponding numeric value, otherwise the API will respond with an error code.

If this Action has a corresponding State (with the same UUID), the placeholder should be initialized with the current corresponding state value, otherwise with the defaultValue.

Here is an example for an int Param:
```
"stateTypes": [
    {
        "id": "uuid",
        "name": "number",
        "displayName": "Number",
        "displayNameEvent": "Number changed",
        "displayNameAction": "Set number",
        "type": "int",
        "defaultValue": 0,
        "writable": true
    }
]
```

If the text line element is smart enough to recognize if the user is finished with the input (i.e. pressed the enter button), the execute button can be dispensed. The default value can be shown as placeholder in the textfield.

### Slider

An Action with one numeric Param (int, uint or double) and limits (minValue and maxValue) can be represented with a slider. The Action will be executed with the value from the slider. The client developer should make sure the action will only be executed once the slider has been released or if the slider hasn't changed the value for ~200 ms, otherwise there would be to much useless traffic.

If this Action has a corresponding State (with the same UUID), the slider should be initialized with the current corresponding state value, otherwise with the defaultValue.

If there is a Unit in the ParamType, the unit should be visible in the Action description.

Here is an example for an int param:

```
{
    "id": "uuid",
    "name": "slider",
    "displayName": "Slider",
    "displayNameEvent": "Slider changed",
    "displayNameAction": "Set slider",
    "type": "int",
    "unit": "Percentage",
    "defaultValue": 0,
    "minValue": 0,
    "maxValue": 100,
    "writable": true
}
```

### Drop down menu

An Action with one numeric Param (int, uint or double) and an array of allowedValue can be represented as combobox. The Action will be executed with the selected value of the combobox.

If this Action has a corresponding State (with the same UUID), the combobox should initially show corresponding state value, otherwise with the defaultValue.

If there is a Unit in the ParamType, the unit should be visible in the Action description.

Here is an example for an int param:

```
{
    "id": "uuid",
    "name": "effect",
    "displayName": "effect",
    "displayNameEvent": "effect changed",
    "displayNameAction": "Set effect",
    "type": "QString",
    "defaultValue": "none",
    "possibleValues": [
        "none",
        "color loop"
    ],
    "writable": true
}
```

### With one String param

An Action with one string Param can be represented by a text line and an button. The Action will be executed with the value in the text line once the button will be pressed.

If this Action has a corresponding State (with the same UUID), the placeholder should be initialized with the current corresponding state value, otherwise with the defaultValue.

Here is an example for an int Param:

```
{
    "id": "uuid",
    "name": "Set string value",
    "paramTypes": [
        {
            "name": "String value",
            "type": "String",
            "inputType": "InputTypeTextLine",
            "defaultValue": "Hello world"
        }
    ]
}
```

If the text line element is smart enough to recognize if the user is finished with the input (i.e. pressed the enter button), the execute button can be dispensed. The default value can be shown as placeholder in the textfield.

### With one String param and allowed values

An Action with one string Param and an array of allowedValue can be represented as combobox. The Action will be executed with the selected value of the combobox.

If this Action has a corresponding State (with the same UUID), the combobox should initially show corresponding state value, otherwise with the defaultValue.

```
{
    "id": "uuid",
    "name": "Set string value",
    "paramTypes": [
        {
            "name": "value",
            "type": "String",
            "defaultValue": "String y",
            "allowedValues": [
                "String x",
                "String y",
                "String z"
            ]
        }
    ]
}
```

### With multiple params

A Device Action with multiple Params can be represented by a list of param inputs in combination with an execute button. Each ParamType has an input for the corresponding type. If the user does not insert a value for one of the Param, the default value should be inserted once the user clicks the execute button.

The button contains the name of the ActionType.

```
{
    "id": "uuid",
    "name": "Configure something",
    "paramTypes": [
        {
            "name": "Mail",
            "type": "String",
            "inputType": "InputTypeMail",
            "defaultValue": "name@example.com"
        },
        {
            "name": "Note",
            "type": "String"
        },
        {
            "name": "Note",
            "type": "String",
            "inputType": "InputTypeTextArea",
            "defaultValue": "I am Batman!"
        },
        {
            "name": "Brightness",
            "type": "Int",
            "minValue": 0,
            "maxValue": 100,
            "unit": "UnitPercentage",
            "defaultValue": 70
        },
        {
            "name": "Details",
            "type": "Bool",
            "defaultValue": true
        }
    ]
}
```

Params
Bool param

A Param from the type Bool can be represented as a switch.
```
{
    "paramTypes": [
        "name": "Bool value",
        "type": "Bool",
        "defaultValue": true
    ]
}
```
## #String input types

Depending on the Types::InputType a string Param can look different:

InputTypeTextLine

InputTypeTextArea

InputTypeSearch

InputTypePassword

InputTypeIPv4

InputTypeMacAddress

InputTypeUrl

InputTypeMail

All other InputTypes (or if the inputType is not specified) can be represented by a simple text line.
Time param

A Param from the type Time can be represented on the api as string "hh:mm". For the user there should be some kind of time picker.

```
{
    "paramTypes": [
        {
            "name": "Time",
            "type": "Time",
            "defaultValue": "00:00"
        }
    ]
}
```

### Unixtime param

A Param from the type int with the unit UnitUnixTime can be represented in the API as int. For the user there should be some kind of date time picker.

```
{
    "paramTypes": [
        {
            "name": "Datetime",
            "type": "int",
            "unit": "UnitUnixTime",
            "defaultValue": 0
        }
    ]
}
```

### Color param

A Param from the type Color can be represented in the API as html string #RRGGBBAA.

For the user there should be some kind of date time picker.

```
{
    "id": "uuid",
    "name": "color",
    "displayName": "color",
    "displayNameEvent": "color changed",
    "displayNameAction": "Set color",
    "type": "QColor",
    "defaultValue": "#000000",
    "writable": true
}
```
