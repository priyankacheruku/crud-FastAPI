# key learnings

## data types
* FastAPI supports default 4 data types  `int` , `str` , `bool`, `float`

## sub clasess of `Param` class
* `Path()` used to add validations for url path parameter

* `Query()` used to add validations for query  parameters

* `Body()` used to declare body or payload variable

Note: these are actually functions that return special classes.


## response
* `response_model()` to limit the output data
* `response_model_exclude_unset` true-->wont show null/empty  values
*  `response_model_include` or `response_model_exclude` to omit some attributes in response

## models
*  `List` ,`Dict` ,`Set` are extra models

