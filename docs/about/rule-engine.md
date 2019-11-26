---
id: ruleEngine
title: Rule engine
---

# Rule engine

Rules define all the logic in nymea. A Tule is composed by a set of Events, States and Actions.

This diagram shows how rules are composed and interpreted by the Rule Engine.

//TODO add rule engine image

A basic concept of a Rule is the trigger path. The path defines when a Rule is triggered for evaluation. 
Each element added on a trigger path (either red or blue) has the possibility to trigger the rule engine 
to evaluate the complete rule and ultimately execute the defined actions if the whole rule evaluates to true. 
Once the trigger path has been left (i.e. a black arrow is followed), subsequent elements will still be evaluated when the rule is triggered, 
but they won't trigger the evaluation themselves.

There are two mechanisms that can trigger a Rule, described by the two trigger paths in the Rules definition figure.

* Event based
* State bindings based

## Event based rules

Event based rules (trigger path 1) contain either one or more Events or are triggered by a State change (disregarding what the changed State's value actually is). 
Such rules may still evaluate states for a certain value (leaving tge trigger path 1 and re-entering the trigger path 2), however, unless otherwise explicitly defined, 
the Rule is not evaluated when such a State change happens (given the Trigger path has been left by crossing a black arrow). 
Those rules are only executed for items on trigger path 1.

### Examples

* This rule will be evaluated and executed whenever _Remote_button1_ is pressed.

    `Event<Remote_button1_pressed> -> Action<Toggle_Light>`

* This rule will be evaluated and executed whenever _Remote_button1_ is pressed or or _Motion_sensor_1_ triggers"

    `Event<Remote_button1_pressed> | Event<Motion_sensor1_triggered> -> Action<Turn_on_Light`

* This rule will be evaluated and executed whenever Remote_button1 is pressed or the temperature changes

    `Event<Remote_button1_pressed> | State<Temperature_changed> -> Action<Turn_on_Light>`

## State bindings based rules

State binding rules (Trigger path 2) are rules which only contains States and Actions. Each time a State on that path changes, the rule is evaluated. That means, all the States in the Rule are examined. If all evaluations are fulfilled, the Rule's Actions are executed. Please note, that such Rules may only check if states are equal to, unequal, less than or greater then some value.

### Examples

* This rule will be evaluated whenever the temperature changes and executed when the temperature equals 10"

    `State<Temperature>==10 -> Action<Toggle_Light>`

* This rule will be evaluated whenever the temperature changes or the Light sensor changes and executed when the temperature is greater 20 
and the light sensor reports values greater 10
 
    `State<Temperature> >20 & State<Light> >10 -> Action<OpenWindow>`

* This rule will be evaluated whenever the temperature changes or the Light sensor changes and executed when the temperature is greater 20 or the light sensor reports values greater 10"
  
    `State<Temperature> >20 | State<Light> >10 -> Action<OpenWindow>`

## Mixing rules types

Having both types of triggers in a single rule is only possible by leaving the trigger path 1, crossing a black arrow and re-entering trigger path 2. 
This however, converts the rule to an Event based rule which means, only the elements on trigger path 1 will be able to trigger the rule evaluation.

###Examples

* This rule will be evaluated whenever the remote button1 is pressed and executed only if the temperature is greater 10

    `Event<Button1_pressed>==10 -> State<Temperature> >10 -> Action<Toggle_Light>`

